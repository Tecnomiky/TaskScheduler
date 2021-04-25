from subprocess import Popen
import time
import argparse

import Config
import Datetime


def is_moment(period_and_command):
    return (Datetime.get_minute() in period_and_command["minute"]) and \
           (Datetime.get_hour() in period_and_command["hour"]) and \
           (Datetime.get_day_month() in period_and_command["day_of_month"]) and \
           (Datetime.get_month() in period_and_command["month"]) and \
           (Datetime.get_day_week() in period_and_command["day_of_week"])


if __name__ == '__main__':

    parser = argparse.ArgumentParser(description="Task scheduler")
    parser.add_argument("config_file", type=str, help="Config file")
    parser.add_argument("-v", "--verbose", help="Return a verbose output", action="store_true")
    args = parser.parse_args()

    config_file = open(args.config_file, 'r')

    while True:
        for line in config_file.readlines():
            period_and_exe = Config.process_config_line(line)
            command = period_and_exe["command"].split()
            if args.verbose:
                print(period_and_exe)
            if is_moment(period_and_exe):
                print("execute "+period_and_exe["command"])
                Popen(command, shell=True, stdin=None, stdout=None,
                      stderr=None, close_fds=True)
        time.sleep(45)


