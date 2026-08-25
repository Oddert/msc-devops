from sqlalchemy import ForeignKey
from sqlalchemy.dialects.postgresql import BYTEA
from sqlalchemy.dialects.oracle import NVARCHAR2, RAW
from sqlalchemy.orm import Mapped, mapped_column, Session
from sqlalchemy.types import BLOB, TEXT

from config.database import ORMBase

from utils.orm_utils import default_uuid


class InstanceAttrModel(ORMBase):
    """Represents additional details associated with an instance for a particular user."""

    __tablename__ = 'PDB_INSTANCE_ATTR'

    description: Mapped[str | None] = mapped_column(
        NVARCHAR2(255).with_variant(TEXT, 'sqlite', 'postgresql'), nullable=True
    )
    instance_attrs_id: Mapped[bytes] = mapped_column(
        RAW(16).with_variant(BLOB, 'sqlite').with_variant(BYTEA, 'postgresql'),
        default=default_uuid,
        nullable=False,
        primary_key=True,
        unique=True,
    )
    pcf_guid: Mapped[str] = mapped_column(
        NVARCHAR2(255).with_variant(TEXT, 'sqlite', 'postgresql'),
        ForeignKey('PDB_INSTANCE.pcf_guid'),
        nullable=False,
    )
    racf: Mapped[str] = mapped_column(
        NVARCHAR2(20).with_variant(TEXT, 'sqlite', 'postgresql'), nullable=False
    )
    readable_name: Mapped[str | None] = mapped_column(
        NVARCHAR2(255).with_variant(TEXT, 'sqlite', 'postgresql'), nullable=True
    )

    def to_json(self):
        """Returns a JSON-serialisable representation of the instance."""
        return {
            'description': self.description,
            'instanceAttrId': self.instance_attrs_id.hex(),
            'pcfGuid': self.pcf_guid,
            'readableName': self.readable_name,
        }

    @classmethod
    def find_by_pcf_guid(cls, pcf_guid: str, racfid: str, database: Session):
        """Queries an record by PCF ID for a specific user."""
        return database.query(cls).filter_by(pcf_guid=pcf_guid, racf=racfid).first()
