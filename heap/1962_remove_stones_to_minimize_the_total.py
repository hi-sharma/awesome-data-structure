import heapq
class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        total_sum = sum(piles)
        maxHeap = [-pile for pile in piles]
        heapq.heapify(maxHeap)
        while k > 0:
            max_ =  -heapq.heappop(maxHeap)
            total_sum = total_sum - max_//2
            max_ = max_ - max_ //2
            heapq.heappush(maxHeap, -max_)
            k -= 1
        return total_sum
