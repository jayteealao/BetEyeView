import pytest
from pprint import pprint
import sys

sys.path.append("C:/Users/HP/Documents/dev/BetEyeView")

import beteyeview  # noqa
from beteyeview.crud.bookies_data import retrieve_data  # noqa


class MockResponse:
    @staticmethod
    def mockreturn():
        return [
            {
                "away": 2.65,
                "draw": 2.95,
                "draw_or_away": 1.38,
                "home": 2.7,
                "home_or_away": 1.33,
                "home_or_draw": 1.39,
                "league": "Ligue 2",
                "league_id": 135910,
                "match": "Quevilly-Rouen - Dijon FCO",
                "match_id": 5205919,
                "time": 1628960400,
            },
            {
                "away": 3.4,
                "draw": 2.85,
                "draw_or_away": 1.5,
                "home": 2.28,
                "home_or_away": 1.34,
                "home_or_draw": 1.27,
                "league": "Ligue 2",
                "league_id": 135910,
                "match": "Paris FC - AJ Auxerre",
                "match_id": 5206885,
                "time": 1629139500,
            },
            {
                "away": 2.55,
                "draw": 3.0,
                "draw_or_away": None,
                "home": 2.8,
                "home_or_away": 1.32,
                "home_or_draw": 1.42,
                "league": "Ligue 2",
                "league_id": 135910,
                "match": "Quevilly-Rouen - SC Bastia",
                "match_id": 5225463,
                "time": 1629306000,
            },
        ]

    @staticmethod
    def get_all():
        print(MockResponse.mockreturn())
        return MockResponse.mockreturn()


def test_retreive_data(mocker):

    mocker.patch.object(
        beteyeview.crud.bookies_data.bet9ja.Bet9ja,
        "get_all",
        return_value=MockResponse.mockreturn(),
    )
    mocker.patch.object(
        beteyeview.crud.bookies_data.betking.Betking,
        "get_all",
        return_value=MockResponse.mockreturn(),
    )
    mocker.patch.object(
        beteyeview.crud.bookies_data.nairabet.Nairabet,
        "get_all",
        return_value=MockResponse.mockreturn(),
    )

    data = retrieve_data()
    pprint(data)
    assert len(data) == 3
    assert data[0][0]["league"] == "Ligue 2"
