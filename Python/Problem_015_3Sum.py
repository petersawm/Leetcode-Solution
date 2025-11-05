"""
Problem: 15 - 3Sum
Difficulty: Medium
Link: https://leetcode.com/problems/3sum/

Problem Statement:
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such 
that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

Approach:
Sort + Two Pointers:
1. Sort the array
2. For each element, use two pointers to find pairs that sum to -element
3. Skip duplicates to avoid duplicate triplets

Key insight: After sorting, use two pointers to find complements in O(N) time

Time Complexity: O(N²) - N iterations, each with O(N) two-pointer scan
Space Complexity: O(1) or O(N) depending on sorting implementation
"""

from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """Sort + Two Pointers approach"""
        nums.sort()
        result = []
        n = len(nums)
        
        for i in range(n - 2):
            # Skip duplicates for first element
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            # Two pointers for remaining elements
            left, right = i + 1, n - 1
            target = -nums[i]
            
            while left < right:
                current_sum = nums[left] + nums[right]
                
                if current_sum == target:
                    result.append([nums[i], nums[left], nums[right]])
                    
                    # Skip duplicates for second element
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    # Skip duplicates for third element
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    
                    left += 1
                    right -= 1
                elif current_sum < target:
                    left += 1
                else:
                    right -= 1
        
        return result
    
    # Using set to avoid duplicates (less efficient)
    def threeSumSet(self, nums: List[int]) -> List[List[int]]:
        """Using set to track seen triplets"""
        nums.sort()
        result = set()
        n = len(nums)
        
        for i in range(n - 2):
            left, right = i + 1, n - 1
            
            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]
                
                if current_sum == 0:
                    result.add((nums[i], nums[left], nums[right]))
                    left += 1
                    right -= 1
                elif current_sum < 0:
                    left += 1
                else:
                    right -= 1
        
        return [list(triplet) for triplet in result]
    
    # Hash map approach (for unsorted array)
    def threeSumHashMap(self, nums: List[int]) -> List[List[int]]:
        """Hash map approach"""
        result = set()
        n = len(nums)
        
        for i in range(n - 1):
            seen = set()
            for j in range(i + 1, n):
                complement = -nums[i] - nums[j]
                if complement in seen:
                    triplet = tuple(sorted([nums[i], nums[j], complement]))
                    result.add(triplet)
                seen.add(nums[j])
        
        return [list(triplet) for triplet in result]
    
    # No-sort approach (works but slower)
    def threeSumNoSort(self, nums: List[int]) -> List[List[int]]:
        """Without sorting (uses more memory)"""
        result = set()
        duplicates = set()
        seen = {}
        
        for i, val1 in enumerate(nums):
            if val1 not in duplicates:
                duplicates.add(val1)
                for j, val2 in enumerate(nums[i+1:]):
                    complement = -val1 - val2
                    if complement in seen and seen[complement] == i:
                        triplet = tuple(sorted([val1, val2, complement]))
                        result.add(triplet)
                    seen[val2] = i
        
        return [list(triplet) for triplet in result]


# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1
    nums1 = [-1, 0, 1, 2, -1, -4]
    print(f"Input: nums = {nums1}")
    print(f"Output: {solution.threeSum(nums1)}")
    print(f"Expected: [[-1,-1,2],[-1,0,1]]\n")
    
    # Test case 2: No solution
    nums2 = [0, 1, 1]
    print(f"Input: nums = {nums2}")
    print(f"Output: {solution.threeSum(nums2)}")
    print(f"Expected: []\n")
    
    # Test case 3: All zeros
    nums3 = [0, 0, 0]
    print(f"Input: nums = {nums3}")
    print(f"Output: {solution.threeSum(nums3)}")
    print(f"Expected: [[0,0,0]]\n")
    
    # Test case 4: Multiple solutions
    nums4 = [-2, 0, 0, 2, 2]
    print(f"Input: nums = {nums4}")
    print(f"Output: {solution.threeSum(nums4)}")
    print(f"Expected: [[-2,0,2]]\n")
    
    # Test case 5: Larger array
    nums5 = [-1, 0, 1, 2, -1, -4, -2, -3, 3, 0, 4]
    print(f"Input: nums = {nums5}")
    print(f"Output: {solution.threeSum(nums5)}")
    print(f"Expected: Multiple triplets\n")
    
    # Compare approaches
    nums6 = [-1, 0, 1, 2, -1, -4]
    print(f"Input: nums = {nums6}")
    print(f"Two Pointers: {solution.threeSum(nums6)}")
    print(f"Using Set: {solution.threeSumSet(nums6)}")
    print(f"Hash Map: {solution.threeSumHashMap(nums6)}")
