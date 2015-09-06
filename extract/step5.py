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
    if a['b_total_num'] < b['b_total_num']:
        return -1
    elif a['b_total_num'] > b['b_total_num']:
        return 1
    else:
        if a['b_total_call'] < b['b_total_call']:
            return -2
        elif a['b_total_call'] > b['b_total_call']:
            return 2
        else:
            if a['b_hash'] < b['b_hash']:
                return -3
            elif a['b_hash'] > b['b_hash']:
                return 3
            else:
                if a['s_path'] < b['s_path']:
                    return -4
                elif a['s_path'] > b['s_path']:
                    return 4
                else:
                    return 0

cnt = 0
cur = {"b_total_call": 0, "b_hash": 0, "s_path": "", "lib": "", "b_total_num": 0}
for i in sorted(not_tagged, cmp=compare_d, reverse=True):
    # 这个判断可以去除很多重复。
    # 比如 android 和 android/support 同时存在而且各种都在的时候
    # 可以删去android
    # 这个和最开始设置Status 5 的原理一致，但是实现方式不太一样。
    # Status 5 的最终操作失败，可以用这种方式补足。
    if cur['b_total_call'] == i['b_total_call'] and cur['b_hash'] == i['b_hash'] and cur['b_total_num'] == i['b_total_num']:
        continue
    output.write(json.dumps(i) + '\n')
    cur = i


input.close()
output.close()