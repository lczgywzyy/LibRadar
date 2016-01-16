# -*- coding:utf-8 -*-
__author__ = 'zach'
"""
文件名 : b2_tgst5_to_export_d1.dat.py
目的 : 把tgst5.dat标注的内容，回到export_d1.dat 中，找到它的_id
    然后下一步，回到数据库中，根据这个_id，找到具体的API特征。
    1 - 导出API特征，用来分析“同一个Library的不同版本”。
    2 - 导出一个apk list，专门只把这个apk list 下载到本地。细致研究。
        可研究内容：Library的 Intent 、SSL信息、具体的API设置以及结构等等，可丰富网站内容，作更细致的Library剖析。

"""