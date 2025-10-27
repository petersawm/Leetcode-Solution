/*
Problem: 133 - Clone Graph
Difficulty: Medium
Link: https://leetcode.com/problems/clone-graph/

Problem Statement:
Given a reference of a node in a connected undirected graph, return a deep copy (clone) 
of the graph. Each node in the graph contains a value (int) and a list (List[Node]) of 
its neighbors.

Approach:
Use DFS or BFS with a hash map to track cloned nodes:

1. DFS Approach:
   - Use recursion and hash map to store original → clone mapping
   - For each node, clone it and recursively clone its neighbors
   - Time: O(N + E), Space: O(N)

2. BFS Approach:
   - Use queue and hash map
   - Clone nodes level by level
   - Time: O(N + E), Space: O(N)

Time Complexity: O(N + E) - N nodes, E edges
Space Complexity: O(N) - Hash map and recursion/queue
*/

#include <vector>
#include <unordered_map>
#include <queue>
#include <stack>
#include <iostream>
#include <unordered_set>

using namespace std;

// Definition for a Node
class Node {
public:
    int val;
    vector<Node*> neighbors;
    
    Node() {
        val = 0;
        neighbors = vector<Node*>();
    }
    
    Node(int _val) {
        val = _val;
        neighbors = vector<Node*>();
    }
    
    Node(int _val, vector<Node*> _neighbors) {
        val = _val;
        neighbors = _neighbors;
    }
};

class Solution {
public:
    // Approach 1: DFS with unordered_map
    Node* cloneGraph(Node* node) {
        if (!node) {
            return nullptr;
        }
        
        unordered_map<Node*, Node*> cloned;
        return dfs(node, cloned);
    }
    
private:
    Node* dfs(Node* node, unordered_map<Node*, Node*>& cloned) {
        // If already cloned, return the clone
        if (cloned.find(node) != cloned.end()) {
            return cloned[node];
        }
        
        // Create clone of current node
        Node* clone = new Node(node->val);
        cloned[node] = clone;
        
        // Clone all neighbors recursively
        for (Node* neighbor : node->neighbors) {
            clone->neighbors.push_back(dfs(neighbor, cloned));
        }
        
        return clone;
    }
    
public:
    // Approach 2: BFS with Queue
    Node* cloneGraphBFS(Node* node) {
        if (!node) {
            return nullptr;
        }
        
        unordered_map<Node*, Node*> cloned;
        
        // Create clone of starting node
        Node* clone = new Node(node->val);
        cloned[node] = clone;
        
        // Queue for BFS
        queue<Node*> q;
        q.push(node);
        
        while (!q.empty()) {
            Node* curr = q.front();
            q.pop();
            
            // Process all neighbors
            for (Node* neighbor : curr->neighbors) {
                if (cloned.find(neighbor) == cloned.end()) {
                    // Clone the neighbor
                    cloned[neighbor] = new Node(neighbor->val);
                    q.push(neighbor);
                }
                
                // Add cloned neighbor to current clone's neighbors
                cloned[curr]->neighbors.push_back(cloned[neighbor]);
            }
        }
        
        return clone;
    }
    
    // Approach 3: Iterative DFS with Stack
    Node* cloneGraphIterativeDFS(Node* node) {
        if (!node) {
            return nullptr;
        }
        
        unordered_map<Node*, Node*> cloned;
        stack<Node*> stk;
        
        // Create clone of starting node
        cloned[node] = new Node(node->val);
        stk.push(node);
        
        while (!stk.empty()) {
            Node* curr = stk.top();
            stk.pop();
            
            for (Node* neighbor : curr->neighbors) {
                if (cloned.find(neighbor) == cloned.end()) {
                    cloned[neighbor] = new Node(neighbor->val);
                    stk.push(neighbor);
                }
                
                cloned[curr]->neighbors.push_back(cloned[neighbor]);
            }
        }
        
        return cloned[node];
    }
};

// Helper function to build graph from adjacency list
Node* buildGraph(const vector<vector<int>>& adjList) {
    if (adjList.empty()) {
        return nullptr;
    }
    
    vector<Node*> nodes;
    for (int i = 0; i < adjList.size(); i++) {
        nodes.push_back(new Node(i + 1));
    }
    
    for (int i = 0; i < adjList.size(); i++) {
        for (int neighborVal : adjList[i]) {
            nodes[i]->neighbors.push_back(nodes[neighborVal - 1]);
        }
    }
    
    return nodes[0];
}

// Helper function to convert graph to adjacency list
vector<vector<int>> graphToAdjList(Node* node) {
    if (!node) {
        return {};
    }
    
    unordered_map<int, vector<int>> adjMap;
    unordered_set<Node*> visited;
    
    function<void(Node*)> dfs = [&](Node* n) {
        if (visited.count(n)) {
            return;
        }
        
        visited.insert(n);
        adjMap[n->val] = {};
        
        for (Node* neighbor : n->neighbors) {
            adjMap[n->val].push_back(neighbor->val);
            dfs(neighbor);
        }
    };
    
    dfs(node);
    
    vector<vector<int>> result;
    for (int i = 1; i <= adjMap.size(); i++) {
        result.push_back(adjMap[i]);
    }
    
    return result;
}

// Helper function to print adjacency list
void printAdjList(const vector<vector<int>>& adjList) {
    cout << "[";
    for (int i = 0; i < adjList.size(); i++) {
        cout << "[";
        for (int j = 0; j < adjList[i].size(); j++) {
            cout << adjList[i][j];
            if (j < adjList[i].size() - 1) cout << ",";
        }
        cout << "]";
        if (i < adjList.size() - 1) cout << ",";
    }
    cout << "]";
}

int main() {
    Solution solution;
    
    // Test case 1: [[2,4],[1,3],[2,4],[1,3]]
    vector<vector<int>> adjList1 = {{2,4},{1,3},{2,4},{1,3}};
    Node* graph1 = buildGraph(adjList1);
    cout << "Input: adjList = [[2,4],[1,3],[2,4],[1,3]]" << endl;
    Node* clone1 = solution.cloneGraph(graph1);
    cout << "Output: ";
    printAdjList(graphToAdjList(clone1));
    cout << "\nExpected: [[2,4],[1,3],[2,4],[1,3]]\n\n";
    
    // Test case 2: [[]]
    vector<vector<int>> adjList2 = {{}};
    Node* graph2 = buildGraph(adjList2);
    cout << "Input: adjList = [[]]" << endl;
    Node* clone2 = solution.cloneGraph(graph2);
    cout << "Output: ";
    printAdjList(graphToAdjList(clone2));
    cout << "\nExpected: [[]]\n\n";
    
    // Test case 3: []
    Node* graph3 = nullptr;
    cout << "Input: adjList = []" << endl;
    Node* clone3 = solution.cloneGraph(graph3);
    cout << "Output: ";
    printAdjList(graphToAdjList(clone3));
    cout << "\nExpected: []\n\n";
    
    // Compare approaches
    vector<vector<int>> adjList4 = {{2},{1}};
    cout << "Input: adjList = [[2],[1]]" << endl;
    
    Node* clone4_dfs = solution.cloneGraph(buildGraph(adjList4));
    cout << "DFS: ";
    printAdjList(graphToAdjList(clone4_dfs));
    cout << endl;
    
    Node* clone4_bfs = solution.cloneGraphBFS(buildGraph(adjList4));
    cout << "BFS: ";
    printAdjList(graphToAdjList(clone4_bfs));
    cout << endl;
    
    Node* clone4_iter = solution.cloneGraphIterativeDFS(buildGraph(adjList4));
    cout << "Iterative DFS: ";
    printAdjList(graphToAdjList(clone4_iter));
    cout << endl;
    
    cout << "Expected: [[2],[1]]" << endl;
    
    return 0;
}