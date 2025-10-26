/*
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
*/

#include <vector>
#include <iostream>

using namespace std;

class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        int n = nums.size();
        vector<int> result(n, 1);
        
        // Calculate prefix products and store in result
        // result[i] = product of all elements before index i
        int prefix = 1;
        for (int i = 0; i < n; i++) {
            result[i] = prefix;
            prefix *= nums[i];
        }
        
        // Calculate suffix products and multiply with result
        // Multiply result[i] with product of all elements after index i
        int suffix = 1;
        for (int i = n - 1; i >= 0; i--) {
            result[i] *= suffix;
            suffix *= nums[i];
        }
        
        return result;
    }
    
    // Alternative: Using separate prefix and suffix arrays (easier to understand)
    vector<int> productExceptSelfVerbose(vector<int>& nums) {
        int n = nums.size();
        
        // Prefix products: prefix[i] = product of nums[0] to nums[i-1]
        vector<int> prefix(n, 1);
        for (int i = 1; i < n; i++) {
            prefix[i] = prefix[i - 1] * nums[i - 1];
        }
        
        // Suffix products: suffix[i] = product of nums[i+1] to nums[n-1]
        vector<int> suffix(n, 1);
        for (int i = n - 2; i >= 0; i--) {
            suffix[i] = suffix[i + 1] * nums[i + 1];
        }
        
        // Combine prefix and suffix
        vector<int> result(n);
        for (int i = 0; i < n; i++) {
            result[i] = prefix[i] * suffix[i];
        }
        
        return result;
    }
    
    // Alternative: Left and right pass with detailed comments
    vector<int> productExceptSelfDetailed(vector<int>& nums) {
        int n = nums.size();
        vector<int> answer(n);
        
        // First pass: Calculate products of all elements to the left
        // answer[i] contains product of all nums[0...i-1]
        answer[0] = 1;  // No elements to the left of index 0
        for (int i = 1; i < n; i++) {
            answer[i] = answer[i - 1] * nums[i - 1];
        }
        
        // Second pass: Calculate products of all elements to the right
        // Multiply with existing values (left products)
        int rightProduct = 1;  // No elements to the right of last index
        for (int i = n - 1; i >= 0; i--) {
            answer[i] *= rightProduct;
            rightProduct *= nums[i];
        }
        
        return answer;
    }
    
    // Alternative: Using long long to avoid overflow (if needed)
    vector<int> productExceptSelfSafe(vector<int>& nums) {
        int n = nums.size();
        vector<int> result(n, 1);
        
        long long prefix = 1;
        for (int i = 0; i < n; i++) {
            result[i] = prefix;
            prefix *= nums[i];
        }
        
        long long suffix = 1;
        for (int i = n - 1; i >= 0; i--) {
            result[i] *= suffix;
            suffix *= nums[i];
        }
        
        return result;
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
    vector<int> nums1 = {1, 2, 3, 4};
    cout << "Input: nums = ";
    printVector(nums1);
    cout << "\nOutput: ";
    printVector(solution.productExceptSelf(nums1));
    cout << "\nExpected: [24,12,8,6]";
    cout << "\nExplanation: [2×3×4, 1×3×4, 1×2×4, 1×2×3]\n\n";
    
    // Test case 2
    vector<int> nums2 = {-1, 1, 0, -3, 3};
    cout << "Input: nums = ";
    printVector(nums2);
    cout << "\nOutput: ";
    printVector(solution.productExceptSelf(nums2));
    cout << "\nExpected: [0,0,9,0,0]\n\n";
    
    // Test case 3
    vector<int> nums3 = {2, 3, 4, 5};
    cout << "Input: nums = ";
    printVector(nums3);
    cout << "\nOutput: ";
    printVector(solution.productExceptSelf(nums3));
    cout << "\nExpected: [60,40,30,24]\n\n";
    
    // Test case 4: Two elements
    vector<int> nums4 = {1, 2};
    cout << "Input: nums = ";
    printVector(nums4);
    cout << "\nOutput: ";
    printVector(solution.productExceptSelf(nums4));
    cout << "\nExpected: [2,1]\n\n";
    
    // Test case 5: Compare approaches
    vector<int> nums5 = {-1, -2, -3, -4};
    cout << "Input: nums = ";
    printVector(nums5);
    cout << "\nOutput (Optimized): ";
    printVector(solution.productExceptSelf(nums5));
    
    vector<int> nums5_copy = nums5;
    cout << "\nOutput (Verbose): ";
    printVector(solution.productExceptSelfVerbose(nums5_copy));
    
    nums5_copy = nums5;
    cout << "\nOutput (Detailed): ";
    printVector(solution.productExceptSelfDetailed(nums5_copy));
    
    cout << "\nExpected: [-24,-12,-8,-6]\n";
    
    return 0;
}