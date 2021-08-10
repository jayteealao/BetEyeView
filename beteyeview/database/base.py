import ormar
from beteyeview.database.db import database, metadata


class BaseMeta(ormar.ModelMeta):
    database = database
    metadata = metadata
