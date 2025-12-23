"""
Problem: 10 - Regular Expression Matching
Difficulty: Hard
Link: https://leetcode.com/problems/regular-expression-matching/
Problem Statement:
Given an input string s and a pattern p, implement regular expression matching 
with support for '.' and '*' where:
- '.' Matches any single character
- '*' Matches zero or more of the preceding element
The matching should cover the entire input string (not partial).
Approach:
Use Dynamic Programming with 2D DP table
dp[i][j] = true if s[0..i-1] matches p[0..j-1]
Handle three cases: character match, '.', '*'
Time Complexity: O(M * N) where M = s.length, N = p.length
Space Complexity: O(M * N)
"""

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m = len(s)
        n = len(p)
        
        # dp[i][j] = true if s[0..i-1] matches p[0..j-1]
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        
        # Base case: empty string matches empty pattern
        dp[0][0] = True
        
        # Handle patterns like a*, a*b*, a*b*c* that match empty string
        for j in range(2, n + 1):
            if p[j - 1] == '*':
                dp[0][j] = dp[0][j - 2]
        
        # Fill DP table
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if p[j - 1] == '*':
                    # '*' matches zero or more of preceding element
                    # Zero case: match without using *
                    dp[i][j] = dp[i][j - 2]
                    
                    # More case: use * to match current character
                    if p[j - 2] == '.' or p[j - 2] == s[i - 1]:
                        dp[i][j] = dp[i][j] or dp[i - 1][j]
                elif p[j - 1] == '.' or p[j - 1] == s[i - 1]:
                    # '.' or character match
                    dp[i][j] = dp[i - 1][j - 1]
        
        return dp[m][n]


# Alternative approach: Memoization (Top-down)
class SolutionMemo:
    def isMatch(self, s: str, p: str) -> bool:
        memo = {}
        
        def dp(i, j):
            # i: position in s, j: position in p
            if (i, j) in memo:
                return memo[(i, j)]
            
            # Base cases
            if j == len(p):
                return i == len(s)
            
            # Check if current characters match
            match = i < len(s) and (s[i] == p[j] or p[j] == '.')
            
            # Handle '*'
            if j + 1 < len(p) and p[j + 1] == '*':
                # Two options: skip pattern or match one character
                result = dp(i, j + 2) or (match and dp(i + 1, j))
            else:
                # No '*', must match current character
                result = match and dp(i + 1, j + 1)
            
            memo[(i, j)] = result
            return result
        
        return dp(0, 0)


# Test cases
if __name__ == "__main__":
    sol = Solution()
    sol_memo = SolutionMemo()
    
    test_cases = [
        ("aa", "a", False),
        ("aa", "a*", True),
        ("ab", ".*", True),
        ("aab", "c*a*b", True),
        ("mississippi", "mis*is*p*.", False),
        ("abc", "a.c", True),
        ("", "", True),
        ("a", ".*", True),
    ]
    
    print("=== DP Approach ===")
    for s, p, expected in test_cases:
        result = sol.isMatch(s, p)
        status = "✓" if result == expected else "✗"
        print(f"{status} isMatch('{s}', '{p}') = {result} (expected {expected})")
    
    print("\n=== Memoization Approach ===")
    for s, p, expected in test_cases:
        result = sol_memo.isMatch(s, p)
        status = "✓" if result == expected else "✗"
        print(f"{status} isMatch('{s}', '{p}') = {result} (expected {expected})")