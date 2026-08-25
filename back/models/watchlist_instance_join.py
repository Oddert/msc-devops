from sqlalchemy import Column, ForeignKey, Table

from config.database import ORMBase

watchlist_instance_join = Table(
    'PDB_WATCHLIST_INSTANCE',
    ORMBase.metadata,
    Column('watchlist_id', ForeignKey('PDB_WATCHLIST.watchlist_id')),
    Column('instance_id', ForeignKey('PDB_INSTANCE.instance_id')),
)
