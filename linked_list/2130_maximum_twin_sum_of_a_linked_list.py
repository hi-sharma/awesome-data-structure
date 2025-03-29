# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def reverse_list(head):
    # Track prev, curr and nextNode. Move curr to prev, prev to nextNode. Update
    prev = None
    curr = head
    while curr:
        nextNode = curr.next
        curr.next = prev
        prev = curr
        curr = nextNode
    return prev

class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        # O(n) time complexity
        #O(1) space complexity
        #base cases
        if not head.next.next:
            return head.val + head.next.val
        # find middle of linked list
        start = head
        num_elem = 0
        ans = 0
        while start:
            num_elem += 1
            start = start.next
        midIndex = num_elem//2
        # reverse 2nd half of linked list
        middleNode = head
        i = 0
        while i < midIndex:
            middleNode = middleNode.next
            i += 1
        middleNode_rev = reverse_list(middleNode)
        # fast pointer starts at n/2. Then compute the max sum
        start = head
        for i in range(midIndex):
            ans = max(ans, start.val + middleNode_rev.val)
            start = start.next
            middleNode_rev = middleNode_rev.next
        return ans
