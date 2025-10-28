/*
Problem: 1 - Two Sum
Difficulty: Easy
Link: https://leetcode.com/problems/two-sum/

Approach:
Use unordered_map to store visited elements and their indices.
Time: O(N), Space: O(N)
*/
#include <vector>
#include <unordered_map>
#include <iostream>
using namespace std;

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        // Hash map: {value -> index}
        unordered_map<int, int> seen;
        
        for (int i = 0; i < nums.size(); i++) {
            int complement = target - nums[i];
            
            // Check if complement exists
            if (seen.find(complement) != seen.end()) {
                return {seen[complement], i};
            }
            
            // Store current element
            seen[nums[i]] = i;
        }
        
        return {};
    }
};

// Test cases
int main() {
    Solution sol;
    
    vector<int> nums1 = {2, 7, 11, 15};
    vector<int> result1 = sol.twoSum(nums1, 9);
    cout << "[" << result1[0] << ", " << result1[1] << "]" << endl;
    vector<int> nums2 = {3, 2, 4};
    vector<int> result2 = sol.twoSum(nums2, 6);
    cout << "[" << result2[0] << ", " << result2[1] << "]" << endl;

    return 0;
}