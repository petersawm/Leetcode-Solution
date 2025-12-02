/*
Problem: 3 - Longest Substring Without Repeating Characters
Difficulty: Medium
Link: https://leetcode.com/problems/longest-substring-without-repeating-characters/
Problem Statement:
Given a string s, find the length of the longest substring without repeating
characters.
Approach:
Use Sliding Window with HashMap to track character indices.
Expand window by moving right pointer.
When duplicate found, contract window from left.
Time Complexity: O(N)
Space Complexity: O(min(N, charset_size))
*/
import java.util.*;

class Solution {
    public int lengthOfLongestSubstring(String s) {
        // HashMap to store {character: index}
        Map<Character, Integer> charIndex = new HashMap<>();
        
        int maxLength = 0;
        int left = 0;  // Left pointer of sliding window
        
        // Right pointer of sliding window
        for (int right = 0; right < s.length(); right++) {
            char c = s.charAt(right);
            
            // If character exists in current window
            if (charIndex.containsKey(c) && charIndex.get(c) >= left) {
                // Move left pointer to right of previous occurrence
                left = charIndex.get(c) + 1;
            }
            
            // Update character index
            charIndex.put(c, right);
            
            // Update max length
            maxLength = Math.max(maxLength, right - left + 1);
        }
        
        return maxLength;
    }
    
    // Test cases
    public static void main(String[] args) {
        Solution sol = new Solution();
        
        // Test 1
        System.out.println("Output: " + sol.lengthOfLongestSubstring("abcabcbb"));
        // Expected: 3 ("abc")
        
        // Test 2
        System.out.println("Output: " + sol.lengthOfLongestSubstring("bbbbb"));
        // Expected: 1 ("b")
        
        // Test 3
        System.out.println("Output: " + sol.lengthOfLongestSubstring("pwwkew"));
        // Expected: 3 ("wke")
        
        // Test 4
        System.out.println("Output: " + sol.lengthOfLongestSubstring("au"));
        // Expected: 2 ("au")
        
        // Test 5
        System.out.println("Output: " + sol.lengthOfLongestSubstring("dvdf"));
        // Expected: 3 ("vdf")
    }
}
