#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 14 16:48:42 2022

@author: heshuyao
"""

from pythonds.basic.stack import Stack
def parChecker(symbolString):
    s=Stack()
    balanced=True
    index=0
    while index<len(symbolString) and balanced:
        if symbolString[index] in '{[(':
            s.push(symbolString[index])
        else:
            if s.isEmpty():
                balanced=False
            else:
                if matches(s.pop(),symbolString[index]):
                    balanced=True
                else:
                    balanced=False
        index=index+1
    if balanced and s.isEmpty():
        return True
    else:
        return False

def matches(open1,close):
 opens='{[('
 closers='}])'
 return opens.index(open1)==closers.index(close)

print (parChecker('()('))
print(parChecker('{[()]}'))
print(parChecker('()'))