from datetime import date
from datetime import datetime

from test_helper import Request

def team1_requests():
    return [
        Request((1, 1, 0, datetime(2016, 1, 1, 8, 0, 0), datetime(2016, 1, 1, 9, 59, 0), 1.5)),
        Request((1, 1, 1, datetime(2016, 1, 1, 10, 0, 0), datetime(2016, 1, 1, 12, 59, 0), 1.1)),
        Request((1, 1, 2, datetime(2016, 1, 1, 14, 0, 0), datetime(2016, 1, 1, 20, 59, 0), 0.3)),
        Request((1, 1, 3, datetime(2016, 1, 1, 12, 0, 0), datetime(2016, 1, 1, 20, 59, 0), 0.5)),
        Request((1, 1, 0, datetime(2016, 1, 2, 8, 0, 0), datetime(2016, 1, 2, 9, 0, 0), 0.5)),
        Request((1, 1, 1, datetime(2016, 1, 2, 12, 0, 0), datetime(2016, 1, 2, 14, 59, 0), 0.2)),
        Request((1, 1, 2, datetime(2016, 1, 2, 17, 0, 0), datetime(2016, 1, 2, 19, 59, 0), 0.3)),
        Request((1, 1, 3, datetime(2016, 1, 1, 10, 0, 0), datetime(2016, 1, 1, 20, 59, 0), 0.2)),
        Request((1, 1, 0, datetime(2016, 1, 3, 8, 0, 0), datetime(2016, 1, 3, 9, 0, 0), 0.4)),
        Request((1, 1, 1, datetime(2016, 1, 3, 12, 0, 0), datetime(2016, 1, 3, 14, 59, 0), 0.2)),
        Request((1, 1, 2, datetime(2016, 1, 3, 17, 0, 0), datetime(2016, 1, 3, 19, 59, 0), 0.8)),
        Request((1, 1, 3, datetime(2016, 1, 1, 14, 0, 0), datetime(2016, 1, 1, 20, 59, 0), 0.3)),
        Request((1, 1, 0, datetime(2016, 1, 4, 8, 0, 0), datetime(2016, 1, 4, 9, 0, 0), 0.9)),
        Request((1, 1, 1, datetime(2016, 1, 4, 12, 0, 0), datetime(2016, 1, 4, 14, 59, 0), 0.2)),
        Request((1, 1, 2, datetime(2016, 1, 4, 17, 0, 0), datetime(2016, 1, 4, 19, 59, 0), 0.3)),
        Request((1, 1, 3, datetime(2016, 1, 1, 9, 0, 0), datetime(2016, 1, 1, 12, 59, 0), 0.3)),
        Request((1, 1, 0, datetime(2016, 1, 5, 8, 0, 0), datetime(2016, 1, 5, 9, 0, 0), 0.1)),
        Request((1, 1, 1, datetime(2016, 1, 5, 12, 0, 0), datetime(2016, 1, 5, 14, 59, 0), 0.2)),
        Request((1, 1, 2, datetime(2016, 1, 1, 14, 0, 0), datetime(2016, 1, 1, 20, 59, 0), 0.3)),
        Request((1, 1, 3, datetime(2016, 1, 5, 12, 0, 0), datetime(2016, 1, 5, 23, 59, 0), 0.3)),
        Request((1, 1, 0, datetime(2016, 1, 6, 8, 0, 0), datetime(2016, 1, 6, 9, 0, 0), 0.1)),
        Request((1, 1, 1, datetime(2016, 1, 6, 12, 0, 0), datetime(2016, 1, 6, 14, 59, 0), 0.5)),
        Request((1, 1, 2, datetime(2016, 1, 6, 17, 0, 0), datetime(2016, 1, 6, 19, 59, 0), 0.6)),
        Request((1, 1, 3, datetime(2016, 1, 1, 14, 0, 0), datetime(2016, 1, 1, 20, 59, 0), 0.3)),
        Request((1, 1, 0, datetime(2016, 1, 7, 8, 0, 0), datetime(2016, 1, 7, 12, 59, 0), 0.1)),
        Request((1, 1, 1, datetime(2016, 1, 7, 12, 0, 0), datetime(2016, 1, 7, 14, 59, 0), 0.9)),
        Request((1, 1, 2, datetime(2016, 1, 7, 17, 0, 0), datetime(2016, 1, 7, 18, 59, 0), 0.3)),
        Request((1, 1, 3, datetime(2016, 1, 1, 9, 0, 0), datetime(2016, 1, 1, 20, 59, 0), 0.1))
    ]
