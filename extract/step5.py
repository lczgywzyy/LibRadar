# -*- coding:utf-8 -*-
# Created at 2015/9/6

"""
    Function:
        Tag Data
        Sort by Total_call
"""
__author__ = 'Zachary Marv - 马子昂'

import json

input_d = "../raw_data/st4.dat"
output_d = "../data/st5.dat"


not_tagged = []

input = open(input_d, 'r')
output = open(output_d, 'w')
for line in input:
    i = json.loads(line)
    not_tagged.append(i)


def compare_d(a, b):
    if a['btn'] < b['btn']:
        return -1
    elif a['btn'] > b['btn']:
        return 1
    else:
        if a['btc'] < b['btc']:
            return -2
        elif a['btc'] > b['btc']:
            return 2
        else:
            if a['bh'] < b['bh']:
                return -3
            elif a['bh'] > b['bh']:
                return 3
            else:
                if a['sp'] < b['sp']:
                    return -4
                elif a['sp'] > b['sp']:
                    return 4
                else:
                    return 0

cnt = 0
cur = {"btc": 0, "bh": 0, "sp": "", "lib": "", "pn": "", "btn": 0}
for i in sorted(not_tagged, cmp=compare_d, reverse=True):
    # 这个判断可以去除很多重复。
    # 比如 android 和 android/support 同时存在而且各种都在的时候
    # 可以删去android
    # 这个和最开始设置Status 5 的原理一致，但是实现方式不太一样。
    # Status 5 的最终操作失败，可以用这种方式补足。
    if cur['btc'] == i['btc'] and cur['bh'] == i['bh'] and cur['btn'] == i['btn']:
        continue
    output.write(json.dumps(i) + '\n')
    cur = i


input.close()
output.close()