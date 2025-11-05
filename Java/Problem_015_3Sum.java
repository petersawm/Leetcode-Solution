/*
Problem: 15 - 3Sum
Difficulty: Medium
Link: https://leetcode.com/problems/3sum/

Problem Statement:
Return all triplets [nums[i], nums[j], nums[k]] such that nums[i] + nums[j] + nums[k] == 0.
The solution set must not contain duplicate triplets.

Approach:
Sort + Two Pointers - O(N²) time

Time Complexity: O(N²)
Space Complexity: O(1) or O(N) for sorting
*/

import java.util.*;

class Solution {
    // Approach 1: Sort + Two Pointers
    public List<List<Integer>> threeSum(int[] nums) {
        Arrays.sort(nums);
        List<List<Integer>> result = new ArrayList<>();
        int n = nums.length;
        
        for (int i = 0; i < n - 2; i++) {
            // Skip duplicates for first element
            if (i > 0 && nums[i] == nums[i - 1]) {
                continue;
            }
            
            // Two pointers for remaining elements
            int left = i + 1, right = n - 1;
            int target = -nums[i];
            
            while (left < right) {
                int currentSum = nums[left] + nums[right];
                
                if (currentSum == target) {
                    result.add(Arrays.asList(nums[i], nums[left], nums[right]));
                    
                    // Skip duplicates for second element
                    while (left < right && nums[left] == nums[left + 1]) {
                        left++;
                    }
                    // Skip duplicates for third element
                    while (left < right && nums[right] == nums[right - 1]) {
                        right--;
                    }
                    
                    left++;
                    right--;
                } else if (currentSum < target) {
                    left++;
                } else {
                    right--;
                }
            }
        }
        
        return result;
    }
    
    // Approach 2: Using HashSet to avoid duplicates
    public List<List<Integer>> threeSumSet(int[] nums) {
        Arrays.sort(nums);
        Set<List<Integer>> result = new HashSet<>();
        int n = nums.length;
        
        for (int i = 0; i < n - 2; i++) {
            int left = i + 1, right = n - 1;
            
            while (left < right) {
                int sum = nums[i] + nums[left] + nums[right];
                
                if (sum == 0) {
                    result.add(Arrays.asList(nums[i], nums[left], nums[right]));
                    left++;
                    right--;
                } else if (sum < 0) {
                    left++;
                } else {
                    right--;
                }
            }
        }
        
        return new ArrayList<>(result);
    }
    
    // Approach 3: Hash Map approach
    public List<List<Integer>> threeSumHashMap(int[] nums) {
        Set<List<Integer>> result = new HashSet<>();
        int n = nums.length;
        
        for (int i = 0; i < n - 1; i++) {
            Set<Integer> seen = new HashSet<>();
            for (int j = i + 1; j < n; j++) {
                int complement = -nums[i] - nums[j];
                if (seen.contains(complement)) {
                    List<Integer> triplet = Arrays.asList(nums[i], nums[j], complement);
                    Collections.sort(triplet);
                    result.add(triplet);
                }
                seen.add(nums[j]);
            }
        }
        
        return new ArrayList<>(result);
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
        int[] nums1 = {-1, 0, 1, 2, -1, -4};
        System.out.print("Input: nums = ");
        printArray(nums1);
        System.out.println("\nOutput: " + solution.threeSum(nums1));
        System.out.println("Expected: [[-1,-1,2],[-1,0,1]]\n");
        
        // Test case 2
        int[] nums2 = {0, 1, 1};
        System.out.print("Input: nums = ");
        printArray(nums2);
        System.out.println("\nOutput: " + solution.threeSum(nums2));
        System.out.println("Expected: []\n");
        
        // Test case 3
        int[] nums3 = {0, 0, 0};
        System.out.print("Input: nums = ");
        printArray(nums3);
        System.out.println("\nOutput: " + solution.threeSum(nums3));
        System.out.println("Expected: [[0,0,0]]\n");
        
        // Test case 4
        int[] nums4 = {-2, 0, 0, 2, 2};
        System.out.print("Input: nums = ");
        printArray(nums4);
        System.out.println("\nOutput: " + solution.threeSum(nums4));
        System.out.println("Expected: [[-2,0,2]]\n");
        
        // Compare approaches
        int[] nums5 = {-1, 0, 1, 2, -1, -4};
        System.out.print("Input: nums = ");
        printArray(nums5);
        System.out.println("\nTwo Pointers: " + solution.threeSum(nums5.clone()));
        System.out.println("Using Set: " + solution.threeSumSet(nums5.clone()));
        System.out.println("Hash Map: " + solution.threeSumHashMap(nums5.clone()));
    }
}