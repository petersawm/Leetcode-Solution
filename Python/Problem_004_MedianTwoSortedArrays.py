"""
Problem: 4 - Median of Two Sorted Arrays
Difficulty: Hard
Link: https://leetcode.com/problems/median-of-two-sorted-arrays/

Problem Statement:
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the 
median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

Approach:
Use Binary Search on the smaller array:
1. Partition both arrays such that left half has same elements as right half
2. Find correct partition using binary search
3. Median is calculated from elements around partition

Key insight: 
- If total elements is odd, median = max(left side)
- If even, median = (max(left) + min(right)) / 2

Time Complexity: O(log(min(m,n))) - Binary search on smaller array
Space Complexity: O(1) - Only using pointers
"""

from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        """Binary search approach - optimal"""
        # Ensure nums1 is the smaller array
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        m, n = len(nums1), len(nums2)
        left, right = 0, m
        
        while left <= right:
            # Partition nums1
            partition1 = (left + right) // 2
            # Partition nums2 (to ensure equal halves)
            partition2 = (m + n + 1) // 2 - partition1
            
            # Get max of left and min of right for both arrays
            maxLeft1 = float('-inf') if partition1 == 0 else nums1[partition1 - 1]
            minRight1 = float('inf') if partition1 == m else nums1[partition1]
            
            maxLeft2 = float('-inf') if partition2 == 0 else nums2[partition2 - 1]
            minRight2 = float('inf') if partition2 == n else nums2[partition2]
            
            # Check if we found the correct partition
            if maxLeft1 <= minRight2 and maxLeft2 <= minRight1:
                # Found correct partition
                if (m + n) % 2 == 0:
                    # Even number of elements
                    return (max(maxLeft1, maxLeft2) + min(minRight1, minRight2)) / 2
                else:
                    # Odd number of elements
                    return max(maxLeft1, maxLeft2)
            elif maxLeft1 > minRight2:
                # Too far right in nums1, move left
                right = partition1 - 1
            else:
                # Too far left in nums1, move right
                left = partition1 + 1
        
        return 0.0
    
    # Alternative: Merge approach (not optimal but easier to understand)
    def findMedianSortedArraysMerge(self, nums1: List[int], nums2: List[int]) -> float:
        """Merge arrays approach - O(m+n) time"""
        merged = []
        i, j = 0, 0
        
        # Merge two sorted arrays
        while i < len(nums1) and j < len(nums2):
            if nums1[i] <= nums2[j]:
                merged.append(nums1[i])
                i += 1
            else:
                merged.append(nums2[j])
                j += 1
        
        # Add remaining elements
        merged.extend(nums1[i:])
        merged.extend(nums2[j:])
        
        # Find median
        n = len(merged)
        if n % 2 == 0:
            return (merged[n // 2 - 1] + merged[n // 2]) / 2
        else:
            return merged[n // 2]
    
    # Space-optimized merge (don't need full array)
    def findMedianSortedArraysOptimized(self, nums1: List[int], nums2: List[int]) -> float:
        """Only track elements needed for median"""
        m, n = len(nums1), len(nums2)
        total = m + n
        target = total // 2
        
        i, j = 0, 0
        prev, curr = 0, 0
        
        # Iterate until we reach median position(s)
        for _ in range(target + 1):
            prev = curr
            
            if i < m and (j >= n or nums1[i] <= nums2[j]):
                curr = nums1[i]
                i += 1
            else:
                curr = nums2[j]
                j += 1
        
        if total % 2 == 0:
            return (prev + curr) / 2
        else:
            return curr


# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1
    nums1 = [1, 3]
    nums2 = [2]
    print(f"Input: nums1 = {nums1}, nums2 = {nums2}")
    print(f"Output: {solution.findMedianSortedArrays(nums1, nums2)}")
    print(f"Expected: 2.0 (merged: [1,2,3], median is 2)\n")
    
    # Test case 2
    nums1_2 = [1, 2]
    nums2_2 = [3, 4]
    print(f"Input: nums1 = {nums1_2}, nums2 = {nums2_2}")
    print(f"Output: {solution.findMedianSortedArrays(nums1_2, nums2_2)}")
    print(f"Expected: 2.5 (merged: [1,2,3,4], median is (2+3)/2)\n")
    
    # Test case 3: One empty array
    nums1_3 = []
    nums2_3 = [1]
    print(f"Input: nums1 = {nums1_3}, nums2 = {nums2_3}")
    print(f"Output: {solution.findMedianSortedArrays(nums1_3, nums2_3)}")
    print(f"Expected: 1.0\n")
    
    # Test case 4: Different sizes
    nums1_4 = [1, 3, 5, 7, 9]
    nums2_4 = [2, 4, 6]
    print(f"Input: nums1 = {nums1_4}, nums2 = {nums2_4}")
    print(f"Output: {solution.findMedianSortedArrays(nums1_4, nums2_4)}")
    print(f"Expected: 5.0\n")
    
    # Compare approaches
    nums1_5 = [1, 3]
    nums2_5 = [2, 4, 5]
    print(f"Input: nums1 = {nums1_5}, nums2 = {nums2_5}")
    print(f"Binary Search: {solution.findMedianSortedArrays(nums1_5, nums2_5)}")
    print(f"Merge: {solution.findMedianSortedArraysMerge(nums1_5, nums2_5)}")
    print(f"Optimized: {solution.findMedianSortedArraysOptimized(nums1_5, nums2_5)}")
    print(f"Expected: 3.0")