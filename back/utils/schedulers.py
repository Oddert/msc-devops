"""
File to hold all application schedulers.

Current scheduled tasks:
- Synchronise the application Instances to the current PCF status.

The scheduler is only created is there are jobs to schedule.
"""

from apscheduler.schedulers.asyncio import AsyncIOScheduler

from resources.instance_resources import schedule_instance_sync


def setup_async_schedulers():
    """Sets up cron job schedules for the application within its startup / shutdown lifecycle."""
    async_scheduler = AsyncIOScheduler()

    async_scheduler.add_job(schedule_instance_sync, 'cron', minute=10)

    return async_scheduler if async_scheduler.get_jobs() else None
