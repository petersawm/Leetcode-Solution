/*
Problem: 215 - Kth Largest Element in an Array
Difficulty: Medium
Link: https://leetcode.com/problems/kth-largest-element-in-an-array/

Problem Statement:
Given an integer array nums and an integer k, return the kth largest element in the array.
Note that it is the kth largest element in the sorted order, not the kth distinct element.

Can you solve it without sorting?

Approach:
Multiple approaches:

1. Min Heap (Priority Queue) - Most efficient for large arrays
   - Maintain heap of size k with smallest elements at top
   - Time: O(N log k), Space: O(k)

2. Quick Select - Average case optimal
   - Partition-based selection
   - Time: O(N) average, O(N²) worst, Space: O(1)

3. Sorting - Simplest but not optimal
   - Sort and return nums[len-k]
   - Time: O(N log N), Space: O(1)

Time Complexity: O(N log k) - Min heap approach
Space Complexity: O(k) - Heap storage
*/

import java.util.*;

class Solution {
    // Approach 1: Min Heap (Priority Queue) - Most efficient
    public int findKthLargest(int[] nums, int k) {
        // Min heap to keep k largest elements
        PriorityQueue<Integer> minHeap = new PriorityQueue<>();
        
        for (int num : nums) {
            minHeap.offer(num);
            
            // Keep heap size at k
            if (minHeap.size() > k) {
                minHeap.poll();
            }
        }
        
        // Top of min heap is kth largest
        return minHeap.peek();
    }
    
    // Approach 2: Max Heap - Alternative heap approach
    public int findKthLargestMaxHeap(int[] nums, int k) {
        // Max heap (reverse order)
        PriorityQueue<Integer> maxHeap = new PriorityQueue<>(Collections.reverseOrder());
        
        for (int num : nums) {
            maxHeap.offer(num);
        }
        
        // Poll k-1 times
        for (int i = 0; i < k - 1; i++) {
            maxHeap.poll();
        }
        
        // kth largest is now at top
        return maxHeap.poll();
    }
    
    // Approach 3: Sorting
    public int findKthLargestSorting(int[] nums, int k) {
        Arrays.sort(nums);
        return nums[nums.length - k];
    }
    
    // Approach 4: Quick Select - Optimal average case
    public int findKthLargestQuickSelect(int[] nums, int k) {
        return quickSelect(nums, 0, nums.length - 1, nums.length - k);
    }
    
    private int quickSelect(int[] nums, int left, int right, int kSmallest) {
        if (left == right) {
            return nums[left];
        }
        
        // Random pivot for better average performance
        Random random = new Random();
        int pivotIndex = left + random.nextInt(right - left + 1);
        
        pivotIndex = partition(nums, left, right, pivotIndex);
        
        if (kSmallest == pivotIndex) {
            return nums[kSmallest];
        } else if (kSmallest < pivotIndex) {
            return quickSelect(nums, left, pivotIndex - 1, kSmallest);
        } else {
            return quickSelect(nums, pivotIndex + 1, right, kSmallest);
        }
    }
    
    private int partition(int[] nums, int left, int right, int pivotIndex) {
        int pivot = nums[pivotIndex];
        
        // Move pivot to end
        swap(nums, pivotIndex, right);
        
        // Move all smaller elements to left
        int storeIndex = left;
        for (int i = left; i < right; i++) {
            if (nums[i] < pivot) {
                swap(nums, storeIndex, i);
                storeIndex++;
            }
        }
        
        // Move pivot to final position
        swap(nums, right, storeIndex);
        return storeIndex;
    }
    
    private void swap(int[] nums, int i, int j) {
        int temp = nums[i];
        nums[i] = nums[j];
        nums[j] = temp;
    }
    
    // Approach 5: Using TreeMap for frequency counting
    public int findKthLargestTreeMap(int[] nums, int k) {
        TreeMap<Integer, Integer> map = new TreeMap<>(Collections.reverseOrder());
        
        for (int num : nums) {
            map.put(num, map.getOrDefault(num, 0) + 1);
        }
        
        int count = 0;
        for (Map.Entry<Integer, Integer> entry : map.entrySet()) {
            count += entry.getValue();
            if (count >= k) {
                return entry.getKey();
            }
        }
        
        return -1;
    }
    
    // Helper method to print array
    private static void printArray(int[] arr) {
        System.out.print("[");
        for (int i = 0; i < arr.length; i++) {
            System.out.print(arr[i]);
            if (i < arr.length - 1) {
                System.out.print(",");
            }
        }
        System.out.print("]");
    }
    
    // Test cases
    public static void main(String[] args) {
        Solution solution = new Solution();
        
        // Test case 1
        int[] nums1 = {3, 2, 1, 5, 6, 4};
        int k1 = 2;
        System.out.print("Input: nums = ");
        printArray(nums1);
        System.out.println(", k = " + k1);
        System.out.println("Output: " + solution.findKthLargest(nums1, k1));
        System.out.println("Expected: 5 (2nd largest)\n");
        
        // Test case 2
        int[] nums2 = {3, 2, 3, 1, 2, 4, 5, 5, 6};
        int k2 = 4;
        System.out.print("Input: nums = ");
        printArray(nums2);
        System.out.println(", k = " + k2);
        System.out.println("Output: " + solution.findKthLargest(nums2, k2));
        System.out.println("Expected: 4 (4th largest)\n");
        
        // Test case 3: k = 1 (largest element)
        int[] nums3 = {1, 2, 3, 4, 5};
        int k3 = 1;
        System.out.print("Input: nums = ");
        printArray(nums3);
        System.out.println(", k = " + k3);
        System.out.println("Output: " + solution.findKthLargest(nums3, k3));
        System.out.println("Expected: 5\n");
        
        // Test case 4: k = n (smallest element)
        int[] nums4 = {7, 6, 5, 4, 3, 2, 1};
        int k4 = 7;
        System.out.print("Input: nums = ");
        printArray(nums4);
        System.out.println(", k = " + k4);
        System.out.println("Output: " + solution.findKthLargest(nums4, k4));
        System.out.println("Expected: 1\n");
        
        // Compare all approaches
        int[] nums5 = {3, 2, 1, 5, 6, 4};
        int k5 = 2;
        System.out.print("Input: nums = ");
        printArray(nums5);
        System.out.println(", k = " + k5);
        System.out.println("Min Heap: " + solution.findKthLargest(nums5.clone(), k5));
        System.out.println("Max Heap: " + solution.findKthLargestMaxHeap(nums5.clone(), k5));
        System.out.println("Sorting: " + solution.findKthLargestSorting(nums5.clone(), k5));
        System.out.println("Quick Select: " + solution.findKthLargestQuickSelect(nums5.clone(), k5));
        System.out.println("TreeMap: " + solution.findKthLargestTreeMap(nums5.clone(), k5));
        System.out.println("Expected: 5");
    }
}