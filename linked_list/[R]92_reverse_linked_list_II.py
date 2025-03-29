# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# 6:35pm
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        # O(n) time and O(1) space
        if not head.next:
            return head
        dummy = ListNode(0, head)
        before = dummy
        for _ in range(1, left):
            before = before.next
        prev = before
        curr = before.next
        for _ in range(left, right+1):
            nextNode = curr.next
            curr.next = prev
            prev = curr
            curr = nextNode
        before.next.next = curr
        before.next = prev
        return dummy.next
        


