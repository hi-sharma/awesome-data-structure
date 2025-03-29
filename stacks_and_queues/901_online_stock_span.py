from collections import deque
class StockSpanner:

    def __init__(self):
        self.queue = deque()
        
    def next(self, price: int) -> int:
        # O(1) amortized time complexity as total n elements and  O(n) space complexity
        # maintain the queue
        ans = 1
        while self.queue and self.queue[-1][0] < price:
            ans += self.queue.pop()[1]
        self.queue.append([price, ans])
        return ans


        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
