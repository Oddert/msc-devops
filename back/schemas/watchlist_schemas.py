from typing import List
from pydantic import BaseModel, Field


class PostWatchlist(BaseModel):
    description: str | None = Field(
        None,
        title='Description',
        description='Optional description for this watchlist.',
        min_length=0,
        max_length=2000,
    )
    instances: List[str] = Field(
        [],
        title='Instance IDs',
        description='Instances to be associated with this Watchlist.',
    )
    isDefault: bool = Field(
        False,
        title='Is Default',
        description='Set to true if this watchlist is to be set as the default.',
    )
    title: str = Field(
        ...,
        title='Title',
        description='Optional title for this watchlist.',
        min_length=0,
        max_length=255,
    )
