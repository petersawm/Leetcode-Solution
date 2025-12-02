"""
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
"""

class Solution:
    def isValid(self, s: str) -> bool:
        # Stack to store opening brackets
        stack = []
        
        # Dictionary to map closing brackets to opening brackets
        bracket_map = {
            ')': '(',
            '}': '{',
            ']': '['
        }
        
        # Iterate through each character
        for c in s:
            # If closing bracket
            if c in bracket_map:
                # Stack must not be empty
                if not stack:
                    return False
                
                # Check if closing bracket matches opening bracket
                if stack[-1] != bracket_map[c]:
                    return False
                
                stack.pop()
            # If opening bracket, push to stack
            else:
                stack.append(c)
        
        # Stack must be empty at the end
        return len(stack) == 0


# Test cases
if __name__ == "__main__":
    sol = Solution()
    
    # Test 1
    print("Output:", sol.isValid("()"))
    # Expected: True
    
    # Test 2
    print("Output:", sol.isValid("()[]{}"))
    # Expected: True
    
    # Test 3
    print("Output:", sol.isValid("(]"))
    # Expected: False
    
    # Test 4
    print("Output:", sol.isValid("([)]"))
    # Expected: False
    
    # Test 5
    print("Output:", sol.isValid("{[]}"))
    # Expected: True