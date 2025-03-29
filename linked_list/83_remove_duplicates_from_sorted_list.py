# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # O(n) time and O(1) space complexity
        current = head
        while current and current.next:
            # Skip if consecutive values are equal
            if current.val == current.next.val:
                current.next = current.next.next
            else:
                current = current.next
        return head    
