/*
Problem: 312 - Burst Balloons
Difficulty: Hard
Link: https://leetcode.com/problems/burst-balloons/
Problem Statement:
You are given n balloons, indexed from 0 to n - 1. Each balloon is painted with 
a number on it represented by an array nums. You are asked to burst all the 
balloons.
If the you burst balloon i you will get nums[left] * nums[i] * nums[right] coins. 
Here left and right are adjacent indices of i after all balloons between them 
have burst.
Find the maximum coins you can collect by bursting all balloons wisely.
Approach:
Use Dynamic Programming with reverse thinking.
Instead of thinking which balloon to burst first, think which balloon to burst last.
dp[left][right] = max coins bursting all balloons between left and right
Add padding 1s at boundaries to simplify edge cases.
Time Complexity: O(N^3)
Space Complexity: O(N^2)
*/
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    int maxCoins(vector<int>& nums) {
        int n = nums.size();
        
        // Create new array with padding 1s
        vector<int> balloons(n + 2);
        balloons[0] = 1;
        balloons[n + 1] = 1;
        for (int i = 0; i < n; i++) {
            balloons[i + 1] = nums[i];
        }
        
        // dp[left][right] = max coins bursting balloons between left and right
        vector<vector<int>> dp(n + 2, vector<int>(n + 2, 0));
        
        // Fill DP table
        // len is the distance between left and right
        for (int len = 2; len <= n + 1; len++) {
            for (int left = 0; left + len - 1 <= n + 1; left++) {
                int right = left + len - 1;
                
                // Try bursting each balloon between left and right as last
                for (int k = left + 1; k < right; k++) {
                    // Coins from bursting balloons between left and k, plus k, plus balloons between k and right
                    int coins = dp[left][k] + balloons[left] * balloons[k] * balloons[right] + dp[k][right];
                    dp[left][right] = max(dp[left][right], coins);
                }
            }
        }
        
        return dp[0][n + 1];
    }
};

// Test cases
int main() {
    Solution sol;
    
    // Test 1
    vector<int> nums1 = {3, 1, 5, 8};
    cout << "Output: " << sol.maxCoins(nums1) << endl;
    // Expected: 167
    
    // Test 2
    vector<int> nums2 = {1, 5};
    cout << "Output: " << sol.maxCoins(nums2) << endl;
    // Expected: 10
    
    // Test 3
    vector<int> nums3 = {9, 76, 64, 21, 97, 60};
    cout << "Output: " << sol.maxCoins(nums3) << endl;
    
    // Test 4
    vector<int> nums4 = {3};
    cout << "Output: " << sol.maxCoins(nums4) << endl;
    // Expected: 3
    
    return 0;
}