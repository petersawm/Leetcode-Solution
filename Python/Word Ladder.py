"""
Problem: 127 - Word Ladder
Difficulty: Hard
Link: https://leetcode.com/problems/word-ladder/
Problem Statement:
Given two words, beginWord and endWord, and a dictionary wordList, return the 
number of words in the shortest transformation sequence from beginWord to 
endWord, or 0 if no such sequence exists.
One letter can be changed at a time, and each transformed word must exist in 
the word list.
Approach:
Use BFS (Breadth-First Search) to find shortest path.
For each word, generate all possible neighbors (one letter change).
Use a visited set to avoid revisiting words.
Time Complexity: O(N * L * 26) where N is word count, L is word length
Space Complexity: O(N)
"""
from collections import deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: list[str]) -> int:
        # Convert list to set for O(1) lookup
        word_set = set(wordList)
        
        # If endWord not in set, no solution
        if endWord not in word_set:
            return 0
        
        # BFS
        queue = deque([beginWord])
        visited = {beginWord}
        level = 1
        
        while queue:
            size = len(queue)
            
            # Process all words at current level
            for _ in range(size):
                word = queue.popleft()
                
                # If reached endWord
                if word == endWord:
                    return level
                
                # Generate all neighbors (one letter change)
                for neighbor in self.get_neighbors(word, word_set):
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append(neighbor)
            
            level += 1
        
        return 0  # No path found
    
    # Get all valid neighbors (one letter change)
    def get_neighbors(self, word: str, word_set: set) -> list[str]:
        neighbors = []
        word_list = list(word)
        
        # Try changing each position
        for i in range(len(word_list)):
            original = word_list[i]
            
            # Try all 26 letters
            for c in 'abcdefghijklmnopqrstuvwxyz':
                if c == original:
                    continue
                
                word_list[i] = c
                neighbor = ''.join(word_list)
                
                if neighbor in word_set:
                    neighbors.append(neighbor)
            
            word_list[i] = original
        
        return neighbors


# Test cases
if __name__ == "__main__":
    sol = Solution()
    
    # Test 1
    beginWord1 = "hit"
    endWord1 = "cog"
    wordList1 = ["hot", "dot", "dog", "lot", "log", "cog"]
    print("Output:", sol.ladderLength(beginWord1, endWord1, wordList1))
    # Expected: 5 (hit -> hot -> dot -> dog -> cog)
    
    # Test 2
    beginWord2 = "hit"
    endWord2 = "cog"
    wordList2 = ["hot", "dot", "dog", "lot", "log"]
    print("Output:", sol.ladderLength(beginWord2, endWord2, wordList2))
    # Expected: 0 (no path)
    
    # Test 3
    beginWord3 = "a"
    endWord3 = "c"
    wordList3 = ["a", "b", "c"]
    print("Output:", sol.ladderLength(beginWord3, endWord3, wordList3))
    # Expected: 2 (a -> c)