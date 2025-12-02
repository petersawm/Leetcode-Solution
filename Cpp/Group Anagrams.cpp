/*
Problem: 49 - Group Anagrams
Difficulty: Medium
Link: https://leetcode.com/problems/group-anagrams/
Problem Statement:
Given an array of strings strs, group the anagrams together. You can return 
the answer in any order.
Approach:
Sort each string's characters and use as key in unordered_map.
Strings with same characters (anagrams) will have same sorted key.
Time Complexity: O(N * K log K) where N is number of strings, K is max length
Space Complexity: O(N * K)
*/
#include <iostream>
#include <vector>
#include <unordered_map>
#include <algorithm>
using namespace std;

class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        // unordered_map to store {sorted_key: list_of_anagrams}
        unordered_map<string, vector<string>> map;
        
        // Iterate through each string
        for (string str : strs) {
            // Sort characters in string
            string sorted = str;
            sort(sorted.begin(), sorted.end());
            
            // Add to corresponding group
            map[sorted].push_back(str);
        }
        
        // Convert map values to vector
        vector<vector<string>> result;
        for (auto& pair : map) {
            result.push_back(pair.second);
        }
        
        return result;
    }
};

// Helper function to print vector of vectors
void printResult(vector<vector<string>>& result) {
    cout << "Output: [";
    for (int i = 0; i < result.size(); i++) {
        cout << "[";
        for (int j = 0; j < result[i].size(); j++) {
            cout << "\"" << result[i][j] << "\"";
            if (j < result[i].size() - 1) cout << ",";
        }
        cout << "]";
        if (i < result.size() - 1) cout << ",";
    }
    cout << "]" << endl;
}

// Test cases
int main() {
    Solution sol;
    
    // Test 1
    vector<string> strs1 = {"eat", "tea", "ate", "eat", "tan", "nat", "bat"};
    vector<vector<string>> result1 = sol.groupAnagrams(strs1);
    printResult(result1);
    // Expected: [["eat","tea","ate"], ["tan","nat"], ["bat"]]
    // Order may vary
    
    // Test 2
    vector<string> strs2 = {""};
    vector<vector<string>> result2 = sol.groupAnagrams(strs2);
    printResult(result2);
    // Expected: [[""]]
    
    // Test 3
    vector<string> strs3 = {"a"};
    vector<vector<string>> result3 = sol.groupAnagrams(strs3);
    printResult(result3);
    // Expected: [["a"]]
    
    return 0;
}