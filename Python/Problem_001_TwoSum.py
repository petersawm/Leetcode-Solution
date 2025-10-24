"""
Problem: 1 - Two Sum
Difficulty: Easy
Link: https://leetcode.com/problems/two-sum/

Problem Statement:
Given an array of integers nums and an integer target, return indices of the 
two numbers such that they add up to target. You may assume that each input 
would have exactly one solution, and you may not use the same element twice.

Approach:
Use a hash map to store the complement (target - current number) as we iterate.
For each number, check if it exists in the hash map. If yes, we found our pair.
If no, store the current number with its index in the hash map.

Time Complexity: O(N) - Single pass through the array
Space Complexity: O(N) - Hash map stores at most N elements
"""

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Hash map to store {value: index}
        seen = {}
        
        # Iterate through the array
        for i, num in enumerate(nums):
            # Calculate the complement needed to reach target
            complement = target - num
            
            # Check if complement exists in hash map
            if complement in seen:
                return [seen[complement], i]
            
            # Store current number with its index
            seen[num] = i
        
        # No solution found (though problem guarantees one exists)
        return []


# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1
    nums1 = [2, 7, 11, 15]
    target1 = 9
    print(f"Input: nums = {nums1}, target = {target1}")
    print(f"Output: {solution.twoSum(nums1, target1)}")  # Expected: [0, 1]
    
    # Test case 2
    nums2 = [3, 2, 4]
    target2 = 6
    print(f"\nInput: nums = {nums2}, target = {target2}")
    print(f"Output: {solution.twoSum(nums2, target2)}")  # Expected: [1, 2]
    
    # Test case 3
    nums3 = [3, 3]
    target3 = 6
    print(f"\nInput: nums = {nums3}, target = {target3}")
    print(f"Output: {solution.twoSum(nums3, target3)}")  # Expected: [0, 1]