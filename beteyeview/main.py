from beteyeview.models.book import Bet9jaOdd, BetkingOdd, NairabetOdd
from mangum import Mangum
from fastapi import FastAPI
import os
check = os.environ.get('AWS_REGION', None)

if check is None:
    import sys
    sys.path.append("C:/Users/HP/Documents/dev/BetEyeView")
    print(sys.path)

from beteyeview.crud.read import read_bet9ja_by_match, read_betking_by_match, read_match_all, read_match_by_id, read_match_by_league, read_bet9ja, read_match_basic, read_nairabet_by_match # noqa
from beteyeview.database import database, engine, metadata # noqa
from beteyeview.models.match import Match # noqa
from typing import List # noqa

# deployed, the application will be accessible with an endpoint that has this shape: 
# https://XXXXXXX.execute-api.eu-west-1.amazonaws.com/stage.
# Out, to generate the documentation, FastAPI needs, by default, to be served through a domain, not a path.
# To solve this problem, we will modify the python code https://adem.sh/blog/tutorial-fastapi-aws-lambda-serverless

stage = os.environ.get("STAGE", None)
openapi_prefix = f"/{stage}" if stage else "/"

app = FastAPI(title="BetEyeView_server", root_path=openapi_prefix)
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
    "/matches",
    response_model=List[Match],
    response_model_exclude={
        "bet9jaodds__match",
        "betkingodds__match",
        "nairabetodds__match",
    },
)
async def get_all():
    return await read_match_all()


@app.get("matches/basic", response_model=List[Match])
async def get_basic_test():
    return await read_match_basic()


@app.get("matches/{id}", response_model=Match)
async def get_match_info_by_id(id: int):
    return await read_match_by_id(id)


@app.get(
    "matches/league/{league_name}",
    response_model=List[Match],
    response_model_exclude={
        "bet9jaodds__match",
        "betkingodds__match",
        "nairabetodds__match",
    },
)
async def get_league(league_name: str):
    return await read_match_by_league(league_name)


@app.get(
    "odds/b9/{match_id}",
    response_model=List[Match],
)
async def get_bet9ja_match_odds(match_id: int):
    return await read_bet9ja_by_match(match_id)


@app.get(
    "odds/bk/{match_id}",
    response_model=List[Match],
)
async def get_betking_match_odds(match_id: int):
    return await read_betking_by_match(match_id)


@app.get(
    "odds/nb/{match_id}",
    response_model=List[Match],
)
async def get_nairabet_match_odds(match_id: int):
    return await read_nairabet_by_match(match_id)


@app.get(
    "odds/{match_id}",
    response_model=List[Bet9jaOdd, BetkingOdd, NairabetOdd],
)
async def get_odds_by_match(match_id: int):
    b9 = await read_bet9ja_by_match(match_id)
    bk = await read_betking_by_match(match_id)
    nb = await read_nairabet_by_match(match_id)

    return [b9, bk, nb]

handler = Mangum(app)
