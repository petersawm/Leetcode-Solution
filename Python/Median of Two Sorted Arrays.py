"""
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
"""

class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        # Ensure nums1 is smaller
        if len(nums1) > len(nums2):
            return self.findMedianSortedArrays(nums2, nums1)
        
        m = len(nums1)
        n = len(nums2)
        low = 0
        high = m
        
        while low <= high:
            cut1 = (low + high) // 2  # Partition point in nums1
            cut2 = (m + n + 1) // 2 - cut1  # Partition point in nums2
            
            # Edge cases: if partition is at boundary
            left1 = float('-inf') if cut1 == 0 else nums1[cut1 - 1]
            left2 = float('-inf') if cut2 == 0 else nums2[cut2 - 1]
            right1 = float('inf') if cut1 == m else nums1[cut1]
            right2 = float('inf') if cut2 == n else nums2[cut2]
            
            # Check if partition is valid
            if left1 <= right2 and left2 <= right1:
                # If total length is even
                if (m + n) % 2 == 0:
                    return (max(left1, left2) + min(right1, right2)) / 2.0
                else:
                    # If total length is odd
                    return float(max(left1, left2))
            elif left1 > right2:
                # Move cut1 to left
                high = cut1 - 1
            else:
                # Move cut1 to right
                low = cut1 + 1
        
        return -1.0  # Should never reach here


# Test cases
if __name__ == "__main__":
    sol = Solution()
    
    # Test 1
    nums1_1 = [1, 3]
    nums2_1 = [2]
    print("Output:", sol.findMedianSortedArrays(nums1_1, nums2_1))
    # Expected: 2.0
    
    # Test 2
    nums1_2 = [1, 2]
    nums2_2 = [3, 4]
    print("Output:", sol.findMedianSortedArrays(nums1_2, nums2_2))
    # Expected: 2.5
    
    # Test 3
    nums1_3 = [0, 0]
    nums2_3 = [0, 0]
    print("Output:", sol.findMedianSortedArrays(nums1_3, nums2_3))
    # Expected: 0.0
    
    # Test 4
    nums1_4 = []
    nums2_4 = [1]
    print("Output:", sol.findMedianSortedArrays(nums1_4, nums2_4))
    # Expected: 1.0
    
    # Test 5
    nums1_5 = [2]
    nums2_5 = []
    print("Output:", sol.findMedianSortedArrays(nums1_5, nums2_5))
    # Expected: 2.0