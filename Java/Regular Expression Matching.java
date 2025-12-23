/*
Problem: 10 - Regular Expression Matching
Difficulty: Hard
Link: https://leetcode.com/problems/regular-expression-matching/
Problem Statement:
Given an input string s and a pattern p, implement regular expression matching 
with support for '.' and '*' where:
- '.' Matches any single character
- '*' Matches zero or more of the preceding element
The matching should cover the entire input string (not partial).
Approach:
Use Dynamic Programming with 2D DP table
dp[i][j] = true if s[0..i-1] matches p[0..j-1]
Handle three cases: character match, '.', '*'
Time Complexity: O(M * N) where M = s.length, N = p.length
Space Complexity: O(M * N)
*/
import java.util.*;

class Solution {
    public boolean isMatch(String s, String p) {
        int m = s.length();
        int n = p.length();
        
        // dp[i][j] = true if s[0..i-1] matches p[0..j-1]
        boolean[][] dp = new boolean[m + 1][n + 1];
        
        // Base case: empty string matches empty pattern
        dp[0][0] = true;
        
        // Handle patterns like a*, a*b*, a*b*c* that match empty string
        for (int j = 2; j <= n; j++) {
            if (p.charAt(j - 1) == '*') {
                dp[0][j] = dp[0][j - 2];
            }
        }
        
        // Fill DP table
        for (int i = 1; i <= m; i++) {
            for (int j = 1; j <= n; j++) {
                if (p.charAt(j - 1) == '*') {
                    // '*' matches zero or more of preceding element
                    // Zero case: match without using *
                    dp[i][j] = dp[i][j - 2];
                    
                    // More case: use * to match current character
                    if (p.charAt(j - 2) == '.' || p.charAt(j - 2) == s.charAt(i - 1)) {
                        dp[i][j] = dp[i][j] || dp[i - 1][j];
                    }
                } else if (p.charAt(j - 1) == '.' || p.charAt(j - 1) == s.charAt(i - 1)) {
                    // '.' or character match
                    dp[i][j] = dp[i - 1][j - 1];
                }
            }
        }
        
        return dp[m][n];
    }
    
    // Test cases
    public static void main(String[] args) {
        Solution sol = new Solution();
        
        // Test 1
        System.out.println("Test 1: " + sol.isMatch("aa", "a"));
        // Expected: false
        
        // Test 2
        System.out.println("Test 2: " + sol.isMatch("aa", "a*"));
        // Expected: true
        
        // Test 3
        System.out.println("Test 3: " + sol.isMatch("ab", ".*"));
        // Expected: true
        
        // Test 4
        System.out.println("Test 4: " + sol.isMatch("aab", "c*a*b"));
        // Expected: true
        
        // Test 5
        System.out.println("Test 5: " + sol.isMatch("mississippi", "mis*is*p*."));
        // Expected: false
        
        // Test 6
        System.out.println("Test 6: " + sol.isMatch("abc", "a.c"));
        // Expected: true
    }
}