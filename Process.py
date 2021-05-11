import os
import sys


def check_pid_unix(pid):
    try:
        os.kill(pid, 0)
    except OSError:
        return False
    else:
        return True


def check_pid_exist(pid):
    result = False

    if sys.platform.startswith('linux') or sys.platform.startswith('darwin'):
        result = check_pid_unix(pid)

    return result
