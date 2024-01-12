"""
author : Ahn Ji Sung
github : https://github.com/j1sung
e-mail : dalssagi00@gmail.com
title : two-sum
description : Binary
"""
class Solution:
    def getSum(self, a: int, b: int) -> int:
        if a==0 and b==0:
            return 0
        if a==0 and b!=0:
            return b
        if a!=0 and b==0:
            return a
        if a<0 and b<0:
            for i in range(abs(b)):
                a-=1
            return a
        elif a>0 and b>0:
            for i in range(b):
                a+=1
            return a
        elif a<0 and b>0:
            for i in range(b):
                a+=1
            return a    
        elif a>0 and b<0:
            for i in range(a):
                b+=1
            return b
        