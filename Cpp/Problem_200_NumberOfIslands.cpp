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

#include <vector>
#include <iostream>
#include <queue>
#include <set>

using namespace std;

class Solution {
public:
    // Approach 1: DFS - Most intuitive
    int numIslands(vector<vector<char>>& grid) {
        if (grid.empty() || grid[0].empty()) {
            return 0;
        }
        
        int rows = grid.size();
        int cols = grid[0].size();
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
    
private:
    void dfs(vector<vector<char>>& grid, int r, int c) {
        int rows = grid.size();
        int cols = grid[0].size();
        
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
    
public:
    // Approach 2: BFS using queue
    int numIslandsBFS(vector<vector<char>>& grid) {
        if (grid.empty() || grid[0].empty()) {
            return 0;
        }
        
        int rows = grid.size();
        int cols = grid[0].size();
        int count = 0;
        
        vector<pair<int, int>> directions = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
        
        for (int r = 0; r < rows; r++) {
            for (int c = 0; c < cols; c++) {
                if (grid[r][c] == '1') {
                    count++;
                    
                    // BFS
                    queue<pair<int, int>> q;
                    q.push({r, c});
                    grid[r][c] = '0';
                    
                    while (!q.empty()) {
                        auto [curr_r, curr_c] = q.front();
                        q.pop();
                        
                        for (auto [dr, dc] : directions) {
                            int nr = curr_r + dr;
                            int nc = curr_c + dc;
                            
                            if (nr >= 0 && nr < rows && nc >= 0 && nc < cols && grid[nr][nc] == '1') {
                                grid[nr][nc] = '0';
                                q.push({nr, nc});
                            }
                        }
                    }
                }
            }
        }
        
        return count;
    }
    
    // Approach 3: DFS with visited set (doesn't modify grid)
    int numIslandsVisited(vector<vector<char>>& grid) {
        if (grid.empty() || grid[0].empty()) {
            return 0;
        }
        
        int rows = grid.size();
        int cols = grid[0].size();
        set<pair<int, int>> visited;
        int count = 0;
        
        for (int r = 0; r < rows; r++) {
            for (int c = 0; c < cols; c++) {
                if (grid[r][c] == '1' && visited.find({r, c}) == visited.end()) {
                    count++;
                    dfsVisited(grid, r, c, visited);
                }
            }
        }
        
        return count;
    }
    
private:
    void dfsVisited(vector<vector<char>>& grid, int r, int c, set<pair<int, int>>& visited) {
        int rows = grid.size();
        int cols = grid[0].size();
        
        if (r < 0 || r >= rows || c < 0 || c >= cols || 
            grid[r][c] == '0' || visited.find({r, c}) != visited.end()) {
            return;
        }
        
        visited.insert({r, c});
        
        // Explore 4 directions
        dfsVisited(grid, r + 1, c, visited);
        dfsVisited(grid, r - 1, c, visited);
        dfsVisited(grid, r, c + 1, visited);
        dfsVisited(grid, r, c - 1, visited);
    }
};

// Helper function to print grid
void printGrid(const vector<vector<char>>& grid) {
    for (const auto& row : grid) {
        cout << "[";
        for (int i = 0; i < row.size(); i++) {
            cout << "'" << row[i] << "'";
            if (i < row.size() - 1) cout << ",";
        }
        cout << "]" << endl;
    }
}

// Helper function to deep copy grid
vector<vector<char>> copyGrid(const vector<vector<char>>& grid) {
    return grid;
}

int main() {
    Solution solution;
    
    // Test case 1
    vector<vector<char>> grid1 = {
        {'1','1','1','1','0'},
        {'1','1','0','1','0'},
        {'1','1','0','0','0'},
        {'0','0','0','0','0'}
    };
    cout << "Input: grid1" << endl;
    printGrid(grid1);
    cout << "Output: " << solution.numIslands(copyGrid(grid1)) << endl;
    cout << "Expected: 1\n\n";
    
    // Test case 2
    vector<vector<char>> grid2 = {
        {'1','1','0','0','0'},
        {'1','1','0','0','0'},
        {'0','0','1','0','0'},
        {'0','0','0','1','1'}
    };
    cout << "Input: grid2" << endl;
    printGrid(grid2);
    cout << "Output: " << solution.numIslands(copyGrid(grid2)) << endl;
    cout << "Expected: 3\n\n";
    
    // Test case 3: Single cell
    vector<vector<char>> grid3 = {{'1'}};
    cout << "Input: grid3" << endl;
    printGrid(grid3);
    cout << "Output: " << solution.numIslands(copyGrid(grid3)) << endl;
    cout << "Expected: 1\n\n";
    
    // Test case 4: All water
    vector<vector<char>> grid4 = {
        {'0','0','0'},
        {'0','0','0'}
    };
    cout << "Input: grid4" << endl;
    printGrid(grid4);
    cout << "Output: " << solution.numIslands(copyGrid(grid4)) << endl;
    cout << "Expected: 0\n\n";
    
    // Compare all approaches
    vector<vector<char>> grid5 = {
        {'1','0','1'},
        {'0','1','0'},
        {'1','0','1'}
    };
    cout << "Input: grid5" << endl;
    printGrid(grid5);
    cout << "DFS: " << solution.numIslands(copyGrid(grid5)) << endl;
    cout << "BFS: " << solution.numIslandsBFS(copyGrid(grid5)) << endl;
    cout << "Visited Set: " << solution.numIslandsVisited(copyGrid(grid5)) << endl;
    cout << "Expected: 5" << endl;
    
    return 0;
}