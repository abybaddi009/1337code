# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        summation = ListNode(0, None)
        
        summer = summation
        while l1 is not None or l2 is not None:
            p = l1.val if l1 is not None else 0
            q = l2.val if l2 is not None else 0
            total = p + q + carry
            carry = total // 10
            summer.next = ListNode(total % 10, None)
            summer = summer.next
            l1 = l1.next if l1 is not None else None
            l2 = l2.next if l2 is not None else None
        
        if carry > 0:
            summer.next = ListNode(carry, None)
        
        return summation.next