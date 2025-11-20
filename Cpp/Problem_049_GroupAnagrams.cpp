/*
Problem: 49 - Group Anagrams
Difficulty: Medium
Link: https://leetcode.com/problems/group-anagrams/

Problem Statement:
Group anagrams together from an array of strings.

Approach:
Use unordered_map with sorted string as key or character count as key.

Time Complexity: O(N * K log K) where N = number of strings, K = max string length
Space Complexity: O(N * K) for storing results
*/

#include <vector>
#include <string>
#include <unordered_map>
#include <algorithm>
#include <iostream>

using namespace std;

class Solution {
public:
    // Approach 1: Hash map with sorted string as key
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<string>> anagramMap;
        
        for (const string& s : strs) {
            // Sort string to get key
            string key = s;
            sort(key.begin(), key.end());
            
            anagramMap[key].push_back(s);
        }
        
        vector<vector<string>> result;
        for (auto& pair : anagramMap) {
            result.push_back(pair.second);
        }
        
        return result;
    }
    
    // Approach 2: Using character count as key
    vector<vector<string>> groupAnagramsCount(vector<string>& strs) {
        unordered_map<string, vector<string>> anagramMap;
        
        for (const string& s : strs) {
            // Count characters (26 lowercase letters)
            vector<int> count(26, 0);
            for (char c : s) {
                count[c - 'a']++;
            }
            
            // Build key from count array
            string key;
            for (int i = 0; i < 26; i++) {
                key += "#" + to_string(count[i]);
            }
            
            anagramMap[key].push_back(s);
        }
        
        vector<vector<string>> result;
        for (auto& pair : anagramMap) {
            result.push_back(pair.second);
        }
        
        return result;
    }
    
    // Approach 3: Using prime number multiplication
    vector<vector<string>> groupAnagramsPrime(vector<string>& strs) {
        vector<long long> primes = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 
                                    59, 61, 67, 71, 73, 79, 83, 89, 97, 101};
        
        unordered_map<long long, vector<string>> anagramMap;
        
        for (const string& s : strs) {
            long long key = 1;
            for (char c : s) {
                key *= primes[c - 'a'];
            }
            
            anagramMap[key].push_back(s);
        }
        
        vector<vector<string>> result;
        for (auto& pair : anagramMap) {
            result.push_back(pair.second);
        }
        
        return result;
    }
};

// Helper function to print result
void printResult(const vector<vector<string>>& result) {
    cout << "[";
    for (int i = 0; i < result.size(); i++) {
        cout << "[";
        for (int j = 0; j < result[i].size(); j++) {
            cout << "\"" << result[i][j] << "\"";
            if (j < result[i].size() - 1) {
                cout << ",";
            }
        }
        cout << "]";
        if (i < result.size() - 1) {
            cout << ",";
        }
    }
    cout << "]" << endl;
}

void printVector(const vector<string>& arr) {
    cout << "[";
    for (int i = 0; i < arr.size(); i++) {
        cout << "\"" << arr[i] << "\"";
        if (i < arr.size() - 1) {
            cout << ",";
        }
    }
    cout << "]";
}

int main() {
    Solution solution;
    
    // Test case 1
    vector<string> strs1 = {"eat","tea","tan","ate","nat","bat"};
    cout << "Input: strs = ";
    printVector(strs1);
    cout << "\nOutput: ";
    printResult(solution.groupAnagrams(strs1));
    cout << "Expected: [[bat],[nat,tan],[ate,eat,tea]] (any order)\n" << endl;
    
    // Test case 2
    vector<string> strs2 = {""};
    cout << "Input: strs = ";
    printVector(strs2);
    cout << "\nOutput: ";
    printResult(solution.groupAnagrams(strs2));
    cout << "Expected: [[\"\"]]\n" << endl;
    
    // Test case 3
    vector<string> strs3 = {"a"};
    cout << "Input: strs = ";
    printVector(strs3);
    cout << "\nOutput: ";
    printResult(solution.groupAnagrams(strs3));
    cout << "Expected: [[a]]\n" << endl;
    
    // Test case 4
    vector<string> strs4 = {"abc","def","ghi"};
    cout << "Input: strs = ";
    printVector(strs4);
    cout << "\nOutput: ";
    printResult(solution.groupAnagrams(strs4));
    cout << "Expected: [[abc],[def],[ghi]]\n" << endl;
    
    // Compare approaches
    vector<string> strs5 = {"eat","tea","tan","ate","nat","bat"};
    cout << "Input: strs = ";
    printVector(strs5);
    cout << "\nSorted Key: ";
    printResult(solution.groupAnagrams(strs5));
    
    vector<string> strs5_copy = strs5;
    cout << "Count Key: ";
    printResult(solution.groupAnagramsCount(strs5_copy));
    
    strs5_copy = strs5;
    cout << "Prime Key: ";
    printResult(solution.groupAnagramsPrime(strs5_copy));
    
    return 0;
}