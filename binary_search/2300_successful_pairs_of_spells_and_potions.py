'''
1 Sort potions in O(m*log m)
2. For each spell use binary search in potions to find the left most index to insert (success// spell[i] + 1)
'''
class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        def binary_search_left_most(arr, target):
            # arr can have duplicate entries
            left = 0
            right = len(arr) - 1
            while left < right:
                mid = (left + right)//2
                if target <= arr[mid]:
                    # search in left sub arr
                    right = mid
                elif target > arr[mid]:
                    # search in right sub arr
                    left = mid + 1
            return left

        potions.sort()
        max_potions = potions[-1]
        num_potions = len(potions)
        ans = []
        for spell in spells:
            left_most_index = bisect.bisect_left(potions, success / spell)
            # left_most_index = binary_search_left_most(potions, success / spell)
            ans.append(num_potions - left_most_index)
        return ans
            
        
        
