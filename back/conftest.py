"""
pytest configuration for devops-demo backend tests.

Patches config.database with an in-memory SQLite engine before any app
modules are imported, so CI never needs a live Postgres connection.
"""

import os
import sys

# ── Required env vars (must be set before config.variables is imported) ──────
os.environ.setdefault('JWT_ACCESS_SECRET', 'ci-test-access-secret')
os.environ.setdefault('JWT_REFRESH_SECRET', 'ci-test-refresh-secret')
os.environ.setdefault('PG_USERNAME', 'test')
os.environ.setdefault('PG_PASSWORD', 'test')
os.environ.setdefault('PG_HOST', 'localhost')
os.environ.setdefault('PG_PORT', '5432')
os.environ.setdefault('PG_DATABASE', 'testdb')

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy.pool import StaticPool

# ── Build the test engine ────────────────────────────────────────────────────
test_engine = create_engine(
    'sqlite://',
    connect_args={'check_same_thread': False},
    poolclass=StaticPool,
)

ORMBase = declarative_base()

TestingSessionLocal = sessionmaker(
    autocommit=False, autoflush=False, bind=test_engine
)


def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()


# ── Stub config.database before any app module imports it ───────────────────
import types

db_module = types.ModuleType('config.database')
db_module.engine = test_engine
db_module.ORMBase = ORMBase
db_module.SessionLocal = TestingSessionLocal
db_module.get_db = override_get_db

sys.modules['config.database'] = db_module
