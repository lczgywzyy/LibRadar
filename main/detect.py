# -*- coding:utf-8 -*-
# Created at 2015/7/20
# Recently Modified at 2015/09/02
# Current Version 1.1.0

__author__ = 'Zachary Marv - 马子昂'

"""
    LibRadar is a tool for detecting third-party libraries in Android apps accurately and instantly.
"""

import os
import json
import glob
import re
import subprocess
import sys
import time


class TimeRecord:
    """
    @ class TimeRecord
    Made for Time Recording.
    用来计时。
    """
    def __init__(self, task_tag=""):
        self.init_time = time.time()
        self.if_start = False
        self.start_time = 0
        self.tag = task_tag

    def start(self):
        self.start_time = time.time()
        self.if_start = True
        print('*' * 60)
        print('Task: '+self.tag+' Starts.')

    def end(self):
        end_time = time.time()
        if self.if_start:
            task_interval = end_time - self.start_time
            print('Task: '+sys.argv[0]+' Ends.')
            m = int(task_interval) / 60
            s = task_interval - m
            if m <= 1:
                mi = 'minute'
            else:
                mi = 'minutes'
            if s <= 1:
                se = 'second'
            else:
                se = 'seconds'
            print(self.tag + ' Consuming '+str(m)+' '+mi+' and '+str(s)+' '+se+'.')
            print('*' * 60)
        self.if_start = False


# Init Two Time Recorder.
time_decode = TimeRecord('Decoding')
time_compare = TimeRecord('Searching')

# For decoding Bug.
reload(sys)
sys.setdefaultencoding("utf-8")


api_dict = {}
packages_feature = []
libs_feature = []
project_path = os.path.dirname(sys.argv[0])


def get_smali(path):
    """
    Convert APK into Smali file.
    :param path:
    :return:
    """
    time_decode.start()
    cmd = project_path + "/" + "../tool/apktool decode %s -o " % path + project_path + "/" + "../decoded/%s" % os.path.basename(path)
    subprocess.call(cmd, shell=True)
    time_decode.end()
    return project_path + '/../decoded/%s' % os.path.basename(path)


def get_hash(apk_path):
    """
    Convert APK into Smali file.
    :param path:
    :return:
    """
    # - Loading Data

    time_compare.start()
    dep_address = project_path + "/" + "../data/st4.dat"
    dict_address = project_path + "/" + "../data/new_dict.dat"
    dep_file = open(dep_address, 'r')
    dict_file = open(dict_address, 'r')

    # -- Loading API Dict
    for line in dict_file:
        # print line
        u = json.loads(line)
        api_dict[u['key']] = u['value']

    # -- Loading Hashed Libs

    for line in dep_file:
        # print line
        u = json.loads(line)
        # s_path = '/'.join(u['path_parts'])
        libs_feature.append((u['b_hash'],  u['b_total_num'], u['b_total_call'], u['s_path'], u['lib']))

    # - All Over
    # print apk_path+'/smali'
    if os.path.exists(apk_path+'/smali'):
        os.chdir(apk_path+'/smali')
        all_over(apk_path, apk_path+'/smali')
        os.chdir(apk_path)

    # Print Res
    # print packages_feature
    '''
    if DEBUG:
        for p in packages_feature:
            print p
    '''
    cur_app_libs = []
    cur_app_routes = []
    for p in packages_feature:
        print p[3]
        for l in libs_feature:
            if l[2] < 5:
                continue
            if p[0] == l[0] and p[1] == l[1] and p[2] == l[2]:
                if l[4] != "" and l[4] != "Nope":
                    tmp = l[4]
                    if tmp not in cur_app_libs:
                        cur_app_libs.append(tmp)
                elif l[4] == "":
                    tmp = l[3]
                    if tmp not in cur_app_routes:
                        cur_app_routes.append(tmp)
    print "--Splitter--"
    for i in cur_app_libs:
        print i + ','
    print "--Splitter--"
    for i in cur_app_routes:
        print i + ','
    print "--Splitter--"
    time_compare.end()
    cmd = 'rm -rf %s' % apk_path
    subprocess.call(cmd, shell=True)
    return "Get Function Ends."


def get_number(string):
    """
    Get API ID From API Dictionary.
    获得API的编号
    :param string: API Name
    :return: API ID
    """
    if string not in api_dict:
        return -1
    return str(api_dict[string])


def all_over(apk_path, path):
    """
    Recursive body of package for getting the features
    :param apk_path: APK Path
    :param path: Packages Path
    :return: API Dict of this package, Directory Number in this Package, File Number, Total API Call.
    """

    find_file = re.compile(r'.smali$')
    p = re.compile(r'Landroid/.*?;?\-?>*?\(|Ljava/.*?;?\-?>*?\(|Ljavax/.*?;?\-?>*?\(|Lunit/runner/.*?;?\-?>*?\('
                   r'|Lunit/framework/.*?;?\-?>*?\('
                   r'|Lorg/apache/commons/logging/.*?;?\-?>*?\(|Lorg/apache/http/.*?;?\-?>*?\(|Lorg/json/.*?;'
                   r'?\-?>*?\(|Lorg/w3c/.*?;?\-?>*?\(|Lorg/xml/.*?;?\-?>*?\(|Lorg/xmlpull/.*?;?\-?>*?\(|'
                   r'Lcom/android/internal/util.*?;?\-?>*?\(')
    all_thing = glob.glob('*')
    this_call_num = 0
    this_dir_num = 0
    this_file_num = 0
    direct_dir_num = 0
    direct_file_num = 0
    this_dict = {}
    for thing in all_thing:
        # If the thing is a directory.
        if os.path.isdir(thing):
            os.chdir(path+'/'+thing)
            # Merge Dictionary
            # 合并字典
            child = all_over(apk_path, path+'/'+thing)
            if child is not None:
                this_dict.update(child[0])
                this_dir_num += child[1] + 1
                direct_dir_num += 1
                this_file_num += child[2]
                this_call_num += child[3]
            os.chdir(path)
        # If the 'thing' is a file
        # 如果 thing 是一个文件
        else:
            try:
                # Is this file a smali file?
                # 如果这个文件是一个SMALI文件
                if not find_file.search(thing):
                    continue
                f = open(thing, 'r')
                for u in f:
                    # For every line in this file.
                    # 搜索每一行。
                    match = p.findall(u)
                    for system_call in match:
                        if '"' in system_call:
                            continue
                        this_call_num += 1
                        call_num = get_number(system_call)
                        if call_num == -1:
                            continue
                        if call_num in this_dict:
                            this_dict[call_num] += 1
                        else:
                            this_dict[call_num] = 1
                f.close()
                this_file_num += 1
                direct_file_num += 1
            except Exception as ex:
                print('Can not Open ' + thing + ' Wrong with:' + str(ex))
    # If there is no API call in this package, just ignore it.
    if len(this_dict) == 0:
        return
    parts = path[len(apk_path)+7:].split("/")
    b_hash = 0
    for a in this_dict:
        b_hash = (b_hash + int(a) * this_dict[a]) % 999983          # 99983 is A Big Prime
    packages_feature.append((b_hash, len(this_dict), this_call_num, '/'.join(parts)))
    return this_dict, this_dir_num, this_file_num, this_call_num


def main_func(path):
    """
    Detect 3rd-party libraries in app.
    The detection result is printed.
    :param path: The path of target app.
    :return: None.
    """
    decoded_path = get_smali(path)
    get_hash(decoded_path)


if __name__ == '__main__':
    if len(sys.argv) <= 1:
        print "No Apk File Name.\nTry to detect 'Yo.apk' for test."
        main_func("~/Downloads/Yo.apk")
    else:
        print os.path.basename(sys.argv[1])
        main_func(sys.argv[1])