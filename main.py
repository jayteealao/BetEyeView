
from beteyeview.crud.create import populate_tables
from beteyeview.crud.read import read_match_all, read_by_league, read_bet9ja
from fastapi import FastAPI
from beteyeview.database import database, engine, metadata
from beteyeview.models.match import Match, TestTable
from pprint import pprint

app = FastAPI()
app.state.database = database


@app.on_event("startup")
async def startup():
    database_ = app.state.database
    metadata.create_all(bind=engine)
    if not database_.is_connected:
        await database_.connect()
    await populate_tables()
    test = await read_by_league('Premier League')
    pprint(test)


@app.on_event("shutdown")
async def shutdown():
    database_ = app.state.database
    if database_.is_connected:
        await database_.disconnect()
    metadata.drop_all(bind=engine)


@app.get("/")
async def root():
    pass


@app.get("/league/{league_name}", response_model=list[Match], response_model_exclude={
    'bet9jaodds__match',
    'betkingodds__match',
    'nairabetodds__match'})
async def get_league(league_name: str):
    return await read_by_league(league_name)
    
