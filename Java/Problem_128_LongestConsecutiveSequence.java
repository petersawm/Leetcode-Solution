/*
Problem: 128 - Longest Consecutive Sequence
Difficulty: Medium
Link: https://leetcode.com/problems/longest-consecutive-sequence/

Problem Statement:
Given an unsorted array of integers nums, return the length of the longest consecutive 
elements sequence. You must write an algorithm that runs in O(n) time.

Approach:
Use Hash Set for O(1) lookups - only count from sequence starts.

Time Complexity: O(N) - Each number visited at most twice
Space Complexity: O(N) - Hash set storage
*/

import java.util.*;

class Solution {
    // Approach 1: Hash Set - O(N) time
    public int longestConsecutive(int[] nums) {
        if (nums == null || nums.length == 0) {
            return 0;
        }
        
        Set<Integer> numSet = new HashSet<>();
        for (int num : nums) {
            numSet.add(num);
        }
        
        int maxLength = 0;
        
        for (int num : numSet) {
            // Only start counting if this is the beginning of a sequence
            if (!numSet.contains(num - 1)) {
                int currentNum = num;
                int currentLength = 1;
                
                // Count consecutive numbers
                while (numSet.contains(currentNum + 1)) {
                    currentNum++;
                    currentLength++;
                }
                
                maxLength = Math.max(maxLength, currentLength);
            }
        }
        
        return maxLength;
    }
    
    // Approach 2: Sorting - O(N log N) time
    public int longestConsecutiveSorting(int[] nums) {
        if (nums.length == 0) {
            return 0;
        }
        
        Arrays.sort(nums);
        int maxLength = 1;
        int currentLength = 1;
        
        for (int i = 1; i < nums.length; i++) {
            // Skip duplicates
            if (nums[i] == nums[i-1]) {
                continue;
            }
            
            // Check if consecutive
            if (nums[i] == nums[i-1] + 1) {
                currentLength++;
            } else {
                maxLength = Math.max(maxLength, currentLength);
                currentLength = 1;
            }
        }
        
        return Math.max(maxLength, currentLength);
    }
    
    // Approach 3: HashMap tracking boundaries
    public int longestConsecutiveHashMap(int[] nums) {
        if (nums.length == 0) {
            return 0;
        }
        
        Map<Integer, Integer> numMap = new HashMap<>();
        int maxLength = 0;
        
        for (int num : nums) {
            if (numMap.containsKey(num)) {
                continue;
            }
            
            // Get lengths of adjacent sequences
            int left = numMap.getOrDefault(num - 1, 0);
            int right = numMap.getOrDefault(num + 1, 0);
            
            // New sequence length
            int length = left + right + 1;
            maxLength = Math.max(maxLength, length);
            
            // Update boundaries
            numMap.put(num, length);
            numMap.put(num - left, length);
            numMap.put(num + right, length);
        }
        
        return maxLength;
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
        int[] nums1 = {100, 4, 200, 1, 3, 2};
        System.out.print("Input: nums = ");
        printArray(nums1);
        System.out.println("\nOutput: " + solution.longestConsecutive(nums1));
        System.out.println("Expected: 4\n");
        
        // Test case 2
        int[] nums2 = {0, 3, 7, 2, 5, 8, 4, 6, 0, 1};
        System.out.print("Input: nums = ");
        printArray(nums2);
        System.out.println("\nOutput: " + solution.longestConsecutive(nums2));
        System.out.println("Expected: 9\n");
        
        // Test case 3
        int[] nums3 = {};
        System.out.print("Input: nums = ");
        printArray(nums3);
        System.out.println("\nOutput: " + solution.longestConsecutive(nums3));
        System.out.println("Expected: 0\n");
        
        // Test case 4
        int[] nums4 = {1};
        System.out.print("Input: nums = ");
        printArray(nums4);
        System.out.println("\nOutput: " + solution.longestConsecutive(nums4));
        System.out.println("Expected: 1\n");
        
        // Test case 5
        int[] nums5 = {1, 2, 0, 1};
        System.out.print("Input: nums = ");
        printArray(nums5);
        System.out.println("\nOutput: " + solution.longestConsecutive(nums5));
        System.out.println("Expected: 3\n");
        
        // Compare approaches
        int[] nums6 = {100, 4, 200, 1, 3, 2};
        System.out.print("Input: nums = ");
        printArray(nums6);
        System.out.println("\nHash Set: " + solution.longestConsecutive(nums6));
        System.out.println("Sorting: " + solution.longestConsecutiveSorting(nums6));
        System.out.println("HashMap: " + solution.longestConsecutiveHashMap(nums6));
        System.out.println("Expected: 4");
    }
}