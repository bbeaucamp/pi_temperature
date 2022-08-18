#!/usr/bin/env python3
"""
Usage:
python3 temperature.py              -> Prints the temperature of the CPU to the screen every 2s. Use CTRL+C to stop.
python3 temperature.py /path/to/csv -> Dumps the temperature reading in the file, ONLY ONCE. The command needs to be run for each temperature reading.
"""
import os
import sys
import time
from datetime import datetime
 

def temperature_of_raspberry_pi():
    # Read the temperature
    cpu_temp = os.popen("vcgencmd measure_temp").readline()
    cpu_temp = cpu_temp.replace("temp=", "").strip('\n').strip("'C")
    now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # ex: 2022/06/24 12:07:18
    return now, cpu_temp


def print_to_screen(ts, temp):
    print(ts, ':', temp + '°C')


def dump_to_file(time, temp, file_path):
    with open(file_path, 'a') as f:  # 'a': append mode. The data will be written at the end of the file
        f.write(time + ',' + temp + '\n')  # \n for line return


def create_data_file(file_path):
    """The directory where file_path is located needs to exist, otherwise this will fail."""
    if not os.path.exists(file_path):
        with open(file_path, 'w') as f:
            f.write('time,temperature\n')
       

if __name__ == '__main__':
    if len(sys.argv) > 1:
        file_path = sys.argv[1]
        create_data_file(file_path)
        ts, temp = temperature_of_raspberry_pi()
        dump_to_file(ts, temp, file_path)
    else:
        while True:
            ts, temp = temperature_of_raspberry_pi()
            print_to_screen(ts, temp)
            time.sleep(2)
        