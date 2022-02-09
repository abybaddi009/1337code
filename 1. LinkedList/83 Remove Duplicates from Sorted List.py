# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pointer1 = head
        
        while pointer1 is not None and pointer1.next is not None:
            pointer2 = pointer1.next
            if pointer1.val == pointer2.val:
                pointer1.next = pointer2.next
                pointer2 = pointer2.next
            else:
                pointer1 = pointer1.next
        return head