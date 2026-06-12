# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # easiest brute force
        nodes = []
        curr = head

        while curr:
            nodes.append(curr)
            curr = curr.next
        
        # Edge Cases
        # remove head
        if n == len(nodes):
            return None if n == 1 else nodes[1] 
        elif n == 1:
            nodes[len(nodes) - 2].next = None
        else:
            nodes[len(nodes) - n - 1].next = nodes[len(nodes) - n + 1]
    
        return head