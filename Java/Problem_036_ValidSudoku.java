/*
Problem: 36 - Valid Sudoku
Difficulty: Medium
Link: https://leetcode.com/problems/valid-sudoku/

Problem Statement:
Determine if a 9 x 9 Sudoku board is valid according to Sudoku rules.

Approach:
Use hash sets to track seen numbers in rows, columns, and 3x3 boxes.

Time Complexity: O(1) - Always 9x9 board = 81 cells
Space Complexity: O(1) - At most 27 sets
*/

import java.util.*;

class Solution {
    // Approach 1: Using sets for each row, column, and box
    public boolean isValidSudoku(char[][] board) {
        Set<Character>[] rows = new HashSet[9];
        Set<Character>[] cols = new HashSet[9];
        Set<Character>[] boxes = new HashSet[9];
        
        for (int i = 0; i < 9; i++) {
            rows[i] = new HashSet<>();
            cols[i] = new HashSet<>();
            boxes[i] = new HashSet<>();
        }
        
        for (int r = 0; r < 9; r++) {
            for (int c = 0; c < 9; c++) {
                if (board[r][c] == '.') {
                    continue;
                }
                
                char num = board[r][c];
                int boxIdx = (r / 3) * 3 + (c / 3);
                
                if (rows[r].contains(num) || 
                    cols[c].contains(num) || 
                    boxes[boxIdx].contains(num)) {
                    return false;
                }
                
                rows[r].add(num);
                cols[c].add(num);
                boxes[boxIdx].add(num);
            }
        }
        
        return true;
    }
    
    // Approach 2: Using single set with string keys
    public boolean isValidSudokuSingleSet(char[][] board) {
        Set<String> seen = new HashSet<>();
        
        for (int r = 0; r < 9; r++) {
            for (int c = 0; c < 9; c++) {
                if (board[r][c] == '.') {
                    continue;
                }
                
                char num = board[r][c];
                
                if (!seen.add(num + " in row " + r) ||
                    !seen.add(num + " in col " + c) ||
                    !seen.add(num + " in box " + (r/3) + "-" + (c/3))) {
                    return false;
                }
            }
        }
        
        return true;
    }
    
    // Approach 3: Using bit masks
    public boolean isValidSudokuBitMask(char[][] board) {
        int[] rows = new int[9];
        int[] cols = new int[9];
        int[] boxes = new int[9];
        
        for (int r = 0; r < 9; r++) {
            for (int c = 0; c < 9; c++) {
                if (board[r][c] == '.') {
                    continue;
                }
                
                int num = board[r][c] - '1';  // 0-indexed
                int bit = 1 << num;
                int boxIdx = (r / 3) * 3 + (c / 3);
                
                if ((rows[r] & bit) != 0 || 
                    (cols[c] & bit) != 0 || 
                    (boxes[boxIdx] & bit) != 0) {
                    return false;
                }
                
                rows[r] |= bit;
                cols[c] |= bit;
                boxes[boxIdx] |= bit;
            }
        }
        
        return true;
    }
    
    // Test cases
    public static void main(String[] args) {
        Solution solution = new Solution();
        
        // Test case 1: Valid sudoku
        char[][] board1 = {
            {'5','3','.','.','7','.','.','.','.'},
            {'6','.','.','1','9','5','.','.','.'},
            {'.','9','8','.','.','.','.','6','.'},
            {'8','.','.','.','6','.','.','.','3'},
            {'4','.','.','8','.','3','.','.','1'},
            {'7','.','.','.','2','.','.','.','6'},
            {'.','6','.','.','.','.','2','8','.'},
            {'.','.','.','4','1','9','.','.','5'},
            {'.','.','.','.','8','.','.','7','9'}
        };
        System.out.println("Test case 1: Valid Sudoku");
        System.out.println("Output: " + solution.isValidSudoku(board1));
        System.out.println("Expected: true\n");
        
        // Test case 2: Invalid sudoku
        char[][] board2 = {
            {'8','3','.','.','7','.','.','.','.'},
            {'6','.','.','1','9','5','.','.','.'},
            {'.','9','8','.','.','.','.','6','.'},
            {'8','.','.','.','6','.','.','.','3'},
            {'4','.','.','8','.','3','.','.','1'},
            {'7','.','.','.','2','.','.','.','6'},
            {'.','6','.','.','.','.','2','8','.'},
            {'.','.','.','4','1','9','.','.','5'},
            {'.','.','.','.','8','.','.','7','9'}
        };
        System.out.println("Test case 2: Invalid Sudoku");
        System.out.println("Output: " + solution.isValidSudoku(board2));
        System.out.println("Expected: false\n");
        
        // Compare approaches
        System.out.println("Compare approaches on valid board:");
        System.out.println("Set-based: " + solution.isValidSudoku(board1));
        System.out.println("Single Set: " + solution.isValidSudokuSingleSet(board1));
        System.out.println("Bit Mask: " + solution.isValidSudokuBitMask(board1));
    }
}