#!/usr/bin/env python3

# Copyright © 2020 Amir Eldor <amir@eldor.dev>
# This work is free. You can redistribute it and/or modify it under the
# terms of the Do What The Fuck You Want To Public License, Version 2,
# as published by Sam Hocevar. See the COPYING file for more details.

from datetime import datetime, timedelta
from os import getenv

filename = "/tmp/i3blockstimerthing.txt"
button = getenv('button') 

def write_stuff_to_file(filename, time_value, state="running"):
    with open(filename, "w") as start_file:
        start_file.writelines('\n'.join([str(time_value), state]))
        return time_value, state

def write_now_timestamp_to_file(filename):
    now_timestamp = datetime.now().timestamp()
    _, state = write_stuff_to_file(filename, str(int(now_timestamp)))
    return 0, state

def read_stuff_from_file(filename):
    with open(filename, "r") as start_file:
        try:
            lines = start_file.readlines()
            time_value = lines[0]
            state = lines[1]
        except:
            start_file.close()
            write_now_timestamp_to_file(filename)
        return time_value, state

def toggle_pause_for_filename(filename):
    time_value, state = read_stuff_from_file(filename)
    if state == "running":
        write_stuff_to_file(filename, second_left, "paused")
    elif state == "paused":
        write_stuff_to_file(filename, second_left, "running")


if button is None:
    time_value, state = read_stuff_from_file(filename)
    start_time = datetime.fromtimestamp(int(time_value))
    seconds_count = (datetime.now() - start_time).total_seconds()
elif button == "1":
    seconds_count, state = write_now_timestamp_to_file(filename)
elif button == "2":
    seconds_count, state = toggle_pause_for_filename(filename)

def format_time(seconds_count):
    minutes = str(int(seconds_count / 60))
    seconds = str(int(seconds_count % 60)).zfill(2)
    return f"{minutes}:{seconds}"

if state == "running":
    icon = "⏱ "
elif state == "paused ":
    icon = "(paused)"

time_display = icon + format_time(seconds_count)
print(time_display)
