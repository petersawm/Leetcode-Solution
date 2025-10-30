"""
Problem: 79 - Word Search
Difficulty: Medium
Link: https://leetcode.com/problems/word-search/

Problem Statement:
Given an m x n grid of characters board and a string word, return true if word exists 
in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent 
cells are horizontally or vertically neighboring. The same letter cell may not be used 
more than once.

Approach:
Use Backtracking with DFS:
1. Try each cell as starting point
2. Use DFS to explore all 4 directions
3. Mark visited cells temporarily
4. Backtrack if path doesn't lead to solution

Time Complexity: O(M × N × 4^L) where L is word length
Space Complexity: O(L) for recursion stack
"""

from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        """Backtracking with DFS"""
        if not board or not board[0]:
            return False
        
        rows, cols = len(board), len(board[0])
        
        def dfs(r: int, c: int, index: int) -> bool:
            # Found complete word
            if index == len(word):
                return True
            
            # Out of bounds or character doesn't match
            if (r < 0 or r >= rows or c < 0 or c >= cols or 
                board[r][c] != word[index]):
                return False
            
            # Mark as visited
            temp = board[r][c]
            board[r][c] = '#'
            
            # Explore all 4 directions
            found = (dfs(r + 1, c, index + 1) or
                    dfs(r - 1, c, index + 1) or
                    dfs(r, c + 1, index + 1) or
                    dfs(r, c - 1, index + 1))
            
            # Backtrack - restore cell
            board[r][c] = temp
            
            return found
        
        # Try each cell as starting point
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == word[0]:
                    if dfs(r, c, 0):
                        return True
        
        return False
    
    # Alternative: Using visited set instead of modifying board
    def existWithVisited(self, board: List[List[str]], word: str) -> bool:
        """Backtracking with visited set"""
        rows, cols = len(board), len(board[0])
        visited = set()
        
        def dfs(r: int, c: int, index: int) -> bool:
            if index == len(word):
                return True
            
            if (r < 0 or r >= rows or c < 0 or c >= cols or 
                (r, c) in visited or board[r][c] != word[index]):
                return False
            
            visited.add((r, c))
            
            found = (dfs(r + 1, c, index + 1) or
                    dfs(r - 1, c, index + 1) or
                    dfs(r, c + 1, index + 1) or
                    dfs(r, c - 1, index + 1))
            
            visited.remove((r, c))
            
            return found
        
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == word[0]:
                    if dfs(r, c, 0):
                        return True
        
        return False
    
    # Optimized: Early termination
    def existOptimized(self, board: List[List[str]], word: str) -> bool:
        """Optimized with early termination checks"""
        rows, cols = len(board), len(board[0])
        
        # Count characters in board
        board_count = {}
        for r in range(rows):
            for c in range(cols):
                board_count[board[r][c]] = board_count.get(board[r][c], 0) + 1
        
        # Check if board has enough characters
        word_count = {}
        for char in word:
            word_count[char] = word_count.get(char, 0) + 1
            if board_count.get(char, 0) < word_count[char]:
                return False
        
        # Reverse word if last character appears less frequently
        # (optimization to reduce search space)
        if board_count.get(word[0], 0) > board_count.get(word[-1], 0):
            word = word[::-1]
        
        def dfs(r: int, c: int, index: int) -> bool:
            if index == len(word):
                return True
            
            if (r < 0 or r >= rows or c < 0 or c >= cols or 
                board[r][c] != word[index]):
                return False
            
            temp = board[r][c]
            board[r][c] = '#'
            
            found = (dfs(r + 1, c, index + 1) or
                    dfs(r - 1, c, index + 1) or
                    dfs(r, c + 1, index + 1) or
                    dfs(r, c - 1, index + 1))
            
            board[r][c] = temp
            return found
        
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == word[0]:
                    if dfs(r, c, 0):
                        return True
        
        return False


# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1
    board1 = [
        ["A","B","C","E"],
        ["S","F","C","S"],
        ["A","D","E","E"]
    ]
    word1 = "ABCCED"
    print(f"Board:")
    for row in board1:
        print(row)
    print(f'Word: "{word1}"')
    print(f"Output: {solution.exist(board1, word1)}")
    print(f"Expected: True\n")
    
    # Test case 2
    board2 = [
        ["A","B","C","E"],
        ["S","F","C","S"],
        ["A","D","E","E"]
    ]
    word2 = "SEE"
    print(f'Word: "{word2}"')
    print(f"Output: {solution.exist(board2, word2)}")
    print(f"Expected: True\n")
    
    # Test case 3
    board3 = [
        ["A","B","C","E"],
        ["S","F","C","S"],
        ["A","D","E","E"]
    ]
    word3 = "ABCB"
    print(f'Word: "{word3}"')
    print(f"Output: {solution.exist(board3, word3)}")
    print(f"Expected: False\n")
    
    # Test case 4: Single cell
    board4 = [["a"]]
    word4 = "a"
    print(f"Board: {board4}")
    print(f'Word: "{word4}"')
    print(f"Output: {solution.exist(board4, word4)}")
    print(f"Expected: True\n")
    
    # Compare approaches
    board5 = [
        ["A","B","C","E"],
        ["S","F","C","S"],
        ["A","D","E","E"]
    ]
    word5 = "ABCCED"
    print("Compare approaches:")
    print(f"Standard: {solution.exist([row[:] for row in board5], word5)}")
    print(f"With Visited: {solution.existWithVisited([row[:] for row in board5], word5)}")
    print(f"Optimized: {solution.existOptimized([row[:] for row in board5], word5)}")