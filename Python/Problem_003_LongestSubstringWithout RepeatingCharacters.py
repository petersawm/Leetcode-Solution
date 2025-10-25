"""
Problem: 3 - Longest Substring Without Repeating Characters
Difficulty: Medium
Link: https://leetcode.com/problems/longest-substring-without-repeating-characters/

Problem Statement:
Given a string s, find the length of the longest substring without repeating characters.

Approach:
Use Sliding Window technique with a hash map:
1. Use two pointers (left and right) to maintain a window
2. Use hash map to store character and its last seen index
3. Expand window by moving right pointer
4. If we see a repeated character, move left pointer to position after last occurrence
5. Track the maximum window size seen

Time Complexity: O(N) - Each character visited at most twice
Space Complexity: O(min(N, M)) - M is charset size, N is string length
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Hash map to store character and its index
        char_index = {}
        max_length = 0
        left = 0
        
        # Expand window with right pointer
        for right in range(len(s)):
            char = s[right]
            
            # If character is repeated and in current window
            if char in char_index and char_index[char] >= left:
                # Move left pointer to position after last occurrence
                left = char_index[char] + 1
            
            # Update character's latest position
            char_index[char] = right
            
            # Update maximum length
            max_length = max(max_length, right - left + 1)
        
        return max_length
    
    # Alternative: Using set (more intuitive)
    def lengthOfLongestSubstringSet(self, s: str) -> int:
        char_set = set()
        left = 0
        max_length = 0
        
        for right in range(len(s)):
            # Shrink window until no duplicate
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1
            
            # Add current character
            char_set.add(s[right])
            
            # Update maximum length
            max_length = max(max_length, right - left + 1)
        
        return max_length
    
    # Alternative: Using array for ASCII characters (fastest)
    def lengthOfLongestSubstringArray(self, s: str) -> int:
        # Array to store last index of each ASCII character
        last_index = [-1] * 128
        max_length = 0
        left = 0
        
        for right in range(len(s)):
            char_code = ord(s[right])
            
            # If character was seen in current window
            if last_index[char_code] >= left:
                left = last_index[char_code] + 1
            
            # Update last seen index
            last_index[char_code] = right
            
            # Update maximum length
            max_length = max(max_length, right - left + 1)
        
        return max_length


# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1
    s1 = "abcabcbb"
    print(f'Input: s = "{s1}"')
    print(f"Output: {solution.lengthOfLongestSubstring(s1)}")
    print(f'Expected: 3 (substring "abc")\n')
    
    # Test case 2
    s2 = "bbbbb"
    print(f'Input: s = "{s2}"')
    print(f"Output: {solution.lengthOfLongestSubstring(s2)}")
    print(f'Expected: 1 (substring "b")\n')
    
    # Test case 3
    s3 = "pwwkew"
    print(f'Input: s = "{s3}"')
    print(f"Output: {solution.lengthOfLongestSubstring(s3)}")
    print(f'Expected: 3 (substring "wke")\n')
    
    # Test case 4
    s4 = ""
    print(f'Input: s = "{s4}"')
    print(f"Output: {solution.lengthOfLongestSubstring(s4)}")
    print(f'Expected: 0\n')
    
    # Test case 5
    s5 = "abcdefghijklmnopqrstuvwxyz"
    print(f'Input: s = "{s5}"')
    print(f"Output: {solution.lengthOfLongestSubstring(s5)}")
    print(f'Expected: 26\n')
    
    # Test case 6
    s6 = "dvdf"
    print(f'Input: s = "{s6}"')
    print(f"Output (HashMap): {solution.lengthOfLongestSubstring(s6)}")
    print(f"Output (Set): {solution.lengthOfLongestSubstringSet(s6)}")
    print(f"Output (Array): {solution.lengthOfLongestSubstringArray(s6)}")
    print(f'Expected: 3 (substring "vdf")')
