/*
Problem: 23 - Merge K Sorted Lists
Difficulty: Hard
Link: https://leetcode.com/problems/merge-k-sorted-lists/
Problem Statement:
You are given an array of k linked-lists lists, each linked-list is sorted 
in ascending order.
Merge all the linked-lists into one sorted linked-list and return it.
Approach:
Use Min Heap (Priority Queue)
Add first node of each list to heap
Pop minimum, add its next node to heap
Continue until all nodes are processed
Time Complexity: O(N * k * log k) where N = total nodes
Space Complexity: O(k) for heap
*/
#include <iostream>
#include <vector>
#include <queue>
using namespace std;

/**
 * Definition for singly-linked list.
 */
struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

class Solution {
public:
    ListNode* mergeKLists(vector<ListNode*>& lists) {
        if (lists.empty()) {
            return nullptr;
        }
        
        // Min heap: comparator for min heap with custom pointer comparison
        auto cmp = [](ListNode* a, ListNode* b) {
            return a->val > b->val;  // For min heap, use >
        };
        priority_queue<ListNode*, vector<ListNode*>, decltype(cmp)> minHeap(cmp);
        
        // Add first node of each list to heap
        for (ListNode* list : lists) {
            if (list != nullptr) {
                minHeap.push(list);
            }
        }
        
        // Create dummy node
        ListNode* dummy = new ListNode(0);
        ListNode* current = dummy;
        
        // Process heap
        while (!minHeap.empty()) {
            // Get minimum node
            ListNode* minNode = minHeap.top();
            minHeap.pop();
            current->next = minNode;
            current = current->next;
            
            // Add next node to heap if exists
            if (minNode->next != nullptr) {
                minHeap.push(minNode->next);
            }
        }
        
        return dummy->next;
    }
    
    // Alternative approach: Divide and Conquer
    ListNode* mergeKLists_DivideAndConquer(vector<ListNode*>& lists) {
        if (lists.empty()) {
            return nullptr;
        }
        
        return mergeListsHelper(lists, 0, lists.size() - 1);
    }
    
private:
    ListNode* mergeListsHelper(vector<ListNode*>& lists, int left, int right) {
        // Base case
        if (left == right) {
            return lists[left];
        }
        
        if (left > right) {
            return nullptr;
        }
        
        // Divide
        int mid = left + (right - left) / 2;
        ListNode* leftMerged = mergeListsHelper(lists, left, mid);
        ListNode* rightMerged = mergeListsHelper(lists, mid + 1, right);
        
        // Conquer: merge two lists
        return merge2Lists(leftMerged, rightMerged);
    }
    
    ListNode* merge2Lists(ListNode* l1, ListNode* l2) {
        ListNode* dummy = new ListNode(0);
        ListNode* current = dummy;
        
        while (l1 != nullptr && l2 != nullptr) {
            if (l1->val <= l2->val) {
                current->next = l1;
                l1 = l1->next;
            } else {
                current->next = l2;
                l2 = l2->next;
            }
            current = current->next;
        }
        
        current->next = l1 != nullptr ? l1 : l2;
        return dummy->next;
    }
    
    // Helper method to create linked list from vector
    ListNode* createList(vector<int>& arr) {
        if (arr.empty()) return nullptr;
        ListNode* head = new ListNode(arr[0]);
        ListNode* current = head;
        for (int i = 1; i < arr.size(); i++) {
            current->next = new ListNode(arr[i]);
            current = current->next;
        }
        return head;
    }
    
    // Helper method to print linked list
    void printList(ListNode* head) {
        cout << "[";
        while (head != nullptr) {
            cout << head->val;
            if (head->next != nullptr) cout << ",";
            head = head->next;
        }
        cout << "]" << endl;
    }

public:
    // Test cases
    void test() {
        // Test 1
        vector<int> arr1 = {1, 4, 5};
        vector<int> arr2 = {1, 3, 4};
        vector<int> arr3 = {2, 6};
        
        vector<ListNode*> lists1 = {createList(arr1), createList(arr2), createList(arr3)};
        cout << "Output (Min Heap): ";
        printList(mergeKLists(lists1));
    }
};

// Test cases
int main() {
    Solution sol;
    sol.test();
    
    return 0;
}