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
import java.util.*;

class Solution {
    public boolean isMatch(String s, String p) {
        int sLen = s.length();
        int pLen = p.length();
        int sIdx = 0, pIdx = 0;
        int starIdx = -1, matchIdx = 0;
        
        while (sIdx < sLen) {
            // Characters match or pattern has '?'
            if (pIdx < pLen && (p.charAt(pIdx) == '?' || s.charAt(sIdx) == p.charAt(pIdx))) {
                sIdx++;
                pIdx++;
            }
            // Pattern has '*'
            else if (pIdx < pLen && p.charAt(pIdx) == '*') {
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
        while (pIdx < pLen && p.charAt(pIdx) == '*') {
            pIdx++;
        }
        
        return pIdx == pLen;
    }
    
    // Test cases
    public static void main(String[] args) {
        Solution sol = new Solution();
        
        // Test 1
        System.out.println("Test 1: " + sol.isMatch("aa", "a"));
        // Expected: false
        
        // Test 2
        System.out.println("Test 2: " + sol.isMatch("aa", "*"));
        // Expected: true
        
        // Test 3
        System.out.println("Test 3: " + sol.isMatch("cb", "?a"));
        // Expected: false
        
        // Test 4
        System.out.println("Test 4: " + sol.isMatch("adceb", "*a*b"));
        // Expected: true
        
        // Test 5
        System.out.println("Test 5: " + sol.isMatch("acdcb", "a*c?b"));
        // Expected: false
        
        // Test 6
        System.out.println("Test 6: " + sol.isMatch("mississippi", "m*iss*p*."));
        // Expected: false
        
        // Test 7
        System.out.println("Test 7: " + sol.isMatch("ab", "?*"));
        // Expected: true
    }
}