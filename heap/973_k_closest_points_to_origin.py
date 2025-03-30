import heapq
import math
def get_distance(point1, point2=[0,0]):
    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # O(nlogk) time and O(k) space complexity
        maxHeap = []
        for point in points:
            distance = get_distance(point)
            heapq.heappush(maxHeap, [-distance, point])
            if len(maxHeap) > k:
                heapq.heappop(maxHeap)
        return [elem[1] for elem in maxHeap]
      
