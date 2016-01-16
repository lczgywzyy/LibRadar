# -*- coding:utf-8 -*-
__author__ = 'zach'

# 这个文件夹的作用是拿着出产的结果比如tgst5.dat回到数据库，去查找有用的内容。

import json
import pymongo

def main_func():
    conn = pymongo.MongoClient('localhost', 27017)
    lib_d = conn['lib-detect']
    brief = lib_d.get_collection('brief_packages')

    # 去找 lib-detect 的 d21 d22
    d1 = lib_d.get_collection('d21')
    d2 = lib_d.get_collection('d22')

    st5 = open('../data/st5.dat')


    res_call = {}
    res_num = {}
    for d in d1.find():

        num = d['dep_num']
        if d['b_total_num'] not in res_num:
            res_num[d['b_total_num']] = num
        else:
            res_num[d['b_total_num']] += num
        if d['b_total_call'] not in res_call:
            res_call[d['b_total_call']] = num
        else:
            res_call[d['b_total_call']] += num
    result = open('res_call.txt', 'w')
    result.write(json.dumps(res_call))
    result.close()
    result = open('res_num.txt', 'w')
    result.write(json.dumps(res_num))
    result.close()

if __name__ == '__main__':
    main_func()