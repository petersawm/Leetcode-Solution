/*
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
Use Sliding Window with HashMap
Track character counts needed and characters in current window
Expand window until all characters are found
Contract window from left to find minimum
Time Complexity: O(M + N) where M = s.length
Space Complexity: O(1) - fixed alphabet size
*/
import java.util.*;

class Solution {
    public String minWindow(String s, String t) {
        if (s.length() < t.length()) {
            return "";
        }
        
        // Count characters needed from t
        Map<Character, Integer> needed = new HashMap<>();
        for (char c : t.toCharArray()) {
            needed.put(c, needed.getOrDefault(c, 0) + 1);
        }
        
        // Track window characters
        Map<Character, Integer> window = new HashMap<>();
        
        int left = 0;
        int formed = 0;  // Number of unique characters with required count
        int required = needed.size();  // Number of unique characters needed
        
        // (length, left, right)
        int[] result = {Integer.MAX_VALUE, 0, 0};
        
        for (int right = 0; right < s.length(); right++) {
            char c = s.charAt(right);
            
            // Add character to window
            window.put(c, window.getOrDefault(c, 0) + 1);
            
            // If character count matches needed count
            if (needed.containsKey(c) && window.get(c).intValue() == needed.get(c).intValue()) {
                formed++;
            }
            
            // Try to shrink window
            while (left <= right && formed == required) {
                char leftChar = s.charAt(left);
                
                // Update result if current window is smaller
                if (right - left + 1 < result[0]) {
                    result[0] = right - left + 1;
                    result[1] = left;
                    result[2] = right;
                }
                
                // Remove character from window
                window.put(leftChar, window.get(leftChar) - 1);
                if (needed.containsKey(leftChar) && window.get(leftChar) < needed.get(leftChar)) {
                    formed--;
                }
                
                left++;
            }
        }
        
        return result[0] == Integer.MAX_VALUE ? "" : s.substring(result[1], result[2] + 1);
    }
    
    // Test cases
    public static void main(String[] args) {
        Solution sol = new Solution();
        
        // Test 1
        System.out.println("Output: \"" + sol.minWindow("ADOBECODEBANC", "ABC") + "\"");
        // Expected: "BANC"
        
        // Test 2
        System.out.println("Output: \"" + sol.minWindow("a", "a") + "\"");
        // Expected: "a"
        
        // Test 3
        System.out.println("Output: \"" + sol.minWindow("a", "aa") + "\"");
        // Expected: ""
        
        // Test 4
        System.out.println("Output: \"" + sol.minWindow("ab", "b") + "\"");
        // Expected: "b"
        
        // Test 5
        System.out.println("Output: \"" + sol.minWindow("aaaaaaaaaaaabbbbbcdd", "abcdd") + "\"");
        // Expected: "aabbbbbcdd"
    }
}