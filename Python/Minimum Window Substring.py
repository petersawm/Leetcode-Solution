"""
Problem: 76 - Minimum Window Substring
Difficulty: Hard
Link: https://leetcode.com/problems/minimum-window-substring/
Problem Statement:
Given two strings s and t of lengths m and n respectively, return the minimum 
window substring of s such that every character in t (including duplicates) is 
included in the window.
If there is no such window in s that covers all characters in t, return an 
empty string "".
Approach:
Use Sliding Window with dictionary
Track character counts needed and characters in current window
Expand window until all characters are found
Contract window from left to find minimum
Time Complexity: O(M + N) where M = s.length
Space Complexity: O(1) - fixed alphabet size
"""
from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        
        # Count characters needed from t
        needed = Counter(t)
        
        # Track window characters
        window = {}
        
        left = 0
        formed = 0  # Number of unique characters with required count
        required = len(needed)  # Number of unique characters needed
        
        # (length, left, right)
        result = (float("inf"), 0, 0)
        
        for right in range(len(s)):
            c = s[right]
            
            # Add character to window
            window[c] = window.get(c, 0) + 1
            
            # If character count matches needed count
            if c in needed and window[c] == needed[c]:
                formed += 1
            
            # Try to shrink window
            while left <= right and formed == required:
                left_char = s[left]
                
                # Update result if current window is smaller
                if right - left + 1 < result[0]:
                    result = (right - left + 1, left, right)
                
                # Remove character from window
                window[left_char] -= 1
                if left_char in needed and window[left_char] < needed[left_char]:
                    formed -= 1
                
                left += 1
        
        return "" if result[0] == float("inf") else s[result[1]:result[2] + 1]
    
    # Alternative approach with early termination
    def minWindow_v2(self, s: str, t: str) -> str:
        if not s or not t:
            return ""
        
        needed = Counter(t)
        window = {}
        
        left = 0
        required = len(needed)
        formed = 0
        
        min_len = float("inf")
        min_left = 0
        
        for right in range(len(s)):
            # Add character to window
            char = s[right]
            window[char] = window.get(char, 0) + 1
            
            # Check if frequency of character matches needed
            if char in needed and window[char] == needed[char]:
                formed += 1
            
            # Try to contract window until it's no longer valid
            while formed == required and left <= right:
                # Save the smallest window
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    min_left = left
                
                # Remove from the left
                char = s[left]
                window[char] -= 1
                if char in needed and window[char] < needed[char]:
                    formed -= 1
                
                left += 1
        
        return "" if min_len == float("inf") else s[min_left:min_left + min_len]


# Test cases
if __name__ == "__main__":
    sol = Solution()
    sol_v2 = Solution()
    
    test_cases = [
        ("ADOBECODEBANC", "ABC", "BANC"),
        ("a", "a", "a"),
        ("a", "aa", ""),
        ("ab", "b", "b"),
        ("aaaaaaaaaaaabbbbbcdd", "abcdd", "aabbbbbcdd"),
    ]
    
    print("=== Approach 1 ===")
    for s, t, expected in test_cases:
        result = sol.minWindow(s, t)
        status = "✓" if result == expected else "✗"
        print(f"{status} minWindow('{s}', '{t}') = '{result}' (expected '{expected}')")
    
    print("\n=== Approach 2 (Alternative) ===")
    for s, t, expected in test_cases:
        result = sol_v2.minWindow_v2(s, t)
        status = "✓" if result == expected else "✗"
        print(f"{status} minWindow('{s}', '{t}') = '{result}' (expected '{expected}')")