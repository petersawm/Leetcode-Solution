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

import java.util.*;

class Solution {
    // Approach 1: Space-optimized DP
    public int rob(int[] nums) {
        if (nums == null || nums.length == 0) {
            return 0;
        }
        if (nums.length == 1) {
            return nums[0];
        }
        
        int prev2 = 0;  // Max money robbed 2 houses ago
        int prev1 = nums[0];  // Max money robbed 1 house ago
        
        for (int i = 1; i < nums.length; i++) {
            int current = Math.max(prev1, prev2 + nums[i]);
            prev2 = prev1;
            prev1 = current;
        }
        
        return prev1;
    }
    
    // Approach 2: DP with array
    public int robDP(int[] nums) {
        if (nums.length == 0) {
            return 0;
        }
        if (nums.length == 1) {
            return nums[0];
        }
        
        int n = nums.length;
        int[] dp = new int[n];
        dp[0] = nums[0];
        dp[1] = Math.max(nums[0], nums[1]);
        
        for (int i = 2; i < n; i++) {
            dp[i] = Math.max(dp[i-1], dp[i-2] + nums[i]);
        }
        
        return dp[n-1];
    }
    
    // Approach 3: Recursive with memoization
    public int robMemo(int[] nums) {
        Map<Integer, Integer> memo = new HashMap<>();
        return helper(nums, nums.length - 1, memo);
    }
    
    private int helper(int[] nums, int i, Map<Integer, Integer> memo) {
        if (i < 0) {
            return 0;
        }
        if (memo.containsKey(i)) {
            return memo.get(i);
        }
        
        int result = Math.max(helper(nums, i-1, memo), 
                             helper(nums, i-2, memo) + nums[i]);
        memo.put(i, result);
        return result;
    }
    
    // Approach 4: Clear variable naming
    public int robClear(int[] nums) {
        if (nums.length == 0) {
            return 0;
        }
        if (nums.length == 1) {
            return nums[0];
        }
        
        int robPrevPrev = 0;
        int robPrev = nums[0];
        
        for (int i = 1; i < nums.length; i++) {
            int robCurrent = Math.max(robPrev, robPrevPrev + nums[i]);
            robPrevPrev = robPrev;
            robPrev = robCurrent;
        }
        
        return robPrev;
    }
    
    // Helper method to print array
    private static void printArray(int[] arr) {
        System.out.print("[");
        for (int i = 0; i < arr.length; i++) {
            System.out.print(arr[i]);
            if (i < arr.length - 1) {
                System.out.print(",");
            }
        }
        System.out.print("]");
    }
    
    // Test cases
    public static void main(String[] args) {
        Solution solution = new Solution();
        
        // Test case 1
        int[] nums1 = {1, 2, 3, 1};
        System.out.print("Input: nums = ");
        printArray(nums1);
        System.out.println("\nOutput: " + solution.rob(nums1));
        System.out.println("Expected: 4\n");
        
        // Test case 2
        int[] nums2 = {2, 7, 9, 3, 1};
        System.out.print("Input: nums = ");
        printArray(nums2);
        System.out.println("\nOutput: " + solution.rob(nums2));
        System.out.println("Expected: 12\n");
        
        // Test case 3
        int[] nums3 = {5};
        System.out.print("Input: nums = ");
        printArray(nums3);
        System.out.println("\nOutput: " + solution.rob(nums3));
        System.out.println("Expected: 5\n");
        
        // Test case 4
        int[] nums4 = {2, 1};
        System.out.print("Input: nums = ");
        printArray(nums4);
        System.out.println("\nOutput: " + solution.rob(nums4));
        System.out.println("Expected: 2\n");
        
        // Compare approaches
        int[] nums5 = {2, 7, 9, 3, 1};
        System.out.print("Input: nums = ");
        printArray(nums5);
        System.out.println("\nOptimized: " + solution.rob(nums5));
        System.out.println("DP Array: " + solution.robDP(nums5));
        System.out.println("Memoization: " + solution.robMemo(nums5));
        System.out.println("Clear Naming: " + solution.robClear(nums5));
        System.out.println("Expected: 12");
    }
}