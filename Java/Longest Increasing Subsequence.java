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
import java.util.*;

class Solution {
    // Approach 1: Dynamic Programming O(N^2)
    public int lengthOfLIS_DP(int[] nums) {
        int n = nums.length;
        int[] dp = new int[n];
        
        // Base case: each element is LIS of length 1
        Arrays.fill(dp, 1);
        
        // Fill dp array
        for (int i = 1; i < n; i++) {
            for (int j = 0; j < i; j++) {
                if (nums[j] < nums[i]) {
                    dp[i] = Math.max(dp[i], dp[j] + 1);
                }
            }
        }
        
        // Return max value in dp
        int maxLength = 0;
        for (int len : dp) {
            maxLength = Math.max(maxLength, len);
        }
        
        return maxLength;
    }
    
    // Approach 2: Binary Search O(N log N)
    public int lengthOfLIS_BinarySearch(int[] nums) {
        List<Integer> tails = new ArrayList<>();
        
        for (int num : nums) {
            // Find position using binary search
            int pos = Collections.binarySearch(tails, num);
            
            // If not found, pos = -(insertion point) - 1
            if (pos < 0) {
                pos = -(pos + 1);
            }
            
            // Add or replace
            if (pos == tails.size()) {
                tails.add(num);
            } else {
                tails.set(pos, num);
            }
        }
        
        return tails.size();
    }
    
    // Test cases
    public static void main(String[] args) {
        Solution sol = new Solution();
        
        // Test 1
        int[] nums1 = {10, 9, 2, 5, 3, 7, 101, 18};
        System.out.println("DP: " + sol.lengthOfLIS_DP(nums1));
        System.out.println("BinarySearch: " + sol.lengthOfLIS_BinarySearch(nums1));
        // Expected: 4 (LIS: [2, 3, 7, 101])
        
        // Test 2
        int[] nums2 = {0, 1, 0, 4, 4, 4, 3, 2, 1};
        System.out.println("DP: " + sol.lengthOfLIS_DP(nums2));
        System.out.println("BinarySearch: " + sol.lengthOfLIS_BinarySearch(nums2));
        // Expected: 2 (LIS: [0, 1])
        
        // Test 3
        int[] nums3 = {1, 2, 3, 4, 5};
        System.out.println("DP: " + sol.lengthOfLIS_DP(nums3));
        System.out.println("BinarySearch: " + sol.lengthOfLIS_BinarySearch(nums3));
        // Expected: 5
        
        // Test 4
        int[] nums4 = {5, 4, 3, 2, 1};
        System.out.println("DP: " + sol.lengthOfLIS_DP(nums4));
        System.out.println("BinarySearch: " + sol.lengthOfLIS_BinarySearch(nums4));
        // Expected: 1
    }
}