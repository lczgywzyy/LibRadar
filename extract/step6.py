# -*- coding:utf-8 -*-
# Created at 2015/9/6

"""
    Function:
        Tag Data
        Sort by Total_call
"""
__author__ = 'Zachary Marv - 马子昂'

import json

input_d = "../data/st5.dat"




input = open(input_d, 'r')
not_tagged_number = 0
tagged_number = 0
for line in input:
    i = json.loads(line)
    if i['lib'] == "":
        not_tagged_number += i['dn']
    else:
        tagged_number += i['dn']

print not_tagged_number
print tagged_number


cnt = 0
cur = {"btc": 0, "bh": 0, "sp": "", "lib": "", "pn": "", "btn": 0}



input.close()