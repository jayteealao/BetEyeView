from NaijaBet_Api.bookmakers import bet9ja, betking, nairabet


def clean_odds(list_of_dicts: list):
    """
    clean_odds: giving a list of dicts containing match information and odds
    reurns a dict the conforms to the book ormar models

    Args:
        list_of_dicts (list): [description]

    Returns:
        [type]: [description]
    """
    # print(list_of_dicts)

    def retreiver(event):
        # print(event)
        data = {'book_id': event['match_id'],
                "home": event['home'],
                "draw": event['draw'],
                "away": event['away'],
                "home_or_draw": event['home_or_draw'],
                "home_or_away": event['home_or_away'],
                "draw_or_away": event['draw_or_away'],
                }
        for k, v in data.items():
            if v is None:
                data[k] = '0.0'
        return data
        
    res = {}
    if len(list_of_dicts) > 0:
        res = retreiver(list_of_dicts[0])

    else:
        res = {}
    return res


def retrieve_data():
    """
    retrieve_data uses the NaijaBet API to retrieve data from bet9ja, betking and nairabet,
    reshapes the data into a list of tuples and returns it

    Returns:
        [type]: a list of dicts containing match information and odds
    """

    b9_data = bet9ja.Bet9ja().get_all()
    bk_data = betking.Betking().get_all()
    nb_data = nairabet.Nairabet().get_all()

    b9_data.sort(key=lambda x: x['match'])
    bk_data.sort(key=lambda x: x['match'])
    nb_data.sort(key=lambda x: x['match'])

    max_data = max(b9_data, bk_data, nb_data, key=len)
    # pprint(max_data)

    # pprint(b9_data)
    # pprint(bk_data)
    # pprint(nb_data)
    res = []

    for event in max_data:
        b9_match = clean_odds(list(filter(lambda x: x['match'] == event['match'], b9_data)))
        bk_match = clean_odds(list(filter(lambda x: x['match'] == event['match'], bk_data)))
        nb_match = clean_odds(list(filter(lambda x: x['match'] == event['match'], nb_data)))
        # print(b9_match, bk_match, nb_match)

        # pprint(b9_odds)
        data = (
            {
                'match': event['match'],
                'match_date': event['time'],
                'league': event['league'],
            },
            {
                **b9_match,
            },
            {
                **bk_match,
            },
            {
                **nb_match,
            })
        res.append(data)
    # pprint(res)
    return res
