#!/usr/bin/env python3

# Copyright © 2020 Amir Eldor <amir@eldor.dev>
# This work is free. You can redistribute it and/or modify it under the
# terms of the Do What The Fuck You Want To Public License, Version 2,
# as published by Sam Hocevar. See the COPYING file for more details.

from datetime import datetime, timedelta
from os import getenv
from typing import Tuple

filename = getenv("I3BLOCKSTIMERTHING_FILE", "/tmp/i3blockstimerthing.txt")
button = getenv('button') 

RUNNING = "running"
PAUSED = "paused"

def write_stuff_to_file(write_this: str, state: str) -> None:
    with open(filename, "w") as timer_file:
        timer_file.write(write_this + " " + state)

def restart_timer():
    now_as_str: str = str(int(datetime.now().timestamp()))
    write_stuff_to_file(now_as_str, RUNNING)
    return 0, RUNNING

def read_stuff_from_file() -> Tuple[int, str]:
    with open(filename, "r") as timer_file:
        lines = timer_file.readlines()
        time_value, state = lines[0].split(' ')
        return int(time_value), state

def file_time_to_seconds_count(file_time: int) -> int:
    """file_time is usually in unix timestamp"""
    start_time = datetime.fromtimestamp(file_time)
    delta = datetime.now() - start_time
    seconds_count = int(delta.total_seconds())
    return seconds_count

def read_timer() -> Tuple[int, str]:
    try:
        time_value, state = read_stuff_from_file()
        if state == RUNNING:
            # time_value is a "start time" timestamp
            seconds_count = file_time_to_seconds_count(time_value)
        elif state == PAUSED:
            # time_value is the total seconds left
            seconds_count = int(time_value)
        else:
            seconds_count = 0

        return seconds_count, state

    except IOError:
        restart_timer()
        return 0, RUNNING

def toggle_timer():
    time_value, state = read_stuff_from_file()
    if state == RUNNING:
        seconds_count = file_time_to_seconds_count(time_value)
        write_stuff_to_file(str(seconds_count), PAUSED)

    elif state == PAUSED:
        now_timestamp = datetime.now().timestamp()
        new_timer_start_time = int(now_timestamp) - time_value
        write_stuff_to_file(str(new_timer_start_time), RUNNING)

if button == "1":
    restart_timer()
elif button == "2" or button == "3":
    toggle_timer()

seconds_count, state = read_timer()


def format_time(seconds_count):
    minutes = str(int(seconds_count / 60))
    seconds = str(int(seconds_count % 60)).zfill(2)
    return f"{minutes}:{seconds}"

if state == "paused":
    icon = "⏸️ "
else:
    icon = "⏱ "

time_display = icon + format_time(seconds_count)
print(time_display)
