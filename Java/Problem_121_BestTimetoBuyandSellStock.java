/*
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
*/

class Solution {
    public int maxProfit(int[] prices) {
        // Edge case: empty or single price
        if (prices == null || prices.length < 2) {
            return 0;
        }
        
        int minPrice = Integer.MAX_VALUE;  // Track minimum price seen so far
        int maxProfit = 0;                 // Track maximum profit
        
        for (int price : prices) {
            // Update minimum price
            if (price < minPrice) {
                minPrice = price;
            } else {
                // Calculate profit if we sell at current price
                int currentProfit = price - minPrice;
                
                // Update maximum profit
                if (currentProfit > maxProfit) {
                    maxProfit = currentProfit;
                }
            }
        }
        
        return maxProfit;
    }
    
    // More concise version using Math methods
    public int maxProfitConcise(int[] prices) {
        int minPrice = Integer.MAX_VALUE;
        int maxProfit = 0;
        
        for (int price : prices) {
            minPrice = Math.min(minPrice, price);
            maxProfit = Math.max(maxProfit, price - minPrice);
        }
        
        return maxProfit;
    }
    
    // Alternative: Kadane's Algorithm approach
    public int maxProfitKadane(int[] prices) {
        if (prices.length < 2) {
            return 0;
        }
        
        int maxProfit = 0;
        int currentProfit = 0;
        
        // Look at price differences between consecutive days
        for (int i = 1; i < prices.length; i++) {
            int dailyChange = prices[i] - prices[i - 1];
            currentProfit = Math.max(0, currentProfit + dailyChange);
            maxProfit = Math.max(maxProfit, currentProfit);
        }
        
        return maxProfit;
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
        int[] prices1 = {7, 1, 5, 3, 6, 4};
        System.out.print("Input: prices = ");
        printArray(prices1);
        System.out.println("\nOutput: " + solution.maxProfit(prices1));
        System.out.println("Expected: 5 (Buy at 1, sell at 6)\n");
        
        // Test case 2
        int[] prices2 = {7, 6, 4, 3, 1};
        System.out.print("Input: prices = ");
        printArray(prices2);
        System.out.println("\nOutput: " + solution.maxProfit(prices2));
        System.out.println("Expected: 0 (No profit possible)\n");
        
        // Test case 3
        int[] prices3 = {2, 4, 1};
        System.out.print("Input: prices = ");
        printArray(prices3);
        System.out.println("\nOutput: " + solution.maxProfit(prices3));
        System.out.println("Expected: 2 (Buy at 2, sell at 4)\n");
        
        // Test case 4
        int[] prices4 = {3, 2, 6, 5, 0, 3};
        System.out.print("Input: prices = ");
        printArray(prices4);
        System.out.println("\nOutput (Standard): " + solution.maxProfit(prices4));
        System.out.println("Output (Kadane): " + solution.maxProfitKadane(prices4));
        System.out.println("Expected: 4 (Buy at 2, sell at 6)\n");
        
        // Test case 5
        int[] prices5 = {1, 2};
        System.out.print("Input: prices = ");
        printArray(prices5);
        System.out.println("\nOutput: " + solution.maxProfit(prices5));
        System.out.println("Expected: 1");
    }
}