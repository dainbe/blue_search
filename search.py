# coding:utf-8
import bluetooth  # PyBluez
import time
import datetime
import json

dev_info = {}
dev_list = []
old_devices = set()


def seach():
    for i in range(5):
        try:
            nearby_devices = bluetooth.discover_devices(lookup_names=True)
        except (IOError, err):
            print(err)
            time.sleep(3)
        else:
            dt = datetime.datetime.now()
            dt_str = dt.strftime("%Y/%m/%d %H:%M:%S")
            new_devices = set(nearby_devices)
            for addr, name in new_devices - old_devices:
                dev_info = {}
                print("+ %s %s %s" % (dt_str, addr, name))
                dev_info['user_name'] = 'unknown'
                dev_info['addr'] = addr

                dev_list.append(dev_info)

            old_devices = new_devices.copy()
            time.sleep(2)
    return dev_list
