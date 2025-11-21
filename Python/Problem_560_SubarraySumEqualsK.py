"""
Problem: 560 - Subarray Sum Equals K
Difficulty: Medium
Link: https://leetcode.com/problems/subarray-sum-equals-k/

Problem Statement:
Given an array of integers nums and an integer k, return the total number of subarrays 
whose sum equals to k.

A subarray is a contiguous non-empty sequence of elements within an array.

Example: nums = [1,1,1], k = 2 → Output: 2

Approach:
Use Prefix Sum + Hash Map:
1. Keep running sum (prefix sum)
2. Use hash map to store frequency of each prefix sum
3. If (current_sum - k) exists in map, add its count to result

Key insight: If prefix_sum[j] - prefix_sum[i] = k, then subarray[i+1...j] sums to k

Time Complexity: O(N) - Single pass through array
Space Complexity: O(N) - Hash map storage
"""

from typing import List
from collections import defaultdict

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        """Prefix sum with hash map - Optimal"""
        count = 0
        prefix_sum = 0
        sum_count = defaultdict(int)
        sum_count[0] = 1  # Base case: empty prefix
        
        for num in nums:
            prefix_sum += num
            
            # Check if (prefix_sum - k) exists
            # This means there's a subarray ending here with sum = k
            if (prefix_sum - k) in sum_count:
                count += sum_count[prefix_sum - k]
            
            # Add current prefix sum to map
            sum_count[prefix_sum] += 1
        
        return count
    
    # Brute force approach (for comparison)
    def subarraySumBruteForce(self, nums: List[int], k: int) -> int:
        """Brute force - O(N²) time"""
        count = 0
        n = len(nums)
        
        for i in range(n):
            current_sum = 0
            for j in range(i, n):
                current_sum += nums[j]
                if current_sum == k:
                    count += 1
        
        return count
    
    # Using prefix sum array
    def subarraySumPrefixArray(self, nums: List[int], k: int) -> int:
        """Using prefix sum array"""
        n = len(nums)
        prefix = [0] * (n + 1)
        
        # Build prefix sum array
        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]
        
        count = 0
        sum_count = defaultdict(int)
        
        for i in range(n + 1):
            # Check if (prefix[i] - k) exists
            if (prefix[i] - k) in sum_count:
                count += sum_count[prefix[i] - k]
            
            sum_count[prefix[i]] += 1
        
        return count
    
    # Without defaultdict
    def subarraySumNoDefault(self, nums: List[int], k: int) -> int:
        """Without using defaultdict"""
        count = 0
        prefix_sum = 0
        sum_count = {0: 1}  # Base case
        
        for num in nums:
            prefix_sum += num
            
            # Check if (prefix_sum - k) exists
            count += sum_count.get(prefix_sum - k, 0)
            
            # Add current prefix sum
            sum_count[prefix_sum] = sum_count.get(prefix_sum, 0) + 1
        
        return count


# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1
    nums1 = [1, 1, 1]
    k1 = 2
    print(f"Input: nums = {nums1}, k = {k1}")
    print(f"Output: {solution.subarraySum(nums1, k1)}")
    print(f"Expected: 2 (subarrays: [1,1], [1,1])\n")
    
    # Test case 2
    nums2 = [1, 2, 3]
    k2 = 3
    print(f"Input: nums = {nums2}, k = {k2}")
    print(f"Output: {solution.subarraySum(nums2, k2)}")
    print(f"Expected: 2 (subarrays: [1,2], [3])\n")
    
    # Test case 3: With negative numbers
    nums3 = [1, -1, 0]
    k3 = 0
    print(f"Input: nums = {nums3}, k = {k3}")
    print(f"Output: {solution.subarraySum(nums3, k3)}")
    print(f"Expected: 3 (subarrays: [1,-1], [0], [1,-1,0])\n")
    
    # Test case 4: Single element
    nums4 = [5]
    k4 = 5
    print(f"Input: nums = {nums4}, k = {k4}")
    print(f"Output: {solution.subarraySum(nums4, k4)}")
    print(f"Expected: 1\n")
    
    # Test case 5: No subarray
    nums5 = [1, 2, 3]
    k5 = 7
    print(f"Input: nums = {nums5}, k = {k5}")
    print(f"Output: {solution.subarraySum(nums5, k5)}")
    print(f"Expected: 0\n")
    
    # Test case 6: Multiple occurrences
    nums6 = [3, 4, 7, 2, -3, 1, 4, 2]
    k6 = 7
    print(f"Input: nums = {nums6}, k = {k6}")
    print(f"Output: {solution.subarraySum(nums6, k6)}")
    print(f"Expected: 4\n")
    
    # Compare approaches
    nums7 = [1, 1, 1]
    k7 = 2
    print(f"Input: nums = {nums7}, k = {k7}")
    print(f"Optimal (Hash Map): {solution.subarraySum(nums7, k7)}")
    print(f"Brute Force: {solution.subarraySumBruteForce(nums7, k7)}")
    print(f"Prefix Array: {solution.subarraySumPrefixArray(nums7, k7)}")
    print(f"No Default: {solution.subarraySumNoDefault(nums7, k7)}")