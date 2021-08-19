from pprint import pprint

from beteyeview.crud.bookies_data import retrieve_data
from beteyeview.models.book import Bet9jaOdd, BetkingOdd, NairabetOdd
from beteyeview.models.match import Match


async def populate_tables():

    data = retrieve_data()
# TODO add mechanism for adding date to odds table after creating it
    for event, b9, bk, nb in data:
        if not await Match.objects.get_or_none(match=event['match'], league=event['league']):
            match = await Match.objects.create(**event)
        else:
            match = await Match.objects.get(match=event['match'], league=event['league'])
        pk = match.pk
        if b9 != {}:
            data = {**b9, 'match': pk}
            await Bet9jaOdd.objects.get_or_create(**data)
        if bk != {}:
            data = {**bk, 'match': pk}
            await BetkingOdd.objects.get_or_create(**data)
        if nb != {}:
            data = {**nb, 'match': pk}
            await NairabetOdd.objects.get_or_create(**data)