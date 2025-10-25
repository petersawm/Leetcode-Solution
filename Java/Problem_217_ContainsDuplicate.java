/*
Problem: 217 - Contains Duplicate
Difficulty: Easy
Link: https://leetcode.com/problems/contains-duplicate/

Problem Statement:
Given an integer array nums, return true if any value appears at least twice 
in the array, and return false if every element is distinct.

Approach:
Multiple approaches with different trade-offs:

1. Hash Set - Most efficient
   - Add elements to set while iterating
   - If element already exists, return true
   - Time: O(N), Space: O(N)

2. Sorting
   - Sort array and check adjacent elements
   - Time: O(N log N), Space: O(1) if in-place sort

3. HashMap with counting
   - Count occurrences using HashMap
   - Time: O(N), Space: O(N)

Time Complexity: O(N) - Hash set approach
Space Complexity: O(N) - Hash set storage
*/

import java.util.*;

class Solution {
    // Approach 1: Hash Set - Most efficient
    public boolean containsDuplicate(int[] nums) {
        Set<Integer> seen = new HashSet<>();
        
        for (int num : nums) {
            // If add returns false, element already exists
            if (!seen.add(num)) {
                return true;
            }
        }
        
        return false;
    }
    
    // Alternative hash set implementation
    public boolean containsDuplicateSet(int[] nums) {
        Set<Integer> seen = new HashSet<>();
        
        for (int num : nums) {
            if (seen.contains(num)) {
                return true;
            }
            seen.add(num);
        }
        
        return false;
    }
    
    // Approach 2: Sorting
    public boolean containsDuplicateSorting(int[] nums) {
        if (nums.length < 2) {
            return false;
        }
        
        Arrays.sort(nums);
        
        for (int i = 1; i < nums.length; i++) {
            if (nums[i] == nums[i - 1]) {
                return true;
            }
        }
        
        return false;
    }
    
    // Approach 3: Using HashMap to count occurrences
    public boolean containsDuplicateHashMap(int[] nums) {
        Map<Integer, Integer> countMap = new HashMap<>();
        
        for (int num : nums) {
            countMap.put(num, countMap.getOrDefault(num, 0) + 1);
            
            if (countMap.get(num) > 1) {
                return true;
            }
        }
        
        return false;
    }
    
    // Approach 4: Using Stream API (Java 8+)
    public boolean containsDuplicateStream(int[] nums) {
        return Arrays.stream(nums).distinct().count() != nums.length;
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
        System.out.println("\nOutput: " + solution.containsDuplicate(nums1));
        System.out.println("Expected: true\n");
        
        // Test case 2
        int[] nums2 = {1, 2, 3, 4};
        System.out.print("Input: nums = ");
        printArray(nums2);
        System.out.println("\nOutput: " + solution.containsDuplicate(nums2));
        System.out.println("Expected: false\n");
        
        // Test case 3
        int[] nums3 = {1, 1, 1, 3, 3, 4, 3, 2, 4, 2};
        System.out.print("Input: nums = ");
        printArray(nums3);
        System.out.println("\nOutput: " + solution.containsDuplicate(nums3));
        System.out.println("Expected: true\n");
        
        // Test case 4: Empty array
        int[] nums4 = {};
        System.out.print("Input: nums = ");
        printArray(nums4);
        System.out.println("\nOutput: " + solution.containsDuplicate(nums4));
        System.out.println("Expected: false\n");
        
        // Test case 5: Single element
        int[] nums5 = {1};
        System.out.print("Input: nums = ");
        printArray(nums5);
        System.out.println("\nOutput: " + solution.containsDuplicate(nums5));
        System.out.println("Expected: false\n");
        
        // Compare different approaches
        int[] nums6 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 1};
        System.out.print("Input: nums = ");
        printArray(nums6);
        System.out.println("\nHash Set: " + solution.containsDuplicate(nums6.clone()));
        System.out.println("Sorting: " + solution.containsDuplicateSorting(nums6.clone()));
        System.out.println("HashMap: " + solution.containsDuplicateHashMap(nums6.clone()));
        System.out.println("Stream: " + solution.containsDuplicateStream(nums6.clone()));
        System.out.println("Expected: true");
    }
}