class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head):
        array = []

        while head is not None:
            array.append(head.val)
            head = head.next

        dummy = ListNode(0, None)
        curr = dummy
        while len(array) > 0:
            value = array.pop()
            curr.next = ListNode(value, None)
            curr = curr.next

        return dummy.next
