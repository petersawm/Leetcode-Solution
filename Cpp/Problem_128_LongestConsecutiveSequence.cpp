/*
Problem: 128 - Longest Consecutive Sequence
Difficulty: Medium
Link: https://leetcode.com/problems/longest-consecutive-sequence/

Problem Statement:
Given an unsorted array of integers nums, return the length of the longest consecutive 
elements sequence. You must write an algorithm that runs in O(n) time.

Approach:
Use unordered_set for O(1) lookups - only count from sequence starts.

Time Complexity: O(N) - Each number visited at most twice
Space Complexity: O(N) - Hash set storage
*/

#include <vector>
#include <unordered_set>
#include <unordered_map>
#include <algorithm>
#include <iostream>

using namespace std;

class Solution {
public:
    // Approach 1: Hash Set - O(N) time
    int longestConsecutive(vector<int>& nums) {
        if (nums.empty()) {
            return 0;
        }
        
        unordered_set<int> numSet(nums.begin(), nums.end());
        int maxLength = 0;
        
        for (int num : numSet) {
            // Only start counting if this is the beginning of a sequence
            if (numSet.find(num - 1) == numSet.end()) {
                int currentNum = num;
                int currentLength = 1;
                
                // Count consecutive numbers
                while (numSet.find(currentNum + 1) != numSet.end()) {
                    currentNum++;
                    currentLength++;
                }
                
                maxLength = max(maxLength, currentLength);
            }
        }
        
        return maxLength;
    }
    
    // Approach 2: Sorting - O(N log N) time
    int longestConsecutiveSorting(vector<int>& nums) {
        if (nums.empty()) {
            return 0;
        }
        
        sort(nums.begin(), nums.end());
        int maxLength = 1;
        int currentLength = 1;
        
        for (int i = 1; i < nums.size(); i++) {
            // Skip duplicates
            if (nums[i] == nums[i-1]) {
                continue;
            }
            
            // Check if consecutive
            if (nums[i] == nums[i-1] + 1) {
                currentLength++;
            } else {
                maxLength = max(maxLength, currentLength);
                currentLength = 1;
            }
        }
        
        return max(maxLength, currentLength);
    }
    
    // Approach 3: HashMap tracking boundaries
    int longestConsecutiveHashMap(vector<int>& nums) {
        if (nums.empty()) {
            return 0;
        }
        
        unordered_map<int, int> numMap;
        int maxLength = 0;
        
        for (int num : nums) {
            if (numMap.find(num) != numMap.end()) {
                continue;
            }
            
            // Get lengths of adjacent sequences
            int left = numMap.count(num - 1) ? numMap[num - 1] : 0;
            int right = numMap.count(num + 1) ? numMap[num + 1] : 0;
            
            // New sequence length
            int length = left + right + 1;
            maxLength = max(maxLength, length);
            
            // Update boundaries
            numMap[num] = length;
            numMap[num - left] = length;
            numMap[num + right] = length;
        }
        
        return maxLength;
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

int main() {
    Solution solution;
    
    // Test case 1
    vector<int> nums1 = {100, 4, 200, 1, 3, 2};
    cout << "Input: nums = ";
    printVector(nums1);
    cout << "\nOutput: " << solution.longestConsecutive(nums1) << endl;
    cout << "Expected: 4\n" << endl;
    
    // Test case 2
    vector<int> nums2 = {0, 3, 7, 2, 5, 8, 4, 6, 0, 1};
    cout << "Input: nums = ";
    printVector(nums2);
    cout << "\nOutput: " << solution.longestConsecutive(nums2) << endl;
    cout << "Expected: 9\n" << endl;
    
    // Test case 3
    vector<int> nums3 = {};
    cout << "Input: nums = ";
    printVector(nums3);
    cout << "\nOutput: " << solution.longestConsecutive(nums3) << endl;
    cout << "Expected: 0\n" << endl;
    
    // Test case 4
    vector<int> nums4 = {1};
    cout << "Input: nums = ";
    printVector(nums4);
    cout << "\nOutput: " << solution.longestConsecutive(nums4) << endl;
    cout << "Expected: 1\n" << endl;
    
    // Test case 5
    vector<int> nums5 = {1, 2, 0, 1};
    cout << "Input: nums = ";
    printVector(nums5);
    cout << "\nOutput: " << solution.longestConsecutive(nums5) << endl;
    cout << "Expected: 3\n" << endl;
    
    // Compare approaches
    vector<int> nums6 = {100, 4, 200, 1, 3, 2};
    cout << "Input: nums = ";
    printVector(nums6);
    cout << "\nHash Set: " << solution.longestConsecutive(nums6) << endl;
    cout << "Sorting: " << solution.longestConsecutiveSorting(nums6) << endl;
    cout << "HashMap: " << solution.longestConsecutiveHashMap(nums6) << endl;
    cout << "Expected: 4" << endl;
    
    return 0;
}