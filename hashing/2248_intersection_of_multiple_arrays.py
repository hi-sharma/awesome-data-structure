from collections import defaultdict
class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        # O(n*log n) time complexity
        # O(n) space complexity
        dic = defaultdict(int)
        max_count = len(nums)
        ans = []
        for sub_arr in nums:
            for elem in sub_arr:
                dic[elem] = dic.get(elem,0) + 1
        for key, val in dic.items():
            if val == max_count:
                ans.append(key)
        return sorted(ans)
        
