"""
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
2. Calculate middle index: mid = (left + right) // 2
3. If nums[mid] == target, return mid
4. If nums[mid] < target, search right half (left = mid + 1)
5. If nums[mid] > target, search left half (right = mid - 1)
6. Repeat until left > right

Time Complexity: O(log N) - Halves search space each iteration
Space Complexity: O(1) - Only using pointers
"""

from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """Iterative binary search"""
        left, right = 0, len(nums) - 1
        
        while left <= right:
            # Calculate middle index (avoid overflow)
            mid = left + (right - left) // 2
            
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                # Search right half
                left = mid + 1
            else:
                # Search left half
                right = mid - 1
        
        # Target not found
        return -1
    
    # Recursive approach
    def searchRecursive(self, nums: List[int], target: int) -> int:
        """Recursive binary search"""
        def binary_search(left: int, right: int) -> int:
            if left > right:
                return -1
            
            mid = left + (right - left) // 2
            
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                return binary_search(mid + 1, right)
            else:
                return binary_search(left, mid - 1)
        
        return binary_search(0, len(nums) - 1)
    
    # Using Python's bisect module
    def searchBisect(self, nums: List[int], target: int) -> int:
        """Using built-in bisect module"""
        import bisect
        
        idx = bisect.bisect_left(nums, target)
        
        if idx < len(nums) and nums[idx] == target:
            return idx
        return -1
    
    # Alternative template (helps with edge cases)
    def searchTemplate(self, nums: List[int], target: int) -> int:
        """Binary search template that's easier to remember"""
        if not nums:
            return -1
        
        left, right = 0, len(nums) - 1
        
        while left < right:
            mid = left + (right - left) // 2
            
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid
        
        # Check if target is found
        return left if nums[left] == target else -1


# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1
    nums1 = [-1, 0, 3, 5, 9, 12]
    target1 = 9
    print(f"Input: nums = {nums1}, target = {target1}")
    print(f"Output: {solution.search(nums1, target1)}")
    print(f"Expected: 4\n")
    
    # Test case 2
    nums2 = [-1, 0, 3, 5, 9, 12]
    target2 = 2
    print(f"Input: nums = {nums2}, target = {target2}")
    print(f"Output: {solution.search(nums2, target2)}")
    print(f"Expected: -1\n")
    
    # Test case 3: Single element - found
    nums3 = [5]
    target3 = 5
    print(f"Input: nums = {nums3}, target = {target3}")
    print(f"Output: {solution.search(nums3, target3)}")
    print(f"Expected: 0\n")
    
    # Test case 4: Single element - not found
    nums4 = [5]
    target4 = 3
    print(f"Input: nums = {nums4}, target = {target4}")
    print(f"Output: {solution.search(nums4, target4)}")
    print(f"Expected: -1\n")
    
    # Test case 5: Target at boundaries
    nums5 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    target5 = 1
    print(f"Input: nums = {nums5}, target = {target5}")
    print(f"Output (Iterative): {solution.search(nums5, target5)}")
    print(f"Output (Recursive): {solution.searchRecursive(nums5, target5)}")
    print(f"Output (Bisect): {solution.searchBisect(nums5, target5)}")
    print(f"Expected: 0\n")
    
    # Test case 6: Large array
    nums6 = list(range(1, 10001, 2))  # Odd numbers from 1 to 10000
    target6 = 9999
    print(f"Input: nums = [1,3,5,...,9999], target = {target6}")
    print(f"Output: {solution.search(nums6, target6)}")
    print(f"Expected: 4999")