from collections import deque
class MovingAverage:

    def __init__(self, size: int):
        self.max_size = size
        self.queue = deque()
        
    def next(self, val: int) -> float:
        ans = []
        while self.queue and len(self.queue) >= self.max_size:
            self.queue.popleft()
        self.queue.append(val)
        if self.queue:
            return sum(self.queue)/len(self.queue)



# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
