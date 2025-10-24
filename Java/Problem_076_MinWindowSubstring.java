/*
Problem: 76 - Minimum Window Substring
Difficulty: Hard
Link: https://leetcode.com/problems/minimum-window-substring/

Problem Statement:
Given two strings s and t of lengths m and n respectively, return the minimum 
window substring of s such that every character in t (including duplicates) is 
included in the window. If there is no such substring, return the empty string "".

Approach:
Use the sliding window technique with two pointers (left and right):
1. Expand the window by moving right pointer until all characters of t are included
2. Once valid window is found, try to shrink from left to find minimum
3. Keep track of the minimum valid window found
4. Use hash maps to count character frequencies

Time Complexity: O(N + M) - N is length of s, M is length of t
Space Complexity: O(M) - Hash maps store characters from t
*/

import java.util.HashMap;
import java.util.Map;

class Solution {
    public String minWindow(String s, String t) {
        if (s == null || t == null || s.length() < t.length()) {
            return "";
        }
        
        // Frequency map for characters in t
        Map<Character, Integer> targetMap = new HashMap<>();
        for (char c : t.toCharArray()) {
            targetMap.put(c, targetMap.getOrDefault(c, 0) + 1);
        }
        
        // Frequency map for current window
        Map<Character, Integer> windowMap = new HashMap<>();
        
        int left = 0, right = 0;
        int minLen = Integer.MAX_VALUE;
        int minStart = 0;
        int required = targetMap.size();  // Number of unique chars in t
        int formed = 0;  // Number of unique chars in window with correct frequency
        
        while (right < s.length()) {
            // Expand window by adding character at right
            char c = s.charAt(right);
            windowMap.put(c, windowMap.getOrDefault(c, 0) + 1);
            
            // Check if current character's frequency matches target
            if (targetMap.containsKey(c) && 
                windowMap.get(c).intValue() == targetMap.get(c).intValue()) {
                formed++;
            }
            
            // Try to shrink window from left while it's valid
            while (left <= right && formed == required) {
                // Update minimum window if current is smaller
                if (right - left + 1 < minLen) {
                    minLen = right - left + 1;
                    minStart = left;
                }
                
                // Remove character at left from window
                char leftChar = s.charAt(left);
                windowMap.put(leftChar, windowMap.get(leftChar) - 1);
                
                if (targetMap.containsKey(leftChar) && 
                    windowMap.get(leftChar).intValue() < targetMap.get(leftChar).intValue()) {
                    formed--;
                }
                
                left++;
            }
            
            right++;
        }
        
        return minLen == Integer.MAX_VALUE ? "" : s.substring(minStart, minStart + minLen);
    }
    
    // Test cases
    public static void main(String[] args) {
        Solution solution = new Solution();
        
        // Test case 1
        String s1 = "ADOBECODEBANC";
        String t1 = "ABC";
        System.out.println("Input: s = \"" + s1 + "\", t = \"" + t1 + "\"");
        System.out.println("Output: \"" + solution.minWindow(s1, t1) + "\"");
        System.out.println("Expected: \"BANC\"\n");
        
        // Test case 2
        String s2 = "a";
        String t2 = "a";
        System.out.println("Input: s = \"" + s2 + "\", t = \"" + t2 + "\"");
        System.out.println("Output: \"" + solution.minWindow(s2, t2) + "\"");
        System.out.println("Expected: \"a\"\n");
        
        // Test case 3
        String s3 = "a";
        String t3 = "aa";
        System.out.println("Input: s = \"" + s3 + "\", t = \"" + t3 + "\"");
        System.out.println("Output: \"" + solution.minWindow(s3, t3) + "\"");
        System.out.println("Expected: \"\"\n");
        
        // Test case 4
        String s4 = "ab";
        String t4 = "b";
        System.out.println("Input: s = \"" + s4 + "\", t = \"" + t4 + "\"");
        System.out.println("Output: \"" + solution.minWindow(s4, t4) + "\"");
        System.out.println("Expected: \"b\"\n");
    }
}