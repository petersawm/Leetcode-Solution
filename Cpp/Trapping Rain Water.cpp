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
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    int trap(vector<int>& height) {
        if (height.empty() || height.size() < 3) {
            return 0;
        }
        
        int left = 0, right = height.size() - 1;
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
};

// Test cases
int main() {
    Solution sol;
    
    // Test 1
    vector<int> height1 = {0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1};
    cout << "Output: " << sol.trap(height1) << endl;
    // Expected: 6
    // Explanation: Water trapped at positions: 1+0+2+1+0+2 = 6
    
    // Test 2
    vector<int> height2 = {4, 2, 0, 3, 2, 5};
    cout << "Output: " << sol.trap(height2) << endl;
    // Expected: 9
    
    // Test 3
    vector<int> height3 = {};
    cout << "Output: " << sol.trap(height3) << endl;
    // Expected: 0
    
    // Test 4
    vector<int> height4 = {3, 0, 2, 0, 4};
    cout << "Output: " << sol.trap(height4) << endl;
    // Expected: 7
    
    return 0;
}