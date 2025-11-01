/*
Problem: 23 - Merge k Sorted Lists
Difficulty: Hard
Link: https://leetcode.com/problems/merge-k-sorted-lists/

Problem Statement:
Merge all the k linked-lists into one sorted linked-list and return it.

Approach:
1. Min Heap (Priority Queue) - O(N log k)
2. Divide and Conquer - O(N log k)

Time Complexity: O(N log k) where N = total nodes, k = number of lists
Space Complexity: O(k) for heap
*/

#include <vector>
#include <queue>
#include <iostream>

using namespace std;

// Definition for singly-linked list
struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

class Solution {
public:
    // Approach 1: Min Heap (Priority Queue)
    ListNode* mergeKLists(vector<ListNode*>& lists) {
        // Comparator for min heap
        auto cmp = [](ListNode* a, ListNode* b) {
            return a->val > b->val;
        };
        priority_queue<ListNode*, vector<ListNode*>, decltype(cmp)> minHeap(cmp);
        
        // Add first node of each list to heap
        for (ListNode* head : lists) {
            if (head) {
                minHeap.push(head);
            }
        }
        
        // Dummy head for result
        ListNode dummy(0);
        ListNode* current = &dummy;
        
        while (!minHeap.empty()) {
            ListNode* node = minHeap.top();
            minHeap.pop();
            
            // Add to result
            current->next = node;
            current = current->next;
            
            // Add next node from same list
            if (node->next) {
                minHeap.push(node->next);
            }
        }
        
        return dummy.next;
    }
    
    // Approach 2: Divide and Conquer
    ListNode* mergeKListsDivideConquer(vector<ListNode*>& lists) {
        if (lists.empty()) {
            return nullptr;
        }
        
        return mergeKListsHelper(lists, 0, lists.size() - 1);
    }
    
private:
    ListNode* mergeKListsHelper(vector<ListNode*>& lists, int left, int right) {
        if (left == right) {
            return lists[left];
        }
        
        int mid = left + (right - left) / 2;
        ListNode* l1 = mergeKListsHelper(lists, left, mid);
        ListNode* l2 = mergeKListsHelper(lists, mid + 1, right);
        
        return mergeTwoLists(l1, l2);
    }
    
    ListNode* mergeTwoLists(ListNode* l1, ListNode* l2) {
        ListNode dummy(0);
        ListNode* current = &dummy;
        
        while (l1 && l2) {
            if (l1->val <= l2->val) {
                current->next = l1;
                l1 = l1->next;
            } else {
                current->next = l2;
                l2 = l2->next;
            }
            current = current->next;
        }
        
        current->next = l1 ? l1 : l2;
        return dummy.next;
    }
    
public:
    // Approach 3: Merge one by one
    ListNode* mergeKListsOneByOne(vector<ListNode*>& lists) {
        if (lists.empty()) {
            return nullptr;
        }
        
        ListNode* result = lists[0];
        for (int i = 1; i < lists.size(); i++) {
            result = mergeTwoLists(result, lists[i]);
        }
        
        return result;
    }
};

// Helper functions
ListNode* createLinkedList(const vector<int>& values) {
    if (values.empty()) {
        return nullptr;
    }
    
    ListNode dummy(0);
    ListNode* current = &dummy;
    for (int val : values) {
        current->next = new ListNode(val);
        current = current->next;
    }
    
    return dummy.next;
}

vector<int> linkedListToArray(ListNode* head) {
    vector<int> result;
    while (head) {
        result.push_back(head->val);
        head = head->next;
    }
    return result;
}

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
    vector<ListNode*> lists1 = {
        createLinkedList({1, 4, 5}),
        createLinkedList({1, 3, 4}),
        createLinkedList({2, 6})
    };
    cout << "Input: lists = [[1,4,5],[1,3,4],[2,6]]" << endl;
    ListNode* result1 = solution.mergeKLists(lists1);
    cout << "Output: ";
    printVector(linkedListToArray(result1));
    cout << "\nExpected: [1,1,2,3,4,4,5,6]\n" << endl;
    
    // Test case 2
    vector<ListNode*> lists2 = {};
    cout << "Input: lists = []" << endl;
    ListNode* result2 = solution.mergeKLists(lists2);
    cout << "Output: ";
    printVector(linkedListToArray(result2));
    cout << "\nExpected: []\n" << endl;
    
    // Test case 3
    vector<ListNode*> lists3 = {createLinkedList({})};
    cout << "Input: lists = [[]]" << endl;
    ListNode* result3 = solution.mergeKLists(lists3);
    cout << "Output: ";
    printVector(linkedListToArray(result3));
    cout << "\nExpected: []\n" << endl;
    
    // Test case 4
    vector<ListNode*> lists4 = {createLinkedList({1, 2, 3})};
    cout << "Input: lists = [[1,2,3]]" << endl;
    ListNode* result4 = solution.mergeKLists(lists4);
    cout << "Output: ";
    printVector(linkedListToArray(result4));
    cout << "\nExpected: [1,2,3]\n" << endl;
    
    // Compare approaches
    cout << "Compare approaches:" << endl;
    vector<ListNode*> lists5_heap = {
        createLinkedList({1, 4, 5}),
        createLinkedList({1, 3, 4}),
        createLinkedList({2, 6})
    };
    cout << "Min Heap: ";
    printVector(linkedListToArray(solution.mergeKLists(lists5_heap)));
    cout << endl;
    
    vector<ListNode*> lists5_dc = {
        createLinkedList({1, 4, 5}),
        createLinkedList({1, 3, 4}),
        createLinkedList({2, 6})
    };
    cout << "Divide & Conquer: ";
    printVector(linkedListToArray(solution.mergeKListsDivideConquer(lists5_dc)));
    cout << endl;
    
    vector<ListNode*> lists5_one = {
        createLinkedList({1, 4, 5}),
        createLinkedList({1, 3, 4}),
        createLinkedList({2, 6})
    };
    cout << "One by One: ";
    printVector(linkedListToArray(solution.mergeKListsOneByOne(lists5_one)));
    cout << endl;
    
    return 0;
}