"""
Problem: 5 - Longest Palindromic Substring
Difficulty: Medium
Link: https://leetcode.com/problems/longest-palindromic-substring/

Problem Statement:
Given a string s, return the longest palindromic substring in s.

A palindromic string is a string that reads the same forward and backward.

Approach:
Multiple approaches:

1. Expand Around Center - Most intuitive
   - For each position, expand outward while characters match
   - Check both odd and even length palindromes
   - Time: O(N²), Space: O(1)

2. Dynamic Programming
   - dp[i][j] = true if s[i:j+1] is palindrome
   - Time: O(N²), Space: O(N²)

3. Manacher's Algorithm - Optimal but complex
   - Linear time algorithm
   - Time: O(N), Space: O(N)

Time Complexity: O(N²) - Expand around center approach
Space Complexity: O(1) - Only storing indices
"""

class Solution:
    def longestPalindrome(self, s: str) -> str:
        """Expand around center - Most intuitive"""
        if not s:
            return ""
        
        start = 0
        max_len = 0
        
        def expand_around_center(left: int, right: int) -> int:
            """Expand while characters match and return length"""
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return right - left - 1
        
        for i in range(len(s)):
            # Check odd length palindromes (center is single character)
            len1 = expand_around_center(i, i)
            
            # Check even length palindromes (center is between two characters)
            len2 = expand_around_center(i, i + 1)
            
            # Get maximum length
            curr_len = max(len1, len2)
            
            # Update start and max_len if we found longer palindrome
            if curr_len > max_len:
                max_len = curr_len
                start = i - (curr_len - 1) // 2
        
        return s[start:start + max_len]
    
    # Dynamic Programming approach
    def longestPalindromeDP(self, s: str) -> str:
        """Dynamic Programming approach"""
        n = len(s)
        if n < 2:
            return s
        
        # dp[i][j] = True if s[i:j+1] is palindrome
        dp = [[False] * n for _ in range(n)]
        
        start = 0
        max_len = 1
        
        # Every single character is a palindrome
        for i in range(n):
            dp[i][i] = True
        
        # Check for two character palindromes
        for i in range(n - 1):
            if s[i] == s[i + 1]:
                dp[i][i + 1] = True
                start = i
                max_len = 2
        
        # Check for lengths greater than 2
        for length in range(3, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                
                # Check if s[i:j+1] is palindrome
                if s[i] == s[j] and dp[i + 1][j - 1]:
                    dp[i][j] = True
                    start = i
                    max_len = length
        
        return s[start:start + max_len]
    
    # Optimized DP with less space
    def longestPalindromeOptimized(self, s: str) -> str:
        """Space-optimized approach"""
        n = len(s)
        if n < 2:
            return s
        
        start = 0
        max_len = 1
        
        # Check all substrings
        for i in range(n):
            # Odd length
            left = right = i
            while left >= 0 and right < n and s[left] == s[right]:
                if right - left + 1 > max_len:
                    start = left
                    max_len = right - left + 1
                left -= 1
                right += 1
            
            # Even length
            left, right = i, i + 1
            while left >= 0 and right < n and s[left] == s[right]:
                if right - left + 1 > max_len:
                    start = left
                    max_len = right - left + 1
                left -= 1
                right += 1
        
        return s[start:start + max_len]
    
    # Brute force (for comparison - not recommended)
    def longestPalindromeBrute(self, s: str) -> str:
        """Brute force - check all substrings"""
        def is_palindrome(sub: str) -> bool:
            return sub == sub[::-1]
        
        n = len(s)
        longest = ""
        
        for i in range(n):
            for j in range(i, n):
                substring = s[i:j+1]
                if is_palindrome(substring) and len(substring) > len(longest):
                    longest = substring
        
        return longest


# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1
    s1 = "babad"
    print(f'Input: s = "{s1}"')
    print(f'Output: "{solution.longestPalindrome(s1)}"')
    print(f'Expected: "bab" or "aba"\n')
    
    # Test case 2
    s2 = "cbbd"
    print(f'Input: s = "{s2}"')
    print(f'Output: "{solution.longestPalindrome(s2)}"')
    print(f'Expected: "bb"\n')
    
    # Test case 3
    s3 = "a"
    print(f'Input: s = "{s3}"')
    print(f'Output: "{solution.longestPalindrome(s3)}"')
    print(f'Expected: "a"\n')
    
    # Test case 4
    s4 = "ac"
    print(f'Input: s = "{s4}"')
    print(f'Output: "{solution.longestPalindrome(s4)}"')
    print(f'Expected: "a" or "c"\n')
    
    # Test case 5
    s5 = "racecar"
    print(f'Input: s = "{s5}"')
    print(f'Output (Expand): "{solution.longestPalindrome(s5)}"')
    print(f'Output (DP): "{solution.longestPalindromeDP(s5)}"')
    print(f'Output (Optimized): "{solution.longestPalindromeOptimized(s5)}"')
    print(f'Expected: "racecar"\n')
    
    # Test case 6: Long palindrome
    s6 = "bananas"
    print(f'Input: s = "{s6}"')
    print(f'Output: "{solution.longestPalindrome(s6)}"')
    print(f'Expected: "anana"')