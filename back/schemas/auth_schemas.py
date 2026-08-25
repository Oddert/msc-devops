from typing import List
from pydantic import BaseModel, Field


class PostLogin(BaseModel):
    username: str = Field(
        ...,
        title='Username',
        description="User's RACFID equivalent for prototyping.",
        min_length=3,
        max_length=30,
    )
    password: str = Field(
        ...,
        title='Password',
        description="The user's chosen password.",
        min_length=6,
        max_length=50,
    )


class PostSignup(PostLogin):
    readableName: str | None = Field(
        None,
        title='Readable Name',
        description="The user's real name or alias to be displayed as-is in the application.",
        min_length=1,
        max_length=50,
    )
    areas: List[str] = Field(
        [],
        title='Auth areas',
        description="Auth areas the user is allowed access to. NOTE: This is unrestriced as this is a prototype and so the user's should be treated as test-users.",
    )


class PostTokenRefresh(BaseModel):
    refreshToken: str = Field(
        ...,
        title='Refresh Token',
        description="The user's refresh token issued at point of authentication.",
        min_length=50,
        max_length=200,
    )
