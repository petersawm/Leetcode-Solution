/*
Problem: 322 - Coin Change
Difficulty: Medium
Link: https://leetcode.com/problems/coin-change/

Problem Statement:
You are given an integer array coins representing coins of different denominations 
and an integer amount representing a total amount of money.
Return the fewest number of coins that you need to make up that amount. 
If that amount of money cannot be made up by any combination of the coins, return -1.

Approach:
Use Dynamic Programming (Bottom-up):
1. Create dp array where dp[i] = minimum coins needed for amount i
2. Initialize dp[0] = 0 (0 coins needed for amount 0)
3. For each amount from 1 to target:
   - Try each coin denomination
   - If coin <= amount, update: dp[amount] = min(dp[amount], dp[amount-coin] + 1)
4. Return dp[target] if valid, else -1

This is the unbounded knapsack problem variant.

Time Complexity: O(N × M) where N = amount, M = number of coins
Space Complexity: O(N) for dp array
*/

#include <vector>
#include <iostream>
#include <algorithm>
#include <climits>

using namespace std;

class Solution {
public:
    int coinChange(vector<int>& coins, int amount) {
        // Edge case
        if (amount == 0) return 0;
        
        // Initialize dp array
        // dp[i] represents minimum coins needed for amount i
        vector<int> dp(amount + 1, INT_MAX);
        dp[0] = 0;  // Base case: 0 coins for amount 0
        
        // Build up solution for each amount
        for (int i = 1; i <= amount; i++) {
            // Try each coin
            for (int coin : coins) {
                // If coin can be used and previous state is valid
                if (coin <= i && dp[i - coin] != INT_MAX) {
                    dp[i] = min(dp[i], dp[i - coin] + 1);
                }
            }
        }
        
        // Return result
        return dp[amount] == INT_MAX ? -1 : dp[amount];
    }
    
    // Alternative: BFS approach (finds shortest path)
    int coinChangeBFS(vector<int>& coins, int amount) {
        if (amount == 0) return 0;
        
        vector<bool> visited(amount + 1, false);
        queue<pair<int, int>> q;  // {current_amount, num_coins}
        q.push({0, 0});
        visited[0] = true;
        
        while (!q.empty()) {
            auto [curr_amount, num_coins] = q.front();
            q.pop();
            
            // Try each coin
            for (int coin : coins) {
                int next_amount = curr_amount + coin;
                
                if (next_amount == amount) {
                    return num_coins + 1;
                }
                
                if (next_amount < amount && !visited[next_amount]) {
                    visited[next_amount] = true;
                    q.push({next_amount, num_coins + 1});
                }
            }
        }
        
        return -1;
    }
    
    // Alternative: Top-down DP with memoization
    int coinChangeMemo(vector<int>& coins, int amount) {
        vector<int> memo(amount + 1, -2);  // -2 means not computed
        return dpHelper(coins, amount, memo);
    }
    
private:
    int dpHelper(vector<int>& coins, int amount, vector<int>& memo) {
        if (amount == 0) return 0;
        if (amount < 0) return -1;
        
        if (memo[amount] != -2) return memo[amount];
        
        int minCoins = INT_MAX;
        for (int coin : coins) {
            int result = dpHelper(coins, amount - coin, memo);
            if (result >= 0 && result < minCoins) {
                minCoins = result + 1;
            }
        }
        
        memo[amount] = (minCoins == INT_MAX) ? -1 : minCoins;
        return memo[amount];
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
    vector<int> coins1 = {1, 2, 5};
    int amount1 = 11;
    cout << "Input: coins = ";
    printArray(coins1);
    cout << ", amount = " << amount1 << endl;
    cout << "Output: " << solution.coinChange(coins1, amount1) << endl;
    cout << "Expected: 3 (5+5+1)\n\n";
    
    // Test case 2
    vector<int> coins2 = {2};
    int amount2 = 3;
    cout << "Input: coins = ";
    printArray(coins2);
    cout << ", amount = " << amount2 << endl;
    cout << "Output: " << solution.coinChange(coins2, amount2) << endl;
    cout << "Expected: -1\n\n";
    
    // Test case 3
    vector<int> coins3 = {1};
    int amount3 = 0;
    cout << "Input: coins = ";
    printArray(coins3);
    cout << ", amount = " << amount3 << endl;
    cout << "Output: " << solution.coinChange(coins3, amount3) << endl;
    cout << "Expected: 0\n\n";
    
    // Test case 4
    vector<int> coins4 = {1, 2, 5};
    int amount4 = 100;
    cout << "Input: coins = ";
    printArray(coins4);
    cout << ", amount = " << amount4 << endl;
    cout << "Output (DP): " << solution.coinChange(coins4, amount4) << endl;
    cout << "Output (Memo): " << solution.coinChangeMemo(coins4, amount4) << endl;
    cout << "Expected: 20 (20 coins of 5)\n\n";
    
    // Test case 5
    vector<int> coins5 = {186, 419, 83, 408};
    int amount5 = 6249;
    cout << "Input: coins = ";
    printArray(coins5);
    cout << ", amount = " << amount5 << endl;
    cout << "Output: " << solution.coinChange(coins5, amount5) << endl;
    cout << "Expected: 20\n";
    
    return 0;
}