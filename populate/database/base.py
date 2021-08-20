import ormar
from populate.database.db import database, metadata


class BaseMeta(ormar.ModelMeta):
    database = database
    metadata = metadata
