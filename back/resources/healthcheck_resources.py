"""Handles all responses on the base endpoint "/instance"."""

from typing import List

from fastapi import (
    APIRouter,
    Depends,
    Request,
    Response,
)
from sqlalchemy import text
from sqlalchemy.orm import Session
from loguru import logger

from config.database import get_db

from utils.responses import (
    respond_ok,
    respond_server_error,
)

router = APIRouter()


@router.get('/api/health')
async def get_all_instances(
    request: Request,
    response: Response,
    database: Session = Depends(get_db),
    racfid: str = Depends(lambda: None),
    roles: List[str] = Depends(lambda: None),
):
    """Retrieves a list of all instances stored within the system."""

    try:
        database.execute(text('select 1'))
        return respond_ok(
            response,
        )
    except Exception as ex:
        logger.error('Health check failed for reason: ')
        logger.error(str(ex))
        return respond_server_error(response, error=str(ex))
