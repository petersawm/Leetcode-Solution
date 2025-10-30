/*
Problem: 347 - Top K Frequent Elements
Difficulty: Medium
Link: https://leetcode.com/problems/top-k-frequent-elements/

Problem Statement:
Given an integer array nums and an integer k, return the k most frequent elements.
You may return the answer in any order.

Approach:
Multiple approaches:

1. Heap (Priority Queue) - Efficient
   - Count frequencies with hash map
   - Use min heap of size k to track top k elements
   - Time: O(N log k), Space: O(N)

2. Bucket Sort - Most efficient
   - Create buckets where index = frequency
   - Time: O(N), Space: O(N)

Time Complexity: O(N log k) - Heap approach
Space Complexity: O(N) - Hash map and heap
*/

#include <vector>
#include <unordered_map>
#include <queue>
#include <iostream>
#include <algorithm>

using namespace std;

class Solution {
public:
    // Approach 1: Min Heap
    vector<int> topKFrequent(vector<int>& nums, int k) {
        // Count frequencies
        unordered_map<int, int> count;
        for (int num : nums) {
            count[num]++;
        }
        
        // Min heap based on frequency
        // pair<frequency, element>
        priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> minHeap;
        
        for (auto& [num, freq] : count) {
            minHeap.push({freq, num});
            
            // Keep heap size at k
            if (minHeap.size() > k) {
                minHeap.pop();
            }
        }
        
        // Extract elements
        vector<int> result;
        while (!minHeap.empty()) {
            result.push_back(minHeap.top().second);
            minHeap.pop();
        }
        
        return result;
    }
    
    // Approach 2: Max Heap
    vector<int> topKFrequentMaxHeap(vector<int>& nums, int k) {
        unordered_map<int, int> count;
        for (int num : nums) {
            count[num]++;
        }
        
        // Max heap based on frequency
        auto cmp = [&count](int a, int b) {
            return count[a] < count[b];
        };
        priority_queue<int, vector<int>, decltype(cmp)> maxHeap(cmp);
        
        for (auto& [num, freq] : count) {
            maxHeap.push(num);
        }
        
        vector<int> result;
        for (int i = 0; i < k; i++) {
            result.push_back(maxHeap.top());
            maxHeap.pop();
        }
        
        return result;
    }
    
    // Approach 3: Bucket Sort - O(N) time
    vector<int> topKFrequentBucket(vector<int>& nums, int k) {
        // Count frequencies
        unordered_map<int, int> count;
        for (int num : nums) {
            count[num]++;
        }
        
        // Create buckets where index = frequency
        vector<vector<int>> buckets(nums.size() + 1);
        
        for (auto& [num, freq] : count) {
            buckets[freq].push_back(num);
        }
        
        // Collect top k frequent elements
        vector<int> result;
        for (int i = buckets.size() - 1; i >= 0 && result.size() < k; i--) {
            result.insert(result.end(), buckets[i].begin(), buckets[i].end());
        }
        
        // Return only k elements
        result.resize(k);
        return result;
    }
    
    // Approach 4: Using partial_sort
    vector<int> topKFrequentPartialSort(vector<int>& nums, int k) {
        unordered_map<int, int> count;
        for (int num : nums) {
            count[num]++;
        }
        
        vector<int> unique;
        for (auto& [num, freq] : count) {
            unique.push_back(num);
        }
        
        // Partial sort based on frequency (descending)
        partial_sort(unique.begin(), unique.begin() + k, unique.end(),
            [&count](int a, int b) {
                return count[a] > count[b];
            });
        
        return vector<int>(unique.begin(), unique.begin() + k);
    }
    
    // Approach 5: Using nth_element
    vector<int> topKFrequentNthElement(vector<int>& nums, int k) {
        unordered_map<int, int> count;
        for (int num : nums) {
            count[num]++;
        }
        
        vector<int> unique;
        for (auto& [num, freq] : count) {
            unique.push_back(num);
        }
        
        // Use nth_element to partition
        nth_element(unique.begin(), unique.begin() + k - 1, unique.end(),
            [&count](int a, int b) {
                return count[a] > count[b];
            });
        
        return vector<int>(unique.begin(), unique.begin() + k);
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
    vector<int> nums1 = {1, 1, 1, 2, 2, 3};
    int k1 = 2;
    cout << "Input: nums = ";
    printVector(nums1);
    cout << ", k = " << k1 << endl;
    cout << "Output: ";
    printVector(solution.topKFrequent(nums1, k1));
    cout << "\nExpected: [1,2]\n\n";
    
    // Test case 2
    vector<int> nums2 = {1};
    int k2 = 1;
    cout << "Input: nums = ";
    printVector(nums2);
    cout << ", k = " << k2 << endl;
    cout << "Output: ";
    printVector(solution.topKFrequent(nums2, k2));
    cout << "\nExpected: [1]\n\n";
    
    // Test case 3
    vector<int> nums3 = {4, 1, -1, 2, -1, 2, 3};
    int k3 = 2;
    cout << "Input: nums = ";
    printVector(nums3);
    cout << ", k = " << k3 << endl;
    cout << "Output: ";
    printVector(solution.topKFrequent(nums3, k3));
    cout << "\nExpected: [-1,2] (any order)\n\n";
    
    // Compare approaches
    vector<int> nums4 = {1, 1, 1, 2, 2, 3};
    int k4 = 2;
    cout << "Input: nums = ";
    printVector(nums4);
    cout << ", k = " << k4 << endl;
    cout << "Min Heap: ";
    printVector(solution.topKFrequent(nums4, k4));
    cout << "\nMax Heap: ";
    printVector(solution.topKFrequentMaxHeap(nums4, k4));
    cout << "\nBucket Sort: ";
    printVector(solution.topKFrequentBucket(nums4, k4));
    cout << "\nPartial Sort: ";
    printVector(solution.topKFrequentPartialSort(nums4, k4));
    cout << "\nNth Element: ";
    printVector(solution.topKFrequentNthElement(nums4, k4));
    cout << "\nExpected: [1,2]" << endl;
    
    return 0;
}