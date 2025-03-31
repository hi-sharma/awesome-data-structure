from collections import deque
import string

class Solution:
    # O(m*2 * n) m is length of each word and n is total number of words in the input word list
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        lowercase_letters = list(string.ascii_lowercase)
        def get_neighbours(word):
            # get neighbours by changing i single letter in word
            ans = []
            for i in range(len(word)):
                for letter in lowercase_letters:
                    if letter != word[i]:
                        ans.append(word[:i] + letter + word[i+1:])
            return ans


        wordList = set(wordList)
        if endWord not in wordList:
            return 0
        steps = 1
        queue = deque([(beginWord, steps)])
        
        seen = {beginWord}

        while queue:
            word, steps = queue.popleft()
            if word == endWord:
                return steps
            neighbours = get_neighbours(word)
            for neighbour in neighbours:
                if neighbour in wordList and neighbour not in seen:
                    seen.add(neighbour)
                    queue.append([neighbour, steps + 1])
        return 0
                    
