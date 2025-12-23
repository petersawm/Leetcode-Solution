"""
Problem: 44 - Wildcard Matching
Difficulty: Hard
Link: https://leetcode.com/problems/wildcard-matching/
Problem Statement:
Given an input string s and a pattern p, implement wildcard pattern matching 
with support for '?' and '*' where:
- '?' Matches any single character
- '*' Matches any sequence of characters (including empty sequence)
The matching should cover the entire input string (not partial).
Approach 1: Two Pointers with Greedy (Optimal)
Track positions in s and p, also track star position for backtracking
Time Complexity: O(M * N) worst case, but usually better
Space Complexity: O(1)

Approach 2: Dynamic Programming
dp[i][j] = true if s[0..i-1] matches p[0..j-1]
Time Complexity: O(M * N)
Space Complexity: O(M * N)
"""

class Solution:
    # Approach 1: Two Pointers with Greedy
    def isMatch(self, s: str, p: str) -> bool:
        s_len = len(s)
        p_len = len(p)
        s_idx = 0
        p_idx = 0
        star_idx = -1
        match_idx = 0
        
        while s_idx < s_len:
            # Characters match or pattern has '?'
            if p_idx < p_len and (p[p_idx] == '?' or s[s_idx] == p[p_idx]):
                s_idx += 1
                p_idx += 1
            # Pattern has '*'
            elif p_idx < p_len and p[p_idx] == '*':
                star_idx = p_idx
                match_idx = s_idx
                p_idx += 1
            # No match, backtrack if we have seen '*'
            elif star_idx != -1:
                p_idx = star_idx + 1
                match_idx += 1
                s_idx = match_idx
            # No match and no '*' to backtrack
            else:
                return False
        
        # Check for remaining characters in pattern (should be only '*')
        while p_idx < p_len and p[p_idx] == '*':
            p_idx += 1
        
        return p_idx == p_len


# Approach 2: Dynamic Programming
class SolutionDP:
    def isMatch(self, s: str, p: str) -> bool:
        m = len(s)
        n = len(p)
        
        # dp[i][j] = true if s[0..i-1] matches p[0..j-1]
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        
        # Base case: empty string matches empty pattern
        dp[0][0] = True
        
        # Handle patterns like *, **, *?, etc. that match empty string
        for j in range(1, n + 1):
            if p[j - 1] == '*':
                dp[0][j] = dp[0][j - 1]
        
        # Fill DP table
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if p[j - 1] == '*':
                    # '*' can match empty or one/more characters
                    dp[i][j] = dp[i][j - 1] or dp[i - 1][j]
                elif p[j - 1] == '?' or s[i - 1] == p[j - 1]:
                    # '?' or character match
                    dp[i][j] = dp[i - 1][j - 1]
        
        return dp[m][n]


# Test cases
if __name__ == "__main__":
    sol = Solution()
    sol_dp = SolutionDP()
    
    test_cases = [
        ("aa", "a", False),
        ("aa", "*", True),
        ("cb", "?a", False),
        ("adceb", "*a*b", True),
        ("acdcb", "a*c?b", False),
        ("mississippi", "m*iss*p*.", False),
        ("ab", "?*", True),
        ("", "", True),
        ("", "*", True),
        ("a", "a", True),
    ]
    
    print("=== Two Pointers Approach ===")
    for s, p, expected in test_cases:
        result = sol.isMatch(s, p)
        status = "✓" if result == expected else "✗"
        print(f"{status} isMatch('{s}', '{p}') = {result} (expected {expected})")
    
    print("\n=== DP Approach ===")
    for s, p, expected in test_cases:
        result = sol_dp.isMatch(s, p)
        status = "✓" if result == expected else "✗"
        print(f"{status} isMatch('{s}', '{p}') = {result} (expected {expected})")