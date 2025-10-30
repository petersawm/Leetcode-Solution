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

#include <vector>
#include <queue>
#include <unordered_set>
#include <iostream>

using namespace std;

class Solution {
public:
    // Approach 1: DFS with cycle detection
    bool canFinish(int numCourses, vector<vector<int>>& prerequisites) {
        // Build adjacency list
        vector<vector<int>> graph(numCourses);
        for (const auto& prereq : prerequisites) {
            graph[prereq[1]].push_back(prereq[0]);
        }
        
        // States: 0 = unvisited, 1 = visiting, 2 = visited
        vector<int> state(numCourses, 0);
        
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
    
private:
    bool hasCycle(int course, vector<vector<int>>& graph, vector<int>& state) {
        if (state[course] == 1) {  // Currently visiting - cycle!
            return true;
        }
        if (state[course] == 2) {  // Already visited
            return false;
        }
        
        // Mark as visiting
        state[course] = 1;
        
        // Visit all neighbors
        for (int neighbor : graph[course]) {
            if (hasCycle(neighbor, graph, state)) {
                return true;
            }
        }
        
        // Mark as visited
        state[course] = 2;
        return false;
    }
    
public:
    // Approach 2: BFS (Kahn's Algorithm)
    bool canFinishBFS(int numCourses, vector<vector<int>>& prerequisites) {
        // Build adjacency list and in-degree array
        vector<vector<int>> graph(numCourses);
        vector<int> inDegree(numCourses, 0);
        
        for (const auto& prereq : prerequisites) {
            graph[prereq[1]].push_back(prereq[0]);
            inDegree[prereq[0]]++;
        }
        
        // Start with courses that have no prerequisites
        queue<int> q;
        for (int i = 0; i < numCourses; i++) {
            if (inDegree[i] == 0) {
                q.push(i);
            }
        }
        
        int processed = 0;
        
        while (!q.empty()) {
            int course = q.front();
            q.pop();
            processed++;
            
            // Process all courses that depend on this one
            for (int neighbor : graph[course]) {
                inDegree[neighbor]--;
                if (inDegree[neighbor] == 0) {
                    q.push(neighbor);
                }
            }
        }
        
        // If we processed all courses, no cycle exists
        return processed == numCourses;
    }
    
    // Approach 3: DFS with visited and visiting sets
    bool canFinishDFSSet(int numCourses, vector<vector<int>>& prerequisites) {
        vector<vector<int>> graph(numCourses);
        for (const auto& prereq : prerequisites) {
            graph[prereq[1]].push_back(prereq[0]);
        }
        
        unordered_set<int> visited;
        unordered_set<int> visiting;
        
        for (int course = 0; course < numCourses; course++) {
            if (visited.find(course) == visited.end()) {
                if (!dfs(course, graph, visited, visiting)) {
                    return false;
                }
            }
        }
        
        return true;
    }
    
private:
    bool dfs(int course, vector<vector<int>>& graph, 
            unordered_set<int>& visited, unordered_set<int>& visiting) {
        if (visiting.find(course) != visiting.end()) {
            return false;  // Cycle detected
        }
        if (visited.find(course) != visited.end()) {
            return true;
        }
        
        visiting.insert(course);
        
        for (int neighbor : graph[course]) {
            if (!dfs(neighbor, graph, visited, visiting)) {
                return false;
            }
        }
        
        visiting.erase(course);
        visited.insert(course);
        return true;
    }
};

// Helper function to print prerequisites
void printPrerequisites(const vector<vector<int>>& prerequisites) {
    cout << "[";
    for (int i = 0; i < prerequisites.size(); i++) {
        cout << "[" << prerequisites[i][0] << "," << prerequisites[i][1] << "]";
        if (i < prerequisites.size() - 1) {
            cout << ",";
        }
    }
    cout << "]";
}

int main() {
    Solution solution;
    
    // Test case 1
    int numCourses1 = 2;
    vector<vector<int>> prerequisites1 = {{1, 0}};
    cout << "Input: numCourses = " << numCourses1 << ", prerequisites = ";
    printPrerequisites(prerequisites1);
    cout << "\nOutput: " << (solution.canFinish(numCourses1, prerequisites1) ? "true" : "false") << endl;
    cout << "Expected: true\n" << endl;
    
    // Test case 2
    int numCourses2 = 2;
    vector<vector<int>> prerequisites2 = {{1, 0}, {0, 1}};
    cout << "Input: numCourses = " << numCourses2 << ", prerequisites = ";
    printPrerequisites(prerequisites2);
    cout << "\nOutput: " << (solution.canFinish(numCourses2, prerequisites2) ? "true" : "false") << endl;
    cout << "Expected: false\n" << endl;
    
    // Test case 3
    int numCourses3 = 4;
    vector<vector<int>> prerequisites3 = {{1, 0}, {2, 0}, {3, 1}, {3, 2}};
    cout << "Input: numCourses = " << numCourses3 << ", prerequisites = ";
    printPrerequisites(prerequisites3);
    cout << "\nOutput: " << (solution.canFinish(numCourses3, prerequisites3) ? "true" : "false") << endl;
    cout << "Expected: true\n" << endl;
    
    // Compare approaches
    int numCourses4 = 5;
    vector<vector<int>> prerequisites4 = {{1, 4}, {2, 4}, {3, 1}, {3, 2}};
    cout << "Input: numCourses = " << numCourses4 << ", prerequisites = ";
    printPrerequisites(prerequisites4);
    cout << "\nDFS: " << (solution.canFinish(numCourses4, prerequisites4) ? "true" : "false") << endl;
    cout << "BFS (Kahn): " << (solution.canFinishBFS(numCourses4, prerequisites4) ? "true" : "false") << endl;
    cout << "DFS with Set: " << (solution.canFinishDFSSet(numCourses4, prerequisites4) ? "true" : "false") << endl;
    cout << "Expected: true" << endl;
    
    return 0;
}