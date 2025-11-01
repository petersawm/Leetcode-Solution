"""
Problem: 198 - House Robber
Difficulty: Medium
Link: https://leetcode.com/problems/house-robber/

Problem Statement:
You are a professional robber planning to rob houses along a street. Each house has 
a certain amount of money stashed, the only constraint stopping you from robbing each 
of them is that adjacent houses have security systems connected and it will automatically 
contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the 
maximum amount of money you can rob tonight without alerting the police.

Approach:
Dynamic Programming:
- At each house, decide whether to rob it or not
- If rob current house: can't rob previous house
- If don't rob current house: take max from previous house

dp[i] = max(dp[i-1], dp[i-2] + nums[i])

Space can be optimized to O(1) by only tracking last two values.

Time Complexity: O(N) - Single pass through array
Space Complexity: O(1) - Only using two variables
"""

from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        """Space-optimized DP - O(1) space"""
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        
        # prev2 = max money robbed 2 houses ago
        # prev1 = max money robbed 1 house ago
        prev2 = 0
        prev1 = nums[0]
        
        for i in range(1, len(nums)):
            # Either rob current house or don't
            current = max(prev1, prev2 + nums[i])
            prev2 = prev1
            prev1 = current
        
        return prev1
    
    # DP with array (easier to understand)
    def robDP(self, nums: List[int]) -> int:
        """DP with array - O(N) space"""
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        
        n = len(nums)
        dp = [0] * n
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        
        for i in range(2, n):
            # Either rob current or skip
            dp[i] = max(dp[i-1], dp[i-2] + nums[i])
        
        return dp[n-1]
    
    # Recursive with memoization
    def robMemo(self, nums: List[int]) -> int:
        """Recursive with memoization"""
        memo = {}
        
        def helper(i: int) -> int:
            if i < 0:
                return 0
            if i in memo:
                return memo[i]
            
            # Rob current or skip
            memo[i] = max(helper(i-1), helper(i-2) + nums[i])
            return memo[i]
        
        return helper(len(nums) - 1)
    
    # Alternative naming for clarity
    def robClear(self, nums: List[int]) -> int:
        """Clear variable naming"""
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        
        rob_prev_prev = 0  # Max if we robbed 2 houses ago
        rob_prev = nums[0]  # Max if we robbed 1 house ago
        
        for i in range(1, len(nums)):
            # Max of: skip current house OR rob current + skip previous
            rob_current = max(rob_prev, rob_prev_prev + nums[i])
            rob_prev_prev = rob_prev
            rob_prev = rob_current
        
        return rob_prev


# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1
    nums1 = [1, 2, 3, 1]
    print(f"Input: nums = {nums1}")
    print(f"Output: {solution.rob(nums1)}")
    print(f"Expected: 4 (Rob house 1 (1) and house 3 (3))\n")
    
    # Test case 2
    nums2 = [2, 7, 9, 3, 1]
    print(f"Input: nums = {nums2}")
    print(f"Output: {solution.rob(nums2)}")
    print(f"Expected: 12 (Rob house 1 (2), 3 (9), and 5 (1))\n")
    
    # Test case 3: Single house
    nums3 = [5]
    print(f"Input: nums = {nums3}")
    print(f"Output: {solution.rob(nums3)}")
    print(f"Expected: 5\n")
    
    # Test case 4: Two houses
    nums4 = [2, 1]
    print(f"Input: nums = {nums4}")
    print(f"Output: {solution.rob(nums4)}")
    print(f"Expected: 2\n")
    
    # Test case 5: All increasing
    nums5 = [1, 2, 3, 4, 5]
    print(f"Input: nums = {nums5}")
    print(f"Output: {solution.rob(nums5)}")
    print(f"Expected: 9 (1 + 3 + 5)\n")
    
    # Compare approaches
    nums6 = [2, 7, 9, 3, 1]
    print(f"Input: nums = {nums6}")
    print(f"Optimized: {solution.rob(nums6)}")
    print(f"DP Array: {solution.robDP(nums6)}")
    print(f"Memoization: {solution.robMemo(nums6)}")
    print(f"Clear Naming: {solution.robClear(nums6)}")
    print(f"Expected: 12")