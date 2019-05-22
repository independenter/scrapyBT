#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:donghui

import threading,json

def doT1():
    for i in range(100):
        print("t1.........")
def doT2():
    for i in range(100):
        print("t2.........")
def doT3():
    for i in range(100):
        print("t3.........")



if __name__=='__main__':

    t1 = threading.Thread(target=doT1(),args=())
    t2 = threading.Thread(target=doT2(), args=())
    t3 = threading.Thread(target=doT3(), args=())
    # t1.start()
    # t2.start()
    # t3.start()

    # with open("EffectiveIp.json",'r') as handler:
    #     ips=json.load(handler)
    #     # print(ips)
    # handler.close()


