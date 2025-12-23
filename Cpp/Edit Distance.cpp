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
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;

class Solution {
public:
    int minDistance(string word1, string word2) {
        int m = word1.length();
        int n = word2.length();
        
        // dp[i][j] = min operations to convert word1[0..i-1] to word2[0..j-1]
        vector<vector<int>> dp(m + 1, vector<int>(n + 1, 0));
        
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
                if (word1[i - 1] == word2[j - 1]) {
                    // Characters match, no operation needed
                    dp[i][j] = dp[i - 1][j - 1];
                } else {
                    // Three operations: insert, delete, replace
                    int insert = dp[i][j - 1] + 1;      // Insert char from word2
                    int del = dp[i - 1][j] + 1;         // Delete char from word1
                    int replace = dp[i - 1][j - 1] + 1; // Replace char
                    
                    dp[i][j] = min({insert, del, replace});
                }
            }
        }
        
        return dp[m][n];
    }
    
    // Space optimized version using 1D array
    int minDistance_Optimized(string word1, string word2) {
        int m = word1.length();
        int n = word2.length();
        
        // Use two 1D arrays instead of 2D
        vector<int> prev(n + 1);
        vector<int> curr(n + 1);
        
        // Base case
        for (int j = 0; j <= n; j++) {
            prev[j] = j;
        }
        
        // Fill DP
        for (int i = 1; i <= m; i++) {
            curr[0] = i;
            
            for (int j = 1; j <= n; j++) {
                if (word1[i - 1] == word2[j - 1]) {
                    curr[j] = prev[j - 1];
                } else {
                    int insert = curr[j - 1] + 1;
                    int del = prev[j] + 1;
                    int replace = prev[j - 1] + 1;
                    
                    curr[j] = min({insert, del, replace});
                }
            }
            
            // Swap arrays
            swap(prev, curr);
        }
        
        return prev[n];
    }
};

// Test cases
int main() {
    Solution sol;
    
    // Test 1
    cout << "Output: " << sol.minDistance("horse", "ros") << endl;
    cout << "Optimized: " << sol.minDistance_Optimized("horse", "ros") << endl;
    // Expected: 3
    
    // Test 2
    cout << "Output: " << sol.minDistance("intention", "execution") << endl;
    cout << "Optimized: " << sol.minDistance_Optimized("intention", "execution") << endl;
    // Expected: 5
    
    // Test 3
    cout << "Output: " << sol.minDistance("", "abc") << endl;
    cout << "Optimized: " << sol.minDistance_Optimized("", "abc") << endl;
    // Expected: 3
    
    // Test 4
    cout << "Output: " << sol.minDistance("abc", "") << endl;
    cout << "Optimized: " << sol.minDistance_Optimized("abc", "") << endl;
    // Expected: 3
    
    return 0;
}