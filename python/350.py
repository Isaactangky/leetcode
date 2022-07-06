#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun  5 15:16:59 2022

@author: IsaacTang
"""
def intersection(nums1, nums2):
    l = len(nums2)
    i = 0
    res = []
    d = {}
    for n in nums1:
        if n in d:
            res.append(n)
            d.pop(n)
            continue
        for m in range(i,l):
            if n == nums2[m]:
                res.append(n)
                i = m
                break
            else:
                d[nums2[m]] = m    


        print(d,res)
    return res
            