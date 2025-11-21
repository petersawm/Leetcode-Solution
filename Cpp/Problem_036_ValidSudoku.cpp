/*
Problem: 36 - Valid Sudoku
Difficulty: Medium
Link: https://leetcode.com/problems/valid-sudoku/

Problem Statement:
Determine if a 9 x 9 Sudoku board is valid according to Sudoku rules.

Approach:
Use unordered_sets to track seen numbers in rows, columns, and 3x3 boxes.

Time Complexity: O(1) - Always 9x9 board = 81 cells
Space Complexity: O(1) - At most 27 sets
*/

#include <vector>
#include <unordered_set>
#include <string>
#include <iostream>

using namespace std;

class Solution {
public:
    // Approach 1: Using sets for each row, column, and box
    bool isValidSudoku(vector<vector<char>>& board) {
        vector<unordered_set<char>> rows(9);
        vector<unordered_set<char>> cols(9);
        vector<unordered_set<char>> boxes(9);
        
        for (int r = 0; r < 9; r++) {
            for (int c = 0; c < 9; c++) {
                if (board[r][c] == '.') {
                    continue;
                }
                
                char num = board[r][c];
                int boxIdx = (r / 3) * 3 + (c / 3);
                
                if (rows[r].count(num) || 
                    cols[c].count(num) || 
                    boxes[boxIdx].count(num)) {
                    return false;
                }
                
                rows[r].insert(num);
                cols[c].insert(num);
                boxes[boxIdx].insert(num);
            }
        }
        
        return true;
    }
    
    // Approach 2: Using single set with string keys
    bool isValidSudokuSingleSet(vector<vector<char>>& board) {
        unordered_set<string> seen;
        
        for (int r = 0; r < 9; r++) {
            for (int c = 0; c < 9; c++) {
                if (board[r][c] == '.') {
                    continue;
                }
                
                char num = board[r][c];
                
                string rowKey = string(1, num) + " in row " + to_string(r);
                string colKey = string(1, num) + " in col " + to_string(c);
                string boxKey = string(1, num) + " in box " + to_string(r/3) + "-" + to_string(c/3);
                
                if (seen.count(rowKey) || seen.count(colKey) || seen.count(boxKey)) {
                    return false;
                }
                
                seen.insert(rowKey);
                seen.insert(colKey);
                seen.insert(boxKey);
            }
        }
        
        return true;
    }
    
    // Approach 3: Using bit masks
    bool isValidSudokuBitMask(vector<vector<char>>& board) {
        vector<int> rows(9, 0);
        vector<int> cols(9, 0);
        vector<int> boxes(9, 0);
        
        for (int r = 0; r < 9; r++) {
            for (int c = 0; c < 9; c++) {
                if (board[r][c] == '.') {
                    continue;
                }
                
                int num = board[r][c] - '1';  // 0-indexed
                int bit = 1 << num;
                int boxIdx = (r / 3) * 3 + (c / 3);
                
                if ((rows[r] & bit) || (cols[c] & bit) || (boxes[boxIdx] & bit)) {
                    return false;
                }
                
                rows[r] |= bit;
                cols[c] |= bit;
                boxes[boxIdx] |= bit;
            }
        }
        
        return true;
    }
};

int main() {
    Solution solution;
    
    // Test case 1: Valid sudoku
    vector<vector<char>> board1 = {
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
    cout << "Test case 1: Valid Sudoku" << endl;
    cout << "Output: " << (solution.isValidSudoku(board1) ? "true" : "false") << endl;
    cout << "Expected: true\n" << endl;
    
    // Test case 2: Invalid sudoku
    vector<vector<char>> board2 = {
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
    cout << "Test case 2: Invalid Sudoku" << endl;
    cout << "Output: " << (solution.isValidSudoku(board2) ? "true" : "false") << endl;
    cout << "Expected: false\n" << endl;
    
    // Compare approaches
    cout << "Compare approaches on valid board:" << endl;
    cout << "Set-based: " << (solution.isValidSudoku(board1) ? "true" : "false") << endl;
    cout << "Single Set: " << (solution.isValidSudokuSingleSet(board1) ? "true" : "false") << endl;
    cout << "Bit Mask: " << (solution.isValidSudokuBitMask(board1) ? "true" : "false") << endl;
    
    return 0;
}