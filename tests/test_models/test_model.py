import pytest
import asyncio
import sqlalchemy
import datetime
import databases
import pydantic
from tests.settings import TEST_DATABASE_URL
from beteyeview.models.match import Match

metadata = sqlalchemy.MetaData()
database = databases.Database(TEST_DATABASE_URL, force_rollback=True)

match_fields = [
    'match_date',
    'id',
    'match',
    'league',
    'created_at']


@pytest.fixture(scope='module')
def event_loop():
    loop = asyncio.get_event_loop()
    yield loop
    loop.close()


@pytest.fixture(autouse=True, scope='module')
async def create_test_database():
    engine = sqlalchemy.create_engine(TEST_DATABASE_URL)
    metadata.create_all(engine)
    yield
    metadata.drop_all(engine)


@pytest.fixture()
def match():
    return Match(
        match='testmatch',
        match_date=datetime.datetime.now(),
        league='testleague',)


def test_not_nullable_field_is_required():
    with pytest.raises(pydantic.error_wrappers.ValidationError):
        Match(
            match_date=datetime.datetime.now(),
            league='testleague',)


def test_pydantic_model_is_created(match):
    assert issubclass(match.__class__, pydantic.BaseModel)
    assert all(field in match.__fields__ for field in match_fields)


def test_sqlalchemy_table_is_created(match):
    assert isinstance(match.Meta.table, sqlalchemy.sql.schema.Table)
    assert all(field in match.Meta.table.columns for field in match_fields)