'''
binary search with Greedy O(n*log m) where m = sum(nums)
left = max(nums) and right = sum(nums) # min and max subarr sum possible
For every mid check the minimum size of subarr needed so that max sub arr sum <= mid, return min_sub_arr_size
if min_sub_arr_size < k -> search in left subarr; otherwise search in right subarr
'''
class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def check(mid):
            # minimum sub arr size with sub arr sum <=mid
            ans = 0
            cumSum = 0
            for i in range(len(nums)):
                cumSum += nums[i]
                if cumSum > mid:
                    ans += 1
                    cumSum = nums[i]
            return ans + 1

        left = max(nums)
        right = sum(nums)
        while left <= right:
            mid = (left + right)//2
            min_sub_arr_size = check(mid)
            if min_sub_arr_size <= k:
                # seach in left sub arr
                right = mid - 1
                minimum_largest_split_sum = mid
            elif min_sub_arr_size > k:
                # search in right sub arr
                left = mid + 1
            else:
                return mid
        return minimum_largest_split_sum
        
