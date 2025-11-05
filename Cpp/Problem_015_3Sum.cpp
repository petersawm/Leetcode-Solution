/*
Problem: 15 - 3Sum
Difficulty: Medium
Link: https://leetcode.com/problems/3sum/

Problem Statement:
Return all triplets [nums[i], nums[j], nums[k]] such that nums[i] + nums[j] + nums[k] == 0.
The solution set must not contain duplicate triplets.

Approach:
Sort + Two Pointers - O(N²) time

Time Complexity: O(N²)
Space Complexity: O(1) or O(N) for sorting
*/

#include <vector>
#include <algorithm>
#include <set>
#include <unordered_set>
#include <iostream>

using namespace std;

class Solution {
public:
    // Approach 1: Sort + Two Pointers
    vector<vector<int>> threeSum(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        vector<vector<int>> result;
        int n = nums.size();
        
        for (int i = 0; i < n - 2; i++) {
            // Skip duplicates for first element
            if (i > 0 && nums[i] == nums[i - 1]) {
                continue;
            }
            
            // Two pointers for remaining elements
            int left = i + 1, right = n - 1;
            int target = -nums[i];
            
            while (left < right) {
                int currentSum = nums[left] + nums[right];
                
                if (currentSum == target) {
                    result.push_back({nums[i], nums[left], nums[right]});
                    
                    // Skip duplicates for second element
                    while (left < right && nums[left] == nums[left + 1]) {
                        left++;
                    }
                    // Skip duplicates for third element
                    while (left < right && nums[right] == nums[right - 1]) {
                        right--;
                    }
                    
                    left++;
                    right--;
                } else if (currentSum < target) {
                    left++;
                } else {
                    right--;
                }
            }
        }
        
        return result;
    }
    
    // Approach 2: Using set to avoid duplicates
    vector<vector<int>> threeSumSet(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        set<vector<int>> resultSet;
        int n = nums.size();
        
        for (int i = 0; i < n - 2; i++) {
            int left = i + 1, right = n - 1;
            
            while (left < right) {
                int sum = nums[i] + nums[left] + nums[right];
                
                if (sum == 0) {
                    resultSet.insert({nums[i], nums[left], nums[right]});
                    left++;
                    right--;
                } else if (sum < 0) {
                    left++;
                } else {
                    right--;
                }
            }
        }
        
        return vector<vector<int>>(resultSet.begin(), resultSet.end());
    }
    
    // Approach 3: Hash map approach
    vector<vector<int>> threeSumHashMap(vector<int>& nums) {
        set<vector<int>> resultSet;
        int n = nums.size();
        
        for (int i = 0; i < n - 1; i++) {
            unordered_set<int> seen;
            for (int j = i + 1; j < n; j++) {
                int complement = -nums[i] - nums[j];
                if (seen.count(complement)) {
                    vector<int> triplet = {nums[i], nums[j], complement};
                    sort(triplet.begin(), triplet.end());
                    resultSet.insert(triplet);
                }
                seen.insert(nums[j]);
            }
        }
        
        return vector<vector<int>>(resultSet.begin(), resultSet.end());
    }
};

// Helper function to print vector
void printVector(const vector<int>& arr) {
    cout << "[";
    for (int i = 0; i < arr.size(); i++) {
        cout << arr[i];
        if (i < arr.size() - 1) cout << ",";
    }
    cout << "]";
}

void printResult(const vector<vector<int>>& result) {
    cout << "[";
    for (int i = 0; i < result.size(); i++) {
        cout << "[";
        for (int j = 0; j < result[i].size(); j++) {
            cout << result[i][j];
            if (j < result[i].size() - 1) cout << ",";
        }
        cout << "]";
        if (i < result.size() - 1) cout << ",";
    }
    cout << "]";
}

int main() {
    Solution solution;
    
    // Test case 1
    vector<int> nums1 = {-1, 0, 1, 2, -1, -4};
    cout << "Input: nums = ";
    printVector(nums1);
    cout << "\nOutput: ";
    printResult(solution.threeSum(nums1));
    cout << "\nExpected: [[-1,-1,2],[-1,0,1]]" << endl << endl;
    
    // Test case 2
    vector<int> nums2 = {0, 1, 1};
    cout << "Input: nums = ";
    printVector(nums2);
    cout << "\nOutput: ";
    printResult(solution.threeSum(nums2));
    cout << "\nExpected: []" << endl << endl;
    
    // Test case 3
    vector<int> nums3 = {0, 0, 0};
    cout << "Input: nums = ";
    printVector(nums3);
    cout << "\nOutput: ";
    printResult(solution.threeSum(nums3));
    cout << "\nExpected: [[0,0,0]]" << endl << endl;
    
    // Test case 4
    vector<int> nums4 = {-2, 0, 0, 2, 2};
    cout << "Input: nums = ";
    printVector(nums4);
    cout << "\nOutput: ";
    printResult(solution.threeSum(nums4));
    cout << "\nExpected: [[-2,0,2]]" << endl << endl;
    
    // Compare approaches
    vector<int> nums5 = {-1, 0, 1, 2, -1, -4};
    cout << "Input: nums = ";
    printVector(nums5);
    cout << "\nTwo Pointers: ";
    printResult(solution.threeSum(nums5));
    
    vector<int> nums5_copy = nums5;
    cout << "\nUsing Set: ";
    printResult(solution.threeSumSet(nums5_copy));
    
    nums5_copy = nums5;
    cout << "\nHash Map: ";
    printResult(solution.threeSumHashMap(nums5_copy));
    cout << endl;
    
    return 0;
}