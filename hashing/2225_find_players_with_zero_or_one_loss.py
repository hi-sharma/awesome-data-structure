from collections import defaultdict 
class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
       #O(n) space complexity
        #O (nlog n) time complexity, k is # players
        win, loss = defaultdict(int), defaultdict(int)
        ans = []
        for match in matches:
            win[match[0]] += 1
            loss[match[1]] += 1
        # list of all players that have not lost any matches
        ans.append(sorted([player for player in win.keys() if player not in loss.keys()]))
        # list of all players that have lost exactly one match.
        ans.append(sorted(player for player, num_loss in loss.items() if num_loss==1))
        return ans

        
        
