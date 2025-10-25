/*
Problem: 20 - Valid Parentheses
Difficulty: Easy
Link: https://leetcode.com/problems/valid-parentheses/

Problem Statement:
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', 
determine if the input string is valid.

An input string is valid if:
1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.
3. Every close bracket has a corresponding open bracket of the same type.

Approach:
Use a stack to track opening brackets:
1. When we encounter an opening bracket, push it onto the stack
2. When we encounter a closing bracket, check if it matches the top of stack
3. If it matches, pop from stack; if not, return false
4. At the end, stack should be empty for valid parentheses

Time Complexity: O(N) - Single pass through the string
Space Complexity: O(N) - Stack can hold at most N/2 opening brackets
*/

import java.util.Stack;
import java.util.HashMap;
import java.util.Map;

class Solution {
    public boolean isValid(String s) {
        // Empty string is valid
        if (s.isEmpty()) {
            return true;
        }
        
        // Odd length strings can't be valid
        if (s.length() % 2 != 0) {
            return false;
        }
        
        // Stack to store opening brackets
        Stack<Character> stack = new Stack<>();
        
        // Map to match closing brackets with opening brackets
        Map<Character, Character> matchingBrackets = new HashMap<>();
        matchingBrackets.put(')', '(');
        matchingBrackets.put('}', '{');
        matchingBrackets.put(']', '[');
        
        // Process each character
        for (char c : s.toCharArray()) {
            // If it's a closing bracket
            if (matchingBrackets.containsKey(c)) {
                // Check if stack is empty or top doesn't match
                if (stack.isEmpty() || stack.peek() != matchingBrackets.get(c)) {
                    return false;
                }
                // Pop the matching opening bracket
                stack.pop();
            } else {
                // It's an opening bracket, push to stack
                stack.push(c);
            }
        }
        
        // Valid only if all brackets were matched (stack is empty)
        return stack.isEmpty();
    }
    
    // Alternative approach without using HashMap
    public boolean isValidSimple(String s) {
        Stack<Character> stack = new Stack<>();
        
        for (char c : s.toCharArray()) {
            if (c == '(') {
                stack.push(')');
            } else if (c == '{') {
                stack.push('}');
            } else if (c == '[') {
                stack.push(']');
            } else if (stack.isEmpty() || stack.pop() != c) {
                return false;
            }
        }
        
        return stack.isEmpty();
    }
    
    // Test cases
    public static void main(String[] args) {
        Solution solution = new Solution();
        
        // Test case 1
        String s1 = "()";
        System.out.println("Input: \"" + s1 + "\"");
        System.out.println("Output: " + solution.isValid(s1));
        System.out.println("Expected: true\n");
        
        // Test case 2
        String s2 = "()[]{}";
        System.out.println("Input: \"" + s2 + "\"");
        System.out.println("Output: " + solution.isValid(s2));
        System.out.println("Expected: true\n");
        
        // Test case 3
        String s3 = "(]";
        System.out.println("Input: \"" + s3 + "\"");
        System.out.println("Output: " + solution.isValid(s3));
        System.out.println("Expected: false\n");
        
        // Test case 4
        String s4 = "([)]";
        System.out.println("Input: \"" + s4 + "\"");
        System.out.println("Output: " + solution.isValid(s4));
        System.out.println("Expected: false\n");
        
        // Test case 5
        String s5 = "{[]}";
        System.out.println("Input: \"" + s5 + "\"");
        System.out.println("Output: " + solution.isValid(s5));
        System.out.println("Expected: true\n");
        
        // Test case 6
        String s6 = "((";
        System.out.println("Input: \"" + s6 + "\"");
        System.out.println("Output: " + solution.isValid(s6));
        System.out.println("Expected: false\n");
    }
}