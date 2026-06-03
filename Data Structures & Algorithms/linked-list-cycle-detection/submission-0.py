# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Floyd's rabbit & hare
        curr = head
        count = 0
        while curr:
            if count > 1000:
                return True 
            curr = curr.next
            count += 1
        return False 