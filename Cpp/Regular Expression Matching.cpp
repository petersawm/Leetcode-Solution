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
#include <iostream>
#include <vector>
#include <string>
using namespace std;

class Solution {
public:
    bool isMatch(string s, string p) {
        int m = s.length();
        int n = p.length();
        
        // dp[i][j] = true if s[0..i-1] matches p[0..j-1]
        vector<vector<bool>> dp(m + 1, vector<bool>(n + 1, false));
        
        // Base case: empty string matches empty pattern
        dp[0][0] = true;
        
        // Handle patterns like a*, a*b*, a*b*c* that match empty string
        for (int j = 2; j <= n; j++) {
            if (p[j - 1] == '*') {
                dp[0][j] = dp[0][j - 2];
            }
        }
        
        // Fill DP table
        for (int i = 1; i <= m; i++) {
            for (int j = 1; j <= n; j++) {
                if (p[j - 1] == '*') {
                    // '*' matches zero or more of preceding element
                    // Zero case: match without using *
                    dp[i][j] = dp[i][j - 2];
                    
                    // More case: use * to match current character
                    if (p[j - 2] == '.' || p[j - 2] == s[i - 1]) {
                        dp[i][j] = dp[i][j] || dp[i - 1][j];
                    }
                } else if (p[j - 1] == '.' || p[j - 1] == s[i - 1]) {
                    // '.' or character match
                    dp[i][j] = dp[i - 1][j - 1];
                }
            }
        }
        
        return dp[m][n];
    }
};

// Test cases
int main() {
    Solution sol;
    
    // Test 1
    cout << "Test 1: " << (sol.isMatch("aa", "a") ? "true" : "false") << endl;
    // Expected: false
    
    // Test 2
    cout << "Test 2: " << (sol.isMatch("aa", "a*") ? "true" : "false") << endl;
    // Expected: true
    
    // Test 3
    cout << "Test 3: " << (sol.isMatch("ab", ".*") ? "true" : "false") << endl;
    // Expected: true
    
    // Test 4
    cout << "Test 4: " << (sol.isMatch("aab", "c*a*b") ? "true" : "false") << endl;
    // Expected: true
    
    // Test 5
    cout << "Test 5: " << (sol.isMatch("mississippi", "mis*is*p*.") ? "true" : "false") << endl;
    // Expected: false
    
    // Test 6
    cout << "Test 6: " << (sol.isMatch("abc", "a.c") ? "true" : "false") << endl;
    // Expected: true
    
    return 0;
}