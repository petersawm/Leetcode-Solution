/*
Problem: 3 - Longest Substring Without Repeating Characters
Difficulty: Medium
Link: https://leetcode.com/problems/longest-substring-without-repeating-characters/
Problem Statement:
Given a string s, find the length of the longest substring without repeating
characters.
Approach:
Use Sliding Window with unordered_map to track character indices.
Expand window by moving right pointer.
When duplicate found, contract window from left.
Time Complexity: O(N)
Space Complexity: O(min(N, charset_size))
*/
#include <iostream>
#include <unordered_map>
#include <string>
#include <algorithm>
using namespace std;

class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        // unordered_map to store {character: index}
        unordered_map<char, int> charIndex;
        
        int maxLength = 0;
        int left = 0;  // Left pointer of sliding window
        
        // Right pointer of sliding window
        for (int right = 0; right < s.length(); right++) {
            char c = s[right];
            
            // If character exists in current window
            if (charIndex.find(c) != charIndex.end() && charIndex[c] >= left) {
                // Move left pointer to right of previous occurrence
                left = charIndex[c] + 1;
            }
            
            // Update character index
            charIndex[c] = right;
            
            // Update max length
            maxLength = max(maxLength, right - left + 1);
        }
        
        return maxLength;
    }
};

// Test cases
int main() {
    Solution sol;
    
    // Test 1
    cout << "Output: " << sol.lengthOfLongestSubstring("abcabcbb") << endl;
    // Expected: 3 ("abc")
    
    // Test 2
    cout << "Output: " << sol.lengthOfLongestSubstring("bbbbb") << endl;
    // Expected: 1 ("b")
    
    // Test 3
    cout << "Output: " << sol.lengthOfLongestSubstring("pwwkew") << endl;
    // Expected: 3 ("wke")
    
    // Test 4
    cout << "Output: " << sol.lengthOfLongestSubstring("au") << endl;
    // Expected: 2 ("au")
    
    // Test 5
    cout << "Output: " << sol.lengthOfLongestSubstring("dvdf") << endl;
    // Expected: 3 ("vdf")
    
    return 0;
}