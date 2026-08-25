from config.database import engine, ORMBase

import models  # noqa: F401

ORMBase.metadata.create_all(engine)
