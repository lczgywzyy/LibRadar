# -*- coding:utf-8 -*-
# Created at 2015/9/2

"""
    Function:
        Tag Data
"""
__author__ = 'Zachary Marv - 马子昂'

import json

input_d = "../raw_data/st2.dat"
output_d = "../raw_data/st3.dat"


not_tagged = []

input = open(input_d, 'r')
output = open(output_d, 'w')
for line in input:
    i = json.loads(line)
    if i['lib'] == "" and len(i['ps'][0].split('/')) <= 4:
        print str(i['ps'] ) + str(i['dn'])

    if "ps" in i:
        if len(i["ps"]) > 2:
            print i["ps"]
    if "ps" in i:
        del i["ps"]
    output.write(json.dumps(i)+'\n')

'''
cnt = 0
for i in sorted(not_tagged, key=lambda u: u['dep_num'], reverse=True):
    cnt += 1
    if cnt > 200:
        break
    print i
'''

input.close()
output.close()