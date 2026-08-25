from typing import Dict, List

from fastapi import WebSocket

from models.instance_model import InstanceModel


class WSManager:
    """
    Used to manage collections of WebSocket connections for Instances.
    """

    def __init__(self) -> None:
        self.instances: Dict[str, List[WebSocket]] = {}

    def register_listener(self, pcf_guid: str, websocket: WebSocket):
        """
        Adds a WebSocket connection for a given PCF instance.

        :param pcf_guid: The PCF ID for the Instance this connection is subscribing to.
        :type pcf_guid: str
        :param websocket: The WebSocket connection to subscribe.
        :type websocket: WebSocket
        """
        if pcf_guid not in self.instances:
            self.instances[pcf_guid] = []
        if websocket not in self.instances[pcf_guid]:
            self.instances[pcf_guid].append(websocket)

    def unregister_listener(self, websocket: WebSocket):
        """
        Un-subscribes a WebSocket connection from all its subscriptions on disconnect.

        :param websocket: The WebSocket connection to remove from all Instances it is subscribed to.
        :type websocket: WebSocket
        """
        for listener_list in self.instances.values():
            if websocket in listener_list:
                listener_list.remove(websocket)

    async def broadcast_update(self, instance: InstanceModel):
        """
        Sends an Instance update to all subscribed parties.

        :param instance: The Instance to be broadcast.
        :type instance: InstanceModel
        """
        pcf_guid = instance.pcf_guid
        if pcf_guid in self.instances:
            for listener in self.instances[pcf_guid]:
                await listener.send_json([instance.to_json()])

    async def broadcast_multiple_updates(self, instances: List[InstanceModel]):
        """
        Sends an update to all subscribed parties for a list of Instances.

        :param instances: The list of Instances to broadcast.
        :type instances: List[InstanceModel]
        """
        listeners: Dict[WebSocket, List[InstanceModel]] = {}
        for instance in instances:
            pcf_guid = instance.pcf_guid
            if pcf_guid in self.instances:
                for listener in self.instances[pcf_guid]:
                    if listener not in listeners:
                        listeners[listener] = []
                    listeners[listener].append(instance)

        for recipient, subscriptions in listeners.items():
            await recipient.send_json(
                [instance.to_json() for instance in subscriptions]
            )


ws_manager = WSManager()
