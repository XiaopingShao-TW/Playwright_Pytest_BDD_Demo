import datetime


def date_time_now(fmt="%Y%m%d %H%M%S"):
    return datetime.datetime.now().strftime(fmt)