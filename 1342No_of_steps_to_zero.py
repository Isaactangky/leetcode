#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 27 15:33:18 2022

@author: IsaacTang
"""

def numofstep(num):
    if not num:
        return 0
    
    count = 0
    while num:
        count += (num&1) + 1
        num >>=1
    return count-1

#268.missing number
def missingnum(nums):
    l = len(nums)
    for i in range(l):
        l ^= i
        print(l)
        l ^= nums[i]
        print(l)
    return l


        