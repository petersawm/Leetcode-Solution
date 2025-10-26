"""
Problem: 238 - Product of Array Except Self
Difficulty: Medium
Link: https://leetcode.com/problems/product-of-array-except-self/

Problem Statement:
Given an integer array nums, return an array answer such that answer[i] is equal 
to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
You must write an algorithm that runs in O(n) time and without using the division operation.

Approach:
Use prefix and suffix products:
1. For each index i, answer[i] = (product of all elements before i) × (product of all elements after i)
2. Create prefix product array: prefix[i] = product of nums[0] to nums[i-1]
3. Create suffix product array: suffix[i] = product of nums[i+1] to nums[n-1]
4. Result: answer[i] = prefix[i] × suffix[i]

Optimization: Use output array to store prefix, then multiply with suffix in-place

Time Complexity: O(N) - Three passes through array
Space Complexity: O(1) - Only output array (not counting output as extra space)
"""

from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [1] * n
        
        # Calculate prefix products and store in result
        # result[i] = product of all elements before index i
        prefix = 1
        for i in range(n):
            result[i] = prefix
            prefix *= nums[i]
        
        # Calculate suffix products and multiply with result
        # Multiply result[i] with product of all elements after index i
        suffix = 1
        for i in range(n - 1, -1, -1):
            result[i] *= suffix
            suffix *= nums[i]
        
        return result
    
    # Alternative: Using separate prefix and suffix arrays (easier to understand)
    def productExceptSelfVerbose(self, nums: List[int]) -> List[int]:
        n = len(nums)
        
        # Prefix products: prefix[i] = product of nums[0] to nums[i-1]
        prefix = [1] * n
        for i in range(1, n):
            prefix[i] = prefix[i - 1] * nums[i - 1]
        
        # Suffix products: suffix[i] = product of nums[i+1] to nums[n-1]
        suffix = [1] * n
        for i in range(n - 2, -1, -1):
            suffix[i] = suffix[i + 1] * nums[i + 1]
        
        # Combine prefix and suffix
        result = [prefix[i] * suffix[i] for i in range(n)]
        
        return result
    
    # Alternative: Using division (violates problem constraint but good to know)
    def productExceptSelfDivision(self, nums: List[int]) -> List[int]:
        """
        This approach uses division - NOT allowed per problem statement
        But useful to understand why division approach has edge cases
        """
        from functools import reduce
        import operator
        
        # Count zeros
        zero_count = nums.count(0)
        
        if zero_count > 1:
            # If more than one zero, all products are zero
            return [0] * len(nums)
        
        if zero_count == 1:
            # If exactly one zero, only that position has non-zero product
            total_product = reduce(operator.mul, [x for x in nums if x != 0], 1)
            return [total_product if num == 0 else 0 for num in nums]
        
        # No zeros - normal division approach
        total_product = reduce(operator.mul, nums, 1)
        return [total_product // num for num in nums]


# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1
    nums1 = [1, 2, 3, 4]
    print(f"Input: nums = {nums1}")
    print(f"Output: {solution.productExceptSelf(nums1)}")
    print(f"Expected: [24, 12, 8, 6]")
    print(f"Explanation: [2×3×4, 1×3×4, 1×2×4, 1×2×3]\n")
    
    # Test case 2
    nums2 = [-1, 1, 0, -3, 3]
    print(f"Input: nums = {nums2}")
    print(f"Output: {solution.productExceptSelf(nums2)}")
    print(f"Expected: [0, 0, 9, 0, 0]\n")
    
    # Test case 3
    nums3 = [2, 3, 4, 5]
    print(f"Input: nums = {nums3}")
    print(f"Output: {solution.productExceptSelf(nums3)}")
    print(f"Expected: [60, 40, 30, 24]\n")
    
    # Test case 4: Two elements
    nums4 = [1, 2]
    print(f"Input: nums = {nums4}")
    print(f"Output: {solution.productExceptSelf(nums4)}")
    print(f"Expected: [2, 1]\n")
    
    # Test case 5: With negative numbers
    nums5 = [-1, -2, -3, -4]
    print(f"Input: nums = {nums5}")
    print(f"Output (Optimized): {solution.productExceptSelf(nums5)}")
    print(f"Output (Verbose): {solution.productExceptSelfVerbose(nums5)}")
    print(f"Expected: [-24, -12, -8, -6]")