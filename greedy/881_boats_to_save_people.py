# sort the arr, maintain two pointers and try to pair lightest person with the heaviest person
# O(nlogn) time and O(n) space for sorting
class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        ans = 0
        left = 0 
        right = len(people) - 1
        while left < right:
            if people[left] + people[right] <= limit:
                left += 1
                right -= 1
            else:
                right -= 1
            ans += 1
        if left == right:
            ans += 1
        return ans
            

        
