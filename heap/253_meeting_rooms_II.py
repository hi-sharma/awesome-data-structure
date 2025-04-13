'''
Sort by meeting end time and find overalls of endtime[i] and startime[i+1]
O(nlogn) time and O(n) space complexity
'''
import heapq
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals, key = lambda x : x[0])
        free_rooms = []
        heapq.heappush(free_rooms, intervals[0][-1])
        for i in range(1, len(intervals)):
            if free_rooms[0] <= intervals[i][0]:
                heapq.heappop(free_rooms)
            heapq.heappush(free_rooms, intervals[i][1])
        return len(free_rooms)
