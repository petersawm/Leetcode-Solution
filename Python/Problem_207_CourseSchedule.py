"""
Problem: 207 - Course Schedule
Difficulty: Medium
Link: https://leetcode.com/problems/course-schedule/

Problem Statement:
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1.
You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you 
must take course bi first if you want to take course ai.

Return true if you can finish all courses. Otherwise, return false.

Approach:
This is a cycle detection problem in a directed graph.

1. DFS with cycle detection:
   - Use 3 states: unvisited (0), visiting (1), visited (2)
   - If we encounter a node in "visiting" state, there's a cycle
   
2. BFS (Kahn's Algorithm - Topological Sort):
   - Use in-degree array
   - Process nodes with in-degree 0
   - If we process all nodes, no cycle exists

Time Complexity: O(V + E) where V = courses, E = prerequisites
Space Complexity: O(V + E) for adjacency list
"""

from typing import List
from collections import deque, defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """DFS with cycle detection"""
        # Build adjacency list
        graph = defaultdict(list)
        for course, prereq in prerequisites:
            graph[prereq].append(course)
        
        # States: 0 = unvisited, 1 = visiting, 2 = visited
        state = [0] * numCourses
        
        def has_cycle(course: int) -> bool:
            """Returns True if cycle detected"""
            if state[course] == 1:  # Currently visiting - cycle!
                return True
            if state[course] == 2:  # Already visited
                return False
            
            # Mark as visiting
            state[course] = 1
            
            # Visit all neighbors
            for neighbor in graph[course]:
                if has_cycle(neighbor):
                    return True
            
            # Mark as visited
            state[course] = 2
            return False
        
        # Check each course
        for course in range(numCourses):
            if state[course] == 0:  # Unvisited
                if has_cycle(course):
                    return False
        
        return True
    
    # BFS approach (Kahn's Algorithm)
    def canFinishBFS(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """BFS with topological sort"""
        # Build adjacency list and in-degree array
        graph = defaultdict(list)
        in_degree = [0] * numCourses
        
        for course, prereq in prerequisites:
            graph[prereq].append(course)
            in_degree[course] += 1
        
        # Start with courses that have no prerequisites
        queue = deque([i for i in range(numCourses) if in_degree[i] == 0])
        processed = 0
        
        while queue:
            course = queue.popleft()
            processed += 1
            
            # Process all courses that depend on this one
            for neighbor in graph[course]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
        
        # If we processed all courses, no cycle exists
        return processed == numCourses
    
    # Alternative DFS with explicit visited set
    def canFinishDFSSet(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """DFS with visited and visiting sets"""
        graph = defaultdict(list)
        for course, prereq in prerequisites:
            graph[prereq].append(course)
        
        visited = set()
        visiting = set()
        
        def dfs(course: int) -> bool:
            if course in visiting:
                return False  # Cycle detected
            if course in visited:
                return True
            
            visiting.add(course)
            
            for neighbor in graph[course]:
                if not dfs(neighbor):
                    return False
            
            visiting.remove(course)
            visited.add(course)
            return True
        
        for course in range(numCourses):
            if course not in visited:
                if not dfs(course):
                    return False
        
        return True


# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1
    numCourses1 = 2
    prerequisites1 = [[1, 0]]
    print(f"Input: numCourses = {numCourses1}, prerequisites = {prerequisites1}")
    print(f"Output: {solution.canFinish(numCourses1, prerequisites1)}")
    print(f"Expected: True (Take course 0, then course 1)\n")
    
    # Test case 2
    numCourses2 = 2
    prerequisites2 = [[1, 0], [0, 1]]
    print(f"Input: numCourses = {numCourses2}, prerequisites = {prerequisites2}")
    print(f"Output: {solution.canFinish(numCourses2, prerequisites2)}")
    print(f"Expected: False (Circular dependency)\n")
    
    # Test case 3
    numCourses3 = 4
    prerequisites3 = [[1, 0], [2, 0], [3, 1], [3, 2]]
    print(f"Input: numCourses = {numCourses3}, prerequisites = {prerequisites3}")
    print(f"Output: {solution.canFinish(numCourses3, prerequisites3)}")
    print(f"Expected: True\n")
    
    # Test case 4: No prerequisites
    numCourses4 = 3
    prerequisites4 = []
    print(f"Input: numCourses = {numCourses4}, prerequisites = {prerequisites4}")
    print(f"Output: {solution.canFinish(numCourses4, prerequisites4)}")
    print(f"Expected: True\n")
    
    # Compare approaches
    numCourses5 = 5
    prerequisites5 = [[1, 4], [2, 4], [3, 1], [3, 2]]
    print(f"Input: numCourses = {numCourses5}, prerequisites = {prerequisites5}")
    print(f"DFS: {solution.canFinish(numCourses5, prerequisites5)}")
    print(f"BFS (Kahn): {solution.canFinishBFS(numCourses5, prerequisites5)}")
    print(f"DFS with Set: {solution.canFinishDFSSet(numCourses5, prerequisites5)}")
    print(f"Expected: True")