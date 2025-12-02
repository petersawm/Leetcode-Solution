"""
Problem: 3 - Longest Substring Without Repeating Characters
Difficulty: Medium
Link: https://leetcode.com/problems/longest-substring-without-repeating-characters/
Problem Statement:
Given a string s, find the length of the longest substring without repeating
characters.
Approach:
Use Sliding Window with dictionary to track character indices.
Expand window by moving right pointer.
When duplicate found, contract window from left.
Time Complexity: O(N)
Space Complexity: O(min(N, charset_size))
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Dictionary to store {character: index}
        char_index = {}
        
        max_length = 0
        left = 0  # Left pointer of sliding window
        
        # Right pointer of sliding window
        for right in range(len(s)):
            c = s[right]
            
            # If character exists in current window
            if c in char_index and char_index[c] >= left:
                # Move left pointer to right of previous occurrence
                left = char_index[c] + 1
            
            # Update character index
            char_index[c] = right
            
            # Update max length
            max_length = max(max_length, right - left + 1)
        
        return max_length


# Test cases
if __name__ == "__main__":
    sol = Solution()
    
    # Test 1
    print("Output:", sol.lengthOfLongestSubstring("abcabcbb"))
    # Expected: 3 ("abc")
    
    # Test 2
    print("Output:", sol.lengthOfLongestSubstring("bbbbb"))
    # Expected: 1 ("b")
    
    # Test 3
    print("Output:", sol.lengthOfLongestSubstring("pwwkew"))
    # Expected: 3 ("wke")
    
    # Test 4
    print("Output:", sol.lengthOfLongestSubstring("au"))
    # Expected: 2 ("au")
    
    # Test 5
    print("Output:", sol.lengthOfLongestSubstring("dvdf"))
    # Expected: 3 ("vdf")