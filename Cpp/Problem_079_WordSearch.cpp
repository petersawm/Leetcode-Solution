/*
Problem: 79 - Word Search
Difficulty: Medium
Link: https://leetcode.com/problems/word-search/

Problem Statement:
Given an m x n grid of characters board and a string word, return true if word exists 
in the grid. The word can be constructed from letters of sequentially adjacent cells.

Approach:
Use Backtracking with DFS

Time Complexity: O(M × N × 4^L) where L is word length
Space Complexity: O(L) for recursion stack
*/

#include <vector>
#include <string>
#include <iostream>

using namespace std;

class Solution {
public:
    bool exist(vector<vector<char>>& board, string word) {
        if (board.empty() || board[0].empty()) {
            return false;
        }
        
        int rows = board.size();
        int cols = board[0].size();
        
        // Try each cell as starting point
        for (int r = 0; r < rows; r++) {
            for (int c = 0; c < cols; c++) {
                if (board[r][c] == word[0]) {
                    if (dfs(board, word, r, c, 0)) {
                        return true;
                    }
                }
            }
        }
        
        return false;
    }
    
private:
    bool dfs(vector<vector<char>>& board, const string& word, int r, int c, int index) {
        // Found complete word
        if (index == word.length()) {
            return true;
        }
        
        // Out of bounds or character doesn't match
        if (r < 0 || r >= board.size() || c < 0 || c >= board[0].size() ||
            board[r][c] != word[index]) {
            return false;
        }
        
        // Mark as visited
        char temp = board[r][c];
        board[r][c] = '#';
        
        // Explore all 4 directions
        bool found = dfs(board, word, r + 1, c, index + 1) ||
                    dfs(board, word, r - 1, c, index + 1) ||
                    dfs(board, word, r, c + 1, index + 1) ||
                    dfs(board, word, r, c - 1, index + 1);
        
        // Backtrack - restore cell
        board[r][c] = temp;
        
        return found;
    }
    
public:
    // Alternative: Using visited array
    bool existWithVisited(vector<vector<char>>& board, string word) {
        int rows = board.size();
        int cols = board[0].size();
        vector<vector<bool>> visited(rows, vector<bool>(cols, false));
        
        for (int r = 0; r < rows; r++) {
            for (int c = 0; c < cols; c++) {
                if (board[r][c] == word[0]) {
                    if (dfsWithVisited(board, word, r, c, 0, visited)) {
                        return true;
                    }
                }
            }
        }
        
        return false;
    }
    
private:
    bool dfsWithVisited(vector<vector<char>>& board, const string& word, 
                       int r, int c, int index, vector<vector<bool>>& visited) {
        if (index == word.length()) {
            return true;
        }
        
        if (r < 0 || r >= board.size() || c < 0 || c >= board[0].size() ||
            visited[r][c] || board[r][c] != word[index]) {
            return false;
        }
        
        visited[r][c] = true;
        
        bool found = dfsWithVisited(board, word, r + 1, c, index + 1, visited) ||
                    dfsWithVisited(board, word, r - 1, c, index + 1, visited) ||
                    dfsWithVisited(board, word, r, c + 1, index + 1, visited) ||
                    dfsWithVisited(board, word, r, c - 1, index + 1, visited);
        
        visited[r][c] = false;
        
        return found;
    }
};

// Helper function to print board
void printBoard(const vector<vector<char>>& board) {
    for (const auto& row : board) {
        cout << "[";
        for (int i = 0; i < row.size(); i++) {
            cout << "'" << row[i] << "'";
            if (i < row.size() - 1) cout << ",";
        }
        cout << "]" << endl;
    }
}

// Helper function to copy board
vector<vector<char>> copyBoard(const vector<vector<char>>& board) {
    return board;
}

int main() {
    Solution solution;
    
    // Test case 1
    vector<vector<char>> board1 = {
        {'A','B','C','E'},
        {'S','F','C','S'},
        {'A','D','E','E'}
    };
    string word1 = "ABCCED";
    cout << "Board:" << endl;
    printBoard(board1);
    cout << "Word: \"" << word1 << "\"" << endl;
    cout << "Output: " << (solution.exist(copyBoard(board1), word1) ? "true" : "false") << endl;
    cout << "Expected: true\n" << endl;
    
    // Test case 2
    vector<vector<char>> board2 = {
        {'A','B','C','E'},
        {'S','F','C','S'},
        {'A','D','E','E'}
    };
    string word2 = "SEE";
    cout << "Word: \"" << word2 << "\"" << endl;
    cout << "Output: " << (solution.exist(copyBoard(board2), word2) ? "true" : "false") << endl;
    cout << "Expected: true\n" << endl;
    
    // Test case 3
    vector<vector<char>> board3 = {
        {'A','B','C','E'},
        {'S','F','C','S'},
        {'A','D','E','E'}
    };
    string word3 = "ABCB";
    cout << "Word: \"" << word3 << "\"" << endl;
    cout << "Output: " << (solution.exist(copyBoard(board3), word3) ? "true" : "false") << endl;
    cout << "Expected: false\n" << endl;
    
    // Compare approaches
    vector<vector<char>> board4 = {
        {'A','B','C','E'},
        {'S','F','C','S'},
        {'A','D','E','E'}
    };
    string word4 = "ABCCED";
    cout << "Compare approaches:" << endl;
    cout << "Standard: " << (solution.exist(copyBoard(board4), word4) ? "true" : "false") << endl;
    cout << "With Visited: " << (solution.existWithVisited(copyBoard(board4), word4) ? "true" : "false") << endl;
    
    return 0;
}