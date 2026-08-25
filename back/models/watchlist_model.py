from sqlalchemy.dialects.postgresql import BYTEA
from sqlalchemy.dialects.oracle import NUMBER, NVARCHAR2, RAW
from sqlalchemy.orm import Mapped, mapped_column, relationship, Session
from sqlalchemy.types import BLOB, INTEGER, TEXT

from config.database import ORMBase

from utils.orm_utils import default_uuid

from models.watchlist_instance_join import watchlist_instance_join


class WatchlistModel(ORMBase):
    """Represents user Watchlist."""

    __tablename__ = 'PDB_WATCHLIST'

    description: Mapped[str | None] = mapped_column(
        NVARCHAR2(2000).with_variant(TEXT, 'sqlite', 'postgresql'),
        nullable=True,
        default='',
    )
    is_default: Mapped[int] = mapped_column(
        NUMBER(1).with_variant(INTEGER, 'sqlite', 'postgresql'),
        nullable=False,
        default=0,
    )
    title: Mapped[str] = mapped_column(
        NVARCHAR2(255).with_variant(TEXT, 'sqlite', 'postgresql'),
        nullable=True,
        default='',
    )
    racf: Mapped[str] = mapped_column(
        NVARCHAR2(20).with_variant(TEXT, 'sqlite', 'postgresql'), nullable=False
    )
    watchlist_id: Mapped[bytes] = mapped_column(
        RAW(16).with_variant(BLOB, 'sqlite').with_variant(BYTEA, 'postgresql'),
        default=default_uuid,
        nullable=False,
        primary_key=True,
        unique=True,
    )

    instances = relationship('InstanceModel', secondary=watchlist_instance_join)

    def to_json(self):
        """Returns a JSON-serialisable representation of the instance."""
        return {
            'description': self.description,
            'instances': [instance.pcf_guid for instance in self.instances],
            'isDefault': bool(self.is_default),
            'title': self.title,
            'racf': self.racf,
            'watchlistId': self.watchlist_id.hex(),
        }

    @classmethod
    def get_all_for_user(cls, racf: str, database: Session):
        """Queries all Watchlists belonging to a user."""
        return database.query(cls).filter_by(racf=racf).all()

    @classmethod
    def get_users_default(cls, racf: str, database: Session):
        """Gets a user's default watchlist."""
        return database.query(cls).filter_by(racf=racf, is_default=1).first()

    @classmethod
    def get_by_id(cls, watchlist_id: str, database: Session):
        """Queries a single watchlist by ID."""
        return (
            database.query(cls)
            .filter_by(watchlist_id=bytes.fromhex(watchlist_id))
            .first()
        )

    @classmethod
    def remove_default_flag(cls, racf: str, database: Session):
        """Removes the is_default flag from all Watchlists for a user."""
        return (
            database.query(cls)
            .filter_by(is_default=1, racf=racf)
            .update(values={'is_default': 0})
        )
