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

import java.util.Arrays;

class Solution {
    public int[] productExceptSelf(int[] nums) {
        int n = nums.length;
        int[] result = new int[n];
        
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
    public int[] productExceptSelfVerbose(int[] nums) {
        int n = nums.length;
        
        // Prefix products: prefix[i] = product of nums[0] to nums[i-1]
        int[] prefix = new int[n];
        prefix[0] = 1;
        for (int i = 1; i < n; i++) {
            prefix[i] = prefix[i - 1] * nums[i - 1];
        }
        
        // Suffix products: suffix[i] = product of nums[i+1] to nums[n-1]
        int[] suffix = new int[n];
        suffix[n - 1] = 1;
        for (int i = n - 2; i >= 0; i--) {
            suffix[i] = suffix[i + 1] * nums[i + 1];
        }
        
        // Combine prefix and suffix
        int[] result = new int[n];
        for (int i = 0; i < n; i++) {
            result[i] = prefix[i] * suffix[i];
        }
        
        return result;
    }
    
    // Alternative: Left and right pass with explanation
    public int[] productExceptSelfDetailed(int[] nums) {
        int n = nums.length;
        int[] answer = new int[n];
        
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
        int[] nums1 = {1, 2, 3, 4};
        System.out.print("Input: nums = ");
        printArray(nums1);
        System.out.print("\nOutput: ");
        printArray(solution.productExceptSelf(nums1));
        System.out.println("\nExpected: [24,12,8,6]");
        System.out.println("Explanation: [2×3×4, 1×3×4, 1×2×4, 1×2×3]\n");
        
        // Test case 2
        int[] nums2 = {-1, 1, 0, -3, 3};
        System.out.print("Input: nums = ");
        printArray(nums2);
        System.out.print("\nOutput: ");
        printArray(solution.productExceptSelf(nums2));
        System.out.println("\nExpected: [0,0,9,0,0]\n");
        
        // Test case 3
        int[] nums3 = {2, 3, 4, 5};
        System.out.print("Input: nums = ");
        printArray(nums3);
        System.out.print("\nOutput: ");
        printArray(solution.productExceptSelf(nums3));
        System.out.println("\nExpected: [60,40,30,24]\n");
        
        // Test case 4: Two elements
        int[] nums4 = {1, 2};
        System.out.print("Input: nums = ");
        printArray(nums4);
        System.out.print("\nOutput: ");
        printArray(solution.productExceptSelf(nums4));
        System.out.println("\nExpected: [2,1]\n");
        
        // Test case 5: Compare approaches
        int[] nums5 = {-1, -2, -3, -4};
        System.out.print("Input: nums = ");
        printArray(nums5);
        System.out.print("\nOutput (Optimized): ");
        printArray(solution.productExceptSelf(nums5));
        System.out.print("\nOutput (Verbose): ");
        printArray(solution.productExceptSelfVerbose(nums5));
        System.out.print("\nOutput (Detailed): ");
        printArray(solution.productExceptSelfDetailed(nums5));
        System.out.println("\nExpected: [-24,-12,-8,-6]");
    }
}