/*
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
*/
import java.util.*;

class Solution {
    public int minDistance(String word1, String word2) {
        int m = word1.length();
        int n = word2.length();
        
        // dp[i][j] = min operations to convert word1[0..i-1] to word2[0..j-1]
        int[][] dp = new int[m + 1][n + 1];
        
        // Base cases
        for (int i = 0; i <= m; i++) {
            dp[i][0] = i;  // Delete i characters
        }
        for (int j = 0; j <= n; j++) {
            dp[0][j] = j;  // Insert j characters
        }
        
        // Fill DP table
        for (int i = 1; i <= m; i++) {
            for (int j = 1; j <= n; j++) {
                if (word1.charAt(i - 1) == word2.charAt(j - 1)) {
                    // Characters match, no operation needed
                    dp[i][j] = dp[i - 1][j - 1];
                } else {
                    // Three operations: insert, delete, replace
                    int insert = dp[i][j - 1] + 1;      // Insert char from word2
                    int delete = dp[i - 1][j] + 1;      // Delete char from word1
                    int replace = dp[i - 1][j - 1] + 1; // Replace char
                    
                    dp[i][j] = Math.min(Math.min(insert, delete), replace);
                }
            }
        }
        
        return dp[m][n];
    }
    
    // Space optimized version using 1D array
    public int minDistance_Optimized(String word1, String word2) {
        int m = word1.length();
        int n = word2.length();
        
        // Use two 1D arrays instead of 2D
        int[] prev = new int[n + 1];
        int[] curr = new int[n + 1];
        
        // Base case
        for (int j = 0; j <= n; j++) {
            prev[j] = j;
        }
        
        // Fill DP
        for (int i = 1; i <= m; i++) {
            curr[0] = i;
            
            for (int j = 1; j <= n; j++) {
                if (word1.charAt(i - 1) == word2.charAt(j - 1)) {
                    curr[j] = prev[j - 1];
                } else {
                    int insert = curr[j - 1] + 1;
                    int delete = prev[j] + 1;
                    int replace = prev[j - 1] + 1;
                    
                    curr[j] = Math.min(Math.min(insert, delete), replace);
                }
            }
            
            // Swap arrays
            int[] temp = prev;
            prev = curr;
            curr = temp;
        }
        
        return prev[n];
    }
    
    // Test cases
    public static void main(String[] args) {
        Solution sol = new Solution();
        
        // Test 1
        System.out.println("Output: " + sol.minDistance("horse", "ros"));
        System.out.println("Optimized: " + sol.minDistance_Optimized("horse", "ros"));
        // Expected: 3 (replace h with r, delete e)
        
        // Test 2
        System.out.println("Output: " + sol.minDistance("intention", "execution"));
        System.out.println("Optimized: " + sol.minDistance_Optimized("intention", "execution"));
        // Expected: 5
        
        // Test 3
        System.out.println("Output: " + sol.minDistance("", "abc"));
        System.out.println("Optimized: " + sol.minDistance_Optimized("", "abc"));
        // Expected: 3
        
        // Test 4
        System.out.println("Output: " + sol.minDistance("abc", ""));
        System.out.println("Optimized: " + sol.minDistance_Optimized("abc", ""));
        // Expected: 3
    }
}