"""
Problem: 133 - Clone Graph
Difficulty: Medium
Link: https://leetcode.com/problems/clone-graph/

Problem Statement:
Given a reference of a node in a connected undirected graph, return a deep copy (clone) 
of the graph. Each node in the graph contains a value (int) and a list (List[Node]) of 
its neighbors.

The graph is represented using an adjacency list. For example, [[2,4],[1,3],[2,4],[1,3]]
represents a graph with 4 nodes.

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
"""

from typing import Optional
from collections import deque

# Definition for a Node
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        """DFS approach with hash map"""
        if not node:
            return None
        
        # Hash map to store original → clone mapping
        cloned = {}
        
        def dfs(node: 'Node') -> 'Node':
            # If already cloned, return the clone
            if node in cloned:
                return cloned[node]
            
            # Create clone of current node
            clone = Node(node.val)
            cloned[node] = clone
            
            # Clone all neighbors recursively
            for neighbor in node.neighbors:
                clone.neighbors.append(dfs(neighbor))
            
            return clone
        
        return dfs(node)
    
    # BFS approach
    def cloneGraphBFS(self, node: Optional['Node']) -> Optional['Node']:
        """BFS approach with queue"""
        if not node:
            return None
        
        # Hash map to store original → clone mapping
        cloned = {node: Node(node.val)}
        
        # Queue for BFS
        queue = deque([node])
        
        while queue:
            curr = queue.popleft()
            
            # Process all neighbors
            for neighbor in curr.neighbors:
                if neighbor not in cloned:
                    # Clone the neighbor
                    cloned[neighbor] = Node(neighbor.val)
                    queue.append(neighbor)
                
                # Add cloned neighbor to current clone's neighbors
                cloned[curr].neighbors.append(cloned[neighbor])
        
        return cloned[node]
    
    # Iterative DFS with stack
    def cloneGraphIterativeDFS(self, node: Optional['Node']) -> Optional['Node']:
        """Iterative DFS with stack"""
        if not node:
            return None
        
        cloned = {node: Node(node.val)}
        stack = [node]
        
        while stack:
            curr = stack.pop()
            
            for neighbor in curr.neighbors:
                if neighbor not in cloned:
                    cloned[neighbor] = Node(neighbor.val)
                    stack.append(neighbor)
                
                cloned[curr].neighbors.append(cloned[neighbor])
        
        return cloned[node]


# Helper functions for testing
def build_graph(adj_list):
    """Build graph from adjacency list"""
    if not adj_list:
        return None
    
    nodes = [Node(i + 1) for i in range(len(adj_list))]
    
    for i, neighbors in enumerate(adj_list):
        for neighbor_val in neighbors:
            nodes[i].neighbors.append(nodes[neighbor_val - 1])
    
    return nodes[0] if nodes else None

def graph_to_adj_list(node):
    """Convert graph to adjacency list"""
    if not node:
        return []
    
    visited = {}
    adj_list = []
    
    def dfs(n):
        if n.val in visited:
            return
        
        visited[n.val] = len(adj_list)
        adj_list.append([])
        
        for neighbor in n.neighbors:
            dfs(neighbor)
            adj_list[visited[n.val]].append(neighbor.val)
    
    dfs(node)
    return adj_list

def verify_clone(original, clone):
    """Verify that clone is deep copy"""
    if not original and not clone:
        return True
    if not original or not clone:
        return False
    
    visited_orig = set()
    visited_clone = set()
    
    def dfs(orig, clo):
        if id(orig) == id(clo):  # Should be different objects
            return False
        
        if orig.val != clo.val:
            return False
        
        if id(orig) in visited_orig:
            return True
        
        visited_orig.add(id(orig))
        visited_clone.add(id(clo))
        
        if len(orig.neighbors) != len(clo.neighbors):
            return False
        
        for i in range(len(orig.neighbors)):
            if not dfs(orig.neighbors[i], clo.neighbors[i]):
                return False
        
        return True
    
    return dfs(original, clone)


# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1: [[2,4],[1,3],[2,4],[1,3]]
    adj_list1 = [[2,4],[1,3],[2,4],[1,3]]
    graph1 = build_graph(adj_list1)
    print(f"Input: adjList = {adj_list1}")
    clone1 = solution.cloneGraph(graph1)
    print(f"Output: {graph_to_adj_list(clone1)}")
    print(f"Is deep copy: {verify_clone(graph1, clone1)}")
    print(f"Expected: [[2,4],[1,3],[2,4],[1,3]]\n")
    
    # Test case 2: [[]]
    adj_list2 = [[]]
    graph2 = build_graph(adj_list2)
    print(f"Input: adjList = {adj_list2}")
    clone2 = solution.cloneGraph(graph2)
    print(f"Output: {graph_to_adj_list(clone2)}")
    print(f"Expected: [[]]\n")
    
    # Test case 3: []
    adj_list3 = []
    graph3 = build_graph(adj_list3)
    print(f"Input: adjList = {adj_list3}")
    clone3 = solution.cloneGraph(graph3)
    print(f"Output: {graph_to_adj_list(clone3)}")
    print(f"Expected: []\n")
    
    # Compare approaches
    adj_list4 = [[2],[1]]
    graph4 = build_graph(adj_list4)
    print(f"Input: adjList = {adj_list4}")
    
    clone4_dfs = solution.cloneGraph(build_graph(adj_list4))
    print(f"DFS: {graph_to_adj_list(clone4_dfs)}")
    
    clone4_bfs = solution.cloneGraphBFS(build_graph(adj_list4))
    print(f"BFS: {graph_to_adj_list(clone4_bfs)}")
    
    clone4_iter = solution.cloneGraphIterativeDFS(build_graph(adj_list4))
    print(f"Iterative DFS: {graph_to_adj_list(clone4_iter)}")
    
    print(f"Expected: [[2],[1]]")