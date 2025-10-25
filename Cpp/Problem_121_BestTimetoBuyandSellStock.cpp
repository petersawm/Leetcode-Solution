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

#include <vector>
#include <iostream>
#include <algorithm>
#include <climits>

using namespace std;

class Solution {
public:
    int maxProfit(vector<int>& prices) {
        // Edge case: empty or single price
        if (prices.empty() || prices.size() < 2) {
            return 0;
        }
        
        int minPrice = INT_MAX;  // Track minimum price seen so far
        int maxProfit = 0;       // Track maximum profit
        
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
    
    // More concise version using std::min and std::max
    int maxProfitConcise(vector<int>& prices) {
        int minPrice = INT_MAX;
        int maxProfit = 0;
        
        for (int price : prices) {
            minPrice = min(minPrice, price);
            maxProfit = max(maxProfit, price - minPrice);
        }
        
        return maxProfit;
    }
    
    // Alternative: Kadane's Algorithm approach
    int maxProfitKadane(vector<int>& prices) {
        if (prices.size() < 2) {
            return 0;
        }
        
        int maxProfit = 0;
        int currentProfit = 0;
        
        // Look at price differences between consecutive days
        for (int i = 1; i < prices.size(); i++) {
            int dailyChange = prices[i] - prices[i - 1];
            currentProfit = max(0, currentProfit + dailyChange);
            maxProfit = max(maxProfit, currentProfit);
        }
        
        return maxProfit;
    }
    
    // Alternative: Using two pointers (buy and sell)
    int maxProfitTwoPointers(vector<int>& prices) {
        if (prices.size() < 2) {
            return 0;
        }
        
        int buy = 0;        // Index to buy
        int sell = 1;       // Index to sell
        int maxProfit = 0;
        
        while (sell < prices.size()) {
            // If we can make profit
            if (prices[buy] < prices[sell]) {
                int profit = prices[sell] - prices[buy];
                maxProfit = max(maxProfit, profit);
            } else {
                // Found a lower buy price
                buy = sell;
            }
            sell++;
        }
        
        return maxProfit;
    }
};

// Helper function to print array
void printArray(const vector<int>& arr) {
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
    vector<int> prices1 = {7, 1, 5, 3, 6, 4};
    cout << "Input: prices = ";
    printArray(prices1);
    cout << "\nOutput: " << solution.maxProfit(prices1) << endl;
    cout << "Expected: 5 (Buy at 1, sell at 6)\n\n";
    
    // Test case 2
    vector<int> prices2 = {7, 6, 4, 3, 1};
    cout << "Input: prices = ";
    printArray(prices2);
    cout << "\nOutput: " << solution.maxProfit(prices2) << endl;
    cout << "Expected: 0 (No profit possible)\n\n";
    
    // Test case 3
    vector<int> prices3 = {2, 4, 1};
    cout << "Input: prices = ";
    printArray(prices3);
    cout << "\nOutput: " << solution.maxProfit(prices3) << endl;
    cout << "Expected: 2 (Buy at 2, sell at 4)\n\n";
    
    // Test case 4
    vector<int> prices4 = {3, 2, 6, 5, 0, 3};
    cout << "Input: prices = ";
    printArray(prices4);
    cout << "\nOutput (Standard): " << solution.maxProfit(prices4) << endl;
    cout << "Output (Kadane): " << solution.maxProfitKadane(prices4) << endl;
    cout << "Output (Two Pointers): " << solution.maxProfitTwoPointers(prices4) << endl;
    cout << "Expected: 4 (Buy at 2, sell at 6)\n\n";
    
    // Test case 5
    vector<int> prices5 = {1, 2};
    cout << "Input: prices = ";
    printArray(prices5);
    cout << "\nOutput: " << solution.maxProfit(prices5) << endl;
    cout << "Expected: 1\n";
    
    return 0;
}