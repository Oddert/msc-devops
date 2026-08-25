from datetime import datetime, timedelta

from config.variables import timezone


class SyncManager:
    """
    Used with the Singleton Pattern to control when syncs with PCF are permitted to be performed.

    Attributes
    ----------
    _update_wait : int
        Time in seconds to determine the wait between syncs.

    Methods
    -------
    log_update()
        Updates the internal record of when the last sync was performed.

    should_update()
        Returns True if enough time has elapsed between the last update and now.
    """

    def __init__(self, _update_wait: int) -> None:
        """
        Constructs a SyncManger object.

        Parameters
        ----------
        _update_wait : int
            Time in seconds to determine the wait between syncs.
        """
        self.last_updated = datetime.now(timezone)
        self.update_wait = _update_wait

    def log_update(self):
        """
        Updates the internal record of when the last sync was performed.
        """
        self.last_updated = datetime.now(timezone)

    def should_update(self):
        """
        Returns True if enough time has elapsed between the last update and now.
        """
        if self.last_updated + timedelta(seconds=self.update_wait) > datetime.now(
            timezone
        ):
            return False
        return True


sync_manager = SyncManager(10)
