from pprint import pprint
from beteyeview.crud.bookies_data import retrieve_data
from beteyeview.models.match import Match
from beteyeview.models.book import Bet9jaOdd, BetkingOdd, NairabetOdd


async def populate_tables():

    data = retrieve_data()

    for event, b9, bk, nb in data:
        match = await Match.objects.update_or_create(**event)
        pk = match.pk
        if b9 != {}:
            await Bet9jaOdd.objects.get_or_create(match=pk, **b9)
        if bk != {}:
            await BetkingOdd.objects.get_or_create(match=pk, **bk)
        if nb != {}:
            await NairabetOdd.objects.get_or_create(match=pk, **nb)

    # print(await Bet9jaOdd.objects.count())
    # b9 = await Bet9jaOdd.objects.get_or_create(**{'match': pk, 'book_id': 145087782, 'home': '3.6', 'draw': '3.15', 'away': '2.1', 'home_or_away': '1.28', 'home_or_draw': '1.6', 'draw_or_away': '1.21'})
    # pprint(b9)
    # print(await Bet9jaOdd.objects.count())

    # print(await Match.objects.all())
    # pprint(await Bet9jaOdd.objects.all())
    # pprint('space')
    # pprint(await Bet9jaOdd.objects.select_all(follow=True).all())
    # print(await BetkingBook.objects.all())
    # print(await NairabetBook.objects.all())
