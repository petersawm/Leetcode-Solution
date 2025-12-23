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
Use Sliding Window with unordered_map
Track character counts needed and characters in current window
Expand window until all characters are found
Contract window from left to find minimum
Time Complexity: O(M + N) where M = s.length
Space Complexity: O(1) - fixed alphabet size
*/
#include <iostream>
#include <string>
#include <unordered_map>
#include <algorithm>
using namespace std;

class Solution {
public:
    string minWindow(string s, string t) {
        if (s.length() < t.length()) {
            return "";
        }
        
        // Count characters needed from t
        unordered_map<char, int> needed;
        for (char c : t) {
            needed[c]++;
        }
        
        // Track window characters
        unordered_map<char, int> window;
        
        int left = 0;
        int formed = 0;  // Number of unique characters with required count
        int required = needed.size();  // Number of unique characters needed
        
        // {length, left, right}
        int minLen = INT_MAX;
        int resultLeft = 0;
        int resultRight = 0;
        
        for (int right = 0; right < s.length(); right++) {
            char c = s[right];
            
            // Add character to window
            window[c]++;
            
            // If character count matches needed count
            if (needed.count(c) && window[c] == needed[c]) {
                formed++;
            }
            
            // Try to shrink window
            while (left <= right && formed == required) {
                char leftChar = s[left];
                
                // Update result if current window is smaller
                if (right - left + 1 < minLen) {
                    minLen = right - left + 1;
                    resultLeft = left;
                    resultRight = right;
                }
                
                // Remove character from window
                window[leftChar]--;
                if (needed.count(leftChar) && window[leftChar] < needed[leftChar]) {
                    formed--;
                }
                
                left++;
            }
        }
        
        return minLen == INT_MAX ? "" : s.substr(resultLeft, minLen);
    }
};

// Test cases
int main() {
    Solution sol;
    
    // Test 1
    cout << "Output: \"" << sol.minWindow("ADOBECODEBANC", "ABC") << "\"" << endl;
    // Expected: "BANC"
    
    // Test 2
    cout << "Output: \"" << sol.minWindow("a", "a") << "\"" << endl;
    // Expected: "a"
    
    // Test 3
    cout << "Output: \"" << sol.minWindow("a", "aa") << "\"" << endl;
    // Expected: ""
    
    // Test 4
    cout << "Output: \"" << sol.minWindow("ab", "b") << "\"" << endl;
    // Expected: "b"
    
    // Test 5
    cout << "Output: \"" << sol.minWindow("aaaaaaaaaaaabbbbbcdd", "abcdd") << "\"" << endl;
    // Expected: "aabbbbbcdd"
    
    return 0;
}