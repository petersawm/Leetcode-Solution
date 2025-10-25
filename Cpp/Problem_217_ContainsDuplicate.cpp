/*
Problem: 217 - Contains Duplicate
Difficulty: Easy
Link: https://leetcode.com/problems/contains-duplicate/

Problem Statement:
Given an integer array nums, return true if any value appears at least twice 
in the array, and return false if every element is distinct.

Approach:
Multiple approaches with different trade-offs:

1. Hash Set (unordered_set) - Most efficient
   - Add elements to set while iterating
   - If element already exists, return true
   - Time: O(N) average, Space: O(N)

2. Sorting
   - Sort array and check adjacent elements
   - Time: O(N log N), Space: O(1) if in-place sort

3. Hash Map (unordered_map)
   - Count occurrences using hash map
   - Time: O(N), Space: O(N)

Time Complexity: O(N) - Hash set approach
Space Complexity: O(N) - Hash set storage
*/

#include <vector>
#include <iostream>
#include <unordered_set>
#include <unordered_map>
#include <algorithm>

using namespace std;

class Solution {
public:
    // Approach 1: Unordered Set - Most efficient
    bool containsDuplicate(vector<int>& nums) {
        unordered_set<int> seen;
        
        for (int num : nums) {
            // If insert fails, element already exists
            if (seen.find(num) != seen.end()) {
                return true;
            }
            seen.insert(num);
        }
        
        return false;
    }
    
    // Alternative using insert return value
    bool containsDuplicateInsert(vector<int>& nums) {
        unordered_set<int> seen;
        
        for (int num : nums) {
            // insert returns pair<iterator, bool>
            // second element is false if element already exists
            if (!seen.insert(num).second) {
                return true;
            }
        }
        
        return false;
    }
    
    // Approach 2: Sorting
    bool containsDuplicateSorting(vector<int>& nums) {
        if (nums.size() < 2) {
            return false;
        }
        
        sort(nums.begin(), nums.end());
        
        for (int i = 1; i < nums.size(); i++) {
            if (nums[i] == nums[i - 1]) {
                return true;
            }
        }
        
        return false;
    }
    
    // Approach 3: Using unordered_map to count occurrences
    bool containsDuplicateHashMap(vector<int>& nums) {
        unordered_map<int, int> countMap;
        
        for (int num : nums) {
            countMap[num]++;
            
            if (countMap[num] > 1) {
                return true;
            }
        }
        
        return false;
    }
    
    // Approach 4: STL set (ordered)
    bool containsDuplicateSet(vector<int>& nums) {
        set<int> seen;
        
        for (int num : nums) {
            if (!seen.insert(num).second) {
                return true;
            }
        }
        
        return false;
    }
    
    // Approach 5: Using count_if and lambda (C++11)
    bool containsDuplicateLambda(vector<int>& nums) {
        unordered_set<int> seen;
        
        return any_of(nums.begin(), nums.end(), [&seen](int num) {
            return !seen.insert(num).second;
        });
    }
};

// Helper function to print vector
void printVector(const vector<int>& arr) {
    cout << "[";
    for (int i = 0; i < arr.size(); i++) {
        cout << arr[i];
        if (i < arr.size() - 1) cout << ",";
    }
    cout << "]";
}

int main() {
    Solution solution;
    
    // Test case 1
    vector<int> nums1 = {1, 2, 3, 1};
    cout << "Input: nums = ";
    printVector(nums1);
    cout << "\nOutput: " << (solution.containsDuplicate(nums1) ? "true" : "false") << endl;
    cout << "Expected: true\n\n";
    
    // Test case 2
    vector<int> nums2 = {1, 2, 3, 4};
    cout << "Input: nums = ";
    printVector(nums2);
    cout << "\nOutput: " << (solution.containsDuplicate(nums2) ? "true" : "false") << endl;
    cout << "Expected: false\n\n";
    
    // Test case 3
    vector<int> nums3 = {1, 1, 1, 3, 3, 4, 3, 2, 4, 2};
    cout << "Input: nums = ";
    printVector(nums3);
    cout << "\nOutput: " << (solution.containsDuplicate(nums3) ? "true" : "false") << endl;
    cout << "Expected: true\n\n";
    
    // Test case 4: Empty vector
    vector<int> nums4 = {};
    cout << "Input: nums = ";
    printVector(nums4);
    cout << "\nOutput: " << (solution.containsDuplicate(nums4) ? "true" : "false") << endl;
    cout << "Expected: false\n\n";
    
    // Test case 5: Single element
    vector<int> nums5 = {1};
    cout << "Input: nums = ";
    printVector(nums5);
    cout << "\nOutput: " << (solution.containsDuplicate(nums5) ? "true" : "false") << endl;
    cout << "Expected: false\n\n";
    
    // Compare different approaches
    vector<int> nums6 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 1};
    cout << "Input: nums = ";
    printVector(nums6);
    cout << "\nHash Set: " << (solution.containsDuplicate(nums6) ? "true" : "false");
    
    vector<int> nums6_copy = nums6;
    cout << "\nSorting: " << (solution.containsDuplicateSorting(nums6_copy) ? "true" : "false");
    
    nums6_copy = nums6;
    cout << "\nHashMap: " << (solution.containsDuplicateHashMap(nums6_copy) ? "true" : "false");
    
    nums6_copy = nums6;
    cout << "\nLambda: " << (solution.containsDuplicateLambda(nums6_copy) ? "true" : "false");
    
    cout << "\nExpected: true" << endl;
    
    return 0;
}