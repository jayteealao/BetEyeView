from mangum import Mangum
from fastapi import FastAPI
import os
from beteyeview.crud.read import read_match_all, read_by_league, read_bet9ja
from beteyeview.database import database, engine, metadata
from beteyeview.models.match import Match
from typing import List

# deployed, the application will be accessible with an endpoint that has this shape: https://XXXXXXX.execute-api.eu-west-1.amazonaws.com/stage.
# Out, to generate the documentation, FastAPI needs, by default, to be served through a domain, not a path.
# To solve this problem, we will modify the python code https://adem.sh/blog/tutorial-fastapi-aws-lambda-serverless

stage = os.environ.get("STAGE", None)
openapi_prefix = f"/{stage}" if stage else "/"

app = FastAPI(title="BetEyeView_server", openapi_prefix=openapi_prefix)
app.state.database = database


@app.on_event("startup")
async def startup():
    metadata.create_all(bind=engine)
    database_ = app.state.database
    if not database_.is_connected:
        await database_.connect()


@app.on_event("shutdown")
async def shutdown():
    database_ = app.state.database
    if database_.is_connected:
        await database_.disconnect()


@app.get("/")
async def root():
    return {"hello": "world"}


@app.get(
    "/league/{league_name}",
    response_model=List[Match],
    response_model_exclude={
        "bet9jaodds__match",
        "betkingodds__match",
        "nairabetodds__match",
    },
)
async def get_league(league_name: str):
    return await read_by_league(league_name)


@app.get(
    "/matches",
    response_model=List[Match],
    response_model_exclude={
        "bet9jaodds__match",
        "betkingodds__match",
        "nairabetodds__match",
    },
)
async def get_all(league_name: str):
    return await read_match_all(league_name)


handler = Mangum(app)
