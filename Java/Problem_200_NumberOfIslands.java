/*
Problem: 200 - Number of Islands
Difficulty: Medium
Link: https://leetcode.com/problems/number-of-islands/

Problem Statement:
Given an m x n 2D binary grid which represents a map of '1's (land) and '0's (water),
return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally 
or vertically. You may assume all four edges of the grid are all surrounded by water.

Approach:
Multiple approaches using graph traversal:

1. DFS (Depth-First Search) - Most intuitive
   - For each unvisited land cell, start DFS to mark entire island
   - Count number of DFS calls
   - Time: O(M×N), Space: O(M×N) for recursion stack

2. BFS (Breadth-First Search) - Iterative alternative
   - Use queue instead of recursion
   - Time: O(M×N), Space: O(min(M,N)) for queue

Time Complexity: O(M × N) - Visit each cell once
Space Complexity: O(M × N) - Recursion stack in worst case
*/

import java.util.*;

class Solution {
    // Approach 1: DFS - Most intuitive
    public int numIslands(char[][] grid) {
        if (grid == null || grid.length == 0) {
            return 0;
        }
        
        int rows = grid.length;
        int cols = grid[0].length;
        int count = 0;
        
        for (int r = 0; r < rows; r++) {
            for (int c = 0; c < cols; c++) {
                if (grid[r][c] == '1') {
                    count++;
                    dfs(grid, r, c);
                }
            }
        }
        
        return count;
    }
    
    private void dfs(char[][] grid, int r, int c) {
        int rows = grid.length;
        int cols = grid[0].length;
        
        // Base cases: out of bounds or water
        if (r < 0 || r >= rows || c < 0 || c >= cols || grid[r][c] == '0') {
            return;
        }
        
        // Mark as visited
        grid[r][c] = '0';
        
        // Explore all 4 directions
        dfs(grid, r + 1, c);  // Down
        dfs(grid, r - 1, c);  // Up
        dfs(grid, r, c + 1);  // Right
        dfs(grid, r, c - 1);  // Left
    }
    
    // Approach 2: BFS using queue
    public int numIslandsBFS(char[][] grid) {
        if (grid == null || grid.length == 0) {
            return 0;
        }
        
        int rows = grid.length;
        int cols = grid[0].length;
        int count = 0;
        
        int[][] directions = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
        
        for (int r = 0; r < rows; r++) {
            for (int c = 0; c < cols; c++) {
                if (grid[r][c] == '1') {
                    count++;
                    
                    // BFS
                    Queue<int[]> queue = new LinkedList<>();
                    queue.offer(new int[]{r, c});
                    grid[r][c] = '0';
                    
                    while (!queue.isEmpty()) {
                        int[] curr = queue.poll();
                        
                        for (int[] dir : directions) {
                            int nr = curr[0] + dir[0];
                            int nc = curr[1] + dir[1];
                            
                            if (nr >= 0 && nr < rows && nc >= 0 && nc < cols && grid[nr][nc] == '1') {
                                grid[nr][nc] = '0';
                                queue.offer(new int[]{nr, nc});
                            }
                        }
                    }
                }
            }
        }
        
        return count;
    }
    
    // Approach 3: DFS with visited set (doesn't modify grid)
    public int numIslandsVisited(char[][] grid) {
        if (grid == null || grid.length == 0) {
            return 0;
        }
        
        int rows = grid.length;
        int cols = grid[0].length;
        boolean[][] visited = new boolean[rows][cols];
        int count = 0;
        
        for (int r = 0; r < rows; r++) {
            for (int c = 0; c < cols; c++) {
                if (grid[r][c] == '1' && !visited[r][c]) {
                    count++;
                    dfsVisited(grid, r, c, visited);
                }
            }
        }
        
        return count;
    }
    
    private void dfsVisited(char[][] grid, int r, int c, boolean[][] visited) {
        int rows = grid.length;
        int cols = grid[0].length;
        
        if (r < 0 || r >= rows || c < 0 || c >= cols || 
            grid[r][c] == '0' || visited[r][c]) {
            return;
        }
        
        visited[r][c] = true;
        
        // Explore 4 directions
        dfsVisited(grid, r + 1, c, visited);
        dfsVisited(grid, r - 1, c, visited);
        dfsVisited(grid, r, c + 1, visited);
        dfsVisited(grid, r, c - 1, visited);
    }
    
    // Helper method to print grid
    private static void printGrid(char[][] grid) {
        for (char[] row : grid) {
            System.out.println(Arrays.toString(row));
        }
    }
    
    // Helper method to deep copy grid
    private static char[][] copyGrid(char[][] grid) {
        char[][] copy = new char[grid.length][];
        for (int i = 0; i < grid.length; i++) {
            copy[i] = grid[i].clone();
        }
        return copy;
    }
    
    // Test cases
    public static void main(String[] args) {
        Solution solution = new Solution();
        
        // Test case 1
        char[][] grid1 = {
            {'1','1','1','1','0'},
            {'1','1','0','1','0'},
            {'1','1','0','0','0'},
            {'0','0','0','0','0'}
        };
        System.out.println("Input: grid1");
        printGrid(grid1);
        System.out.println("Output: " + solution.numIslands(copyGrid(grid1)));
        System.out.println("Expected: 1\n");
        
        // Test case 2
        char[][] grid2 = {
            {'1','1','0','0','0'},
            {'1','1','0','0','0'},
            {'0','0','1','0','0'},
            {'0','0','0','1','1'}
        };
        System.out.println("Input: grid2");
        printGrid(grid2);
        System.out.println("Output: " + solution.numIslands(copyGrid(grid2)));
        System.out.println("Expected: 3\n");
        
        // Test case 3: Single cell
        char[][] grid3 = {{'1'}};
        System.out.println("Input: grid3");
        printGrid(grid3);
        System.out.println("Output: " + solution.numIslands(copyGrid(grid3)));
        System.out.println("Expected: 1\n");
        
        // Test case 4: All water
        char[][] grid4 = {
            {'0','0','0'},
            {'0','0','0'}
        };
        System.out.println("Input: grid4");
        printGrid(grid4);
        System.out.println("Output: " + solution.numIslands(copyGrid(grid4)));
        System.out.println("Expected: 0\n");
        
        // Compare all approaches
        char[][] grid5 = {
            {'1','0','1'},
            {'0','1','0'},
            {'1','0','1'}
        };
        System.out.println("Input: grid5");
        printGrid(grid5);
        System.out.println("DFS: " + solution.numIslands(copyGrid(grid5)));
        System.out.println("BFS: " + solution.numIslandsBFS(copyGrid(grid5)));
        System.out.println("Visited Set: " + solution.numIslandsVisited(copyGrid(grid5)));
        System.out.println("Expected: 5");
    }
}