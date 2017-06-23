from datetime import datetime

SEASONS = {
    "2010": (datetime(2010, 3, 20, 14, 32), datetime(2010, 6, 21, 8, 28),
             datetime(2010, 9, 23, 0, 9), datetime(2010, 12, 21, 20, 38)),
    "2011": (datetime(2011, 3, 20, 20, 21), datetime(2011, 6, 21, 14, 16),
             datetime(2011, 9, 23, 6, 4), datetime(2011, 12, 22, 2, 30)),
    "2012": (datetime(2012, 3, 20, 2, 14), datetime(2012, 6, 20, 20, 9),
             datetime(2012, 9, 22, 11, 49), datetime(2012, 12, 21, 8, 11)),
    "2013": (datetime(2013, 3, 20, 8, 2), datetime(2013, 6, 21, 2, 4),
             datetime(2013, 9, 22, 17, 44), datetime(2013, 12, 21, 14, 11)),
    "2014": (datetime(2014, 3, 20, 13, 57), datetime(2014, 6, 21, 7, 51),
             datetime(2014, 9, 22, 23, 29), datetime(2014, 12, 21, 20, 3)),
    "2015": (datetime(2015, 3, 20, 19, 45), datetime(2015, 6, 21, 13, 38),
             datetime(2015, 9, 23, 5, 20), datetime(2015, 12, 22, 1, 48)),
    "2016": (datetime(2016, 3, 20, 1, 30), datetime(2016, 6, 20, 19, 34),
             datetime(2016, 9, 22, 11, 21), datetime(2016, 12, 21, 7, 44)),
    "2017": (datetime(2017, 3, 20, 7, 29), datetime(2017, 6, 21, 1, 24),
             datetime(2017, 9, 22, 17, 2), datetime(2017, 12, 21, 13, 28)),
    "2018": (datetime(2018, 3, 20, 13, 15), datetime(2018, 6, 21, 7, 7),
             datetime(2018, 9, 22, 22, 54), datetime(2018, 12, 21, 19, 23)),
    "2019": (datetime(2019, 3, 20, 18, 58), datetime(2019, 6, 21, 12, 54),
             datetime(2019, 9, 23, 4, 50), datetime(2019, 12, 22, 1, 19)),
    "2020": (datetime(2020, 3, 20, 0, 50), datetime(2020, 6, 20, 18, 44),
             datetime(2020, 9, 22, 10, 31), datetime(2020, 12, 21, 7, 2))
}


def get_season(date):
    """
    Gets Brazilian Season from date
    :param date: datetime.date
    """
    outono, inverno, primavera, verao = SEASONS[date.strftime("%Y")]
    if outono < date <= inverno:
        return u"Outono"
    elif inverno < date <= primavera:
        return u"Inverno"
    elif primavera < date <= verao:
        return u"Primavera"
    else:
        return u"Verão"
