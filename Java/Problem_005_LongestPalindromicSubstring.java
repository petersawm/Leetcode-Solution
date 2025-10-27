/*
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

Time Complexity: O(N²) - Expand around center approach
Space Complexity: O(1) - Only storing indices
*/

class Solution {
    // Approach 1: Expand Around Center - Most intuitive
    public String longestPalindrome(String s) {
        if (s == null || s.length() < 1) {
            return "";
        }
        
        int start = 0;
        int maxLen = 0;
        
        for (int i = 0; i < s.length(); i++) {
            // Check odd length palindromes (center is single character)
            int len1 = expandAroundCenter(s, i, i);
            
            // Check even length palindromes (center is between two characters)
            int len2 = expandAroundCenter(s, i, i + 1);
            
            // Get maximum length
            int currLen = Math.max(len1, len2);
            
            // Update start and maxLen if we found longer palindrome
            if (currLen > maxLen) {
                maxLen = currLen;
                start = i - (currLen - 1) / 2;
            }
        }
        
        return s.substring(start, start + maxLen);
    }
    
    private int expandAroundCenter(String s, int left, int right) {
        while (left >= 0 && right < s.length() && s.charAt(left) == s.charAt(right)) {
            left--;
            right++;
        }
        return right - left - 1;
    }
    
    // Approach 2: Dynamic Programming
    public String longestPalindromeDP(String s) {
        int n = s.length();
        if (n < 2) {
            return s;
        }
        
        boolean[][] dp = new boolean[n][n];
        int start = 0;
        int maxLen = 1;
        
        // Every single character is a palindrome
        for (int i = 0; i < n; i++) {
            dp[i][i] = true;
        }
        
        // Check for two character palindromes
        for (int i = 0; i < n - 1; i++) {
            if (s.charAt(i) == s.charAt(i + 1)) {
                dp[i][i + 1] = true;
                start = i;
                maxLen = 2;
            }
        }
        
        // Check for lengths greater than 2
        for (int length = 3; length <= n; length++) {
            for (int i = 0; i < n - length + 1; i++) {
                int j = i + length - 1;
                
                if (s.charAt(i) == s.charAt(j) && dp[i + 1][j - 1]) {
                    dp[i][j] = true;
                    start = i;
                    maxLen = length;
                }
            }
        }
        
        return s.substring(start, start + maxLen);
    }
    
    // Approach 3: Optimized expand around center
    public String longestPalindromeOptimized(String s) {
        int n = s.length();
        if (n < 2) {
            return s;
        }
        
        int start = 0;
        int maxLen = 1;
        
        for (int i = 0; i < n; ) {
            int left = i;
            int right = i;
            
            // Skip duplicate characters to handle even length palindromes
            while (right + 1 < n && s.charAt(right) == s.charAt(right + 1)) {
                right++;
            }
            
            // Next center will be after the duplicates
            i = right + 1;
            
            // Expand around the center
            while (left - 1 >= 0 && right + 1 < n && s.charAt(left - 1) == s.charAt(right + 1)) {
                left--;
                right++;
            }
            
            int currLen = right - left + 1;
            if (currLen > maxLen) {
                maxLen = currLen;
                start = left;
            }
        }
        return s.substring(start, start + maxLen);
    }