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
            if (Datetime.get_minute() not in running_task["minute"]) and (Datetime.get_hour() in running_task["hour"]) \
                    and running_task["id"] != period_and_command["id"]:

                run_task(period_and_command)

        running_tasks = [task for task in running_tasks if (Datetime.get_minute() > task["minute"][0]) and
                         (Datetime.get_hour() >= task["hour"][0])]


def run_task(period_and_command):
    global running_tasks

    command = [period_and_command["command"]]
    Popen(command, shell=True, stdin=None, stdout=None, stderr=None, close_fds=True)
    task = {"id": period_and_command["id"], "minute": period_and_command["minute"],
            "hour": period_and_command["hour"]}
    running_tasks.append(task)


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
        index = 1
        for line in list_config:
            period_and_exe = Config.process_config_line(line, index)
            command = [period_and_exe["command"]]
            if args.verbose:
                print(period_and_exe)
            if is_moment(period_and_exe):
                print("execute "+str(period_and_exe["id"])+" "+period_and_exe["command"])
#                proc = Popen(command, shell=True, stdin=None, stdout=None, stderr=None, close_fds=True)
#                print(proc.pid)
                check_whether_to_run_the_task(period_and_exe)
            index += 1
        time.sleep(50)


