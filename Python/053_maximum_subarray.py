"""
Problem: 53 - Maximum Subarray
Difficulty: Medium
Link: https://leetcode.com/problems/maximum-subarray/

Problem Statement:
Given an integer array nums, find the contiguous subarray (containing at least 
one number) which has the largest sum and return its sum.

Approach - Kadane's Algorithm:
At each position, we have two choices:
1. Extend the current subarray by including current element
2. Start a new subarray from current element

We choose whichever gives us the larger sum.
Keep track of the maximum sum encountered.

Key insight: If current_sum becomes negative, it's better to start fresh.

Time Complexity: O(N) - Single pass through array
Space Complexity: O(1) - Only two variables used
"""
from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Initialize with first element
        max_sum = current_sum = nums[0]
        
        # Process remaining elements
        for num in nums[1:]:
            # Extend current subarray or start new one
            current_sum = max(num, current_sum + num)
            
            # Update global maximum
            max_sum = max(max_sum, current_sum)
        
        return max_sum

# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    test_cases = [
        ([-2,1,-3,4,-1,2,1,-5,4], 6),  # [4,-1,2,1]
        ([1], 1),
        ([5,4,-1,7,8], 23),  # entire array
        ([-1], -1),
        ([-2,-1], -1)
    ]
    
    for nums, expected in test_cases:
        result = solution.maxSubArray(nums)
        status = "✓" if result == expected else "✗"
        print(f"{status} Input: {nums}")
        print(f"   Output: {result} | Expected: {expected}\n")