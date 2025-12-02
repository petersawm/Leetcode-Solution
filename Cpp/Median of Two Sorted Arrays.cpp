/*
Problem: 4 - Median of Two Sorted Arrays
Difficulty: Hard
Link: https://leetcode.com/problems/median-of-two-sorted-arrays/
Problem Statement:
Given two sorted arrays nums1 and nums2 of size m and n respectively, return 
the median of the two sorted arrays.
The overall run time complexity should be O(log (m+n)).
Approach:
Use Binary Search on the smaller array.
Partition both arrays such that left half and right half have equal elements.
Find median from partition positions.
Time Complexity: O(log(min(m, n)))
Space Complexity: O(1)
*/
#include <iostream>
#include <vector>
#include <algorithm>
#include <climits>
using namespace std;

class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        // Ensure nums1 is smaller
        if (nums1.size() > nums2.size()) {
            return findMedianSortedArrays(nums2, nums1);
        }
        
        int m = nums1.size();
        int n = nums2.size();
        int low = 0, high = m;
        
        while (low <= high) {
            int cut1 = (low + high) / 2;  // Partition point in nums1
            int cut2 = (m + n + 1) / 2 - cut1;  // Partition point in nums2
            
            // Edge cases: if partition is at boundary
            int left1 = cut1 == 0 ? INT_MIN : nums1[cut1 - 1];
            int left2 = cut2 == 0 ? INT_MIN : nums2[cut2 - 1];
            int right1 = cut1 == m ? INT_MAX : nums1[cut1];
            int right2 = cut2 == n ? INT_MAX : nums2[cut2];
            
            // Check if partition is valid
            if (left1 <= right2 && left2 <= right1) {
                // If total length is even
                if ((m + n) % 2 == 0) {
                    return (max(left1, left2) + min(right1, right2)) / 2.0;
                } else {
                    // If total length is odd
                    return (double) max(left1, left2);
                }
            } else if (left1 > right2) {
                // Move cut1 to left
                high = cut1 - 1;
            } else {
                // Move cut1 to right
                low = cut1 + 1;
            }
        }
        
        return -1.0;  // Should never reach here
    }
};

// Test cases
int main() {
    Solution sol;
    
    // Test 1
    vector<int> nums1_1 = {1, 3};
    vector<int> nums2_1 = {2};
    cout << "Output: " << sol.findMedianSortedArrays(nums1_1, nums2_1) << endl;
    // Expected: 2.0
    
    // Test 2
    vector<int> nums1_2 = {1, 2};
    vector<int> nums2_2 = {3, 4};
    cout << "Output: " << sol.findMedianSortedArrays(nums1_2, nums2_2) << endl;
    // Expected: 2.5
    
    // Test 3
    vector<int> nums1_3 = {0, 0};
    vector<int> nums2_3 = {0, 0};
    cout << "Output: " << sol.findMedianSortedArrays(nums1_3, nums2_3) << endl;
    // Expected: 0.0
    
    // Test 4
    vector<int> nums1_4 = {};
    vector<int> nums2_4 = {1};
    cout << "Output: " << sol.findMedianSortedArrays(nums1_4, nums2_4) << endl;
    // Expected: 1.0
    
    // Test 5
    vector<int> nums1_5 = {2};
    vector<int> nums2_5 = {};
    cout << "Output: " << sol.findMedianSortedArrays(nums1_5, nums2_5) << endl;
    // Expected: 2.0
    
    return 0;
}