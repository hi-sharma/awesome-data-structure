#O(nlogk) where n = len(piles) and k = max(piles)
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def check(piles, k):
            # check if possible to eat with k=mid within h hours
            ans = 0
            for i in range(len(piles)):
                ans += ceil(piles[i]/k)
            return ans <= h

        left = 1
        right = max(piles)
        while left <= right:
            mid = (left + right)//2
            can_finish_piles = check(piles, mid)
            if can_finish_piles:
                # search in left sub arr to find min
                right = mid - 1
            else:
                # search in right sub arr to find min
                left = mid + 1
        return left
