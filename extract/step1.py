# -*- coding:utf-8 -*-
# Created at 2015/9/2

"""
    Function:
        raw_data export_d1.dat to raw_data/st1.dat
"""
__author__ = 'Zachary Marv - 马子昂'

import json

raw_file = open("../raw_data/export_d1.dat", 'r')
tg100 = open("../raw_data/st1.dat", 'w')
bad_API = 0
support_API = 0
a_API = 0
for line in raw_file:
    item = json.loads(line)
    # Dep
    if item['dep_num'] < 100:
        continue
    # Size
    if item['b_total_call'] < 10:
        continue
    if item['b_total_num'] < 5:
        continue
    new_item = {}
    new_item['b_hash'] = item['b_hash']
    new_item['pp'] = item['pp']
    new_item['dep_num'] = item['dep_num']
    new_item['b_total_num'] = item['b_total_num']
    new_item['b_total_call'] = item['b_total_call']
    tg100.write(json.dumps(new_item)+'\n')
tg100.close()
