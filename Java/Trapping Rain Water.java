/*
Problem: 42 - Trapping Rain Water
Difficulty: Hard
Link: https://leetcode.com/problems/trapping-rain-water/
Problem Statement:
Given n non-negative integers representing an elevation map where the width of 
each bar is 1, compute how much water can be trapped after raining.
Approach:
Use Two Pointers strategy.
Track maximum height from left and right.
For each position, water trapped = min(maxLeft, maxRight) - height[i]
Time Complexity: O(N)
Space Complexity: O(1)
*/
import java.util.*;

class Solution {
    public int trap(int[] height) {
        if (height == null || height.length < 3) {
            return 0;
        }
        
        int left = 0, right = height.length - 1;
        int maxLeft = 0, maxRight = 0;
        int water = 0;
        
        while (left < right) {
            // Move from side with smaller max
            if (height[left] < height[right]) {
                if (height[left] >= maxLeft) {
                    maxLeft = height[left];
                } else {
                    // Water trapped at this position
                    water += maxLeft - height[left];
                }
                left++;
            } else {
                if (height[right] >= maxRight) {
                    maxRight = height[right];
                } else {
                    // Water trapped at this position
                    water += maxRight - height[right];
                }
                right--;
            }
        }
        
        return water;
    }
    
    // Test cases
    public static void main(String[] args) {
        Solution sol = new Solution();
        
        // Test 1
        int[] height1 = {0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1};
        System.out.println("Output: " + sol.trap(height1));
        // Expected: 6
        // Explanation: Water trapped at positions: 1+0+2+1+0+2 = 6
        
        // Test 2
        int[] height2 = {4, 2, 0, 3, 2, 5};
        System.out.println("Output: " + sol.trap(height2));
        // Expected: 9
        
        // Test 3
        int[] height3 = {};
        System.out.println("Output: " + sol.trap(height3));
        // Expected: 0
        
        // Test 4
        int[] height4 = {3, 0, 2, 0, 4};
        System.out.println("Output: " + sol.trap(height4));
        // Expected: 7
    }
}