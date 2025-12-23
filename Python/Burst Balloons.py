"""
Problem: 312 - Burst Balloons
Difficulty: Hard
Link: https://leetcode.com/problems/burst-balloons/
Problem Statement:
You are given n balloons, indexed from 0 to n - 1. Each balloon is painted with 
a number on it represented by an array nums. You are asked to burst all the 
balloons.
If the you burst balloon i you will get nums[left] * nums[i] * nums[right] coins. 
Here left and right are adjacent indices of i after all balloons between them 
have burst.
Find the maximum coins you can collect by bursting all balloons wisely.
Approach:
Use Dynamic Programming with reverse thinking.
Instead of thinking which balloon to burst first, think which balloon to burst last.
dp[left][right] = max coins bursting all balloons between left and right
Add padding 1s at boundaries to simplify edge cases.
Time Complexity: O(N^3)
Space Complexity: O(N^2)
"""

class Solution:
    def maxCoins(self, nums: list[int]) -> int:
        n = len(nums)
        
        # Create new array with padding 1s
        balloons = [1] + nums + [1]
        
        # dp[left][right] = max coins bursting balloons between left and right
        dp = [[0] * (n + 2) for _ in range(n + 2)]
        
        # Fill DP table
        # len is the distance between left and right
        for length in range(2, n + 2):
            for left in range(0, n + 2 - length):
                right = left + length - 1
                
                # Try bursting each balloon between left and right as last
                for k in range(left + 1, right):
                    # Coins from bursting balloons between left and k, plus k, plus balloons between k and right
                    coins = dp[left][k] + balloons[left] * balloons[k] * balloons[right] + dp[k][right]
                    dp[left][right] = max(dp[left][right], coins)
        
        return dp[0][n + 1]


# Alternative approach with Memoization
class SolutionMemo:
    def maxCoins(self, nums: list[int]) -> int:
        # Create new array with padding 1s
        balloons = [1] + nums + [1]
        memo = {}
        
        def dp(left, right):
            # Base case: no balloons between left and right
            if right - left <= 1:
                return 0
            
            if (left, right) in memo:
                return memo[(left, right)]
            
            max_coins = 0
            
            # Try bursting each balloon between left and right as last
            for k in range(left + 1, right):
                # Coins from bursting balloons between left and k
                coins_left = dp(left, k)
                
                # Coins from bursting k (when all balloons between left and right except k are burst)
                coins_k = balloons[left] * balloons[k] * balloons[right]
                
                # Coins from bursting balloons between k and right
                coins_right = dp(k, right)
                
                total = coins_left + coins_k + coins_right
                max_coins = max(max_coins, total)
            
            memo[(left, right)] = max_coins
            return max_coins
        
        return dp(0, len(balloons) - 1)


# Test cases
if __name__ == "__main__":
    sol = Solution()
    sol_memo = SolutionMemo()
    
    test_cases = [
        ([3, 1, 5, 8], 167),
        ([1, 5], 10),
        ([9, 76, 64, 21, 97, 60], None),  # Just check it runs
        ([3], 3),
    ]
    
    print("=== DP Approach ===")
    for nums, expected in test_cases:
        result = sol.maxCoins(nums)
        if expected is not None:
            status = "✓" if result == expected else "✗"
            print(f"{status} maxCoins({nums}) = {result} (expected {expected})")
        else:
            print(f"maxCoins({nums}) = {result}")
    
    print("\n=== Memoization Approach ===")
    for nums, expected in test_cases:
        result = sol_memo.maxCoins(nums)
        if expected is not None:
            status = "✓" if result == expected else "✗"
            print(f"{status} maxCoins({nums}) = {result} (expected {expected})")
        else:
            print(f"maxCoins({nums}) = {result}")