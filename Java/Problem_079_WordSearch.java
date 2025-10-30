/*
Problem: 79 - Word Search
Difficulty: Medium
Link: https://leetcode.com/problems/word-search/

Problem Statement:
Given an m x n grid of characters board and a string word, return true if word exists 
in the grid. The word can be constructed from letters of sequentially adjacent cells.

Approach:
Use Backtracking with DFS:
1. Try each cell as starting point
2. Use DFS to explore all 4 directions
3. Mark visited cells temporarily
4. Backtrack if path doesn't lead to solution

Time Complexity: O(M × N × 4^L) where L is word length
Space Complexity: O(L) for recursion stack
*/

class Solution {
    public boolean exist(char[][] board, String word) {
        if (board == null || board.length == 0) {
            return false;
        }
        
        int rows = board.length;
        int cols = board[0].length;
        
        // Try each cell as starting point
        for (int r = 0; r < rows; r++) {
            for (int c = 0; c < cols; c++) {
                if (board[r][c] == word.charAt(0)) {
                    if (dfs(board, word, r, c, 0)) {
                        return true;
                    }
                }
            }
        }
        
        return false;
    }
    
    private boolean dfs(char[][] board, String word, int r, int c, int index) {
        // Found complete word
        if (index == word.length()) {
            return true;
        }
        
        // Out of bounds or character doesn't match
        if (r < 0 || r >= board.length || c < 0 || c >= board[0].length ||
            board[r][c] != word.charAt(index)) {
            return false;
        }
        
        // Mark as visited
        char temp = board[r][c];
        board[r][c] = '#';
        
        // Explore all 4 directions
        boolean found = dfs(board, word, r + 1, c, index + 1) ||
                       dfs(board, word, r - 1, c, index + 1) ||
                       dfs(board, word, r, c + 1, index + 1) ||
                       dfs(board, word, r, c - 1, index + 1);
        
        // Backtrack - restore cell
        board[r][c] = temp;
        
        return found;
    }
    
    // Alternative: Using boolean visited array
    public boolean existWithVisited(char[][] board, String word) {
        int rows = board.length;
        int cols = board[0].length;
        boolean[][] visited = new boolean[rows][cols];
        
        for (int r = 0; r < rows; r++) {
            for (int c = 0; c < cols; c++) {
                if (board[r][c] == word.charAt(0)) {
                    if (dfsWithVisited(board, word, r, c, 0, visited)) {
                        return true;
                    }
                }
            }
        }
        
        return false;
    }
    
    private boolean dfsWithVisited(char[][] board, String word, int r, int c, 
                                   int index, boolean[][] visited) {
        if (index == word.length()) {
            return true;
        }
        
        if (r < 0 || r >= board.length || c < 0 || c >= board[0].length ||
            visited[r][c] || board[r][c] != word.charAt(index)) {
            return false;
        }
        
        visited[r][c] = true;
        
        boolean found = dfsWithVisited(board, word, r + 1, c, index + 1, visited) ||
                       dfsWithVisited(board, word, r - 1, c, index + 1, visited) ||
                       dfsWithVisited(board, word, r, c + 1, index + 1, visited) ||
                       dfsWithVisited(board, word, r, c - 1, index + 1, visited);
        
        visited[r][c] = false;
        
        return found;
    }
    
    // Helper method to print board
    private static void printBoard(char[][] board) {
        for (char[] row : board) {
            System.out.print("[");
            for (int i = 0; i < row.length; i++) {
                System.out.print("'" + row[i] + "'");
                if (i < row.length - 1) System.out.print(",");
            }
            System.out.println("]");
        }
    }
    
    // Helper method to copy board
    private static char[][] copyBoard(char[][] board) {
        char[][] copy = new char[board.length][];
        for (int i = 0; i < board.length; i++) {
            copy[i] = board[i].clone();
        }
        return copy;
    }
    
    // Test cases
    public static void main(String[] args) {
        Solution solution = new Solution();
        
        // Test case 1
        char[][] board1 = {
            {'A','B','C','E'},
            {'S','F','C','S'},
            {'A','D','E','E'}
        };
        String word1 = "ABCCED";
        System.out.println("Board:");
        printBoard(board1);
        System.out.println("Word: \"" + word1 + "\"");
        System.out.println("Output: " + solution.exist(copyBoard(board1), word1));
        System.out.println("Expected: true\n");
        
        // Test case 2
        char[][] board2 = {
            {'A','B','C','E'},
            {'S','F','C','S'},
            {'A','D','E','E'}
        };
        String word2 = "SEE";
        System.out.println("Word: \"" + word2 + "\"");
        System.out.println("Output: " + solution.exist(copyBoard(board2), word2));
        System.out.println("Expected: true\n");
        
        // Test case 3
        char[][] board3 = {
            {'A','B','C','E'},
            {'S','F','C','S'},
            {'A','D','E','E'}
        };
        String word3 = "ABCB";
        System.out.println("Word: \"" + word3 + "\"");
        System.out.println("Output: " + solution.exist(copyBoard(board3), word3));
        System.out.println("Expected: false\n");
        
        // Compare approaches
        char[][] board4 = {
            {'A','B','C','E'},
            {'S','F','C','S'},
            {'A','D','E','E'}
        };
        String word4 = "ABCCED";
        System.out.println("Compare approaches:");
        System.out.println("Standard: " + solution.exist(copyBoard(board4), word4));
        System.out.println("With Visited: " + solution.existWithVisited(copyBoard(board4), word4));
    }
}