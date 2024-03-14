import datetime
import random

def random_date(d1, d2, format):
    """
    This function will return a random datetime between two datetime objects.
    """
    start = datetime.datetime.strptime(d1, format)
    end = datetime.datetime.strptime(d2, format)
    delta = end - start
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = random.randrange(int_delta)
    return start + datetime.timedelta(seconds=random_second)