from datetime import datetime
from time import mktime
from typing import List

from sqlalchemy import and_
from sqlalchemy.dialects.postgresql import BYTEA, DOUBLE_PRECISION
from sqlalchemy.dialects.oracle import DATE, NUMBER, NVARCHAR2, RAW
from sqlalchemy.orm import Mapped, mapped_column, relationship, Session
from sqlalchemy.types import BLOB, DOUBLE, INTEGER, FLOAT, TEXT

from config.database import ORMBase
from config.variables import timezone

from models.instance_attrs_model import InstanceAttrModel

from utils.orm_utils import default_uuid


class InstanceModel(ORMBase):
    """Represents an individual PCF instance with optional information overrides."""

    __tablename__ = 'PDB_INSTANCE'

    contact_info: Mapped[str] = mapped_column(
        NVARCHAR2(2000).with_variant(TEXT, 'sqlite', 'postgresql'), nullable=True
    )
    created_at: Mapped[datetime] = mapped_column(
        DATE, nullable=False, default=lambda: datetime.now(timezone)
    )
    instance_id: Mapped[bytes] = mapped_column(
        RAW(16).with_variant(BLOB, 'sqlite').with_variant(BYTEA, 'postgresql'),
        default=default_uuid,
        nullable=False,
        primary_key=True,
        unique=True,
    )
    message: Mapped[str] = mapped_column(
        NVARCHAR2(1000).with_variant(TEXT, 'sqlite', 'postgresql'), nullable=True
    )
    pcf_app_name: Mapped[str] = mapped_column(
        NVARCHAR2(255).with_variant(TEXT, 'sqlite', 'postgresql'), nullable=False
    )
    pcf_cpu: Mapped[float] = mapped_column(
        NUMBER().with_variant(FLOAT, 'sqlite', 'postgresql'), nullable=True
    )
    pcf_guid: Mapped[str] = mapped_column(
        NVARCHAR2(255).with_variant(TEXT, 'sqlite', 'postgresql'),
        nullable=False,
        unique=True,
    )
    pcf_space_id: Mapped[str] = mapped_column(
        NVARCHAR2(20).with_variant(TEXT, 'sqlite', 'postgresql'), nullable=False
    )
    pcf_org_id: Mapped[str] = mapped_column(
        NVARCHAR2(20).with_variant(TEXT, 'sqlite', 'postgresql'), nullable=False
    )
    pcf_instances_total: Mapped[int] = mapped_column(
        NUMBER().with_variant(INTEGER, 'sqlite', 'postgresql'),
        nullable=False,
        default=1,
    )
    pcf_ram: Mapped[float] = mapped_column(
        NUMBER().with_variant(FLOAT, 'sqlite', 'postgresql'), nullable=True
    )
    readable_name: Mapped[str] = mapped_column(
        NVARCHAR2(255).with_variant(TEXT, 'sqlite', 'postgresql'), nullable=True
    )
    status: Mapped[str] = mapped_column(
        NVARCHAR2(20).with_variant(TEXT, 'sqlite', 'postgresql'),
        nullable=False,
        default='UNKNOWN',
    )
    tick_override: Mapped[float] = mapped_column(
        NUMBER()
        .with_variant(DOUBLE, 'sqlite')
        .with_variant(DOUBLE_PRECISION, 'postgresql'),
        nullable=True,
    )
    updated_at: Mapped[datetime] = mapped_column(
        DATE, nullable=False, default=lambda: datetime.now(timezone)
    )

    instance_attr = relationship(
        InstanceAttrModel,
        primaryjoin='InstanceModel.pcf_guid == InstanceAttrModel.pcf_guid',
        lazy='selectin',
    )

    def to_json(self):
        return {
            'contactInfo': self.contact_info,
            'createdAt': mktime(self.created_at.timetuple())
            if self.created_at
            else None,
            'instanceId': self.instance_id.hex(),
            'message': self.message,
            'pcfAppName': self.pcf_app_name,
            'pcfCpu': self.pcf_cpu,
            'pcfInstancesTotal': self.pcf_instances_total,
            'pcfGuid': self.pcf_guid,
            'pcfOrganisationId': self.pcf_org_id,
            'pcfRam': self.pcf_ram,
            'pcfSpaceId': self.pcf_space_id,
            'readableName': self.readable_name,
            'status': self.status,
            'tickOverride': self.tick_override,
            'updatedAt': mktime(self.updated_at.timetuple())
            if self.updated_at
            else None,
            'userOverrides': self.instance_attr[0].to_json()
            if self.instance_attr and len(self.instance_attr)
            else None,
        }

    @classmethod
    def find_by_app_id(cls, instance_id: str, racf: str, database: Session):
        """Queries a single Instance by the application ID."""
        return (
            database.query(cls)
            .filter_by(instance_id=bytes.fromhex(instance_id))
            .outerjoin(
                InstanceAttrModel,
                and_(
                    InstanceAttrModel.pcf_guid == cls.pcf_guid,
                    InstanceAttrModel.racf == racf,
                ),
            )
            # .options(contains_eager(cls.instance_id))
            .first()
        )

    @classmethod
    def find_by_pcf_guid(cls, pcf_guid: str, racf: str, database: Session):
        """Queries a single Instance by the PCF ID."""
        return (
            database.query(cls)
            .filter_by(pcf_guid=pcf_guid)
            .outerjoin(
                InstanceAttrModel,
                and_(
                    InstanceAttrModel.pcf_guid == cls.pcf_guid,
                    InstanceAttrModel.racf == racf,
                ),
            )
            # .options(contains_eager(cls.instance_id))
            .first()
        )

    @classmethod
    def find_by_pcf_guid_and_org(
        cls, pcf_guid: str, org_ids: List[str], racf: str, database: Session
    ):
        """Queries an instance by PCF ID but only if the organisation ID is in the permitted list."""
        return (
            database.query(cls)
            .filter_by(pcf_guid=pcf_guid)
            .filter(cls.pcf_org_id.in_(org_ids))
            .outerjoin(
                InstanceAttrModel,
                and_(
                    InstanceAttrModel.pcf_guid == cls.pcf_guid,
                    InstanceAttrModel.racf == racf,
                ),
            )
            # .options(contains_eager(cls.instance_id))
            .first()
        )

    @classmethod
    def find_by_org_id_list(cls, org_ids: List[str], racf: str, database: Session):
        """Queries all instances belonging to a given organisation ID."""
        return (
            database.query(cls)
            .filter(cls.pcf_org_id.in_(org_ids))
            .outerjoin(
                InstanceAttrModel,
                and_(
                    InstanceAttrModel.pcf_guid == cls.pcf_guid,
                    InstanceAttrModel.racf == racf,
                ),
            )
            # .options(contains_eager(cls.instance_id))
            .all()
        )

    @classmethod
    def find_all(cls, racf: str, database: Session):
        """Queries all instances held by the system."""
        return (
            database.query(cls)
            .outerjoin(
                InstanceAttrModel,
                and_(
                    InstanceAttrModel.pcf_guid == cls.pcf_guid,
                    InstanceAttrModel.racf == racf,
                ),
            )
            # .options(contains_eager(cls.instance_id))
            .all()
        )
