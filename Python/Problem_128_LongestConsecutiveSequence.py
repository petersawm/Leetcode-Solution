"""
Problem: 128 - Longest Consecutive Sequence
Difficulty: Medium
Link: https://leetcode.com/problems/longest-consecutive-sequence/

Problem Statement:
Given an unsorted array of integers nums, return the length of the longest consecutive 
elements sequence.

You must write an algorithm that runs in O(n) time.

Example: [100,4,200,1,3,2] → 4 (sequence: [1,2,3,4])

Approach:
Use Hash Set for O(1) lookups:
1. Put all numbers in a set
2. For each number, check if it's the start of a sequence (num-1 not in set)
3. If it's a start, count consecutive numbers
4. Track maximum length

Key insight: Only count from sequence starts to avoid redundant work

Time Complexity: O(N) - Each number visited at most twice
Space Complexity: O(N) - Hash set storage
"""

from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """Hash Set approach - O(N) time"""
        if not nums:
            return 0
        
        num_set = set(nums)
        max_length = 0
        
        for num in num_set:
            # Only start counting if this is the beginning of a sequence
            if num - 1 not in num_set:
                current_num = num
                current_length = 1
                
                # Count consecutive numbers
                while current_num + 1 in num_set:
                    current_num += 1
                    current_length += 1
                
                max_length = max(max_length, current_length)
        
        return max_length
    
    # Alternative: Sorting approach (not O(n) but simpler)
    def longestConsecutiveSorting(self, nums: List[int]) -> int:
        """Sorting approach - O(N log N) time"""
        if not nums:
            return 0
        
        nums.sort()
        max_length = 1
        current_length = 1
        
        for i in range(1, len(nums)):
            # Skip duplicates
            if nums[i] == nums[i-1]:
                continue
            
            # Check if consecutive
            if nums[i] == nums[i-1] + 1:
                current_length += 1
            else:
                max_length = max(max_length, current_length)
                current_length = 1
        
        return max(max_length, current_length)
    
    # Union-Find approach (overkill but educational)
    def longestConsecutiveUnionFind(self, nums: List[int]) -> int:
        """Union-Find approach"""
        if not nums:
            return 0
        
        parent = {}
        size = {}
        
        def find(x):
            if x != parent[x]:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            root_x, root_y = find(x), find(y)
            if root_x != root_y:
                # Union by size
                if size[root_x] < size[root_y]:
                    root_x, root_y = root_y, root_x
                parent[root_y] = root_x
                size[root_x] += size[root_y]
        
        # Initialize
        for num in nums:
            if num not in parent:
                parent[num] = num
                size[num] = 1
        
        # Union consecutive numbers
        for num in nums:
            if num + 1 in parent:
                union(num, num + 1)
        
        # Find maximum size
        return max(size[find(num)] for num in nums)
    
    # HashMap approach (tracking sequence boundaries)
    def longestConsecutiveHashMap(self, nums: List[int]) -> int:
        """HashMap tracking sequence boundaries"""
        if not nums:
            return 0
        
        num_map = {}  # num -> length of sequence containing num
        max_length = 0
        
        for num in nums:
            if num in num_map:
                continue
            
            # Get lengths of adjacent sequences
            left = num_map.get(num - 1, 0)
            right = num_map.get(num + 1, 0)
            
            # New sequence length
            length = left + right + 1
            max_length = max(max_length, length)
            
            # Update boundaries
            num_map[num] = length
            num_map[num - left] = length
            num_map[num + right] = length
        
        return max_length


# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1
    nums1 = [100, 4, 200, 1, 3, 2]
    print(f"Input: nums = {nums1}")
    print(f"Output: {solution.longestConsecutive(nums1)}")
    print(f"Expected: 4 (sequence: [1,2,3,4])\n")
    
    # Test case 2
    nums2 = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
    print(f"Input: nums = {nums2}")
    print(f"Output: {solution.longestConsecutive(nums2)}")
    print(f"Expected: 9 (sequence: [0,1,2,3,4,5,6,7,8])\n")
    
    # Test case 3: Empty array
    nums3 = []
    print(f"Input: nums = {nums3}")
    print(f"Output: {solution.longestConsecutive(nums3)}")
    print(f"Expected: 0\n")
    
    # Test case 4: Single element
    nums4 = [1]
    print(f"Input: nums = {nums4}")
    print(f"Output: {solution.longestConsecutive(nums4)}")
    print(f"Expected: 1\n")
    
    # Test case 5: Duplicates
    nums5 = [1, 2, 0, 1]
    print(f"Input: nums = {nums5}")
    print(f"Output: {solution.longestConsecutive(nums5)}")
    print(f"Expected: 3 (sequence: [0,1,2])\n")
    
    # Compare approaches
    nums6 = [100, 4, 200, 1, 3, 2]
    print(f"Input: nums = {nums6}")
    print(f"Hash Set: {solution.longestConsecutive(nums6)}")
    print(f"Sorting: {solution.longestConsecutiveSorting(nums6)}")
    print(f"Union-Find: {solution.longestConsecutiveUnionFind(nums6)}")
    print(f"HashMap: {solution.longestConsecutiveHashMap(nums6)}")
    print(f"Expected: 4")