import os
import glob
import time

os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')

def read_temp_raw(temp_id):
    device_file = '/sys/bus/w1/devices/' + temp_id + '/w1_slave'
    f = open(device_file, 'r')
    lines = f.readlines()
    f.close()
    return lines

def read_temp(temp_id):
    lines = read_temp_raw(temp_id)
    while lines[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        lines = read_temp_raw()
    equals_pos = lines[1].find('t=')
    if equals_pos != -1:
        temp_string = lines[1][equals_pos+2:]
        temp_c = float(temp_string) / 1000.0
        temp_f = temp_c * 9.0 / 5.0 + 32.0
        return temp_f
