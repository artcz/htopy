#!/usr/bin/env python3
# coding: utf-8

"""
Using python 3.7
"""


from datetime import datetime, timedelta
import os


def loadavg():
    return os.getloadavg()


def uptime():
    with open('/proc/uptime', 'r') as f:
        return timedelta(seconds=float(f.readline().split()[0]))


print(" {} up {}, load average: {}".format(
    datetime.now().strftime("%H:%M:%S"),
    uptime(),
    ", ".join(str(x) for x in loadavg())
))
