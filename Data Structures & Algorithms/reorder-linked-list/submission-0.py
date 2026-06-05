# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Brute Force
        # Space O(n)

        # Copy into array O(n)
        nodes = []
        curr = head
        while curr:
            nodes.append(curr)
            curr = curr.next

        # Rewire O(n)
        # Forward
        n = len(nodes)
        for i in range(n // 2):
            nodes[i].next = nodes[n - (i+1)]
        
        # Backwards
        stop = n // 2 - 1 if n % 2 == 0 else n // 2
        for i in range(stop):
            nodes[n - (i + 1)].next = nodes[i+1]

        nodes[n // 2].next = None