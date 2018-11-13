# coding:utf-8
import bluetooth  # PyBluez
import time
import datetime
import json

sleep_time = 10

with open('dev_list.json', 'r') as f:
    dev_list = json.load(f)

addr_list = [d.get('addr') for d in dev_list]
user_name_list = [d.get('user_name') for d in dev_list]
#dev_name_list=[d.get('name') for d in dev_list]


def scan():
    old_addr = set()
    while True:
        # name_list=[]
        active_addr_list = []
        post_list = []
        active_list = []
        dt = datetime.datetime.now()
        dt_str = dt.strftime("%Y/%m/%d %H:%M:%S")
        for addr in addr_list:
            seach_devices = bluetooth.lookup_name(addr)
            if (type(seach_devices) is str) is True:
                active_addr_list.append(addr)
        new_addr = set(active_addr_list)
        # enter
        for i in new_addr - old_addr:
            post_dic = {}
            post_dic['boolmean'] = True
            post_dic['user_name'] = user_name_list[addr_list.index(i)]
            post_dic['addr'] = addr_list[addr_list.index(i)]
            post_dic['time'] = dt_str
            print("{}".format(json.dumps(post_dic, indent=4)))

        # leave
        for i in old_addr - new_addr:
            post_dic = {}
            post_dic['boolmean'] = False
            post_dic['user_name'] = user_name_list[addr_list.index(i)]
            post_dic['addr'] = addr_list[addr_list.index(i)]
            post_dic['time'] = dt_str
            print("{}".format(json.dumps(post_dic, indent=4)))

        #active
        for i in active_addr_list:
            active_dic = {}
            active_dic['name'] = user_name_list[addr_list.index(i)]
            active_list.append(active_dic)

        #print(active_list)

        with open("active_list.json", "w") as f:
            json.dump(active_list, f, ensure_ascii=False, indent=4,
                      sort_keys=True, separators=(',', ': '))

        old_addr = new_addr.copy()
        time.sleep(sleep_time)
# scan()
