"""
Problem: 121 - Best Time to Buy and Sell Stock
Difficulty: Easy
Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

Problem Statement:
You are given an array prices where prices[i] is the price of a given stock on the ith day.
You want to maximize your profit by choosing a single day to buy one stock and choosing 
a different day in the future to sell that stock.
Return the maximum profit you can achieve from this transaction. If you cannot achieve 
any profit, return 0.

Approach:
Use single pass with tracking minimum price and maximum profit:
1. Keep track of minimum price seen so far
2. For each price, calculate potential profit if we sell at current price
3. Update maximum profit if current profit is higher
4. Update minimum price if current price is lower

Key insight: We need to buy at lowest price and sell at highest price after that.

Time Complexity: O(N) - Single pass through array
Space Complexity: O(1) - Only using two variables
"""

from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Edge case: empty or single price
        if not prices or len(prices) < 2:
            return 0
        
        min_price = float('inf')  # Track minimum price seen so far
        max_profit = 0            # Track maximum profit
        
        for price in prices:
            # Update minimum price
            if price < min_price:
                min_price = price
            
            # Calculate profit if we sell at current price
            current_profit = price - min_price
            
            # Update maximum profit
            if current_profit > max_profit:
                max_profit = current_profit
        
        return max_profit
    
    # More concise version
    def maxProfitConcise(self, prices: List[int]) -> int:
        min_price = float('inf')
        max_profit = 0
        
        for price in prices:
            min_price = min(min_price, price)
            max_profit = max(max_profit, price - min_price)
        
        return max_profit
    
    # Alternative: Kadane's Algorithm approach (looking at daily changes)
    def maxProfitKadane(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0
        
        max_profit = 0
        current_profit = 0
        
        # Look at price differences between consecutive days
        for i in range(1, len(prices)):
            daily_change = prices[i] - prices[i-1]
            current_profit = max(0, current_profit + daily_change)
            max_profit = max(max_profit, current_profit)
        
        return max_profit


# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1
    prices1 = [7, 1, 5, 3, 6, 4]
    print(f"Input: prices = {prices1}")
    print(f"Output: {solution.maxProfit(prices1)}")
    print(f"Expected: 5 (Buy at 1, sell at 6)\n")
    
    # Test case 2
    prices2 = [7, 6, 4, 3, 1]
    print(f"Input: prices = {prices2}")
    print(f"Output: {solution.maxProfit(prices2)}")
    print(f"Expected: 0 (No profit possible)\n")
    
    # Test case 3
    prices3 = [2, 4, 1]
    print(f"Input: prices = {prices3}")
    print(f"Output: {solution.maxProfit(prices3)}")
    print(f"Expected: 2 (Buy at 2, sell at 4)\n")
    
    # Test case 4
    prices4 = [3, 2, 6, 5, 0, 3]
    print(f"Input: prices = {prices4}")
    print(f"Output (Standard): {solution.maxProfit(prices4)}")
    print(f"Output (Kadane): {solution.maxProfitKadane(prices4)}")
    print(f"Expected: 4 (Buy at 2, sell at 6)\n")
    
    # Test case 5
    prices5 = [1, 2]
    print(f"Input: prices = {prices5}")
    print(f"Output: {solution.maxProfit(prices5)}")
    print(f"Expected: 1")