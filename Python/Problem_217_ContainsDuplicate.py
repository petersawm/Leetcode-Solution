"""
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

3. Brute Force
   - Compare each element with all others
   - Time: O(N²), Space: O(1)

Time Complexity: O(N) - Hash set approach
Space Complexity: O(N) - Hash set storage
"""

from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        """Hash Set approach - Most efficient"""
        seen = set()
        
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        
        return False
    
    # Pythonic one-liner using set
    def containsDuplicatePythonic(self, nums: List[int]) -> bool:
        """Compare length of array with length of set"""
        return len(nums) != len(set(nums))
    
    # Sorting approach
    def containsDuplicateSorting(self, nums: List[int]) -> bool:
        """Sort and check adjacent elements"""
        if len(nums) < 2:
            return False
        
        nums.sort()
        
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                return True
        
        return False
    
    # Brute force approach (not recommended for large inputs)
    def containsDuplicateBruteForce(self, nums: List[int]) -> bool:
        """Compare each element with all others - O(N²)"""
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j]:
                    return True
        
        return False
    
    # Using Counter from collections
    def containsDuplicateCounter(self, nums: List[int]) -> bool:
        """Use Counter to count occurrences"""
        from collections import Counter
        counter = Counter(nums)
        return any(count > 1 for count in counter.values())


# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1
    nums1 = [1, 2, 3, 1]
    print(f"Input: nums = {nums1}")
    print(f"Output: {solution.containsDuplicate(nums1)}")
    print(f"Expected: True\n")
    
    # Test case 2
    nums2 = [1, 2, 3, 4]
    print(f"Input: nums = {nums2}")
    print(f"Output: {solution.containsDuplicate(nums2)}")
    print(f"Expected: False\n")
    
    # Test case 3
    nums3 = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
    print(f"Input: nums = {nums3}")
    print(f"Output: {solution.containsDuplicate(nums3)}")
    print(f"Expected: True\n")
    
    # Test case 4: Empty array
    nums4 = []
    print(f"Input: nums = {nums4}")
    print(f"Output: {solution.containsDuplicate(nums4)}")
    print(f"Expected: False\n")
    
    # Test case 5: Single element
    nums5 = [1]
    print(f"Input: nums = {nums5}")
    print(f"Output: {solution.containsDuplicate(nums5)}")
    print(f"Expected: False\n")
    
    # Compare different approaches
    nums6 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1]
    print(f"Input: nums = {nums6}")
    print(f"Hash Set: {solution.containsDuplicate(nums6)}")
    print(f"Pythonic: {solution.containsDuplicatePythonic(nums6)}")
    print(f"Sorting: {solution.containsDuplicateSorting(nums6.copy())}")
    print(f"Counter: {solution.containsDuplicateCounter(nums6)}")
    print(f"Expected: True")