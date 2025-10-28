/*
Problem: 1 - Two Sum
Difficulty: Easy
Link: https://leetcode.com/problems/two-sum/

Problem Statement:
Given an array of integers nums and an integer target, return indices of the 
two numbers such that they add up to target.

Approach:
Use HashMap to store complement values and their indices.
For each element, check if (target - current) exists in the map.

Time Complexity: O(N)
Space Complexity: O(N)
*/
import java.util.*;

class Solution {
    public int[] twoSum(int[] nums, int target) {
        // HashMap to store {value: index}
        Map<Integer, Integer> seen = new HashMap<>();
        
        // Iterate through array
        for (int i = 0; i < nums.length; i++) {
            // Calculate complement
            int complement = target - nums[i];
            
            // Check if complement exists
            if (seen.containsKey(complement)) {
                return new int[] {seen.get(complement), i};
            }
            
            // Store current number
            seen.put(nums[i], i);
        }
        
        return new int[] {};
    }
    
    // Test cases
    public static void main(String[] args) {
        Solution sol = new Solution();
        
        // Test 1
        int[] nums1 = {2, 7, 11, 15};
        System.out.println("Output: " + Arrays.toString(sol.twoSum(nums1, 9)));
        // Expected: [0, 1]
        
        // Test 2
        int[] nums2 = {3, 2, 4};
        System.out.println("Output: " + Arrays.toString(sol.twoSum(nums2, 6)));
        // Expected: [1, 2]
    }
}