"""Handles all responses on the base endpoint "/"."""

from fastapi import (
    APIRouter,
    Request,
    Response,
)
from utils.responses import respond_ok

router = APIRouter()


@router.get('/')
def get_root(request: Request, response: Response):
    """Fallback endpoint for the root of the API."""
    return respond_ok(response)
