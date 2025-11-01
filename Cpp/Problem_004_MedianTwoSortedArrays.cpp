/*
Problem: 4 - Median of Two Sorted Arrays
Difficulty: Hard
Link: https://leetcode.com/problems/median-of-two-sorted-arrays/

Problem Statement:
Given two sorted arrays nums1 and nums2, return the median of the two sorted arrays.
The overall run time complexity should be O(log (m+n)).

Approach:
Use Binary Search on the smaller array to find correct partition.

Time Complexity: O(log(min(m,n))) - Binary search on smaller array
Space Complexity: O(1) - Only using pointers
*/

#include <vector>
#include <iostream>
#include <algorithm>
#include <climits>

using namespace std;

class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        // Ensure nums1 is the smaller array
        if (nums1.size() > nums2.size()) {
            return findMedianSortedArrays(nums2, nums1);
        }
        
        int m = nums1.size();
        int n = nums2.size();
        int left = 0, right = m;
        
        while (left <= right) {
            // Partition nums1
            int partition1 = (left + right) / 2;
            // Partition nums2
            int partition2 = (m + n + 1) / 2 - partition1;
            
            // Get max of left and min of right for both arrays
            int maxLeft1 = (partition1 == 0) ? INT_MIN : nums1[partition1 - 1];
            int minRight1 = (partition1 == m) ? INT_MAX : nums1[partition1];
            
            int maxLeft2 = (partition2 == 0) ? INT_MIN : nums2[partition2 - 1];
            int minRight2 = (partition2 == n) ? INT_MAX : nums2[partition2];
            
            // Check if we found the correct partition
            if (maxLeft1 <= minRight2 && maxLeft2 <= minRight1) {
                // Found correct partition
                if ((m + n) % 2 == 0) {
                    // Even number of elements
                    return (max(maxLeft1, maxLeft2) + min(minRight1, minRight2)) / 2.0;
                } else {
                    // Odd number of elements
                    return max(maxLeft1, maxLeft2);
                }
            } else if (maxLeft1 > minRight2) {
                // Too far right in nums1
                right = partition1 - 1;
            } else {
                // Too far left in nums1
                left = partition1 + 1;
            }
        }
        
        return 0.0;
    }
    
    // Alternative: Merge approach
    double findMedianSortedArraysMerge(vector<int>& nums1, vector<int>& nums2) {
        int m = nums1.size();
        int n = nums2.size();
        vector<int> merged(m + n);
        
        int i = 0, j = 0, k = 0;
        
        // Merge two sorted arrays
        while (i < m && j < n) {
            if (nums1[i] <= nums2[j]) {
                merged[k++] = nums1[i++];
            } else {
                merged[k++] = nums2[j++];
            }
        }
        
        // Add remaining elements
        while (i < m) {
            merged[k++] = nums1[i++];
        }
        while (j < n) {
            merged[k++] = nums2[j++];
        }
        
        // Find median
        int total = m + n;
        if (total % 2 == 0) {
            return (merged[total / 2 - 1] + merged[total / 2]) / 2.0;
        } else {
            return merged[total / 2];
        }
    }
    
    // Space-optimized approach
    double findMedianSortedArraysOptimized(vector<int>& nums1, vector<int>& nums2) {
        int m = nums1.size();
        int n = nums2.size();
        int total = m + n;
        int target = total / 2;
        
        int i = 0, j = 0;
        int prev = 0, curr = 0;
        
        // Iterate until we reach median position(s)
        for (int count = 0; count <= target; count++) {
            prev = curr;
            
            if (i < m && (j >= n || nums1[i] <= nums2[j])) {
                curr = nums1[i++];
            } else {
                curr = nums2[j++];
            }
        }
        
        if (total % 2 == 0) {
            return (prev + curr) / 2.0;
        } else {
            return curr;
        }
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
    vector<int> nums1 = {1, 3};
    vector<int> nums2 = {2};
    cout << "Input: nums1 = ";
    printVector(nums1);
    cout << ", nums2 = ";
    printVector(nums2);
    cout << "\nOutput: " << solution.findMedianSortedArrays(nums1, nums2) << endl;
    cout << "Expected: 2.0\n" << endl;
    
    // Test case 2
    vector<int> nums1_2 = {1, 2};
    vector<int> nums2_2 = {3, 4};
    cout << "Input: nums1 = ";
    printVector(nums1_2);
    cout << ", nums2 = ";
    printVector(nums2_2);
    cout << "\nOutput: " << solution.findMedianSortedArrays(nums1_2, nums2_2) << endl;
    cout << "Expected: 2.5\n" << endl;
    
    // Test case 3
    vector<int> nums1_3 = {};
    vector<int> nums2_3 = {1};
    cout << "Input: nums1 = ";
    printVector(nums1_3);
    cout << ", nums2 = ";
    printVector(nums2_3);
    cout << "\nOutput: " << solution.findMedianSortedArrays(nums1_3, nums2_3) << endl;
    cout << "Expected: 1.0\n" << endl;
    
    // Compare approaches
    vector<int> nums1_4 = {1, 3};
    vector<int> nums2_4 = {2, 4, 5};
    cout << "Input: nums1 = ";
    printVector(nums1_4);
    cout << ", nums2 = ";
    printVector(nums2_4);
    cout << "\nBinary Search: " << solution.findMedianSortedArrays(nums1_4, nums2_4) << endl;
    cout << "Merge: " << solution.findMedianSortedArraysMerge(nums1_4, nums2_4) << endl;
    cout << "Optimized: " << solution.findMedianSortedArraysOptimized(nums1_4, nums2_4) << endl;
    cout << "Expected: 3.0" << endl;
    
    return 0;
}