"""
Problem: 20 - Valid Parentheses
Difficulty: Easy
Link: https://leetcode.com/problems/valid-parentheses/

Problem Statement:
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', 
determine if the input string is valid.

Valid conditions:
1. Open brackets must be closed by the same type of brackets
2. Open brackets must be closed in the correct order
3. Every close bracket has a corresponding open bracket of the same type

Approach:
Use a stack data structure:
- Push opening brackets onto stack
- For closing brackets, check if stack top matches
- At the end, stack should be empty

Time Complexity: O(N) - Process each character once
Space Complexity: O(N) - Stack can hold up to N/2 characters
"""

class Solution:
    def isValid(self, s: str) -> bool:
        # Stack to store opening brackets
        stack = []
        
        # Mapping of closing to opening brackets
        pairs = {
            ')': '(',
            ']': '[',
            '}': '{'
        }
        
        for char in s:
            # If closing bracket
            if char in pairs:
                # Check if stack is empty or top doesn't match
                if not stack or stack[-1] != pairs[char]:
                    return False
                stack.pop()
            else:
                # Opening bracket - push to stack
                stack.append(char)
        
        # Valid if stack is empty
        return len(stack) == 0

# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    test_cases = [
        ("()", True),
        ("()[]{}", True),
        ("(]", False),
        ("([)]", False),
        ("{[]}", True),
        ("", True),
        ("((", False),
        ("))", False)
    ]
    
    for s, expected in test_cases:
        result = solution.isValid(s)
        status = "✓" if result == expected else "✗"
        print(f"{status} Input: '{s}' | Output: {result} | Expected: {expected}")