# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        value_dict = {}
        while head is not None:
            head_id = id(head)
            if head_id not in value_dict.keys():
                value_dict[head_id] = head
            else:
                return value_dict[head_id]
            head = head.next
        return None