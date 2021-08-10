import ormar
import json
from beteyeview.database.base import BaseMeta
from beteyeview.models.match import Match
from typing import Optional


class Bet9jaOdd(ormar.Model):
    class Meta(BaseMeta):
        table_name = 'bet9jaodds'

    # book_id: int = ormar.Integer(primary_key=True, autoincrement=False)
    # match_id: int = ormar.Integer()
    id: int = ormar.Integer(primary_key=True)
    book_id: int = ormar.Integer()
    match: Optional[Match] = ormar.ForeignKey(Match)
    # match_id: int = ormar.Integer()
    # name: str = ormar.String(nullable=False, max_length=255)
    # odds: json = ormar.JSON(nullable=False)
    home: str = ormar.String(nullable=False, max_length=5)
    draw: str = ormar.String(nullable=False, max_length=5)
    away: str = ormar.String(nullable=False, max_length=5)
    home_or_away: str = ormar.String(nullable=False, max_length=5)
    home_or_draw: str = ormar.String(nullable=False, max_length=5)
    draw_or_away: str = ormar.String(nullable=False, max_length=5)


class BetkingOdd(ormar.Model):
    class Meta(BaseMeta):
        table_name = 'betkingodds'

    id: int = ormar.Integer(primary_key=True)
    book_id: int = ormar.Integer()
    # match_id: int = ormar.Integer()
    # book_id: int = ormar.Integer(primary_key=True, autoincrement=False)
    match: Optional[Match] = ormar.ForeignKey(Match)
    # match_id: int = ormar.Integer()
    # name: str = ormar.String(nullable=False, max_length=255)
    # odds: json = ormar.JSON(nullable=False)
    home: float = ormar.Float(nullable=False, default=0.0)
    draw: float = ormar.Float(nullable=False, default=0.0)
    away: float = ormar.Float(nullable=False, default=0.0)
    home_or_away: float = ormar.Float(nullable=False, default=0.0)
    home_or_draw: float = ormar.Float(nullable=False, default=0.0)
    draw_or_away: float = ormar.Float(nullable=False, default=0.0)


class NairabetOdd(ormar.Model):
    class Meta(BaseMeta):
        table_name = 'nairabetodds'

    id: int = ormar.Integer(primary_key=True)
    book_id: int = ormar.Integer()
    # match_id: int = ormar.Integer()
    # book_id: int = ormar.Integer(primary_key=True, autoincrement=False)
    match: Optional[Match] = ormar.ForeignKey(Match)
    # match_id: int = ormar.Integer()
    # name: str = ormar.String(nullable=False, max_length=255)
    # odds: json = ormar.JSON(nullable=False)
    home: float = ormar.Float(nullable=False, default=0.0)
    draw: float = ormar.Float(nullable=False, default=0.0)
    away: float = ormar.Float(nullable=False, default=0.0)
    home_or_away: float = ormar.Float(nullable=False, default=0.0)
    home_or_draw: float = ormar.Float(nullable=False, default=0.0)
    draw_or_away: float = ormar.Float(nullable=False, default=0.0)
