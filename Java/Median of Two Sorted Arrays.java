/*
Problem: 4 - Median of Two Sorted Arrays
Difficulty: Hard
Link: https://leetcode.com/problems/median-of-two-sorted-arrays/
Problem Statement:
Given two sorted arrays nums1 and nums2 of size m and n respectively, return 
the median of the two sorted arrays.
The overall run time complexity should be O(log (m+n)).
Approach:
Use Binary Search on the smaller array.
Partition both arrays such that left half and right half have equal elements.
Find median from partition positions.
Time Complexity: O(log(min(m, n)))
Space Complexity: O(1)
*/
import java.util.*;

class Solution {
    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
        // Ensure nums1 is smaller
        if (nums1.length > nums2.length) {
            return findMedianSortedArrays(nums2, nums1);
        }
        
        int m = nums1.length;
        int n = nums2.length;
        int low = 0, high = m;
        
        while (low <= high) {
            int cut1 = (low + high) / 2;  // Partition point in nums1
            int cut2 = (m + n + 1) / 2 - cut1;  // Partition point in nums2
            
            // Edge cases: if partition is at boundary
            int left1 = cut1 == 0 ? Integer.MIN_VALUE : nums1[cut1 - 1];
            int left2 = cut2 == 0 ? Integer.MIN_VALUE : nums2[cut2 - 1];
            int right1 = cut1 == m ? Integer.MAX_VALUE : nums1[cut1];
            int right2 = cut2 == n ? Integer.MAX_VALUE : nums2[cut2];
            
            // Check if partition is valid
            if (left1 <= right2 && left2 <= right1) {
                // If total length is even
                if ((m + n) % 2 == 0) {
                    return (Math.max(left1, left2) + Math.min(right1, right2)) / 2.0;
                } else {
                    // If total length is odd
                    return (double) Math.max(left1, left2);
                }
            } else if (left1 > right2) {
                // Move cut1 to left
                high = cut1 - 1;
            } else {
                // Move cut1 to right
                low = cut1 + 1;
            }
        }
        
        return -1.0;  // Should never reach here
    }
    
    // Test cases
    public static void main(String[] args) {
        Solution sol = new Solution();
        
        // Test 1
        int[] nums1_1 = {1, 3};
        int[] nums2_1 = {2};
        System.out.println("Output: " + sol.findMedianSortedArrays(nums1_1, nums2_1));
        // Expected: 2.0
        
        // Test 2
        int[] nums1_2 = {1, 2};
        int[] nums2_2 = {3, 4};
        System.out.println("Output: " + sol.findMedianSortedArrays(nums1_2, nums2_2));
        // Expected: 2.5
        
        // Test 3
        int[] nums1_3 = {0, 0};
        int[] nums2_3 = {0, 0};
        System.out.println("Output: " + sol.findMedianSortedArrays(nums1_3, nums2_3));
        // Expected: 0.0
        
        // Test 4
        int[] nums1_4 = {};
        int[] nums2_4 = {1};
        System.out.println("Output: " + sol.findMedianSortedArrays(nums1_4, nums2_4));
        // Expected: 1.0
        
        // Test 5
        int[] nums1_5 = {2};
        int[] nums2_5 = {};
        System.out.println("Output: " + sol.findMedianSortedArrays(nums1_5, nums2_5));
        // Expected: 2.0
    }
}