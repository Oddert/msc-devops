"""Handles all responses on the base endpoint "/instance"."""

from datetime import datetime
from math import ceil
from typing import List

from fastapi import (
    APIRouter,
    Depends,
    Request,
    Response,
)
from loguru import logger
from sqlalchemy.orm import Session

from config.database import get_db
from config.variables import timezone

from constants.auth_constants import auth_areas

from models.instance_model import InstanceModel
from models.instance_attrs_model import InstanceAttrModel

from mocks.fake_instance_call import fake_pcf_call
from mocks.fake_pcf_api import org_names, spaces_by_id
from mocks.fake_tasks_call import tasks_by_pcf_name

from schemas.instance_schemas import PostInstanceAttr

from security.middleware import protected_endpoint
from security.roles import get_org_ids_for_user

from utils.responses import (
    respond_not_found,
    respond_ok,
    respond_server_error,
    respond_unauthorised,
)
from utils.sync_manager import sync_manager
from utils.ws_manager import ws_manager

router = APIRouter(prefix='/instance')


@router.get('/')
@protected_endpoint()
async def get_all_instances(
    request: Request,
    response: Response,
    database: Session = Depends(get_db),
    racfid: str = Depends(lambda: None),
    roles: List[str] = Depends(lambda: None),
):
    """Retrieves a list of all instances stored within the system."""

    try:
        if sync_manager.should_update():
            await syc_and_create_instances(database)
            sync_manager.log_update()

        org_ids = get_org_ids_for_user(roles)
        instances = InstanceModel.find_by_org_id_list(org_ids, racfid, database)
        await ws_manager.broadcast_multiple_updates(instances)
        return respond_ok(
            response, instances=[instance.to_json() for instance in instances]
        )
    except Exception as ex:
        return respond_server_error(response, error=str(ex))


@router.get('/org-names')
# @protected_endpoint()
async def get_space_mapping(
    request: Request,
    response: Response,
    database: Session = Depends(get_db),
    racfid: str = Depends(lambda: None),
    roles: List[str] = Depends(lambda: None),
):
    """Sends the mapping of all PCF organisations from ID to name."""

    try:
        return respond_ok(response, orgNames=org_names)
    except Exception as ex:
        return respond_server_error(response, error=str(ex))


@router.get('/tasks/pcf-id/{instance_id}')
@protected_endpoint()
async def get_tasks_by_pcf_guid(
    request: Request,
    response: Response,
    instance_id: str,
    database: Session = Depends(get_db),
    racfid: str = Depends(lambda: None),
    roles: List[str] = Depends(lambda: None),
):
    """Retrieves a specific instance by ID. Note that this is the PCF GUD the app's internal ID."""

    try:
        org_ids = get_org_ids_for_user(roles)
        instance = InstanceModel.find_by_pcf_guid(instance_id, racfid, database)

        if not instance:
            return respond_not_found(
                response, error=f'No instance found for PCF ID "{instance_id}".'
            )

        if instance.pcf_org_id not in org_ids:
            return respond_unauthorised(
                response,
                f'You do not have the required roles to access the instance with ID "{instance_id}".',
            )

        tasks = []
        if instance.pcf_app_name in tasks_by_pcf_name:
            tasks = tasks_by_pcf_name[instance.pcf_app_name]

        return respond_ok(
            response,
            tasks={
                'pagination': {
                    'total_results': len(tasks),
                    'total_pages': ceil(len(tasks)),
                    'first': {
                        'href': 'https://api.example.org/v3/apps/ccc25a0f-c8f4-4b39-9f1b-de9f328d0ee5/tasks?page=1&per_page=2'
                    },
                    'last': {
                        'href': 'https://api.example.org/v3/apps/ccc25a0f-c8f4-4b39-9f1b-de9f328d0ee5/tasks?page=2&per_page=2'
                    },
                    'next': {
                        'href': 'https://api.example.org/v3/apps/ccc25a0f-c8f4-4b39-9f1b-de9f328d0ee5/tasks?page=2&per_page=2'
                    },
                    'previous': None,
                },
                'resources': tasks,
            },
        )
    except ValueError as ex:
        return respond_not_found(
            response,
            message=f'Instance PCF GUID of "{instance_id}" is not valid.',
            error=str(ex),
        )
    except Exception as ex:
        return respond_server_error(response, error=str(ex))


@router.get('/app-id/{instance_id}')
@protected_endpoint()
async def get_single_instance_by_id(
    request: Request,
    response: Response,
    instance_id: str,
    database: Session = Depends(get_db),
    racfid: str = Depends(lambda: None),
    roles: List[str] = Depends(lambda: None),
):
    """Retrieves a specific instance by ID. Note that this is the app's internal ID not the PCF GUD."""

    try:
        org_ids = get_org_ids_for_user(roles)
        instance = InstanceModel.find_by_app_id(instance_id, racfid, database)

        if not instance:
            return respond_not_found(
                response, error=f'No instance found for ID "{instance_id}".'
            )

        if instance.pcf_org_id not in org_ids:
            return respond_unauthorised(
                response,
                f'You do not have the required roles to access the instance with ID "{instance_id}".',
            )

        return respond_ok(response, instance=instance.to_json())
    except ValueError as ex:
        return respond_not_found(
            response,
            message=f'Instance ID of "{instance_id}" is not valid.',
            error=str(ex),
        )
    except Exception as ex:
        return respond_server_error(response, error=str(ex))


@router.get('/pcf-id/{instance_id}')
@protected_endpoint()
async def get_single_instance_by_pcf_guid(
    request: Request,
    response: Response,
    instance_id: str,
    database: Session = Depends(get_db),
    racfid: str = Depends(lambda: None),
    roles: List[str] = Depends(lambda: None),
):
    """Retrieves a specific instance by ID. Note that this is the PCF GUD the app's internal ID."""

    try:
        org_ids = get_org_ids_for_user(roles)
        instance = InstanceModel.find_by_pcf_guid(instance_id, racfid, database)

        if not instance:
            return respond_not_found(
                response, error=f'No instance found for PCF ID "{instance_id}".'
            )

        if instance.pcf_org_id not in org_ids:
            return respond_unauthorised(
                response,
                f'You do not have the required roles to access the instance with ID "{instance_id}".',
            )

        return respond_ok(response, instance=instance.to_json())
    except ValueError as ex:
        return respond_not_found(
            response,
            message=f'Instance PCF GUID of "{instance_id}" is not valid.',
            error=str(ex),
        )
    except Exception as ex:
        return respond_server_error(response, error=str(ex))


@router.put('/user-overrides/{pcf_guid}')
@protected_endpoint(for_areas=[auth_areas.ADMIN])
async def update_user_overrides(
    request: Request,
    response: Response,
    pcf_guid: str,
    instance_attributes: PostInstanceAttr,
    database: Session = Depends(get_db),
    racfid: str = Depends(lambda: None),
    roles: List[str] = Depends(lambda: None),
):
    """Endpoint to manually trigger PCF Instance syncs."""

    try:
        instance = InstanceModel.find_by_pcf_guid(pcf_guid, racfid, database)

        if not instance:
            return respond_not_found(
                response, message=f'No Instance found for GUID "{pcf_guid}"'
            )

        instance_attr = InstanceAttrModel.find_by_pcf_guid(pcf_guid, racfid, database)

        if instance_attr:
            instance_attr.description = instance_attributes.description
            instance_attr.readable_name = instance_attributes.readableName
        else:
            instance_attr = InstanceAttrModel(
                description=instance_attributes.description,
                pcf_guid=pcf_guid,
                racf=racfid,
                readable_name=instance_attributes.readableName,
            )
            database.add(instance_attr)

        database.commit()
        database.flush()

        return respond_ok(
            response,
            instanceAttributes=instance_attr.to_json(),
        )
    except Exception as ex:
        return respond_server_error(response, error=str(ex))


@router.post('/')
@protected_endpoint(for_areas=[auth_areas.ADMIN])
async def user_sync_instances(
    request: Request,
    response: Response,
    database: Session = Depends(get_db),
    racfid: str = Depends(lambda: None),
    roles: List[str] = Depends(lambda: None),
):
    """Endpoint to manually trigger PCF Instance syncs."""

    try:
        await syc_and_create_instances(database=database)
        return respond_ok(
            response,
            message='Instance list created and synced with PCF.',
            updated=datetime.now(timezone),
        )
    except Exception as ex:
        return respond_server_error(response, error=str(ex))


@router.get('/debug')
@protected_endpoint()
async def debug_get_pcf_call(
    request: Request,
    response: Response,
    database: Session = Depends(get_db),
    racfid: str = Depends(lambda: None),
    roles: List[str] = Depends(lambda: None),
):
    """Retrieves a list of all instances stored within the system."""

    try:
        instance_map = {}
        for organisation in fake_pcf_call:
            if organisation['org_id'] not in instance_map:
                instance_map[organisation['org_id']] = {
                    'name': organisation['org_name'],
                    'spaces': {},
                }

            for instance in organisation['instances']:
                if (
                    instance['space_id']
                    not in instance_map[organisation['org_id']]['spaces']
                ):
                    instance_map[organisation['org_id']]['spaces'][
                        instance['space_id']
                    ] = {'name': spaces_by_id[instance['space_id']], 'instances': []}

                instance_map[organisation['org_id']]['spaces'][instance['space_id']][
                    'instances'
                ].append(organisation)

        return respond_ok(
            response,
            instances=instance_map,
        )
    except Exception as ex:
        return respond_server_error(response, error=str(ex))


@router.put('/demo/{pcf_guid}/{action}')
@protected_endpoint()
async def demo_endpoint(
    request: Request,
    response: Response,
    pcf_guid: str,
    action: str,
    database: Session = Depends(get_db),
    racfid: str = Depends(lambda: None),
    roles: List[str] = Depends(lambda: None),
):
    """Retrieves a list of all instances stored within the system."""

    try:
        for org in fake_pcf_call:
            for instance in org['instances']:
                if instance['guid'] == pcf_guid:
                    instance['desired_state'] = action

        return respond_ok(
            response,
        )
    except Exception as ex:
        return respond_server_error(response, error=str(ex))


async def syc_and_create_instances(
    database: Session = Depends(get_db),
):
    """Checks all PCF spaces to create or delete application Instances, based on the current makeup of PCF."""

    try:
        for pcf_org in fake_pcf_call:
            to_broadcast: List[InstanceModel] = []
            for pcf_instance in pcf_org['instances']:
                queried_app_instance = InstanceModel.find_by_pcf_guid(
                    pcf_instance['guid'], '', database
                )
                if queried_app_instance:
                    queried_app_instance.created_at = datetime.fromisoformat(
                        pcf_instance['created_at']
                    )
                    queried_app_instance.pcf_app_name = pcf_instance['name']
                    queried_app_instance.pcf_cpu = 0
                    queried_app_instance.pcf_org_id = pcf_org['org_id']
                    queried_app_instance.pcf_space_id = pcf_instance['space_id']
                    queried_app_instance.pcf_instances_total = 1
                    queried_app_instance.pcf_ram = 1
                    queried_app_instance.readable_name = pcf_instance['name']
                    queried_app_instance.status = pcf_instance['desired_state']
                    queried_app_instance.updated_at = datetime.fromisoformat(
                        pcf_instance['updated_at']
                    )
                else:
                    queried_app_instance = InstanceModel(
                        created_at=datetime.fromisoformat(pcf_instance['created_at']),
                        pcf_app_name=pcf_instance['name'],
                        pcf_cpu=0,
                        pcf_guid=pcf_instance['guid'],
                        pcf_org_id=pcf_org['org_id'],
                        pcf_space_id=pcf_instance['space_id'],
                        pcf_instances_total=1,
                        pcf_ram=1,
                        readable_name=pcf_instance['name'],
                        status=pcf_instance['desired_state'],
                        updated_at=datetime.fromisoformat(pcf_instance['updated_at']),
                    )
                    database.add(queried_app_instance)
                to_broadcast.append(queried_app_instance)
            await ws_manager.broadcast_multiple_updates(to_broadcast)

        database.commit()
        return {'message': 'Sync completed successfully'}
    except Exception as ex:
        raise ex


async def schedule_instance_sync():
    """Scheduler task to sync the Instances database."""
    try:
        logger.info('Beginning schedule of Instances from PCF')
        database = next(get_db())
        result = await syc_and_create_instances(database=database)
        logger.info('PCF sync job complete.')
        return result
    except Exception as ex:
        logger.error(str(ex))
