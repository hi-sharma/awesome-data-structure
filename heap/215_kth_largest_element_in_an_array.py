import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
      # O(nlogk) time and O(k) space complexity
        minHeap = []
        for num in nums:
            heapq.heappush(minHeap, num)
            if len(minHeap) > k:
                heapq.heappop(minHeap)
        return heapq.heappop(minHeap)
