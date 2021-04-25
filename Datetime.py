from datetime import datetime


def get_minute():
    datetime_object = datetime.now()
    return datetime_object.minute


def get_hour():
    datetime_object = datetime.now()
    return datetime_object.hour


def get_day_month():
    datetime_object = datetime.now()
    return datetime_object.day


def get_month():
    datetime_object = datetime.now()
    return datetime_object.month


def get_day_week():
    datetime_object = datetime.now()
    return datetime_object.weekday()
