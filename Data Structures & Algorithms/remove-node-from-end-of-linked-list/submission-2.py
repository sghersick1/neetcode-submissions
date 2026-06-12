# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        ''' 
        flip pointer as we go through list
        at end: go back n
        remove node
        '''

        curr = head
        prev = None
        list_len = 0
        # Traverse list
        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp 
            list_len += 1

        # undo pointers 
        curr = prev
        prev = None
        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp 
        
        curr = prev
        for i in range(list_len - n - 1):
            curr = curr.next
            prev = curr

        # remove the len - nth node
        if list_len == n:
            return prev.next

        prev.next = curr.next.next

        return head

        
        
