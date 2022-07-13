
"""
Created on Wed Jul 13 15:35:01 2022

@author: IsaacTang

find the length and tail of LL
k rotation = k %length rotation
p1 -> p1.next for k times
p1: node before the new head

new_head = p1.next
p1 next = null
current tail -> current head

"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head: return head
        length, tail = 1, head
        while tail.next:
            tail = tail.next
            length += 1
        k = k % length
        if k == 0:
            return head
        
        cur = head
        for i in range(length - k - 1):
            cur = cur.next
        new_head = cur.next
        cur.next = None
        tail.next = head
        return new_head
        