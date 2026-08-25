from datetime import datetime
from typing import List

from sqlalchemy.orm import Mapped, mapped_column, Session
from sqlalchemy.dialects.oracle import DATE, NVARCHAR2, RAW
from sqlalchemy.dialects.postgresql import BYTEA
from sqlalchemy.types import BLOB, TEXT

from config.database import ORMBase
from config.variables import timezone

from utils.orm_utils import default_uuid


class UserModel(ORMBase):
    """Represents a system user."""

    __tablename__ = 'PDB_USER'

    areas: Mapped[str] = mapped_column(
        NVARCHAR2(255).with_variant(TEXT, 'sqlite', 'postgresql'),
        nullable=False,
        default='',
    )
    created_on: Mapped[datetime] = mapped_column(
        DATE, nullable=False, default=lambda: datetime.now(timezone)
    )
    password: Mapped[str] = mapped_column(
        NVARCHAR2(100).with_variant(TEXT, 'sqlite', 'postgresql'), nullable=False
    )
    readable_name: Mapped[str] = mapped_column(
        NVARCHAR2(100).with_variant(TEXT, 'sqlite', 'postgresql'), nullable=False
    )
    user_id: Mapped[bytes] = mapped_column(
        RAW(16).with_variant(BLOB, 'sqlite').with_variant(BYTEA, 'postgresql'),
        default=default_uuid,
        nullable=False,
        primary_key=True,
        unique=True,
    )
    username: Mapped[str] = mapped_column(
        NVARCHAR2(100).with_variant(TEXT, 'sqlite', 'postgresql'), nullable=False
    )

    def __repr__(self):
        return f'<UserModel \
areas={self.get_roles_as_list()} \
created_on={self.created_on} \
password={self.password} \
readable_name={self.readable_name} \
user_id={self.user_id.hex() if self.user_id else None} \
username={self.username} />'

    def to_json(self):
        return {
            'areas': self.get_roles_as_list(),
            'createdOn': self.created_on,
            'readableName': self.readable_name,
            'userId': self.user_id.hex() if self.user_id else None,
            'username': self.username,
        }

    def get_roles_as_list(self) -> List[str]:
        return self.areas.split(',')

    @classmethod
    def find_by_username(cls, username: str, database: Session):
        return database.query(cls).filter_by(username=username).first()
