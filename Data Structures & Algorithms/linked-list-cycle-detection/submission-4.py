# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast = slow = head
        while fast:
            for i in range(2):
                if fast:
                    fast = fast.next
            slow = slow.next

            if fast and slow == fast:
                return True
        return False