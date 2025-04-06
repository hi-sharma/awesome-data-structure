'''
Sort the arr and initialise cumSum with mass. Each step check if asteroid can be destroyed greedily
O(nlogn) time
'''
class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        asteroids.sort()
        cumSum = mass
        for i in range(len(asteroids)):
            if cumSum >= asteroids[i]:
                cumSum += asteroids[i]
            else:
                return False
        return True
        
