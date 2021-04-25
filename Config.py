import sys


def get_cron_expression(text):
    """
    Create a list from the string using as a separator the space.
    The split method default use space as separator
    """
    cron_statement = text.split()

    return cron_statement


def process_minute(minute):
    """
    Process the minute string for get the corresponding interval as a list
    :param minute: The minute string
    :return: A list of interval
    """
    minutes = []

    try:
        if "-" in minute:
            range_m = minute.split("-")
            for m in range(int(range_m[0]), int(range_m[1]) + 1):
                minutes.append(m)
        elif "," in minute:
            minutes_c = minute.split(",")
            for minute in minutes_c:
                minutes.append(int(minute))
        elif "/" in minute:
            parts = minute.split("/")
            for m in range(int(parts[0]), 60, int(parts[1])):
                minutes.append(m)
        elif "*" in minute:
            for m in range(0, 60):
                minutes.append(m)
        else:
            minutes.append(int(minute))
    except ValueError as error:
        minutes = None
        print('Input for minute not valid', file=sys.stderr)

    return minutes


def process_hour(hour):
    """
    Process the hour string for get the corresponding interval as a list
    :param hour: The minute string
    :return: A list of interval
    """
    hours = []

    try:
        if "-" in hour:
            range_m = hour.split("-")
            for m in range(int(range_m[0]), int(range_m[1]) + 1):
                hours.append(m)
        elif "," in hour:
            hours_c = hour.split(",")
            for hour in hours_c:
                hours.append(int(hour))
        elif "/" in hour:
            parts = hour.split("/")
            for h in range(int(parts[0]), 24, int(parts[1])):
                hours.append(h)
        elif "*" in hour:
            for h in range(0, 24):
                hours.append(int(h))
        else:
            hours.append(int(hour))
    except ValueError as error:
        hours = None
        print('Input for hour not valid', file=sys.stderr)

    return hours


def process_day_month(day):
    """
    Process the day of month string for get the corresponding interval as a list
    :param day: The day of month string
    :return: A list of interval
    """
    days = []

    try:
        if "-" in day:
            range_m = day.split("-")
            for m in range(int(range_m[0]), int(range_m[1]) + 1):
                days.append(m)
        elif "," in day:
            days_c = day.split(",")
            for day in days_c:
                days.append(int(day))
        elif "/" in day:
            parts = day.split("/")
            for d in range(int(parts[0]), 32, int(parts[1])):
                days.append(d)
        elif "*" in day:
            for d in range(1, 32):
                days.append(d)
        else:
            days.append(day)
    except ValueError as error:
        days = None
        print('Input for day of month valid', file=sys.stderr)

    return days


def process_month(month):
    """
    Process the month string for get the corresponding interval as a list
    :param month: The minute string
    :return: A list of interval
    """
    months = []

    try:
        if "-" in month:
            range_m = month.split("-")
            for m in range(int(range_m[0]), int(range_m[1]) + 1):
                months.append(m)
        elif "," in month:
            months_c = month.split(",")
            for month in months_c:
                months.append(int(month))
        elif "/" in month:
            parts = month.split("/")
            for m in range(int(parts[0]), 13, int(parts[1])):
                months.append(m)
        elif "*" in month:
            for m in range(1, 13):
                months.append(m)
        else:
            months.append(int(month))
    except ValueError as error:
        months = None
        print('Input for month not valid', file=sys.stderr)

    return months


def process_day_week(day_week):
    """
    Process the day of week string for get the corresponding interval as a list
    :param day_week: The day if week string
    :return: A list of interval
    """
    days_week = []

    try:
        if "-" in day_week:
            range_m = day_week.split("-")
            for m in range(int(range_m[0]), int(range_m[1]) + 1):
                days_week.append(m)
        elif "," in day_week:
            days_week_c = day_week.split(",")
            for day_week in days_week_c:
                days_week.append(int(day_week))
        elif "/" in day_week:
            parts = day_week.split("/")
            for d in range(int(parts[0]), 7, int(parts[1])):
                days_week.append(d)
        elif "*" in day_week:
            for d in range(0, 7):
                days_week.append(d)
        else:
            days_week.append(int(day_week))
    except ValueError as error:
        days_week = None
        print('Input for day of week not valid', file=sys.stderr)

    return days_week


def get_period_and_command(cron_expression):
    """
    Create a cron dictionary from the list
    :param cron_expression: The cron list
    :return: Cron dictionary
    """
    command = ""
    for i in range(5, len(cron_expression)):
        command += cron_expression[i] + " "

    period_and_command = {
        "minute": process_minute(cron_expression[0]),
        "hour": process_hour(cron_expression[1]),
        "day_of_month": process_day_month(cron_expression[2]),
        "month": process_month(cron_expression[3]),
        "day_of_week": process_day_week(cron_expression[4]),
        "command": command
    }

    return period_and_command


def process_config_line(line):
    """
    Process the config line for get a cron dictionary
    :param line: The config line
    :return: The cron dictionary
    """
    return get_period_and_command(get_cron_expression(line))

