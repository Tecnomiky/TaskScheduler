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
from subprocess import Popen
import time
import argparse

import Config
import Datetime


def is_moment(period_and_command):
    """
    Check if the current datetime match with config item
    :param period_and_command: Item of config
    :return: True if check is positive otherwise false
    """
    return (Datetime.get_minute() in period_and_command["minute"]) and \
           (Datetime.get_hour() in period_and_command["hour"]) and \
           (Datetime.get_day_month() in period_and_command["day_of_month"]) and \
           (Datetime.get_month() in period_and_command["month"]) and \
           (Datetime.get_day_week() in period_and_command["day_of_week"])


if __name__ == '__main__':
    "Code for the console interface"
    parser = argparse.ArgumentParser(description="Task scheduler")
    parser.add_argument("config_file", type=str, help="Config file in the cron Linux standard")
    parser.add_argument("-v", "--verbose", help="Return a verbose output", action="store_true")
    args = parser.parse_args()

    config_file = open(args.config_file, 'r')
    list_config = list(config_file)
    config_file.close()

    while True:
        for line in list_config:
            period_and_exe = Config.process_config_line(line)
            command = [period_and_exe["command"]]
            if args.verbose:
                print(period_and_exe)
            if is_moment(period_and_exe):
                print("execute "+period_and_exe["command"])
                Popen(command, shell=True, stdin=None, stdout=None, stderr=None, close_fds=True)
        time.sleep(40)


