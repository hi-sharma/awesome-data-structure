from collections import defaultdict
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # O(n) time and space complexity
        # stack for nums and hashmap for next large elem
        stack = []
        count = defaultdict(int)
        ans = []
        for num in nums2:
            while stack and stack[-1] < num:
                count[stack[-1]] = num
                stack.pop()
            stack.append(num)
        while stack:
            count[stack[-1]] = -1
            stack.pop()
        for num in nums1:
            ans.append(count.get(num, -1))
        return ans
