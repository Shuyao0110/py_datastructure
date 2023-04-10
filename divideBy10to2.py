#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 14 20:48:13 2022

@author: heshuyao
"""

from pythonds.basic.stack import Stack
def divideBy2(originNum):
    s=Stack()
    while originNum>=1:
        s.push(originNum%2)
        originNum=originNum//2
    resultNum=''
    while not s.isEmpty():
        resultNum=resultNum+str(s.pop())
    return resultNum
print(divideBy2(32))