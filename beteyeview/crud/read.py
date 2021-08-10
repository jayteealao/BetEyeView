from beteyeview.models.match import Match
from beteyeview.models.book import Bet9jaOdd, BetkingOdd, NairabetOdd
from datetime import datetime


async def read_match_all():
    return await Match.objects.select_all().filter(
        Match.match_date > datetime.now()).order_by(
            Match.match_date.asc()).all() 


async def read_by_league(league):
    return await Match.objects.select_all().filter(
        Match.league.iexact(league)).order_by(
            Match.match_date.asc()).all()


async def read_bet9ja():
    return await Bet9jaOdd.objects.select_related('match').filter(
        Bet9jaOdd.match.match_date > datetime.now()).order_by(
            Bet9jaOdd.match.match_date.asc()).all()


async def read_betking():
    return await BetkingOdd.objects.select_related('match').filter(
        BetkingOdd.match.match_date > datetime.now()).order_by(
            BetkingOdd.match.match_date.asc()).all()


async def read_nairabet():
    return await NairabetOdd.objects.select_related('match').filter(
        NairabetOdd.match.match_date > datetime.now()).order_by(
            NairabetOdd.match.match_date.asc()).all()


async def read_bet9ja_by_league(league):
    return await Bet9jaOdd.objects.select_related('match').filter(
        (Bet9jaOdd.match.match_date > datetime.now()) & Bet9jaOdd.match.league.iexact(league)).order_by(
            Bet9jaOdd.match.match_date.asc()).all()


async def read_betkingbet_by_league(league):
    return await BetkingOdd.objects.select_related('match').filter(
        (BetkingOdd.match.match_date > datetime.now()) & BetkingOdd.match.league.iexact(league)).order_by(
            BetkingOdd.match.match_date.asc()).all()


async def read_nairabet_by_league(league):
    return await NairabetOdd.objects.select_related('match').filter(
        (NairabetOdd.match.match_date > datetime.now()) & NairabetOdd.match.league.iexact(league)).order_by(
            NairabetOdd.match.match_date.asc()).all()
