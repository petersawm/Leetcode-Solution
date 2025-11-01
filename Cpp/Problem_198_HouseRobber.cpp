/*
Problem: 198 - House Robber
Difficulty: Medium
Link: https://leetcode.com/problems/house-robber/

Problem Statement:
Given an integer array nums representing the amount of money of each house, return the 
maximum amount of money you can rob tonight without alerting the police (can't rob 
adjacent houses).

Approach:
Dynamic Programming: dp[i] = max(dp[i-1], dp[i-2] + nums[i])

Time Complexity: O(N) - Single pass through array
Space Complexity: O(1) - Only using two variables
*/

#include <vector>
#include <iostream>
#include <algorithm>
#include <unordered_map>

using namespace std;

class Solution {
public:
    // Approach 1: Space-optimized DP
    int rob(vector<int>& nums) {
        if (nums.empty()) {
            return 0;
        }
        if (nums.size() == 1) {
            return nums[0];
        }
        
        int prev2 = 0;  // Max money robbed 2 houses ago
        int prev1 = nums[0];  // Max money robbed 1 house ago
        
        for (int i = 1; i < nums.size(); i++) {
            int current = max(prev1, prev2 + nums[i]);
            prev2 = prev1;
            prev1 = current;
        }
        
        return prev1;
    }
    
    // Approach 2: DP with array
    int robDP(vector<int>& nums) {
        if (nums.empty()) {
            return 0;
        }
        if (nums.size() == 1) {
            return nums[0];
        }
        
        int n = nums.size();
        vector<int> dp(n);
        dp[0] = nums[0];
        dp[1] = max(nums[0], nums[1]);
        
        for (int i = 2; i < n; i++) {
            dp[i] = max(dp[i-1], dp[i-2] + nums[i]);
        }
        
        return dp[n-1];
    }
    
    // Approach 3: Recursive with memoization
    int robMemo(vector<int>& nums) {
        unordered_map<int, int> memo;
        return helper(nums, nums.size() - 1, memo);
    }
    
private:
    int helper(vector<int>& nums, int i, unordered_map<int, int>& memo) {
        if (i < 0) {
            return 0;
        }
        if (memo.find(i) != memo.end()) {
            return memo[i];
        }
        
        memo[i] = max(helper(nums, i-1, memo), 
                     helper(nums, i-2, memo) + nums[i]);
        return memo[i];
    }
    
public:
    // Approach 4: Clear variable naming
    int robClear(vector<int>& nums) {
        if (nums.empty()) {
            return 0;
        }
        if (nums.size() == 1) {
            return nums[0];
        }
        
        int robPrevPrev = 0;
        int robPrev = nums[0];
        
        for (int i = 1; i < nums.size(); i++) {
            int robCurrent = max(robPrev, robPrevPrev + nums[i]);
            robPrevPrev = robPrev;
            robPrev = robCurrent;
        }
        
        return robPrev;
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
    cout << "\nOutput: " << solution.rob(nums1) << endl;
    cout << "Expected: 4\n" << endl;
    
    // Test case 2
    vector<int> nums2 = {2, 7, 9, 3, 1};
    cout << "Input: nums = ";
    printVector(nums2);
    cout << "\nOutput: " << solution.rob(nums2) << endl;
    cout << "Expected: 12\n" << endl;
    
    // Test case 3
    vector<int> nums3 = {5};
    cout << "Input: nums = ";
    printVector(nums3);
    cout << "\nOutput: " << solution.rob(nums3) << endl;
    cout << "Expected: 5\n" << endl;
    
    // Test case 4
    vector<int> nums4 = {2, 1};
    cout << "Input: nums = ";
    printVector(nums4);
    cout << "\nOutput: " << solution.rob(nums4) << endl;
    cout << "Expected: 2\n" << endl;
    
    // Compare approaches
    vector<int> nums5 = {2, 7, 9, 3, 1};
    cout << "Input: nums = ";
    printVector(nums5);
    cout << "\nOptimized: " << solution.rob(nums5) << endl;
    cout << "DP Array: " << solution.robDP(nums5) << endl;
    cout << "Memoization: " << solution.robMemo(nums5) << endl;
    cout << "Clear Naming: " << solution.robClear(nums5) << endl;
    cout << "Expected: 12" << endl;
    
    return 0;
}