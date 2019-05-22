#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Dob

import json


f = open("EffectiveIp.json", 'r',encoding='UTF-8')
ips = json.load(f)
print(type(ips))
print(len(ips))