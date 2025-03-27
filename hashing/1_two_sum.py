class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # O(n) Time complexity
        # O(n) Space complexity
        dic = {}
        for i in range(len(nums)):
            num = nums[i]
            complement = target - num
            if complement in dic:
                return [i, dic[complement]]
            dic[num] = i       
