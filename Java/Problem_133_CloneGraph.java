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

import java.util.*;

// Definition for a Node
class Node {
    public int val;
    public List<Node> neighbors;
    
    public Node() {
        val = 0;
        neighbors = new ArrayList<Node>();
    }
    
    public Node(int _val) {
        val = _val;
        neighbors = new ArrayList<Node>();
    }
    
    public Node(int _val, ArrayList<Node> _neighbors) {
        val = _val;
        neighbors = _neighbors;
    }
}

class Solution {
    // Approach 1: DFS with HashMap
    public Node cloneGraph(Node node) {
        if (node == null) {
            return null;
        }
        
        // Hash map to store original → clone mapping
        Map<Node, Node> cloned = new HashMap<>();
        return dfs(node, cloned);
    }
    
    private Node dfs(Node node, Map<Node, Node> cloned) {
        // If already cloned, return the clone
        if (cloned.containsKey(node)) {
            return cloned.get(node);
        }
        
        // Create clone of current node
        Node clone = new Node(node.val);
        cloned.put(node, clone);
        
        // Clone all neighbors recursively
        for (Node neighbor : node.neighbors) {
            clone.neighbors.add(dfs(neighbor, cloned));
        }
        
        return clone;
    }
    
    // Approach 2: BFS with Queue
    public Node cloneGraphBFS(Node node) {
        if (node == null) {
            return null;
        }
        
        // Hash map to store original → clone mapping
        Map<Node, Node> cloned = new HashMap<>();
        
        // Create clone of starting node
        Node clone = new Node(node.val);
        cloned.put(node, clone);
        
        // Queue for BFS
        Queue<Node> queue = new LinkedList<>();
        queue.offer(node);
        
        while (!queue.isEmpty()) {
            Node curr = queue.poll();
            
            // Process all neighbors
            for (Node neighbor : curr.neighbors) {
                if (!cloned.containsKey(neighbor)) {
                    // Clone the neighbor
                    cloned.put(neighbor, new Node(neighbor.val));
                    queue.offer(neighbor);
                }
                
                // Add cloned neighbor to current clone's neighbors
                cloned.get(curr).neighbors.add(cloned.get(neighbor));
            }
        }
        
        return clone;
    }
    
    // Approach 3: Iterative DFS with Stack
    public Node cloneGraphIterativeDFS(Node node) {
        if (node == null) {
            return null;
        }
        
        Map<Node, Node> cloned = new HashMap<>();
        Stack<Node> stack = new Stack<>();
        
        // Create clone of starting node
        cloned.put(node, new Node(node.val));
        stack.push(node);
        
        while (!stack.isEmpty()) {
            Node curr = stack.pop();
            
            for (Node neighbor : curr.neighbors) {
                if (!cloned.containsKey(neighbor)) {
                    cloned.put(neighbor, new Node(neighbor.val));
                    stack.push(neighbor);
                }
                
                cloned.get(curr).neighbors.add(cloned.get(neighbor));
            }
        }
        
        return cloned.get(node);
    }
    
    // Helper method to build graph from adjacency list
    private static Node buildGraph(int[][] adjList) {
        if (adjList == null || adjList.length == 0) {
            return null;
        }
        
        Node[] nodes = new Node[adjList.length];
        for (int i = 0; i < adjList.length; i++) {
            nodes[i] = new Node(i + 1);
        }
        
        for (int i = 0; i < adjList.length; i++) {
            for (int neighborVal : adjList[i]) {
                nodes[i].neighbors.add(nodes[neighborVal - 1]);
            }
        }
        
        return nodes[0];
    }
    
    // Helper method to convert graph to adjacency list
    private static List<List<Integer>> graphToAdjList(Node node) {
        if (node == null) {
            return new ArrayList<>();
        }
        
        Map<Integer, List<Integer>> adjMap = new HashMap<>();
        Set<Node> visited = new HashSet<>();
        
        dfsToList(node, adjMap, visited);
        
        List<List<Integer>> result = new ArrayList<>();
        for (int i = 1; i <= adjMap.size(); i++) {
            result.add(adjMap.getOrDefault(i, new ArrayList<>()));
        }
        
        return result;
    }
    
    private static void dfsToList(Node node, Map<Integer, List<Integer>> adjMap, Set<Node> visited) {
        if (visited.contains(node)) {
            return;
        }
        
        visited.add(node);
        adjMap.put(node.val, new ArrayList<>());
        
        for (Node neighbor : node.neighbors) {
            adjMap.get(node.val).add(neighbor.val);
            dfsToList(neighbor, adjMap, visited);
        }
    }
    
    // Test cases
    public static void main(String[] args) {
        Solution solution = new Solution();
        
        // Test case 1: [[2,4],[1,3],[2,4],[1,3]]
        int[][] adjList1 = {{2,4},{1,3},{2,4},{1,3}};
        Node graph1 = buildGraph(adjList1);
        System.out.println("Input: adjList = [[2,4],[1,3],[2,4],[1,3]]");
        Node clone1 = solution.cloneGraph(graph1);
        System.out.println("Output: " + graphToAdjList(clone1));
        System.out.println("Expected: [[2,4],[1,3],[2,4],[1,3]]\n");
        
        // Test case 2: [[]]
        int[][] adjList2 = {{}};
        Node graph2 = buildGraph(adjList2);
        System.out.println("Input: adjList = [[]]");
        Node clone2 = solution.cloneGraph(graph2);
        System.out.println("Output: " + graphToAdjList(clone2));
        System.out.println("Expected: [[]]\n");
        
        // Test case 3: []
        Node graph3 = null;
        System.out.println("Input: adjList = []");
        Node clone3 = solution.cloneGraph(graph3);
        System.out.println("Output: " + graphToAdjList(clone3));
        System.out.println("Expected: []\n");
        
        // Compare approaches
        int[][] adjList4 = {{2},{1}};
        System.out.println("Input: adjList = [[2],[1]]");
        
        Node clone4_dfs = solution.cloneGraph(buildGraph(adjList4));
        System.out.println("DFS: " + graphToAdjList(clone4_dfs));
        
        Node clone4_bfs = solution.cloneGraphBFS(buildGraph(adjList4));
        System.out.println("BFS: " + graphToAdjList(clone4_bfs));
        
        Node clone4_iter = solution.cloneGraphIterativeDFS(buildGraph(adjList4));
        System.out.println("Iterative DFS: " + graphToAdjList(clone4_iter));
        
        System.out.println("Expected: [[2],[1]]");
    }
}