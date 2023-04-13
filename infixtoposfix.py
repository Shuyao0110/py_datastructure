#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 14 20:48:52 2022

@author: heshuyao
"""

from pythonds.basic.stack import Stack

def infixtoPostfix(infixNum):
    prec={}
    #prec['(']=1#
    prec['*']=2
    prec['/']=2
    prec['+']=3
    prec['-']=3
    s=Stack()
    postfixList=''
  
    for char in infixNum:
        if char in ('ABCDEFGHIJKLMNOPQRSTUVWXYZ' or '0123456789'):
            postfixList=postfixList+char
        elif char=='(':
            s.push(char)
        elif char==')':
            toptoken=s.pop()
            while toptoken!='(':
                s.push(toptoken)
                toptoken=s.pop()
        else:
            if s.isEmpty():
                s.push(char)
            else:
                toptoken=s.pop()
                if prec[str(toptoken)]<prec[char]:
                    postfixList=postfixList+str(toptoken)
                    s.push(char)
                else:
                    s.push(toptoken)
                    s.push(char)
    
    while not s.isEmpty():
        postfixList=postfixList+s.pop()
    return postfixList

resulttest=infixtoPostfix('A*B+C*D')
print(resulttest)
                
def calpostfixNum(postfixNum):
    s=Stack()
    for Num in postfixNum:
        if Num in '0123456789':
            s.push(Num)
        else:
            n1=s.pop()
            n2=s.pop()
            nn=doMath(Num, n1, n2)
            s.push(nn)
    return s.pop()
            
def doMath(op,op1,op2):
    if op=='+':
        return op1+op2
    elif op=='-':
        return op1-op2
    elif op=='*':
        return op1*op2
    else:
        return op1/op2

caltest=calpostfixNum('34*56*+')
print(caltest)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
                
        
    