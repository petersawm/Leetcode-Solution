"""
Problem: 215 - Kth Largest Element in an Array
Difficulty: Medium
Link: https://leetcode.com/problems/kth-largest-element-in-an-array/

Problem Statement:
Given an integer array nums and an integer k, return the kth largest element in the array.
Note that it is the kth largest element in the sorted order, not the kth distinct element.

Can you solve it without sorting?

Approach:
Multiple approaches:

1. Min Heap - Most efficient for large arrays
   - Maintain heap of size k with smallest elements at top
   - Time: O(N log k), Space: O(k)

2. Quick Select - Average case optimal
   - Partition-based selection (like quicksort)
   - Time: O(N) average, O(N²) worst, Space: O(1)

3. Sorting - Simplest but not optimal
   - Sort and return nums[len-k]
   - Time: O(N log N), Space: O(1)

Time Complexity: O(N log k) - Min heap approach
Space Complexity: O(k) - Heap storage
"""

from typing import List
import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """Min Heap approach - Most efficient"""
        # Create min heap of size k
        # Heap keeps k largest elements, smallest at top
        min_heap = []
        
        for num in nums:
            heapq.heappush(min_heap, num)
            
            # Keep heap size at k
            if len(min_heap) > k:
                heapq.heappop(min_heap)
        
        # Top of min heap is kth largest
        return min_heap[0]
    
    # Alternative: Using heapq.nlargest
    def findKthLargestNlargest(self, nums: List[int], k: int) -> int:
        """Using built-in nlargest function"""
        return heapq.nlargest(k, nums)[-1]
    
    # Sorting approach
    def findKthLargestSorting(self, nums: List[int], k: int) -> int:
        """Sort and return kth from end"""
        nums.sort()
        return nums[len(nums) - k]
    
    # Quick Select approach (optimal average case)
    def findKthLargestQuickSelect(self, nums: List[int], k: int) -> int:
        """Quick Select algorithm - O(N) average"""
        def partition(left: int, right: int, pivot_idx: int) -> int:
            pivot = nums[pivot_idx]
            # Move pivot to end
            nums[pivot_idx], nums[right] = nums[right], nums[pivot_idx]
            
            # Move all smaller elements to left
            store_idx = left
            for i in range(left, right):
                if nums[i] < pivot:
                    nums[store_idx], nums[i] = nums[i], nums[store_idx]
                    store_idx += 1
            
            # Move pivot to final position
            nums[right], nums[store_idx] = nums[store_idx], nums[right]
            return store_idx
        
        def select(left: int, right: int, k_smallest: int) -> int:
            if left == right:
                return nums[left]
            
            # Choose random pivot
            import random
            pivot_idx = random.randint(left, right)
            
            # Partition and get pivot position
            pivot_idx = partition(left, right, pivot_idx)
            
            if k_smallest == pivot_idx:
                return nums[k_smallest]
            elif k_smallest < pivot_idx:
                return select(left, pivot_idx - 1, k_smallest)
            else:
                return select(pivot_idx + 1, right, k_smallest)
        
        # kth largest is (n-k)th smallest
        return select(0, len(nums) - 1, len(nums) - k)
    
    # Max Heap approach (convert min heap to max heap)
    def findKthLargestMaxHeap(self, nums: List[int], k: int) -> int:
        """Using max heap (negate values)"""
        # Python heapq is min heap, so negate values for max heap
        max_heap = [-num for num in nums]
        heapq.heapify(max_heap)
        
        # Pop k-1 times
        for _ in range(k - 1):
            heapq.heappop(max_heap)
        
        # kth largest is now at top
        return -heapq.heappop(max_heap)


# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1
    nums1 = [3, 2, 1, 5, 6, 4]
    k1 = 2
    print(f"Input: nums = {nums1}, k = {k1}")
    print(f"Output: {solution.findKthLargest(nums1, k1)}")
    print(f"Expected: 5 (2nd largest)\n")
    
    # Test case 2
    nums2 = [3, 2, 3, 1, 2, 4, 5, 5, 6]
    k2 = 4
    print(f"Input: nums = {nums2}, k = {k2}")
    print(f"Output: {solution.findKthLargest(nums2, k2)}")
    print(f"Expected: 4 (4th largest)\n")
    
    # Test case 3: k = 1 (largest element)
    nums3 = [1, 2, 3, 4, 5]
    k3 = 1
    print(f"Input: nums = {nums3}, k = {k3}")
    print(f"Output: {solution.findKthLargest(nums3, k3)}")
    print(f"Expected: 5\n")
    
    # Test case 4: k = n (smallest element)
    nums4 = [7, 6, 5, 4, 3, 2, 1]
    k4 = 7
    print(f"Input: nums = {nums4}, k = {k4}")
    print(f"Output: {solution.findKthLargest(nums4, k4)}")
    print(f"Expected: 1\n")
    
    # Compare all approaches
    nums5 = [3, 2, 1, 5, 6, 4]
    k5 = 2
    print(f"Input: nums = {nums5}, k = {k5}")
    print(f"Min Heap: {solution.findKthLargest(nums5.copy(), k5)}")
    print(f"Nlargest: {solution.findKthLargestNlargest(nums5.copy(), k5)}")
    print(f"Sorting: {solution.findKthLargestSorting(nums5.copy(), k5)}")
    print(f"Quick Select: {solution.findKthLargestQuickSelect(nums5.copy(), k5)}")
    print(f"Max Heap: {solution.findKthLargestMaxHeap(nums5.copy(), k5)}")
    print(f"Expected: 5")