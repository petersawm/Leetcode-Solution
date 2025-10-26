/*
Problem: 242 - Valid Anagram
Difficulty: Easy
Link: https://leetcode.com/problems/valid-anagram/

Problem Statement:
Given two strings s and t, return true if t is an anagram of s, and false otherwise.
An Anagram is a word or phrase formed by rearranging the letters of a different word 
or phrase, typically using all the original letters exactly once.

Approach:
Multiple approaches:

1. Sorting - Sort both strings and compare
   Time: O(N log N), Space: O(1)

2. Hash Map - Count character frequencies
   Time: O(N), Space: O(1) for lowercase English letters (max 26 chars)

3. Array counting - Use fixed-size array for ASCII/lowercase letters
   Time: O(N), Space: O(1)

Time Complexity: O(N) - Hash map/array approach
Space Complexity: O(1) - At most 26 characters for lowercase English
*/

#include <string>
#include <iostream>
#include <unordered_map>
#include <algorithm>
#include <vector>

using namespace std;

class Solution {
public:
    // Approach 1: Array counting (most efficient for lowercase English letters)
    bool isAnagram(string s, string t) {
        // Different lengths can't be anagrams
        if (s.length() != t.length()) {
            return false;
        }
        
        // Array for 26 lowercase English letters
        int count[26] = {0};
        
        // Count characters in s and t simultaneously
        for (int i = 0; i < s.length(); i++) {
            count[s[i] - 'a']++;
            count[t[i] - 'a']--;
        }
        
        // Check if all counts are zero
        for (int i = 0; i < 26; i++) {
            if (count[i] != 0) {
                return false;
            }
        }
        
        return true;
    }
    
    // Approach 2: Using unordered_map
    bool isAnagramHashMap(string s, string t) {
        if (s.length() != t.length()) {
            return false;
        }
        
        unordered_map<char, int> countMap;
        
        // Count characters in s
        for (char c : s) {
            countMap[c]++;
        }
        
        // Decrement count for characters in t
        for (char c : t) {
            if (countMap.find(c) == countMap.end()) {
                return false;
            }
            countMap[c]--;
            if (countMap[c] < 0) {
                return false;
            }
        }
        
        return true;
    }
    
    // Approach 3: Sorting
    bool isAnagramSorting(string s, string t) {
        // Different lengths can't be anagrams
        if (s.length() != t.length()) {
            return false;
        }
        
        // Sort both strings
        sort(s.begin(), s.end());
        sort(t.begin(), t.end());
        
        // Compare sorted strings
        return s == t;
    }
    
    // Approach 4: Using vector instead of array
    bool isAnagramVector(string s, string t) {
        if (s.length() != t.length()) {
            return false;
        }
        
        vector<int> count(26, 0);
        
        for (int i = 0; i < s.length(); i++) {
            count[s[i] - 'a']++;
            count[t[i] - 'a']--;
        }
        
        for (int c : count) {
            if (c != 0) {
                return false;
            }
        }
        
        return true;
    }
    
    // Approach 5: Using two arrays
    bool isAnagramTwoArrays(string s, string t) {
        if (s.length() != t.length()) {
            return false;
        }
        
        int sCount[26] = {0};
        int tCount[26] = {0};
        
        for (int i = 0; i < s.length(); i++) {
            sCount[s[i] - 'a']++;
            tCount[t[i] - 'a']++;
        }
        
        for (int i = 0; i < 26; i++) {
            if (sCount[i] != tCount[i]) {
                return false;
            }
        }
        
        return true;
    }
};

int main() {
    Solution solution;
    
    // Test case 1
    string s1 = "anagram", t1 = "nagaram";
    cout << "Input: s = \"" << s1 << "\", t = \"" << t1 << "\"" << endl;
    cout << "Output: " << (solution.isAnagram(s1, t1) ? "true" : "false") << endl;
    cout << "Expected: true\n\n";
    
    // Test case 2
    string s2 = "rat", t2 = "car";
    cout << "Input: s = \"" << s2 << "\", t = \"" << t2 << "\"" << endl;
    cout << "Output: " << (solution.isAnagram(s2, t2) ? "true" : "false") << endl;
    cout << "Expected: false\n\n";
    
    // Test case 3
    string s3 = "listen", t3 = "silent";
    cout << "Input: s = \"" << s3 << "\", t = \"" << t3 << "\"" << endl;
    cout << "Output: " << (solution.isAnagram(s3, t3) ? "true" : "false") << endl;
    cout << "Expected: true\n\n";
    
    // Test case 4: Different lengths
    string s4 = "a", t4 = "ab";
    cout << "Input: s = \"" << s4 << "\", t = \"" << t4 << "\"" << endl;
    cout << "Output: " << (solution.isAnagram(s4, t4) ? "true" : "false") << endl;
    cout << "Expected: false\n\n";
    
    // Test case 5: Empty strings
    string s5 = "", t5 = "";
    cout << "Input: s = \"" << s5 << "\", t = \"" << t5 << "\"" << endl;
    cout << "Output: " << (solution.isAnagram(s5, t5) ? "true" : "false") << endl;
    cout << "Expected: true\n\n";
    
    // Compare all approaches
    string s6 = "triangle", t6 = "integral";
    cout << "Input: s = \"" << s6 << "\", t = \"" << t6 << "\"" << endl;
    cout << "Array: " << (solution.isAnagram(s6, t6) ? "true" : "false") << endl;
    cout << "HashMap: " << (solution.isAnagramHashMap(s6, t6) ? "true" : "false") << endl;
    cout << "Sorting: " << (solution.isAnagramSorting(s6, t6) ? "true" : "false") << endl;
    cout << "Vector: " << (solution.isAnagramVector(s6, t6) ? "true" : "false") << endl;
    cout << "Two Arrays: " << (solution.isAnagramTwoArrays(s6, t6) ? "true" : "false") << endl;
    cout << "Expected: true" << endl;
    
    return 0;
}