"""
Problem: 300 - Longest Increasing Subsequence
Difficulty: Medium
Link: https://leetcode.com/problems/longest-increasing-subsequence/
Problem Statement:
Given an integer array nums, return the length of the longest strictly 
increasing subsequence.
Approach 1: Dynamic Programming
dp[i] = length of LIS ending at index i
For each i, check all j < i where nums[j] < nums[i]
Time Complexity: O(N^2)
Space Complexity: O(N)

Approach 2: Binary Search (Optimal)
Maintain sorted list of smallest tail elements for each LIS length
Use binary search to find position to update
Time Complexity: O(N log N)
Space Complexity: O(N)
"""
import bisect

class Solution:
    # Approach 1: Dynamic Programming O(N^2)
    def lengthOfLIS_DP(self, nums: list[int]) -> int:
        n = len(nums)
        dp = [1] * n
        
        # Fill dp array
        for i in range(1, n):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
        
        # Return max value in dp
        return max(dp)
    
    # Approach 2: Binary Search O(N log N)
    def lengthOfLIS_BinarySearch(self, nums: list[int]) -> int:
        tails = []
        
        for num in nums:
            # Find position using binary search
            pos = bisect.bisect_left(tails, num)
            
            # Add or replace
            if pos == len(tails):
                tails.append(num)
            else:
                tails[pos] = num
        
        return len(tails)
    
    # Approach 3: Reconstruct LIS
    def lengthOfLIS_WithPath(self, nums: list[int]) -> tuple:
        n = len(nums)
        dp = [1] * n
        parent = [-1] * n
        
        # Fill dp array and track parent
        for i in range(1, n):
            for j in range(i):
                if nums[j] < nums[i] and dp[j] + 1 > dp[i]:
                    dp[i] = dp[j] + 1
                    parent[i] = j
        
        # Find max length and its index
        max_length = max(dp)
        max_idx = dp.index(max_length)
        
        # Reconstruct path
        lis = []
        idx = max_idx
        while idx != -1:
            lis.append(nums[idx])
            idx = parent[idx]
        
        lis.reverse()
        return max_length, lis


# Test cases
if __name__ == "__main__":
    sol = Solution()
    
    # Test 1
    nums1 = [10, 9, 2, 5, 3, 7, 101, 18]
    print("DP:", sol.lengthOfLIS_DP(nums1))
    print("BinarySearch:", sol.lengthOfLIS_BinarySearch(nums1))
    length, path = sol.lengthOfLIS_WithPath(nums1)
    print("With Path:", length, path)
    # Expected: 4 (LIS: [2, 3, 7, 101])
    
    print()
    
    # Test 2
    nums2 = [0, 1, 0, 4, 4, 4, 3, 2, 1]
    print("DP:", sol.lengthOfLIS_DP(nums2))
    print("BinarySearch:", sol.lengthOfLIS_BinarySearch(nums2))
    length, path = sol.lengthOfLIS_WithPath(nums2)
    print("With Path:", length, path)
    # Expected: 2 (LIS: [0, 1])
    
    print()
    
    # Test 3
    nums3 = [1, 2, 3, 4, 5]
    print("DP:", sol.lengthOfLIS_DP(nums3))
    print("BinarySearch:", sol.lengthOfLIS_BinarySearch(nums3))
    length, path = sol.lengthOfLIS_WithPath(nums3)
    print("With Path:", length, path)
    # Expected: 5
    
    print()
    
    # Test 4
    nums4 = [5, 4, 3, 2, 1]
    print("DP:", sol.lengthOfLIS_DP(nums4))
    print("BinarySearch:", sol.lengthOfLIS_BinarySearch(nums4))
    length, path = sol.lengthOfLIS_WithPath(nums4)
    print("With Path:", length, path)
    # Expected: 1