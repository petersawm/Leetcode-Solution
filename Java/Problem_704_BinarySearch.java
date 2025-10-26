/*
Problem: 704 - Binary Search
Difficulty: Easy
Link: https://leetcode.com/problems/binary-search/

Problem Statement:
Given an array of integers nums which is sorted in ascending order, and an integer target,
write a function to search target in nums. If target exists, then return its index.
Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.

Approach:
Classic Binary Search:
1. Use two pointers: left and right
2. Calculate middle index: mid = (left + right) / 2
3. If nums[mid] == target, return mid
4. If nums[mid] < target, search right half (left = mid + 1)
5. If nums[mid] > target, search left half (right = mid - 1)
6. Repeat until left > right

Time Complexity: O(log N) - Halves search space each iteration
Space Complexity: O(1) - Only using pointers
*/

class Solution {
    // Approach 1: Iterative binary search
    public int search(int[] nums, int target) {
        int left = 0;
        int right = nums.length - 1;
        
        while (left <= right) {
            // Calculate middle index (avoid overflow)
            int mid = left + (right - left) / 2;
            
            if (nums[mid] == target) {
                return mid;
            } else if (nums[mid] < target) {
                // Search right half
                left = mid + 1;
            } else {
                // Search left half
                right = mid - 1;
            }
        }
        
        // Target not found
        return -1;
    }
    
    // Approach 2: Recursive binary search
    public int searchRecursive(int[] nums, int target) {
        return binarySearchHelper(nums, target, 0, nums.length - 1);
    }
    
    private int binarySearchHelper(int[] nums, int target, int left, int right) {
        if (left > right) {
            return -1;
        }
        
        int mid = left + (right - left) / 2;
        
        if (nums[mid] == target) {
            return mid;
        } else if (nums[mid] < target) {
            return binarySearchHelper(nums, target, mid + 1, right);
        } else {
            return binarySearchHelper(nums, target, left, mid - 1);
        }
    }
    
    // Approach 3: Alternative template (easier for complex variants)
    public int searchTemplate(int[] nums, int target) {
        if (nums == null || nums.length == 0) {
            return -1;
        }
        
        int left = 0;
        int right = nums.length - 1;
        
        while (left < right) {
            int mid = left + (right - left) / 2;
            
            if (nums[mid] < target) {
                left = mid + 1;
            } else {
                right = mid;
            }
        }
        
        // Check if target is found
        return nums[left] == target ? left : -1;
    }
    
    // Approach 4: Using Arrays.binarySearch
    public int searchBuiltIn(int[] nums, int target) {
        int result = java.util.Arrays.binarySearch(nums, target);
        return result >= 0 ? result : -1;
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
        int[] nums1 = {-1, 0, 3, 5, 9, 12};
        int target1 = 9;
        System.out.print("Input: nums = ");
        printArray(nums1);
        System.out.println(", target = " + target1);
        System.out.println("Output: " + solution.search(nums1, target1));
        System.out.println("Expected: 4\n");
        
        // Test case 2
        int[] nums2 = {-1, 0, 3, 5, 9, 12};
        int target2 = 2;
        System.out.print("Input: nums = ");
        printArray(nums2);
        System.out.println(", target = " + target2);
        System.out.println("Output: " + solution.search(nums2, target2));
        System.out.println("Expected: -1\n");
        
        // Test case 3: Single element - found
        int[] nums3 = {5};
        int target3 = 5;
        System.out.print("Input: nums = ");
        printArray(nums3);
        System.out.println(", target = " + target3);
        System.out.println("Output: " + solution.search(nums3, target3));
        System.out.println("Expected: 0\n");
        
        // Test case 4: Single element - not found
        int[] nums4 = {5};
        int target4 = 3;
        System.out.print("Input: nums = ");
        printArray(nums4);
        System.out.println(", target = " + target4);
        System.out.println("Output: " + solution.search(nums4, target4));
        System.out.println("Expected: -1\n");
        
        // Test case 5: Compare approaches
        int[] nums5 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
        int target5 = 1;
        System.out.print("Input: nums = ");
        printArray(nums5);
        System.out.println(", target = " + target5);
        System.out.println("Iterative: " + solution.search(nums5, target5));
        System.out.println("Recursive: " + solution.searchRecursive(nums5, target5));
        System.out.println("Template: " + solution.searchTemplate(nums5, target5));
        System.out.println("Built-in: " + solution.searchBuiltIn(nums5, target5));
        System.out.println("Expected: 0");
    }
}