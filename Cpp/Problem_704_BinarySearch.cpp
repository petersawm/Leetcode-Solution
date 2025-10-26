/*
Problem: 704 - Binary Search
Difficulty: Easy
Link: https://leetcode.com/problems/binary-search/

Problem Statement:
Given an array of integers nums which is sorted in ascending order, and an integer target,
write a function to search target in nums. If target exists, then return its index.
Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.

Approach:
Classic Binary Search:
1. Use two pointers: left and right
2. Calculate middle index: mid = (left + right) / 2
3. If nums[mid] == target, return mid
4. If nums[mid] < target, search right half (left = mid + 1)
5. If nums[mid] > target, search left half (right = mid - 1)
6. Repeat until left > right

Time Complexity: O(log N) - Halves search space each iteration
Space Complexity: O(1) - Only using pointers
*/

#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

class Solution {
public:
    // Approach 1: Iterative binary search
    int search(vector<int>& nums, int target) {
        int left = 0;
        int right = nums.size() - 1;
        
        while (left <= right) {
            // Calculate middle index (avoid overflow)
            int mid = left + (right - left) / 2;
            
            if (nums[mid] == target) {
                return mid;
            } else if (nums[mid] < target) {
                // Search right half
                left = mid + 1;
            } else {
                // Search left half
                right = mid - 1;
            }
        }
        
        // Target not found
        return -1;
    }
    
    // Approach 2: Recursive binary search
    int searchRecursive(vector<int>& nums, int target) {
        return binarySearchHelper(nums, target, 0, nums.size() - 1);
    }
    
private:
    int binarySearchHelper(vector<int>& nums, int target, int left, int right) {
        if (left > right) {
            return -1;
        }
        
        int mid = left + (right - left) / 2;
        
        if (nums[mid] == target) {
            return mid;
        } else if (nums[mid] < target) {
            return binarySearchHelper(nums, target, mid + 1, right);
        } else {
            return binarySearchHelper(nums, target, left, mid - 1);
        }
    }
    
public:
    // Approach 3: Alternative template
    int searchTemplate(vector<int>& nums, int target) {
        if (nums.empty()) {
            return -1;
        }
        
        int left = 0;
        int right = nums.size() - 1;
        
        while (left < right) {
            int mid = left + (right - left) / 2;
            
            if (nums[mid] < target) {
                left = mid + 1;
            } else {
                right = mid;
            }
        }
        
        // Check if target is found
        return nums[left] == target ? left : -1;
    }
    
    // Approach 4: Using STL lower_bound
    int searchSTL(vector<int>& nums, int target) {
        auto it = lower_bound(nums.begin(), nums.end(), target);
        
        if (it != nums.end() && *it == target) {
            return distance(nums.begin(), it);
        }
        return -1;
    }
    
    // Approach 5: Using STL binary_search (returns bool)
    int searchSTLBool(vector<int>& nums, int target) {
        if (binary_search(nums.begin(), nums.end(), target)) {
            // If found, use lower_bound to get index
            auto it = lower_bound(nums.begin(), nums.end(), target);
            return distance(nums.begin(), it);
        }
        return -1;
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
    vector<int> nums1 = {-1, 0, 3, 5, 9, 12};
    int target1 = 9;
    cout << "Input: nums = ";
    printVector(nums1);
    cout << ", target = " << target1 << endl;
    cout << "Output: " << solution.search(nums1, target1) << endl;
    cout << "Expected: 4\n\n";
    
    // Test case 2
    vector<int> nums2 = {-1, 0, 3, 5, 9, 12};
    int target2 = 2;
    cout << "Input: nums = ";
    printVector(nums2);
    cout << ", target = " << target2 << endl;
    cout << "Output: " << solution.search(nums2, target2) << endl;
    cout << "Expected: -1\n\n";
    
    // Test case 3: Single element - found
    vector<int> nums3 = {5};
    int target3 = 5;
    cout << "Input: nums = ";
    printVector(nums3);
    cout << ", target = " << target3 << endl;
    cout << "Output: " << solution.search(nums3, target3) << endl;
    cout << "Expected: 0\n\n";
    
    // Test case 4: Single element - not found
    vector<int> nums4 = {5};
    int target4 = 3;
    cout << "Input: nums = ";
    printVector(nums4);
    cout << ", target = " << target4 << endl;
    cout << "Output: " << solution.search(nums4, target4) << endl;
    cout << "Expected: -1\n\n";
    
    // Test case 5: Compare approaches
    vector<int> nums5 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
    int target5 = 1;
    cout << "Input: nums = ";
    printVector(nums5);
    cout << ", target = " << target5 << endl;
    cout << "Iterative: " << solution.search(nums5, target5) << endl;
    cout << "Recursive: " << solution.searchRecursive(nums5, target5) << endl;
    cout << "Template: " << solution.searchTemplate(nums5, target5) << endl;
    cout << "STL lower_bound: " << solution.searchSTL(nums5, target5) << endl;
    cout << "STL binary_search: " << solution.searchSTLBool(nums5, target5) << endl;
    cout << "Expected: 0\n";
    
    return 0;
}