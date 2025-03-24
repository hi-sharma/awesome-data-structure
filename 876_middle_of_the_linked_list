# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Using 2 pointer approach
        middle = head
        end = head
        while end is not None and end.next is not None:
            middle = middle.next
            end = end.next.next
        return middle            
        
# class Solution:
#     def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         if head is None or head.next is None:
#             return head
#         node = head.next
#         list_len = 1
#         while node is not None:
#             list_len += 1
#             node = node.next
#         mid = list_len//2
#         counter = 1
#         node = head.next
#         while node is not None and counter < mid:
#             counter += 1
#             node = node.next
#         return node
                
            
            
        
