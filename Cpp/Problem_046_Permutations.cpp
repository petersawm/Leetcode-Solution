/*
Problem: 46 - Permutations
Difficulty: Medium
Link: https://leetcode.com/problems/permutations/

Problem Statement:
Given an array nums of distinct integers, return all the possible permutations.
You can return the answer in any order.

Approach:
Use backtracking to generate all permutations. We build permutations by:
1. Starting with an empty current permutation
2. For each element not yet used, add it to current permutation
3. Recursively generate permutations with remaining elements
4. Backtrack by removing the element and trying the next one

Time Complexity: O(N! * N) - N! permutations, each takes O(N) to construct
Space Complexity: O(N) - Recursion depth and temporary storage (excluding output)
*/

#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

class Solution {
public:
    vector<vector<int>> permute(vector<int>& nums) {
        vector<vector<int>> result;
        vector<int> current;
        vector<bool> used(nums.size(), false);
        
        backtrack(nums, current, used, result);
        return result;
    }
    
private:
    void backtrack(vector<int>& nums, vector<int>& current, 
                   vector<bool>& used, vector<vector<int>>& result) {
        // Base case: current permutation is complete
        if (current.size() == nums.size()) {
            result.push_back(current);
            return;
        }
        
        // Try adding each unused number
        for (int i = 0; i < nums.size(); i++) {
            if (used[i]) continue;  // Skip if already used
            
            // Choose
            current.push_back(nums[i]);
            used[i] = true;
            
            // Explore
            backtrack(nums, current, used, result);
            
            // Unchoose (backtrack)
            current.pop_back();
            used[i] = false;
        }
    }
};

// Alternative approach using swap (in-place)
class SolutionSwap {
public:
    vector<vector<int>> permute(vector<int>& nums) {
        vector<vector<int>> result;
        backtrack(nums, 0, result);
        return result;
    }
    
private:
    void backtrack(vector<int>& nums, int start, vector<vector<int>>& result) {
        if (start == nums.size()) {
            result.push_back(nums);
            return;
        }
        
        for (int i = start; i < nums.size(); i++) {
            swap(nums[start], nums[i]);     // Choose
            backtrack(nums, start + 1, result);  // Explore
            swap(nums[start], nums[i]);     // Unchoose
        }
    }
};

// Test function
void printPermutations(const vector<vector<int>>& perms) {
    cout << "[";
    for (int i = 0; i < perms.size(); i++) {
        cout << "[";
        for (int j = 0; j < perms[i].size(); j++) {
            cout << perms[i][j];
            if (j < perms[i].size() - 1) cout << ",";
        }
        cout << "]";
        if (i < perms.size() - 1) cout << ",";
    }
    cout << "]" << endl;
}

int main() {
    Solution solution;
    
    // Test case 1
    vector<int> nums1 = {1, 2, 3};
    cout << "Input: nums = [1,2,3]" << endl;
    cout << "Output: ";
    vector<vector<int>> result1 = solution.permute(nums1);
    printPermutations(result1);
    
    // Test case 2
    vector<int> nums2 = {0, 1};
    cout << "\nInput: nums = [0,1]" << endl;
    cout << "Output: ";
    vector<vector<int>> result2 = solution.permute(nums2);
    printPermutations(result2);
    
    // Test case 3
    vector<int> nums3 = {1};
    cout << "\nInput: nums = [1]" << endl;
    cout << "Output: ";
    vector<vector<int>> result3 = solution.permute(nums3);
    printPermutations(result3);
    
    return 0;
}