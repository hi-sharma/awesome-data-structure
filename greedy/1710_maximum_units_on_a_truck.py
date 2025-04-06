'''
Arrange in decreasing order of units, i.e. 2nd index. Choose upto cumSum of 1st index of 10. Return sum of second index
O(nlogn) time and O(n) space
'''
class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes = sorted(boxTypes, key = lambda inner_list: inner_list[1], reverse=True)
        ans = 0 
        cumSum = 0
        print(boxTypes)
        for i in range(len(boxTypes)):
            print(i, cumSum, ans)
            if cumSum >= truckSize:
                return ans
            if cumSum + boxTypes[i][0] > truckSize:
                diff = truckSize - cumSum
                ans += boxTypes[i][1]* diff
                return ans
            cumSum += boxTypes[i][0]
            ans += boxTypes[i][1]*boxTypes[i][0]
        return ans
            
        
