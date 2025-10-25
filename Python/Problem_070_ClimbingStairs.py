"""
Problem: 70 - Climbing Stairs
Difficulty: Easy
Link: https://leetcode.com/problems/climbing-stairs/

Problem Statement:
You are climbing a staircase. It takes n steps to reach the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways 
can you climb to the top?

Approach:
This is a classic dynamic programming problem (similar to Fibonacci sequence).
To reach step n, we can either:
1. Come from step (n-1) and take 1 step
2. Come from step (n-2) and take 2 steps

Therefore: dp[n] = dp[n-1] + dp[n-2]

Base cases:
- dp[1] = 1 (only one way to reach step 1)
- dp[2] = 2 (two ways: 1+1 or 2)

We can optimize space by only keeping track of last two values.

Time Complexity: O(N) - Calculate each step once
Space Complexity: O(1) - Only store two variables
"""

class Solution:
    def climbStairs(self, n: int) -> int:
        # Base cases
        if n <= 2:
            return n
        
        # Only need to track previous two values
        prev2 = 1  # Ways to reach step 1
        prev1 = 2  # Ways to reach step 2
        
        # Calculate for steps 3 to n
        for i in range(3, n + 1):
            current = prev1 + prev2
            prev2 = prev1
            prev1 = current
        
        return prev1
    
    # Alternative: Using array (more intuitive but uses O(N) space)
    def climbStairsDP(self, n: int) -> int:
        if n <= 2:
            return n
        
        dp = [0] * (n + 1)
        dp[1] = 1
        dp[2] = 2
        
        for i in range(3, n + 1):
            dp[i] = dp[i-1] + dp[i-2]
        
        return dp[n]
    
    # Alternative: Recursive with memoization
    def climbStairsMemo(self, n: int) -> int:
        memo = {}
        return self._climb_helper(n, memo)
    
    def _climb_helper(self, n: int, memo: dict) -> int:
        if n <= 2:
            return n
        
        if n in memo:
            return memo[n]
        
        memo[n] = self._climb_helper(n-1, memo) + self._climb_helper(n-2, memo)
        return memo[n]
    
    # Mathematical approach using Fibonacci formula (most efficient)
    def climbStairsMath(self, n: int) -> int:
        # Fibonacci formula: F(n) = (φ^n - ψ^n) / √5
        # where φ = (1 + √5) / 2 and ψ = (1 - √5) / 2
        sqrt5 = 5 ** 0.5
        phi = (1 + sqrt5) / 2
        psi = (1 - sqrt5) / 2
        
        # Adjust for our sequence starting at n=1
        return int((phi ** (n + 1) - psi ** (n + 1)) / sqrt5)


# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1
    n1 = 2
    print(f"Input: n = {n1}")
    print(f"Output: {solution.climbStairs(n1)}")
    print(f"Expected: 2 (1+1 or 2)\n")
    
    # Test case 2
    n2 = 3
    print(f"Input: n = {n2}")
    print(f"Output: {solution.climbStairs(n2)}")
    print(f"Expected: 3 (1+1+1, 1+2, or 2+1)\n")
    
    # Test case 3
    n3 = 5
    print(f"Input: n = {n3}")
    print(f"Output: {solution.climbStairs(n3)}")
    print(f"Expected: 8\n")
    
    # Test case 4
    n4 = 10
    print(f"Input: n = {n4}")
    print(f"Output: {solution.climbStairs(n4)}")
    print(f"Expected: 89\n")
    
    # Compare all approaches
    n5 = 20
    print(f"Input: n = {n5}")
    print(f"Optimized: {solution.climbStairs(n5)}")
    print(f"DP Array: {solution.climbStairsDP(n5)}")
    print(f"Memoization: {solution.climbStairsMemo(n5)}")
    print(f"Mathematical: {solution.climbStairsMath(n5)}")
    print(f"All should give: 10946")
"""