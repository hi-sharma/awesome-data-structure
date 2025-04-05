'''
1. sort nums in O(n*logn)
2. Create a prefix sum arr for nums to store cumulative prefix sum in O(n) space. 
3. do binary search each time to find the rightmost index to insert an elem
3. Find ans
Time = O((m+n)*logn) Space = O(n)
'''
class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        def get_right_most_index(arr, target):
            left = 0
            right = len(arr) - 1
            while left < right:
                mid = (left + right)//2
                if target < arr[mid]:
                    # search in left sub arr
                    right = mid
                elif target >= arr[mid]:
                    # search in right sub arr
                    left = mid + 1
            return left
            
        ans = []
        nums.sort()
        prefix = [0]*len(nums)
        prefix[0] = nums[0]
        for i in range(1, len(nums)):
            prefix[i] = prefix[i-1] + nums[i]
        max_prefix = prefix[-1]
        num_prefix = len(prefix)
        for query in queries:
            if query >= max_prefix:
                ans.append(num_prefix)
            else:
                ans.append(get_right_most_index(prefix, query))
        return ans
        
        
