# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Edge case(s) 
        # 1. Carry Over
        # 2. Different length lists (size_1 = 2, size_2 = 5)
        
        carry = 0
        dummy = cur = ListNode() 
        while l1 and l2:
            combine = l1.val + l2.val + carry
            node_val = combine % 10
            carry = combine // 10 

            cur.next = ListNode(node_val)
            cur = cur.next
            l1 = l1.next
            l2 = l2.next

        # handle remains
        while l1:
            combine = l1.val + carry
            node_val = combine % 10
            carry = combine // 10

            cur.next = ListNode(node_val)
            cur = cur.next
            l1 = l1.next
            
        while l2:
            combine = l2.val + carry
            node_val = combine % 10
            carry = combine // 10

            cur.next = ListNode(node_val)
            cur = cur.next
            l2 = l2.next

        if carry:
            cur.next = ListNode(1)

        return dummy.next
            
            

