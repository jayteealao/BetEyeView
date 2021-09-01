from beteyeview.models.match import Match
from beteyeview.models.book import Bet9jaOdd, BetkingOdd, NairabetOdd
from datetime import datetime, timezone



async def read_match_all():
    return await Match.objects.prefetch_related(
        [Match.bet9jaodds, Match.betkingodds, Match.nairabetodds]).filter(
            Match.match_date > datetime.now(tz=timezone.utc)).order_by(
                Match.match_date.asc()).all()


async def read_match_basic():
    return await Match.objects.filter(
        Match.match_date > datetime.now(tz=timezone.utc)).order_by(
            Match.match_date.asc()).all()


async def read_match_by_league(league):
    return await Match.objects.select_all().filter(
        (Match.match_date > datetime.now(tz=timezone.utc)) & (Match.league.iexact(league))).order_by(
            Match.match_date.asc()).all()


async def read_match_by_id(match_id):
    return await Match.objects.select_all().filter(
        Match.id == match_id).order_by(
            Match.match_date.asc()).all()


async def read_bet9ja():
    return await Bet9jaOdd.objects.select_related('match').filter(
        Bet9jaOdd.match.match_date > datetime.now(tz=timezone.utc)).order_by(
            Bet9jaOdd.match.match_date.asc()).all()


async def read_bet9ja_by_league(league):
    return await Bet9jaOdd.objects.select_related('match').filter(
        (Bet9jaOdd.match.match_date > datetime.now(tz=timezone.utc)) & Bet9jaOdd.match.league.iexact(league)).order_by(
            Bet9jaOdd.match.match_date.asc()).all()


async def read_bet9ja_basic():
    return await Bet9jaOdd.objects.filter(
        Bet9jaOdd.match.match_date > datetime.now(tz=timezone.utc)).order_by(
            Bet9jaOdd.match.match_date.asc()).all()


async def read_bet9ja_by_match(match_id):
    return await Bet9jaOdd.objects.filter(
        Bet9jaOdd.match.id == match_id).order_by(
            Bet9jaOdd.match.match_date.asc()).all()


async def read_betking():
    return await BetkingOdd.objects.select_related('match').filter(
        BetkingOdd.match.match_date > datetime.now(tz=timezone.utc)).order_by(
            BetkingOdd.match.match_date.asc()).all()


async def read_betkingbet_by_league(league):
    return await BetkingOdd.objects.select_related('match').filter(
        (BetkingOdd.match.match_date > datetime.now(tz=timezone.utc)) & BetkingOdd.match.league.iexact(league)).order_by(
            BetkingOdd.match.match_date.asc()).all()


async def read_betking_basic():
    return await BetkingOdd.objects.filter(
        BetkingOdd.match.match_date > datetime.now(tz=timezone.utc)).order_by(
            BetkingOdd.match.match_date.asc()).all()


async def read_betking_by_match(match_id):
    return await BetkingOdd.objects.filter(
        BetkingOdd.match.id == match_id).order_by(
            BetkingOdd.match.match_date.asc()).all()


async def read_nairabet():
    return await NairabetOdd.objects.select_related('match').filter(
        NairabetOdd.match.match_date > datetime.now(tz=timezone.utc)).order_by(
            NairabetOdd.match.match_date.asc()).all()


async def read_nairabet_by_league(league):
    return await NairabetOdd.objects.select_related('match').filter(
        (NairabetOdd.match.match_date > datetime.now(tz=timezone.utc)) & NairabetOdd.match.league.iexact(league)).order_by(
            NairabetOdd.match.match_date.asc()).all()


async def read_nairabet_basic():
    return await NairabetOdd.objects.filter(
        NairabetOdd.match.match_date > datetime.now(tz=timezone.utc)).order_by(
            NairabetOdd.match.match_date.asc()).all()


async def read_nairabet_by_match(match_id):
    return await NairabetOdd.objects.filter(
        NairabetOdd.match.id == match_id).order_by(
            NairabetOdd.match.match_date.asc()).all()
