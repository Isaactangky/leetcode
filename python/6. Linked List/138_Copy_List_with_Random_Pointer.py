
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        oldToNew = {None:None}
        new_head = p =  Node(-1)
        p2 = head
        while head:
            node = Node(head.val)
            p.next = node
            
            #map the old node to new
            oldToNew[head] = node
            
            p = p.next
            head = head.next
        #assigning the random node
        p = new_head.next
        while p:
            p.random = oldToNew[p2.random]
            p = p.next
            p2 = p2.next
        
        return new_head.next
            
            
