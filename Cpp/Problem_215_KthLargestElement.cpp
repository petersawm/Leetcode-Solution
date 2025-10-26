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

#include <vector>
#include <iostream>
#include <queue>
#include <algorithm>
#include <functional>
#include <random>

using namespace std;

class Solution {
public:
    // Approach 1: Min Heap - Most efficient
    int findKthLargest(vector<int>& nums, int k) {
        // Min heap to keep k largest elements
        priority_queue<int, vector<int>, greater<int>> minHeap;
        
        for (int num : nums) {
            minHeap.push(num);
            
            // Keep heap size at k
            if (minHeap.size() > k) {
                minHeap.pop();
            }
        }
        
        // Top of min heap is kth largest
        return minHeap.top();
    }
    
    // Approach 2: Max Heap - Alternative heap approach
    int findKthLargestMaxHeap(vector<int>& nums, int k) {
        // Max heap (default for priority_queue)
        priority_queue<int> maxHeap(nums.begin(), nums.end());
        
        // Pop k-1 times
        for (int i = 0; i < k - 1; i++) {
            maxHeap.pop();
        }
        
        // kth largest is now at top
        return maxHeap.top();
    }
    
    // Approach 3: Sorting
    int findKthLargestSorting(vector<int>& nums, int k) {
        sort(nums.begin(), nums.end());
        return nums[nums.size() - k];
    }
    
    // Approach 4: Quick Select - Optimal average case
    int findKthLargestQuickSelect(vector<int>& nums, int k) {
        return quickSelect(nums, 0, nums.size() - 1, nums.size() - k);
    }
    
private:
    int quickSelect(vector<int>& nums, int left, int right, int kSmallest) {
        if (left == right) {
            return nums[left];
        }
        
        // Random pivot for better average performance
        random_device rd;
        mt19937 gen(rd());
        uniform_int_distribution<> dis(left, right);
        int pivotIndex = dis(gen);
        
        pivotIndex = partition(nums, left, right, pivotIndex);
        
        if (kSmallest == pivotIndex) {
            return nums[kSmallest];
        } else if (kSmallest < pivotIndex) {
            return quickSelect(nums, left, pivotIndex - 1, kSmallest);
        } else {
            return quickSelect(nums, pivotIndex + 1, right, kSmallest);
        }
    }
    
    int partition(vector<int>& nums, int left, int right, int pivotIndex) {
        int pivot = nums[pivotIndex];
        
        // Move pivot to end
        swap(nums[pivotIndex], nums[right]);
        
        // Move all smaller elements to left
        int storeIndex = left;
        for (int i = left; i < right; i++) {
            if (nums[i] < pivot) {
                swap(nums[storeIndex], nums[i]);
                storeIndex++;
            }
        }
        
        // Move pivot to final position
        swap(nums[right], nums[storeIndex]);
        return storeIndex;
    }
    
public:
    // Approach 5: Using STL nth_element (partial sort)
    int findKthLargestNthElement(vector<int>& nums, int k) {
        // nth_element partitions array so that element at position n-k is in correct position
        nth_element(nums.begin(), nums.begin() + nums.size() - k, nums.end());
        return nums[nums.size() - k];
    }
    
    // Approach 6: Using STL partial_sort
    int findKthLargestPartialSort(vector<int>& nums, int k) {
        // Partially sort so that largest k elements are at the end
        partial_sort(nums.begin(), nums.begin() + k, nums.end(), greater<int>());
        return nums[k - 1];
    }
};

// Helper function to print vector
void printVector(const vector<int>& arr) {
    cout << "[";
    for (int i = 0; i < arr.size(); i++) {
        cout << arr[i];
        if (i < arr.size() - 1) cout << ",";
    }
    cout << "]";
}

int main() {
    Solution solution;
    
    // Test case 1
    vector<int> nums1 = {3, 2, 1, 5, 6, 4};
    int k1 = 2;
    cout << "Input: nums = ";
    printVector(nums1);
    cout << ", k = " << k1 << endl;
    cout << "Output: " << solution.findKthLargest(nums1, k1) << endl;
    cout << "Expected: 5 (2nd largest)\n\n";
    
    // Test case 2
    vector<int> nums2 = {3, 2, 3, 1, 2, 4, 5, 5, 6};
    int k2 = 4;
    cout << "Input: nums = ";
    printVector(nums2);
    cout << ", k = " << k2 << endl;
    cout << "Output: " << solution.findKthLargest(nums2, k2) << endl;
    cout << "Expected: 4 (4th largest)\n\n";
    
    // Test case 3: k = 1 (largest element)
    vector<int> nums3 = {1, 2, 3, 4, 5};
    int k3 = 1;
    cout << "Input: nums = ";
    printVector(nums3);
    cout << ", k = " << k3 << endl;
    cout << "Output: " << solution.findKthLargest(nums3, k3) << endl;
    cout << "Expected: 5\n\n";
    
    // Test case 4: k = n (smallest element)
    vector<int> nums4 = {7, 6, 5, 4, 3, 2, 1};
    int k4 = 7;
    cout << "Input: nums = ";
    printVector(nums4);
    cout << ", k = " << k4 << endl;
    cout << "Output: " << solution.findKthLargest(nums4, k4) << endl;
    cout << "Expected: 1\n\n";
    
    // Compare all approaches
    vector<int> nums5 = {3, 2, 1, 5, 6, 4};
    int k5 = 2;
    cout << "Input: nums = ";
    printVector(nums5);
    cout << ", k = " << k5 << endl;
    cout << "Min Heap: " << solution.findKthLargest(nums5, k5) << endl;
    
    vector<int> nums5_copy = nums5;
    cout << "Max Heap: " << solution.findKthLargestMaxHeap(nums5_copy, k5) << endl;
    
    nums5_copy = nums5;
    cout << "Sorting: " << solution.findKthLargestSorting(nums5_copy, k5) << endl;
    
    nums5_copy = nums5;
    cout << "Quick Select: " << solution.findKthLargestQuickSelect(nums5_copy, k5) << endl;
    
    nums5_copy = nums5;
    cout << "nth_element: " << solution.findKthLargestNthElement(nums5_copy, k5) << endl;
    
    nums5_copy = nums5;
    cout << "partial_sort: " << solution.findKthLargestPartialSort(nums5_copy, k5) << endl;
    
    cout << "Expected: 5" << endl;
    
    return 0;
}