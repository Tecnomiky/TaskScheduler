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
import textwrap
from subprocess import Popen
import time
import argparse

import Config
import Datetime

running_tasks = []


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


def check_whether_to_run_the_task(period_and_command):
    global running_tasks

    if len(running_tasks) == 0:
        run_task(period_and_command)

    else:
        for running_task in running_tasks:
            now = Datetime.get_now()
            if (running_task["datetime"] != now) and (running_task["id"] != period_and_command["id"]):
                run_task(period_and_command)

                running_tasks = [running_task for running_task in running_tasks if (now == running_task["datetime"])]


def run_task(period_and_command):
    global running_tasks

    print("execute " + str(period_and_command["id"]) + " " + str(period_and_command["command"]))
    cmd = period_and_command["command"]
    Popen(cmd, shell=False, stdin=None, stdout=None, stderr=None, close_fds=True)
    task = {"id": period_and_command["id"], "minute": period_and_command["minute"],
            "hour": period_and_command["hour"],
            "datetime": Datetime.get_now()}
    running_tasks.append(task)


if __name__ == '__main__':
    "Code for the console interface"
    parser = argparse.ArgumentParser(description=textwrap.dedent('''Task scheduler
TaskScheduler is a task scheduler software, wrote in Python, that use cron linux standard for the config file
The comments in the config file are accepted and it has to begin with a #
'''), formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("config_file", type=str, help="Config file in the cron Linux standard")
    parser.add_argument("-v", "--verbose", help="Return a verbose output", action="store_true")
    args = parser.parse_args()

    config_file = open(args.config_file, 'r')
    list_config = list(config_file)
    config_file.close()

    while True:
        index = 1
        for line in list_config:
            if not line.strip().startswith("#"):
                period_and_exe = Config.process_config_line(line, index)
                command = [period_and_exe["command"]]
                if args.verbose:
                    print(period_and_exe)
                if is_moment(period_and_exe):
                    # print("execute " + str(period_and_exe["id"]) + " " + str(period_and_exe["command"]))
                    check_whether_to_run_the_task(period_and_exe)
                index += 1
        time.sleep(50)
