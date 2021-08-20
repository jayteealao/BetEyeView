from mangum import Mangum
from fastapi import FastAPI

from populate.crud.create import populate_tables
from populate.crud.read import read_by_league
from populate.database import database, engine, metadata
from pprint import pprint

app = FastAPI()
app.state.database = database


@app.on_event("startup")
async def startup():
    metadata.create_all(bind=engine)
    database_ = app.state.database
    if not database_.is_connected:
        await database_.connect()
    await populate_tables()
    test = await read_by_league("Premier League")
    for match in test:
        pprint(match.match)


@app.on_event("shutdown")
async def shutdown():
    database_ = app.state.database
    if database_.is_connected:
        await database_.disconnect()
    # metadata.drop_all(bind=engine)


@app.get("/")
async def root():
    return {"hello": "world"}


handler = Mangum(app)