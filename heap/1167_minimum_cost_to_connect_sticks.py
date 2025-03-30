import heapq
class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        cost = 0
        stick_len = len(sticks)
        minHeap = sticks
        heapq.heapify(minHeap)
        while stick_len > 1:
            # Do something: get 2 min sticks, connect them, add to heap
            min1 = heapq.heappop(minHeap)
            min2 = heapq.heappop(minHeap)
            cost += min1 + min2
            heapq.heappush(minHeap, min1+ min2)
            # reduce counter
            stick_len -= 1
        return cost
        
