/*
Problem: 20 - Valid Parentheses
Difficulty: Easy
Link: https://leetcode.com/problems/valid-parentheses/
Problem Statement:
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
determine if the input string is valid. An input string is valid if:
1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.
Approach:
Use Stack to match opening and closing brackets.
Push opening brackets onto stack.
For closing bracket, check if it matches top of stack.
Time Complexity: O(N)
Space Complexity: O(N)
*/
import java.util.*;

class Solution {
    public boolean isValid(String s) {
        // Stack to store opening brackets
        Stack<Character> stack = new Stack<>();
        
        // Iterate through each character
        for (char c : s.toCharArray()) {
            // If opening bracket, push to stack
            if (c == '(' || c == '{' || c == '[') {
                stack.push(c);
            } 
            // If closing bracket
            else {
                // Stack must not be empty
                if (stack.isEmpty()) {
                    return false;
                }
                
                // Check if closing bracket matches opening bracket
                char top = stack.pop();
                if ((c == ')' && top != '(') ||
                    (c == '}' && top != '{') ||
                    (c == ']' && top != '[')) {
                    return false;
                }
            }
        }
        
        // Stack must be empty at the end
        return stack.isEmpty();
    }
    
    // Test cases
    public static void main(String[] args) {
        Solution sol = new Solution();
        
        // Test 1
        System.out.println("Output: " + sol.isValid("()"));
        // Expected: true
        
        // Test 2
        System.out.println("Output: " + sol.isValid("()[]{}"));
        // Expected: true
        
        // Test 3
        System.out.println("Output: " + sol.isValid("(]"));
        // Expected: false
        
        // Test 4
        System.out.println("Output: " + sol.isValid("([)]"));
        // Expected: false
        
        // Test 5
        System.out.println("Output: " + sol.isValid("{[]}"));
        // Expected: true
    }
}