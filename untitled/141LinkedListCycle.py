#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  1 13:32:13 2022

@author: IsaacTang
"""
# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None

def hasCycle(head):
    """
    :type head: ListNode
    :rtype: bool
    """    
    if not head or not head.next: 
        return False
    d = {}
    while head:
        if head in d:
            return True
        d[head] = head.val
        head = head.next
        print(d)
    return False

def createNode(l,pos=-1):
    k = []
    for i in l:
        k.append( ListNode(i))
    for i in range(len(k)-1):
        k[i].next = k[i+1]
    if pos != -1:
        k[-1].next = k[pos]
    return k[0]
        