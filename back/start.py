"""Entry point for the application."""

from typing import Annotated
from jwt import ExpiredSignatureError, InvalidTokenError

from apscheduler.schedulers.asyncio import AsyncIOScheduler
from contextlib import asynccontextmanager
from fastapi import (
    Depends,
    FastAPI,
    status,
    WebSocket,
    WebSocketDisconnect,
    WebSocketException,
)
from loguru import logger
from sqlalchemy.orm import Session
from uvicorn import run

from config.database import get_db

from models.instance_model import InstanceModel

from resources import (
    auth_resources,
    healthcheck_resources,
    instance_resources,
    root_resources,
    watchlist_resources,
)

from security.middleware import CustomCorsMW, get_ws_token, verify_extracted_token
from starlette.responses import FileResponse
from security.roles import get_org_ids_for_user

from utils.exceptions import NeedsAuthorisation, NeedsLogin
from utils.schedulers import setup_async_schedulers
from utils.ws_manager import ws_manager


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Lifespan handler for the application, initialising jobs on startup."""
    # Initialise schedulers on app load.
    async_schedulers = setup_async_schedulers()
    app.state.scheduler = async_schedulers
    if async_schedulers:
        async_schedulers.start()
        logger.info(f'Schedulers started: {async_schedulers}')
    yield
    # Deactivate the app schedulers on app shutdown.
    scheduler: AsyncIOScheduler | None = app.state.scheduler
    if scheduler:
        scheduler.shutdown()


app = FastAPI(lifespan=lifespan)


@app.get('/voice')
def get_voice():
    return FileResponse('voice.html')


allowed_origins = [
    'http://localhost:8081',
    'http://localhost:5173',
    'ws://localhost:5173',
    'http://msc-dashboard-web-lb-1-1166048007.eu-north-1.elb.amazonaws.com',
    'https://msc-dashboard-web-lb-1-1166048007.eu-north-1.elb.amazonaws.com',
    'ws://msc-dashboard-web-lb-1-1166048007.eu-north-1.elb.amazonaws.com',
]


app.add_middleware(CustomCorsMW)

routes = [
    (auth_resources.router, 'Auth'),
    (instance_resources.router, 'Instances'),
    (root_resources.router, 'Root'),
    (watchlist_resources.router, 'Watchlist'),
]

app.include_router(healthcheck_resources.router, tags=['Health Check'])

for route, tags in routes:
    logger.info(f'Initialising route: {tags}')
    app.include_router(route, prefix='/api/v0', tags=[tags])


@app.websocket('/ws')
async def websocket_endpoint(
    *,
    websocket: WebSocket,
    token: Annotated[str, Depends(get_ws_token)],
    database: Session = Depends(get_db),
):
    """Handles WebSocket connections, subscribing a user to receive updates from their instances."""
    try:
        await websocket.accept()
        decoded_verified_token = verify_extracted_token(token)
        org_ids = get_org_ids_for_user(decoded_verified_token['roles'])
        instances = InstanceModel.find_by_org_id_list(org_ids, '', database)

        for instance in instances:
            ws_manager.register_listener(instance.pcf_guid, websocket)
        try:
            while True:
                await websocket.receive_text()
                # await ws_manager.broadcast_multiple_updates(instances)
        except WebSocketDisconnect:
            ws_manager.unregister_listener(websocket)
    except NeedsLogin:
        raise WebSocketException(code=status.WS_1008_POLICY_VIOLATION)
    except NeedsAuthorisation:
        raise WebSocketException(code=status.WS_1008_POLICY_VIOLATION)
    except ExpiredSignatureError:
        raise WebSocketException(code=status.WS_1008_POLICY_VIOLATION)
    except InvalidTokenError:
        raise WebSocketException(code=status.WS_1008_POLICY_VIOLATION)
    except ValueError:
        raise WebSocketException(code=status.WS_1008_POLICY_VIOLATION)


if __name__ == '__main__':
    run(
        'start:app',
        port=80,
        reload=True,
    )
