"""
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
"""

class Solution:
    def trap(self, height: list[int]) -> int:
        if not height or len(height) < 3:
            return 0
        
        left = 0
        right = len(height) - 1
        max_left = 0
        max_right = 0
        water = 0
        
        while left < right:
            # Move from side with smaller max
            if height[left] < height[right]:
                if height[left] >= max_left:
                    max_left = height[left]
                else:
                    # Water trapped at this position
                    water += max_left - height[left]
                left += 1
            else:
                if height[right] >= max_right:
                    max_right = height[right]
                else:
                    # Water trapped at this position
                    water += max_right - height[right]
                right -= 1
        
        return water


# Alternative approach using prefix and suffix arrays
class SolutionDP:
    def trap(self, height: list[int]) -> int:
        if not height or len(height) < 3:
            return 0
        
        n = len(height)
        
        # Calculate max height to the left of each position
        left_max = [0] * n
        left_max[0] = height[0]
        for i in range(1, n):
            left_max[i] = max(left_max[i - 1], height[i])
        
        # Calculate max height to the right of each position
        right_max = [0] * n
        right_max[n - 1] = height[n - 1]
        for i in range(n - 2, -1, -1):
            right_max[i] = max(right_max[i + 1], height[i])
        
        # Calculate trapped water
        water = 0
        for i in range(n):
            water += min(left_max[i], right_max[i]) - height[i]
        
        return water


# Test cases
if __name__ == "__main__":
    sol = Solution()
    sol_dp = SolutionDP()
    
    # Test 1
    height1 = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    print("Output (Two Pointers):", sol.trap(height1))
    print("Output (DP):", sol_dp.trap(height1))
    # Expected: 6
    
    # Test 2
    height2 = [4, 2, 0, 3, 2, 5]
    print("Output (Two Pointers):", sol.trap(height2))
    print("Output (DP):", sol_dp.trap(height2))
    # Expected: 9
    
    # Test 3
    height3 = []
    print("Output (Two Pointers):", sol.trap(height3))
    print("Output (DP):", sol_dp.trap(height3))
    # Expected: 0
    
    # Test 4
    height4 = [3, 0, 2, 0, 4]
    print("Output (Two Pointers):", sol.trap(height4))
    print("Output (DP):", sol_dp.trap(height4))
    # Expected: 7