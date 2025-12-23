/*
Problem: 44 - Wildcard Matching
Difficulty: Hard
Link: https://leetcode.com/problems/wildcard-matching/
Problem Statement:
Given an input string s and a pattern p, implement wildcard pattern matching 
with support for '?' and '*' where:
- '?' Matches any single character
- '*' Matches any sequence of characters (including empty sequence)
The matching should cover the entire input string (not partial).
Approach:
Use Two Pointers with Greedy approach
Track positions in s and p, also track star position for backtracking
Time Complexity: O(M * N) worst case, but usually better
Space Complexity: O(1)
*/
#include <iostream>
#include <string>
using namespace std;

class Solution {
public:
    bool isMatch(string s, string p) {
        int sLen = s.length();
        int pLen = p.length();
        int sIdx = 0, pIdx = 0;
        int starIdx = -1, matchIdx = 0;
        
        while (sIdx < sLen) {
            // Characters match or pattern has '?'
            if (pIdx < pLen && (p[pIdx] == '?' || s[sIdx] == p[pIdx])) {
                sIdx++;
                pIdx++;
            }
            // Pattern has '*'
            else if (pIdx < pLen && p[pIdx] == '*') {
                starIdx = pIdx;
                matchIdx = sIdx;
                pIdx++;
            }
            // No match, backtrack if we have seen '*'
            else if (starIdx != -1) {
                pIdx = starIdx + 1;
                matchIdx++;
                sIdx = matchIdx;
            }
            // No match and no '*' to backtrack
            else {
                return false;
            }
        }
        
        // Check for remaining characters in pattern (should be only '*')
        while (pIdx < pLen && p[pIdx] == '*') {
            pIdx++;
        }
        
        return pIdx == pLen;
    }
};

// Test cases
int main() {
    Solution sol;
    
    // Test 1
    cout << "Test 1: " << (sol.isMatch("aa", "a") ? "true" : "false") << endl;
    // Expected: false
    
    // Test 2
    cout << "Test 2: " << (sol.isMatch("aa", "*") ? "true" : "false") << endl;
    // Expected: true
    
    // Test 3
    cout << "Test 3: " << (sol.isMatch("cb", "?a") ? "true" : "false") << endl;
    // Expected: false
    
    // Test 4
    cout << "Test 4: " << (sol.isMatch("adceb", "*a*b") ? "true" : "false") << endl;
    // Expected: true
    
    // Test 5
    cout << "Test 5: " << (sol.isMatch("acdcb", "a*c?b") ? "true" : "false") << endl;
    // Expected: false
    
    // Test 6
    cout << "Test 6: " << (sol.isMatch("mississippi", "m*iss*p*.") ? "true" : "false") << endl;
    // Expected: false
    
    // Test 7
    cout << "Test 7: " << (sol.isMatch("ab", "?*") ? "true" : "false") << endl;
    // Expected: true
    
    return 0;
}