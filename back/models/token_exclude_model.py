from datetime import datetime

from sqlalchemy.orm import Mapped, mapped_column, Session
from sqlalchemy.dialects.oracle import DATE, NVARCHAR2
from sqlalchemy.types import TEXT

from config.database import ORMBase


class TokenExcludeModel(ORMBase):
    """
    Represents a JWT which has been added to the exclude-list.
    Used by the authentication system to block tokens which have been replaced using token refresh logic.
    """

    __tablename__ = 'PDB_TOKEN_EXCLUDE'

    expires: Mapped[datetime] = mapped_column(
        DATE,
        nullable=False,
    )
    jti: Mapped[str] = mapped_column(
        NVARCHAR2(36).with_variant(TEXT, 'sqlite', 'postgresql'),
        nullable=False,
        primary_key=True,
    )

    def __repr__(self):
        return f'<TokenExcludeModel \
expires={self.expires} \
jti={self.jti} />'

    @classmethod
    def find_by_jti(cls, jti: str, database: Session):
        return database.query(cls).filter_by(jti=jti).first()
