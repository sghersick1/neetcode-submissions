"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return None
            
        map = {}

        # pass 1
        curr = head
        while curr:
            map[curr] = Node(curr.val)
            curr = curr.next

        # pass 2 
        curr = head
        while curr:
            if curr.next:
                map[curr].next = map[curr.next]
            if curr.random:
                map[curr].random = map[curr.random]
            curr = curr.next

        return map[head]