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
#include <iostream>
#include <stack>
#include <string>
using namespace std;

class Solution {
public:
    bool isValid(string s) {
        // Stack to store opening brackets
        stack<char> st;
        
        // Iterate through each character
        for (char c : s) {
            // If opening bracket, push to stack
            if (c == '(' || c == '{' || c == '[') {
                st.push(c);
            }
            // If closing bracket
            else {
                // Stack must not be empty
                if (st.empty()) {
                    return false;
                }
                
                // Check if closing bracket matches opening bracket
                char top = st.top();
                st.pop();
                if ((c == ')' && top != '(') ||
                    (c == '}' && top != '{') ||
                    (c == ']' && top != '[')) {
                    return false;
                }
            }
        }
        
        // Stack must be empty at the end
        return st.empty();
    }
};

// Test cases
int main() {
    Solution sol;
    
    // Test 1
    cout << "Output: " << (sol.isValid("()") ? "true" : "false") << endl;
    // Expected: true
    
    // Test 2
    cout << "Output: " << (sol.isValid("()[]{}") ? "true" : "false") << endl;
    // Expected: true
    
    // Test 3
    cout << "Output: " << (sol.isValid("(]") ? "true" : "false") << endl;
    // Expected: false
    
    // Test 4
    cout << "Output: " << (sol.isValid("([)]") ? "true" : "false") << endl;
    // Expected: false
    
    // Test 5
    cout << "Output: " << (sol.isValid("{[]}") ? "true" : "false") << endl;
    // Expected: true
    
    return 0;
}