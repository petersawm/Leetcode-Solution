/*
Problem: 300 - Longest Increasing Subsequence
Difficulty: Medium
Link: https://leetcode.com/problems/longest-increasing-subsequence/
Problem Statement:
Given an integer array nums, return the length of the longest strictly 
increasing subsequence.
Approach 1: Dynamic Programming
dp[i] = length of LIS ending at index i
For each i, check all j < i where nums[j] < nums[i]
Time Complexity: O(N^2)
Space Complexity: O(N)

Approach 2: Binary Search (Optimal)
Maintain sorted list of smallest tail elements for each LIS length
Use binary search to find position to update
Time Complexity: O(N log N)
Space Complexity: O(N)
*/
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    // Approach 1: Dynamic Programming O(N^2)
    int lengthOfLIS_DP(vector<int>& nums) {
        int n = nums.size();
        vector<int> dp(n, 1);
        
        // Fill dp array
        for (int i = 1; i < n; i++) {
            for (int j = 0; j < i; j++) {
                if (nums[j] < nums[i]) {
                    dp[i] = max(dp[i], dp[j] + 1);
                }
            }
        }
        
        // Return max value in dp
        return *max_element(dp.begin(), dp.end());
    }
    
    // Approach 2: Binary Search O(N log N)
    int lengthOfLIS_BinarySearch(vector<int>& nums) {
        vector<int> tails;
        
        for (int num : nums) {
            // Find position using binary search
            auto it = lower_bound(tails.begin(), tails.end(), num);
            
            // Add or replace
            if (it == tails.end()) {
                tails.push_back(num);
            } else {
                *it = num;
            }
        }
        
        return tails.size();
    }
};

// Test cases
int main() {
    Solution sol;
    
    // Test 1
    vector<int> nums1 = {10, 9, 2, 5, 3, 7, 101, 18};
    cout << "DP: " << sol.lengthOfLIS_DP(nums1) << endl;
    cout << "BinarySearch: " << sol.lengthOfLIS_BinarySearch(nums1) << endl;
    // Expected: 4 (LIS: [2, 3, 7, 101])
    
    // Test 2
    vector<int> nums2 = {0, 1, 0, 4, 4, 4, 3, 2, 1};
    cout << "DP: " << sol.lengthOfLIS_DP(nums2) << endl;
    cout << "BinarySearch: " << sol.lengthOfLIS_BinarySearch(nums2) << endl;
    // Expected: 2 (LIS: [0, 1])
    
    // Test 3
    vector<int> nums3 = {1, 2, 3, 4, 5};
    cout << "DP: " << sol.lengthOfLIS_DP(nums3) << endl;
    cout << "BinarySearch: " << sol.lengthOfLIS_BinarySearch(nums3) << endl;
    // Expected: 5
    
    // Test 4
    vector<int> nums4 = {5, 4, 3, 2, 1};
    cout << "DP: " << sol.lengthOfLIS_DP(nums4) << endl;
    cout << "BinarySearch: " << sol.lengthOfLIS_BinarySearch(nums4) << endl;
    // Expected: 1
    
    return 0;
}