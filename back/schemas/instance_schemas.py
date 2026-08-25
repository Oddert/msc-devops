from pydantic import BaseModel, Field


class PostInstanceAttr(BaseModel):
    description: str | None = Field(
        None,
        title='Description',
        description='Optional description for this Instance.',
        min_length=0,
        max_length=2000,
    )
    readableName: str | None = Field(
        None,
        title='Readable Name',
        description='Optional alias to name this Instance.',
        min_length=0,
        max_length=255,
    )
