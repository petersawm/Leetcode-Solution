/*
Problem: 94 - Binary Tree Inorder Traversal
Difficulty: Easy
Link: https://leetcode.com/problems/binary-tree-inorder-traversal/

Problem Statement:
Given the root of a binary tree, return the inorder traversal of its nodes' values.

Inorder Traversal Order: Left → Root → Right

Approach:
1. Recursive: Simple and intuitive - recursively visit left, process root, visit right
2. Iterative: Use a stack to simulate recursion

Time Complexity: O(N) - Visit each node exactly once
Space Complexity: 
  - Recursive: O(H) where H is height (call stack)
  - Iterative: O(H) for stack storage
*/

import java.util.*;

// Definition for a binary tree node
class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;
    
    TreeNode() {}
    
    TreeNode(int val) {
        this.val = val;
    }
    
    TreeNode(int val, TreeNode left, TreeNode right) {
        this.val = val;
        this.left = left;
        this.right = right;
    }
}

class Solution {
    // Approach 1: Recursive
    public List<Integer> inorderTraversal(TreeNode root) {
        List<Integer> result = new ArrayList<>();
        inorderHelper(root, result);
        return result;
    }
    
    private void inorderHelper(TreeNode node, List<Integer> result) {
        if (node == null) {
            return;
        }
        
        // Visit left subtree
        inorderHelper(node.left, result);
        
        // Process current node
        result.add(node.val);
        
        // Visit right subtree
        inorderHelper(node.right, result);
    }
    
    // Approach 2: Iterative using Stack
    public List<Integer> inorderTraversalIterative(TreeNode root) {
        List<Integer> result = new ArrayList<>();
        Stack<TreeNode> stack = new Stack<>();
        TreeNode current = root;
        
        while (current != null || !stack.isEmpty()) {
            // Go to the leftmost node
            while (current != null) {
                stack.push(current);
                current = current.left;
            }
            
            // Current is null, so pop from stack
            current = stack.pop();
            result.add(current.val);
            
            // Visit right subtree
            current = current.right;
        }
        
        return result;
    }
    
    // Approach 3: Morris Traversal (O(1) space)
    public List<Integer> inorderTraversalMorris(TreeNode root) {
        List<Integer> result = new ArrayList<>();
        TreeNode current = root;
        
        while (current != null) {
            if (current.left == null) {
                // No left child, process current and go right
                result.add(current.val);
                current = current.right;
            } else {
                // Find inorder predecessor
                TreeNode predecessor = current.left;
                while (predecessor.right != null && predecessor.right != current) {
                    predecessor = predecessor.right;
                }
                
                if (predecessor.right == null) {
                    // Create thread
                    predecessor.right = current;
                    current = current.left;
                } else {
                    // Thread exists, remove it and process current
                    predecessor.right = null;
                    result.add(current.val);
                    current = current.right;
                }
            }
        }
        
        return result;
    }
    
    // Helper method to create tree from array
    public static TreeNode createTree(Integer[] values) {
        if (values == null || values.length == 0 || values[0] == null) {
            return null;
        }
        
        TreeNode root = new TreeNode(values[0]);
        Queue<TreeNode> queue = new LinkedList<>();
        queue.offer(root);
        int i = 1;
        
        while (i < values.length) {
            TreeNode current = queue.poll();
            
            // Left child
            if (i < values.length && values[i] != null) {
                current.left = new TreeNode(values[i]);
                queue.offer(current.left);
            }
            i++;
            
            // Right child
            if (i < values.length && values[i] != null) {
                current.right = new TreeNode(values[i]);
                queue.offer(current.right);
            }
            i++;
        }
        
        return root;
    }
    
    // Test cases
    public static void main(String[] args) {
        Solution solution = new Solution();
        
        // Test case 1: [1,null,2,3]
        TreeNode root1 = createTree(new Integer[]{1, null, 2, 3});
        System.out.println("Input: [1,null,2,3]");
        System.out.println("Output (Recursive): " + solution.inorderTraversal(root1));
        
        root1 = createTree(new Integer[]{1, null, 2, 3});
        System.out.println("Output (Iterative): " + solution.inorderTraversalIterative(root1));
        System.out.println("Expected: [1,3,2]\n");
        
        // Test case 2: []
        TreeNode root2 = createTree(new Integer[]{});
        System.out.println("Input: []");
        System.out.println("Output: " + solution.inorderTraversal(root2));
        System.out.println("Expected: []\n");
        
        // Test case 3: [1]
        TreeNode root3 = createTree(new Integer[]{1});
        System.out.println("Input: [1]");
        System.out.println("Output: " + solution.inorderTraversal(root3));
        System.out.println("Expected: [1]\n");
        
        // Test case 4: [1,2,3,4,5]
        TreeNode root4 = createTree(new Integer[]{1, 2, 3, 4, 5});
        System.out.println("Input: [1,2,3,4,5]");
        System.out.println("Output (Recursive): " + solution.inorderTraversal(root4));
        
        root4 = createTree(new Integer[]{1, 2, 3, 4, 5});
        System.out.println("Output (Morris): " + solution.inorderTraversalMorris(root4));
        System.out.println("Expected: [4,2,5,1,3]");
    }
}