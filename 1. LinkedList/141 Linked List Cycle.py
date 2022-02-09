# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        value_dict = {}
        while head is not None:
            head_id = id(head)
            if head_id not in value_dict.keys():
                value_dict[head_id] = 1
            else:
                return True
            head = head.next
        return False