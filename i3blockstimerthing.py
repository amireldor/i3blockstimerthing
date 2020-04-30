#!/usr/bin/env python3

# Copyright © 2020 Amir Eldor <amir@eldor.dev>
# This work is free. You can redistribute it and/or modify it under the
# terms of the Do What The Fuck You Want To Public License, Version 2,
# as published by Sam Hocevar. See the COPYING file for more details.

from datetime import datetime, timedelta
from os import getenv

filename = "/tmp/i3blockstimerthing.txt"

def write_start_file_with_now():
    with open(filename, "w") as start_file:
        start_time = datetime.now()
        start_file.write(str(int(start_time.timestamp())))
        return start_time


if getenv('button') is None:
    try:
        with open(filename, "r") as start_file:
            try:
                lines = start_file.readlines()
                start_time = datetime.fromtimestamp(int(lines[0]))
            except:
                start_file.close()

    except IOError:
        start_time = write_start_file_with_now()
else:
    start_time = write_start_file_with_now()

dt = datetime.now() - start_time
total_seconds = dt.total_seconds()
minutes = str(int(total_seconds / 60))
seconds = str(int(total_seconds % 60)).zfill(2)
formatted = f"⏱ {minutes}:{seconds}"
print(formatted)
