"""
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

3. Union-Find - Advanced approach
   - Connect adjacent land cells
   - Count number of disjoint sets

Time Complexity: O(M × N) - Visit each cell once
Space Complexity: O(M × N) - Recursion stack in worst case
"""

from typing import List
from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """DFS approach - Most intuitive"""
        if not grid or not grid[0]:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        count = 0
        
        def dfs(r: int, c: int):
            # Base cases: out of bounds or water
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == '0':
                return
            
            # Mark as visited by changing to '0'
            grid[r][c] = '0'
            
            # Explore all 4 directions
            dfs(r + 1, c)  # Down
            dfs(r - 1, c)  # Up
            dfs(r, c + 1)  # Right
            dfs(r, c - 1)  # Left
        
        # Iterate through all cells
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    count += 1
                    dfs(r, c)  # Mark entire island
        
        return count
    
    # BFS approach
    def numIslandsBFS(self, grid: List[List[str]]) -> int:
        """BFS approach using queue"""
        if not grid or not grid[0]:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        count = 0
        
        def bfs(r: int, c: int):
            queue = deque([(r, c)])
            grid[r][c] = '0'
            
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            
            while queue:
                curr_r, curr_c = queue.popleft()
                
                for dr, dc in directions:
                    nr, nc = curr_r + dr, curr_c + dc
                    
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == '1':
                        grid[nr][nc] = '0'
                        queue.append((nr, nc))
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    count += 1
                    bfs(r, c)
        
        return count
    
    # DFS with visited set (doesn't modify grid)
    def numIslandsVisited(self, grid: List[List[str]]) -> int:
        """DFS with separate visited set"""
        if not grid or not grid[0]:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        visited = set()
        count = 0
        
        def dfs(r: int, c: int):
            if (r < 0 or r >= rows or c < 0 or c >= cols or 
                grid[r][c] == '0' or (r, c) in visited):
                return
            
            visited.add((r, c))
            
            # Explore 4 directions
            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                dfs(r + dr, c + dc)
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1' and (r, c) not in visited:
                    count += 1
                    dfs(r, c)
        
        return count
    
    # Union-Find approach
    def numIslandsUnionFind(self, grid: List[List[str]]) -> int:
        """Union-Find (Disjoint Set) approach"""
        if not grid or not grid[0]:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        
        class UnionFind:
            def __init__(self, grid):
                self.parent = {}
                self.rank = {}
                self.count = 0
                
                for r in range(rows):
                    for c in range(cols):
                        if grid[r][c] == '1':
                            self.parent[(r, c)] = (r, c)
                            self.rank[(r, c)] = 0
                            self.count += 1
            
            def find(self, x):
                if self.parent[x] != x:
                    self.parent[x] = self.find(self.parent[x])
                return self.parent[x]
            
            def union(self, x, y):
                root_x = self.find(x)
                root_y = self.find(y)
                
                if root_x != root_y:
                    if self.rank[root_x] > self.rank[root_y]:
                        self.parent[root_y] = root_x
                    elif self.rank[root_x] < self.rank[root_y]:
                        self.parent[root_x] = root_y
                    else:
                        self.parent[root_y] = root_x
                        self.rank[root_x] += 1
                    self.count -= 1
        
        uf = UnionFind(grid)
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    # Union with right neighbor
                    if c + 1 < cols and grid[r][c + 1] == '1':
                        uf.union((r, c), (r, c + 1))
                    # Union with down neighbor
                    if r + 1 < rows and grid[r + 1][c] == '1':
                        uf.union((r, c), (r + 1, c))
        
        return uf.count


# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1
    grid1 = [
        ["1","1","1","1","0"],
        ["1","1","0","1","0"],
        ["1","1","0","0","0"],
        ["0","0","0","0","0"]
    ]
    print("Input: grid1")
    for row in grid1:
        print(row)
    print(f"Output: {solution.numIslands([row[:] for row in grid1])}")
    print(f"Expected: 1\n")
    
    # Test case 2
    grid2 = [
        ["1","1","0","0","0"],
        ["1","1","0","0","0"],
        ["0","0","1","0","0"],
        ["0","0","0","1","1"]
    ]
    print("Input: grid2")
    for row in grid2:
        print(row)
    print(f"Output: {solution.numIslands([row[:] for row in grid2])}")
    print(f"Expected: 3\n")
    
    # Test case 3: Single cell
    grid3 = [["1"]]
    print(f"Input: {grid3}")
    print(f"Output: {solution.numIslands([row[:] for row in grid3])}")
    print(f"Expected: 1\n")
    
    # Compare all approaches
    grid4 = [
        ["1","0","1"],
        ["0","1","0"],
        ["1","0","1"]
    ]
    print("Input: grid4")
    for row in grid4:
        print(row)
    print(f"DFS: {solution.numIslands([row[:] for row in grid4])}")
    print(f"BFS: {solution.numIslandsBFS([row[:] for row in grid4])}")
    print(f"Visited Set: {solution.numIslandsVisited([row[:] for row in grid4])}")
    print(f"Union-Find: {solution.numIslandsUnionFind([row[:] for row in grid4])}")
    print(f"Expected: 5")