"""
Problem: 36 - Valid Sudoku
Difficulty: Medium
Link: https://leetcode.com/problems/valid-sudoku/

Problem Statement:
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated 
according to the following rules:
1. Each row must contain the digits 1-9 without repetition.
2. Each column must contain the digits 1-9 without repetition.
3. Each of the nine 3 x 3 sub-boxes must contain the digits 1-9 without repetition.

Note: A Sudoku board (partially filled) could be valid but is not necessarily solvable.

Approach:
Use hash sets to track seen numbers in:
- Each row
- Each column
- Each 3x3 box

For 3x3 boxes, use formula: box_index = (row // 3) * 3 + (col // 3)

Time Complexity: O(1) - Always 9x9 board = 81 cells
Space Complexity: O(1) - At most 27 sets with 9 elements each
"""

from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """Using sets for each row, column, and box"""
        # Initialize sets for rows, columns, and boxes
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        
        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    continue
                
                num = board[r][c]
                
                # Calculate box index
                box_idx = (r // 3) * 3 + (c // 3)
                
                # Check if number already exists
                if num in rows[r] or num in cols[c] or num in boxes[box_idx]:
                    return False
                
                # Add number to respective sets
                rows[r].add(num)
                cols[c].add(num)
                boxes[box_idx].add(num)
        
        return True
    
    # Using single set with tuple keys
    def isValidSudokuSingleSet(self, board: List[List[str]]) -> bool:
        """Using single set with tuple keys"""
        seen = set()
        
        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    continue
                
                num = board[r][c]
                
                # Create unique identifiers for row, col, and box
                row_key = (r, num)
                col_key = (num, c)
                box_key = (r // 3, c // 3, num)
                
                if row_key in seen or col_key in seen or box_key in seen:
                    return False
                
                seen.add(row_key)
                seen.add(col_key)
                seen.add(box_key)
        
        return True
    
    # Using dictionaries
    def isValidSudokuDict(self, board: List[List[str]]) -> bool:
        """Using dictionaries"""
        from collections import defaultdict
        
        rows = defaultdict(set)
        cols = defaultdict(set)
        boxes = defaultdict(set)
        
        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    continue
                
                num = board[r][c]
                box_idx = (r // 3, c // 3)
                
                if (num in rows[r] or 
                    num in cols[c] or 
                    num in boxes[box_idx]):
                    return False
                
                rows[r].add(num)
                cols[c].add(num)
                boxes[box_idx].add(num)
        
        return True
    
    # Bit manipulation approach (advanced)
    def isValidSudokuBitMask(self, board: List[List[str]]) -> bool:
        """Using bit masks for space optimization"""
        rows = [0] * 9
        cols = [0] * 9
        boxes = [0] * 9
        
        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    continue
                
                num = int(board[r][c]) - 1  # 0-indexed
                bit = 1 << num
                box_idx = (r // 3) * 3 + (c // 3)
                
                if (rows[r] & bit) or (cols[c] & bit) or (boxes[box_idx] & bit):
                    return False
                
                rows[r] |= bit
                cols[c] |= bit
                boxes[box_idx] |= bit
        
        return True


# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1: Valid sudoku
    board1 = [
        ["5","3",".",".","7",".",".",".","."],
        ["6",".",".","1","9","5",".",".","."],
        [".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],
        ["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],
        [".",".",".","4","1","9",".",".","5"],
        [".",".",".",".","8",".",".","7","9"]
    ]
    print("Test case 1: Valid Sudoku")
    print(f"Output: {solution.isValidSudoku(board1)}")
    print(f"Expected: True\n")
    
    # Test case 2: Invalid sudoku (duplicate in column)
    board2 = [
        ["8","3",".",".","7",".",".",".","."],
        ["6",".",".","1","9","5",".",".","."],
        [".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],
        ["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],
        [".",".",".","4","1","9",".",".","5"],
        [".",".",".",".","8",".",".","7","9"]
    ]
    print("Test case 2: Invalid Sudoku (duplicate 8 in first column)")
    print(f"Output: {solution.isValidSudoku(board2)}")
    print(f"Expected: False\n")
    
    # Test case 3: Invalid sudoku (duplicate in 3x3 box)
    board3 = [
        ["5","3",".",".","7",".",".",".","."],
        ["6",".",".","1","9","5",".",".","."],
        [".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],
        ["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],
        [".",".",".","4","1","9",".",".","5"],
        ["5",".",".","8",".",".",".","7","9"]
    ]
    print("Test case 3: Invalid Sudoku (duplicate 5 in box)")
    print(f"Output: {solution.isValidSudoku(board3)}")
    print(f"Expected: False\n")
    
    # Compare approaches
    print("Compare approaches on valid board:")
    print(f"Set-based: {solution.isValidSudoku(board1)}")
    print(f"Single Set: {solution.isValidSudokuSingleSet(board1)}")
    print(f"Dictionary: {solution.isValidSudokuDict(board1)}")
    print(f"Bit Mask: {solution.isValidSudokuBitMask(board1)}")