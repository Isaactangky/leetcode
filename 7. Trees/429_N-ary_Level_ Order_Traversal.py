#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []
        
        res = [[root.val]]
        q = deque()
        q.append(root)
        while q:
            val = []
            for i in range(len(q)):
                node = q.popleft()
                if node.children:
                    #print(node.children)
                    for n in node.children:
                        q.append(n)
                        val.append(n.val)
            if val:
                res.append(val)

        return res
                    
