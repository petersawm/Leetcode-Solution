/*
Problem: 4 - Median of Two Sorted Arrays
Difficulty: Hard
Link: https://leetcode.com/problems/median-of-two-sorted-arrays/

Problem Statement:
Given two sorted arrays nums1 and nums2, return the median of the two sorted arrays.
The overall run time complexity should be O(log (m+n)).

Approach:
Use Binary Search on the smaller array to find correct partition.

Time Complexity: O(log(min(m,n))) - Binary search on smaller array
Space Complexity: O(1) - Only using pointers
*/

class Solution {
    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
        // Ensure nums1 is the smaller array
        if (nums1.length > nums2.length) {
            return findMedianSortedArrays(nums2, nums1);
        }
        
        int m = nums1.length;
        int n = nums2.length;
        int left = 0, right = m;
        
        while (left <= right) {
            // Partition nums1
            int partition1 = (left + right) / 2;
            // Partition nums2
            int partition2 = (m + n + 1) / 2 - partition1;
            
            // Get max of left and min of right for both arrays
            int maxLeft1 = (partition1 == 0) ? Integer.MIN_VALUE : nums1[partition1 - 1];
            int minRight1 = (partition1 == m) ? Integer.MAX_VALUE : nums1[partition1];
            
            int maxLeft2 = (partition2 == 0) ? Integer.MIN_VALUE : nums2[partition2 - 1];
            int minRight2 = (partition2 == n) ? Integer.MAX_VALUE : nums2[partition2];
            
            // Check if we found the correct partition
            if (maxLeft1 <= minRight2 && maxLeft2 <= minRight1) {
                // Found correct partition
                if ((m + n) % 2 == 0) {
                    // Even number of elements
                    return (Math.max(maxLeft1, maxLeft2) + Math.min(minRight1, minRight2)) / 2.0;
                } else {
                    // Odd number of elements
                    return Math.max(maxLeft1, maxLeft2);
                }
            } else if (maxLeft1 > minRight2) {
                // Too far right in nums1
                right = partition1 - 1;
            } else {
                // Too far left in nums1
                left = partition1 + 1;
            }
        }
        
        return 0.0;
    }
    
    // Alternative: Merge approach
    public double findMedianSortedArraysMerge(int[] nums1, int[] nums2) {
        int m = nums1.length;
        int n = nums2.length;
        int[] merged = new int[m + n];
        
        int i = 0, j = 0, k = 0;
        
        // Merge two sorted arrays
        while (i < m && j < n) {
            if (nums1[i] <= nums2[j]) {
                merged[k++] = nums1[i++];
            } else {
                merged[k++] = nums2[j++];
            }
        }
        
        // Add remaining elements
        while (i < m) {
            merged[k++] = nums1[i++];
        }
        while (j < n) {
            merged[k++] = nums2[j++];
        }
        
        // Find median
        int total = m + n;
        if (total % 2 == 0) {
            return (merged[total / 2 - 1] + merged[total / 2]) / 2.0;
        } else {
            return merged[total / 2];
        }
    }
    
    // Space-optimized approach
    public double findMedianSortedArraysOptimized(int[] nums1, int[] nums2) {
        int m = nums1.length;
        int n = nums2.length;
        int total = m + n;
        int target = total / 2;
        
        int i = 0, j = 0;
        int prev = 0, curr = 0;
        
        // Iterate until we reach median position(s)
        for (int count = 0; count <= target; count++) {
            prev = curr;
            
            if (i < m && (j >= n || nums1[i] <= nums2[j])) {
                curr = nums1[i++];
            } else {
                curr = nums2[j++];
            }
        }
        
        if (total % 2 == 0) {
            return (prev + curr) / 2.0;
        } else {
            return curr;
        }
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
        int[] nums1 = {1, 3};
        int[] nums2 = {2};
        System.out.print("Input: nums1 = ");
        printArray(nums1);
        System.out.print(", nums2 = ");
        printArray(nums2);
        System.out.println("\nOutput: " + solution.findMedianSortedArrays(nums1, nums2));
        System.out.println("Expected: 2.0\n");
        
        // Test case 2
        int[] nums1_2 = {1, 2};
        int[] nums2_2 = {3, 4};
        System.out.print("Input: nums1 = ");
        printArray(nums1_2);
        System.out.print(", nums2 = ");
        printArray(nums2_2);
        System.out.println("\nOutput: " + solution.findMedianSortedArrays(nums1_2, nums2_2));
        System.out.println("Expected: 2.5\n");
        
        // Test case 3
        int[] nums1_3 = {};
        int[] nums2_3 = {1};
        System.out.print("Input: nums1 = ");
        printArray(nums1_3);
        System.out.print(", nums2 = ");
        printArray(nums2_3);
        System.out.println("\nOutput: " + solution.findMedianSortedArrays(nums1_3, nums2_3));
        System.out.println("Expected: 1.0\n");
        
        // Compare approaches
        int[] nums1_4 = {1, 3};
        int[] nums2_4 = {2, 4, 5};
        System.out.print("Input: nums1 = ");
        printArray(nums1_4);
        System.out.print(", nums2 = ");
        printArray(nums2_4);
        System.out.println("\nBinary Search: " + solution.findMedianSortedArrays(nums1_4, nums2_4));
        System.out.println("Merge: " + solution.findMedianSortedArraysMerge(nums1_4, nums2_4));
        System.out.println("Optimized: " + solution.findMedianSortedArraysOptimized(nums1_4, nums2_4));
        System.out.println("Expected: 3.0");
    }
}