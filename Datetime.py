"""
TaskScheduler
Copyright (C) 2021 Michele Giorgio

This file is part of TaskScheduler.

Foobar is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

Foobar is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with TaskScheduler.  If not, see <https://www.gnu.org/licenses/>.
"""
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
