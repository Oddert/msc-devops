"""Handles all responses on the base endpoint "/instance"."""

from typing import List

from fastapi import (
    APIRouter,
    Depends,
    Request,
    Response,
)
from sqlalchemy.orm import Session

from config.database import get_db

from models.instance_model import InstanceModel
from models.watchlist_model import WatchlistModel

from schemas.watchlist_schemas import PostWatchlist

from security.middleware import protected_endpoint
from security.roles import get_org_ids_for_user

from utils.responses import (
    respond_created,
    respond_not_found,
    respond_ok,
    respond_server_error,
    respond_unauthorised,
)

router = APIRouter(prefix='/watchlist')


@router.get('/')
@protected_endpoint()
async def get_all_watchlists(
    request: Request,
    response: Response,
    database: Session = Depends(get_db),
    racfid: str = Depends(lambda: None),
    roles: List[str] = Depends(lambda: None),
):
    """Retrieves a list of all Watchlists stored within the system."""

    try:
        watchlists = WatchlistModel.get_all_for_user(racfid, database)
        return respond_ok(
            response, watchlists=[watchlist.to_json() for watchlist in watchlists]
        )
    except Exception as ex:
        return respond_server_error(response, error=str(ex))


@router.get('/default')
@protected_endpoint()
async def get_default_watchlists(
    request: Request,
    response: Response,
    database: Session = Depends(get_db),
    racfid: str = Depends(lambda: None),
    roles: List[str] = Depends(lambda: None),
):
    """Retrieves a list of all Watchlists stored within the system."""

    try:
        watchlist = WatchlistModel.get_users_default(racfid, database)
        return respond_ok(
            response,
            watchlist=watchlist.to_json() if watchlist else None,
        )
    except Exception as ex:
        return respond_server_error(response, error=str(ex))


@router.post('/')
@protected_endpoint()
async def create_single_watchlist(
    request: Request,
    response: Response,
    watchlist: PostWatchlist,
    database: Session = Depends(get_db),
    racfid: str = Depends(lambda: None),
    roles: List[str] = Depends(lambda: None),
):
    """Creates a new Watchlist."""

    try:
        created_watchlist = WatchlistModel(
            description=watchlist.description,
            racf=racfid,
            title=watchlist.title,
        )
        database.add(created_watchlist)

        org_ids = get_org_ids_for_user(roles)

        for instance_id in watchlist.instances:
            instance = InstanceModel.find_by_pcf_guid_and_org(
                instance_id, org_ids, racfid, database
            )
            if instance:
                created_watchlist.instances.append(instance)

        if watchlist.isDefault:
            WatchlistModel.remove_default_flag(racfid, database)
            created_watchlist.is_default = 1

        database.commit()
        database.flush()

        return respond_ok(
            response,
            watchlist=created_watchlist.to_json(),
        )
    except Exception as ex:
        return respond_server_error(response, error=str(ex))


@router.put('/make-default/{watchlist_id}')
@protected_endpoint()
async def change_default_watchlist(
    request: Request,
    response: Response,
    watchlist_id: str,
    database: Session = Depends(get_db),
    racfid: str = Depends(lambda: None),
    roles: List[str] = Depends(lambda: None),
):
    """Get a single Watchlist by ID."""

    try:
        retrieved_watchlist = WatchlistModel.get_by_id(watchlist_id, database)

        if not retrieved_watchlist:
            return respond_not_found(
                response, f'No Watchlist found for ID "{watchlist_id}"'
            )

        if retrieved_watchlist.racf != racfid:
            return respond_unauthorised(
                response, 'You are not the owner of this Watchlist'
            )

        WatchlistModel.remove_default_flag(racfid, database)
        retrieved_watchlist.is_default = 1

        database.commit()
        database.flush()

        return respond_created(
            response,
            watchlist=retrieved_watchlist.to_json(),
        )
    except Exception as ex:
        return respond_server_error(response, error=str(ex))


@router.get('/{watchlist_id}')
@protected_endpoint()
async def get_watchlist_by_id(
    request: Request,
    response: Response,
    watchlist_id: str,
    database: Session = Depends(get_db),
    racfid: str = Depends(lambda: None),
    roles: List[str] = Depends(lambda: None),
):
    """Get a single Watchlist by ID."""

    try:
        retrieved_watchlist = WatchlistModel.get_by_id(watchlist_id, database)

        if not retrieved_watchlist:
            return respond_not_found(
                response, f'No Watchlist found for ID "{watchlist_id}"'
            )

        if retrieved_watchlist.racf != racfid:
            return respond_unauthorised(
                response, 'You are not the owner of this Watchlist'
            )

        return respond_ok(
            response,
            watchlist=retrieved_watchlist.to_json(),
        )
    except Exception as ex:
        return respond_server_error(response, error=str(ex))


@router.put('/{watchlist_id}')
@protected_endpoint()
async def update_watchlist(
    request: Request,
    response: Response,
    watchlist: PostWatchlist,
    watchlist_id: str,
    database: Session = Depends(get_db),
    racfid: str = Depends(lambda: None),
    roles: List[str] = Depends(lambda: None),
):
    """Get a single Watchlist by ID."""

    try:
        retrieved_watchlist = WatchlistModel.get_by_id(watchlist_id, database)

        if not retrieved_watchlist:
            return respond_not_found(
                response, f'No Watchlist found for ID "{watchlist_id}"'
            )

        if retrieved_watchlist.racf != racfid:
            return respond_unauthorised(
                response, 'You are not the owner of this Watchlist'
            )

        next_instances = []

        org_ids = get_org_ids_for_user(roles)

        for instance_id in watchlist.instances:
            instance = InstanceModel.find_by_pcf_guid_and_org(
                instance_id, org_ids, racfid, database
            )
            if instance:
                next_instances.append(instance)

        retrieved_watchlist.description = watchlist.description
        retrieved_watchlist.instances = next_instances
        retrieved_watchlist.title = watchlist.title

        if watchlist.isDefault:
            WatchlistModel.remove_default_flag(racfid, database)
            retrieved_watchlist.is_default = 1

        database.commit()
        database.flush()

        return respond_ok(
            response,
            watchlist=retrieved_watchlist.to_json(),
        )
    except Exception as ex:
        return respond_server_error(response, error=str(ex))


@router.delete('/{watchlist_id}')
@protected_endpoint()
async def delete_watchlist(
    request: Request,
    response: Response,
    watchlist_id: str,
    database: Session = Depends(get_db),
    racfid: str = Depends(lambda: None),
    roles: List[str] = Depends(lambda: None),
):
    """Get a single Watchlist by ID."""

    try:
        retrieved_watchlist = WatchlistModel.get_by_id(watchlist_id, database)

        if not retrieved_watchlist:
            return respond_not_found(
                response, f'No Watchlist found for ID "{watchlist_id}"'
            )

        if retrieved_watchlist.racf != racfid:
            return respond_unauthorised(
                response, 'You are not the owner of this Watchlist'
            )

        database.delete(retrieved_watchlist)
        database.commit()
        database.flush()

        return respond_ok(
            response,
            watchlist=retrieved_watchlist.to_json(),
        )
    except Exception as ex:
        return respond_server_error(response, error=str(ex))
