from datetime import datetime
import ormar
from pydantic.typing import Optional, ForwardRef
from beteyeview.database.base import BaseMeta
from sqlalchemy import func


class Match(ormar.Model):
    class Meta(BaseMeta):
        tablename = "matches"

    id: int = ormar.Integer(primary_key=True)
    match: str = ormar.String(nullable=False, max_length=255)
    # consider removing or reconsidering match_date, if match_date changes a new match will be created
    # which isnt the behaviour we want, consider making it a pydantic only field, or putting it in a separate table
    match_date: str = ormar.DateTime(nullable=False, timezone=True)
    league: str = ormar.String(nullable=False, max_length=255)
    # bet9ja_id: Optional[int] = ormar.Integer(nullable=True)
    # betking_id: Optional[int] = ormar.Integer(nullable=True)
    # nairabet_id: Optional[int] = ormar.Integer(nullable=True)
    created_at: datetime = ormar.DateTime(server_default=func.now())
    # created_at: str = ormar.DateTime(nullable=False, default=datetime.datetime.now(), timezone=True)
    # updated_at: str = ormar.DateTime(nullable=False, default=datetime.datetime.now(), timezone=True)


# class TestTable(ormar.Model):
#     class Meta(BaseMeta):
#         tablename = 'tests'

#     id: int = ormar.Integer(primary_key=True)
#     created_at: datetime = ormar.DateTime(server_default=func.now())
