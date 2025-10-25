/*
Problem: 53 - Maximum Subarray
Difficulty: Medium
Link: https://leetcode.com/problems/maximum-subarray/

Problem Statement:
Given an integer array nums, find the subarray with the largest sum, 
and return its sum.

Approach:
Use Kadane's Algorithm - a dynamic programming approach:
1. Keep track of current_sum (max sum ending at current position)
2. Keep track of max_sum (overall maximum sum found so far)
3. At each position, decide whether to extend current subarray or start new one
4. current_sum = max(nums[i], current_sum + nums[i])
5. Update max_sum if current_sum is larger

The key insight: At each position, either continue the previous subarray 
or start a new subarray from current position.

Time Complexity: O(N) - Single pass through array
Space Complexity: O(1) - Only using two variables
*/

#include <vector>
#include <iostream>
#include <algorithm>
#include <climits>

using namespace std;

class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        // Handle empty array
        if (nums.empty()) return 0;
        
        // Initialize with first element
        int current_sum = nums[0];
        int max_sum = nums[0];
        
        // Iterate through array starting from second element
        for (int i = 1; i < nums.size(); i++) {
            // Either extend current subarray or start new one
            current_sum = max(nums[i], current_sum + nums[i]);
            
            // Update maximum sum if current is larger
            max_sum = max(max_sum, current_sum);
        }
        
        return max_sum;
    }
    
    // Alternative: Divide and Conquer approach
    int maxSubArrayDivideConquer(vector<int>& nums) {
        return maxSubArrayHelper(nums, 0, nums.size() - 1);
    }
    
private:
    int maxSubArrayHelper(vector<int>& nums, int left, int right) {
        // Base case: single element
        if (left == right) {
            return nums[left];
        }
        
        int mid = left + (right - left) / 2;
        
        // Maximum in left half
        int leftMax = maxSubArrayHelper(nums, left, mid);
        
        // Maximum in right half
        int rightMax = maxSubArrayHelper(nums, mid + 1, right);
        
        // Maximum crossing the middle
        int crossMax = maxCrossingSum(nums, left, mid, right);
        
        // Return maximum of three
        return max({leftMax, rightMax, crossMax});
    }
    
    int maxCrossingSum(vector<int>& nums, int left, int mid, int right) {
        // Sum of left part
        int leftSum = INT_MIN;
        int sum = 0;
        for (int i = mid; i >= left; i--) {
            sum += nums[i];
            leftSum = max(leftSum, sum);
        }
        
        // Sum of right part
        int rightSum = INT_MIN;
        sum = 0;
        for (int i = mid + 1; i <= right; i++) {
            sum += nums[i];
            rightSum = max(rightSum, sum);
        }
        
        return leftSum + rightSum;
    }
};

// Helper function to print array
void printArray(const vector<int>& arr) {
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
    vector<int> nums1 = {-2, 1, -3, 4, -1, 2, 1, -5, 4};
    cout << "Input: ";
    printArray(nums1);
    cout << "\nOutput: " << solution.maxSubArray(nums1) << endl;
    cout << "Expected: 6 (subarray [4,-1,2,1])\n\n";
    
    // Test case 2
    vector<int> nums2 = {1};
    cout << "Input: ";
    printArray(nums2);
    cout << "\nOutput: " << solution.maxSubArray(nums2) << endl;
    cout << "Expected: 1\n\n";
    
    // Test case 3
    vector<int> nums3 = {5, 4, -1, 7, 8};
    cout << "Input: ";
    printArray(nums3);
    cout << "\nOutput: " << solution.maxSubArray(nums3) << endl;
    cout << "Expected: 23\n\n";
    
    // Test case 4 (all negative)
    vector<int> nums4 = {-2, -3, -1, -4};
    cout << "Input: ";
    printArray(nums4);
    cout << "\nOutput: " << solution.maxSubArray(nums4) << endl;
    cout << "Expected: -1\n\n";
    
    // Test divide and conquer approach
    vector<int> nums5 = {-2, 1, -3, 4, -1, 2, 1, -5, 4};
    cout << "Input (Divide & Conquer): ";
    printArray(nums5);
    cout << "\nOutput: " << solution.maxSubArrayDivideConquer(nums5) << endl;
    cout << "Expected: 6\n";
    
    return 0;
}