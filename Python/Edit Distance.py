"""
Problem: 72 - Edit Distance
Difficulty: Hard
Link: https://leetcode.com/problems/edit-distance/
Problem Statement:
Given two strings word1 and word2, return the minimum number of operations 
required to convert word1 to word2.
You have the following three operations permitted on a word:
- Insert a character
- Delete a character
- Replace a character
Approach:
Use Dynamic Programming (Levenshtein Distance)
dp[i][j] = minimum operations to convert word1[0..i-1] to word2[0..j-1]
Three cases: insert, delete, replace
Time Complexity: O(M * N)
Space Complexity: O(M * N)
"""

class Solution:
    # Approach 1: 2D DP
    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1)
        n = len(word2)
        
        # dp[i][j] = min operations to convert word1[0..i-1] to word2[0..j-1]
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        # Base cases
        for i in range(m + 1):
            dp[i][0] = i  # Delete i characters
        for j in range(n + 1):
            dp[0][j] = j  # Insert j characters
        
        # Fill DP table
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    # Characters match, no operation needed
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    # Three operations: insert, delete, replace
                    insert = dp[i][j - 1] + 1      # Insert char from word2
                    delete = dp[i - 1][j] + 1      # Delete char from word1
                    replace = dp[i - 1][j - 1] + 1 # Replace char
                    
                    dp[i][j] = min(insert, delete, replace)
        
        return dp[m][n]
    
    # Approach 2: Space optimized using 1D array
    def minDistance_Optimized(self, word1: str, word2: str) -> int:
        m = len(word1)
        n = len(word2)
        
        # Use two 1D arrays instead of 2D
        prev = list(range(n + 1))
        curr = [0] * (n + 1)
        
        # Fill DP
        for i in range(1, m + 1):
            curr[0] = i
            
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    curr[j] = prev[j - 1]
                else:
                    insert = curr[j - 1] + 1
                    delete = prev[j] + 1
                    replace = prev[j - 1] + 1
                    
                    curr[j] = min(insert, delete, replace)
            
            # Swap arrays
            prev, curr = curr, prev
        
        return prev[n]
    
    # Approach 3: Memoization (Top-down)
    def minDistance_Memo(self, word1: str, word2: str) -> int:
        memo = {}
        
        def dp(i, j):
            # i: position in word1, j: position in word2
            if (i, j) in memo:
                return memo[(i, j)]
            
            # Base cases
            if i == 0:
                return j
            if j == 0:
                return i
            
            if word1[i - 1] == word2[j - 1]:
                result = dp(i - 1, j - 1)
            else:
                insert = dp(i, j - 1) + 1
                delete = dp(i - 1, j) + 1
                replace = dp(i - 1, j - 1) + 1
                
                result = min(insert, delete, replace)
            
            memo[(i, j)] = result
            return result
        
        return dp(len(word1), len(word2))


# Test cases
if __name__ == "__main__":
    sol = Solution()
    
    test_cases = [
        ("horse", "ros", 3),
        ("intention", "execution", 5),
        ("", "abc", 3),
        ("abc", "", 3),
        ("a", "a", 0),
        ("ab", "cd", 2),
    ]
    
    print("=== 2D DP Approach ===")
    for word1, word2, expected in test_cases:
        result = sol.minDistance(word1, word2)
        status = "✓" if result == expected else "✗"
        print(f"{status} minDistance('{word1}', '{word2}') = {result} (expected {expected})")
    
    print("\n=== Space Optimized Approach ===")
    for word1, word2, expected in test_cases:
        result = sol.minDistance_Optimized(word1, word2)
        status = "✓" if result == expected else "✗"
        print(f"{status} minDistance('{word1}', '{word2}') = {result} (expected {expected})")
    
    print("\n=== Memoization Approach ===")
    for word1, word2, expected in test_cases:
        result = sol.minDistance_Memo(word1, word2)
        status = "✓" if result == expected else "✗"
        print(f"{status} minDistance('{word1}', '{word2}') = {result} (expected {expected})")