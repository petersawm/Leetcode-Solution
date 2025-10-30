/*
Problem: 207 - Course Schedule
Difficulty: Medium
Link: https://leetcode.com/problems/course-schedule/

Problem Statement:
Given numCourses and prerequisites, return true if you can finish all courses.

Approach:
Cycle detection in directed graph using DFS or BFS (Topological Sort)

Time Complexity: O(V + E) where V = courses, E = prerequisites
Space Complexity: O(V + E) for adjacency list
*/

import java.util.*;

class Solution {
    // Approach 1: DFS with cycle detection
    public boolean canFinish(int numCourses, int[][] prerequisites) {
        // Build adjacency list
        List<List<Integer>> graph = new ArrayList<>();
        for (int i = 0; i < numCourses; i++) {
            graph.add(new ArrayList<>());
        }
        
        for (int[] prereq : prerequisites) {
            graph.get(prereq[1]).add(prereq[0]);
        }
        
        // States: 0 = unvisited, 1 = visiting, 2 = visited
        int[] state = new int[numCourses];
        
        // Check each course
        for (int course = 0; course < numCourses; course++) {
            if (state[course] == 0) {
                if (hasCycle(course, graph, state)) {
                    return false;
                }
            }
        }
        
        return true;
    }
    
    private boolean hasCycle(int course, List<List<Integer>> graph, int[] state) {
        if (state[course] == 1) {  // Currently visiting - cycle!
            return true;
        }
        if (state[course] == 2) {  // Already visited
            return false;
        }
        
        // Mark as visiting
        state[course] = 1;
        
        // Visit all neighbors
        for (int neighbor : graph.get(course)) {
            if (hasCycle(neighbor, graph, state)) {
                return true;
            }
        }
        
        // Mark as visited
        state[course] = 2;
        return false;
    }
    
    // Approach 2: BFS (Kahn's Algorithm)
    public boolean canFinishBFS(int numCourses, int[][] prerequisites) {
        // Build adjacency list and in-degree array
        List<List<Integer>> graph = new ArrayList<>();
        int[] inDegree = new int[numCourses];
        
        for (int i = 0; i < numCourses; i++) {
            graph.add(new ArrayList<>());
        }
        
        for (int[] prereq : prerequisites) {
            graph.get(prereq[1]).add(prereq[0]);
            inDegree[prereq[0]]++;
        }
        
        // Start with courses that have no prerequisites
        Queue<Integer> queue = new LinkedList<>();
        for (int i = 0; i < numCourses; i++) {
            if (inDegree[i] == 0) {
                queue.offer(i);
            }
        }
        
        int processed = 0;
        
        while (!queue.isEmpty()) {
            int course = queue.poll();
            processed++;
            
            // Process all courses that depend on this one
            for (int neighbor : graph.get(course)) {
                inDegree[neighbor]--;
                if (inDegree[neighbor] == 0) {
                    queue.offer(neighbor);
                }
            }
        }
        
        // If we processed all courses, no cycle exists
        return processed == numCourses;
    }
    
    // Approach 3: DFS with visited and visiting sets
    public boolean canFinishDFSSet(int numCourses, int[][] prerequisites) {
        List<List<Integer>> graph = new ArrayList<>();
        for (int i = 0; i < numCourses; i++) {
            graph.add(new ArrayList<>());
        }
        
        for (int[] prereq : prerequisites) {
            graph.get(prereq[1]).add(prereq[0]);
        }
        
        Set<Integer> visited = new HashSet<>();
        Set<Integer> visiting = new HashSet<>();
        
        for (int course = 0; course < numCourses; course++) {
            if (!visited.contains(course)) {
                if (!dfs(course, graph, visited, visiting)) {
                    return false;
                }
            }
        }
        
        return true;
    }
    
    private boolean dfs(int course, List<List<Integer>> graph, 
                       Set<Integer> visited, Set<Integer> visiting) {
        if (visiting.contains(course)) {
            return false;  // Cycle detected
        }
        if (visited.contains(course)) {
            return true;
        }
        
        visiting.add(course);
        
        for (int neighbor : graph.get(course)) {
            if (!dfs(neighbor, graph, visited, visiting)) {
                return false;
            }
        }
        
        visiting.remove(course);
        visited.add(course);
        return true;
    }
    
    // Helper method to print prerequisites
    private static void printPrerequisites(int[][] prerequisites) {
        System.out.print("[");
        for (int i = 0; i < prerequisites.length; i++) {
            System.out.print("[" + prerequisites[i][0] + "," + prerequisites[i][1] + "]");
            if (i < prerequisites.length - 1) {
                System.out.print(",");
            }
        }
        System.out.print("]");
    }
    
    // Test cases
    public static void main(String[] args) {
        Solution solution = new Solution();
        
        // Test case 1
        int numCourses1 = 2;
        int[][] prerequisites1 = {{1, 0}};
        System.out.print("Input: numCourses = " + numCourses1 + ", prerequisites = ");
        printPrerequisites(prerequisites1);
        System.out.println("\nOutput: " + solution.canFinish(numCourses1, prerequisites1));
        System.out.println("Expected: true\n");
        
        // Test case 2
        int numCourses2 = 2;
        int[][] prerequisites2 = {{1, 0}, {0, 1}};
        System.out.print("Input: numCourses = " + numCourses2 + ", prerequisites = ");
        printPrerequisites(prerequisites2);
        System.out.println("\nOutput: " + solution.canFinish(numCourses2, prerequisites2));
        System.out.println("Expected: false\n");
        
        // Test case 3
        int numCourses3 = 4;
        int[][] prerequisites3 = {{1, 0}, {2, 0}, {3, 1}, {3, 2}};
        System.out.print("Input: numCourses = " + numCourses3 + ", prerequisites = ");
        printPrerequisites(prerequisites3);
        System.out.println("\nOutput: " + solution.canFinish(numCourses3, prerequisites3));
        System.out.println("Expected: true\n");
        
        // Compare approaches
        int numCourses4 = 5;
        int[][] prerequisites4 = {{1, 4}, {2, 4}, {3, 1}, {3, 2}};
        System.out.print("Input: numCourses = " + numCourses4 + ", prerequisites = ");
        printPrerequisites(prerequisites4);
        System.out.println("\nDFS: " + solution.canFinish(numCourses4, prerequisites4));
        System.out.println("BFS (Kahn): " + solution.canFinishBFS(numCourses4, prerequisites4));
        System.out.println("DFS with Set: " + solution.canFinishDFSSet(numCourses4, prerequisites4));
        System.out.println("Expected: true");
    }
}