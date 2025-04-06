# sort in ascending order, pick till cumsum is <=5000. O(nlogn) time and O(n) space
class Solution:
    def maxNumberOfApples(self, weight: List[int]) -> int:
        weight = sorted(weight)
        cumSum = 0
        max_weight = 5000
        for i in range(len(weight)):
            cumSum += weight[i]
            if cumSum > max_weight:
                i -= 1
                break
        return i+1


        
