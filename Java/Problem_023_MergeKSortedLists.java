/*
Problem: 23 - Merge k Sorted Lists
Difficulty: Hard
Link: https://leetcode.com/problems/merge-k-sorted-lists/

Problem Statement:
Merge all the k linked-lists into one sorted linked-list and return it.

Approach:
1. Min Heap (Priority Queue) - O(N log k)
2. Divide and Conquer - O(N log k)
3. Merge one by one - O(N*k)

Time Complexity: O(N log k) where N = total nodes, k = number of lists
Space Complexity: O(k) for heap
*/

import java.util.*;

// Definition for singly-linked list
class ListNode {
    int val;
    ListNode next;
    ListNode() {}
    ListNode(int val) { this.val = val; }
    ListNode(int val, ListNode next) { this.val = val; this.next = next; }
}

class Solution {
    // Approach 1: Min Heap (Priority Queue)
    public ListNode mergeKLists(ListNode[] lists) {
        if (lists == null || lists.length == 0) {
            return null;
        }
        
        // Min heap based on node values
        PriorityQueue<ListNode> minHeap = new PriorityQueue<>(
            (a, b) -> a.val - b.val
        );
        
        // Add first node of each list to heap
        for (ListNode head : lists) {
            if (head != null) {
                minHeap.offer(head);
            }
        }
        
        // Dummy head for result
        ListNode dummy = new ListNode(0);
        ListNode current = dummy;
        
        while (!minHeap.isEmpty()) {
            ListNode node = minHeap.poll();
            
            // Add to result
            current.next = node;
            current = current.next;
            
            // Add next node from same list
            if (node.next != null) {
                minHeap.offer(node.next);
            }
        }
        
        return dummy.next;
    }
    
    // Approach 2: Divide and Conquer
    public ListNode mergeKListsDivideConquer(ListNode[] lists) {
        if (lists == null || lists.length == 0) {
            return null;
        }
        
        return mergeKListsHelper(lists, 0, lists.length - 1);
    }
    
    private ListNode mergeKListsHelper(ListNode[] lists, int left, int right) {
        if (left == right) {
            return lists[left];
        }
        
        int mid = left + (right - left) / 2;
        ListNode l1 = mergeKListsHelper(lists, left, mid);
        ListNode l2 = mergeKListsHelper(lists, mid + 1, right);
        
        return mergeTwoLists(l1, l2);
    }
    
    private ListNode mergeTwoLists(ListNode l1, ListNode l2) {
        ListNode dummy = new ListNode(0);
        ListNode current = dummy;
        
        while (l1 != null && l2 != null) {
            if (l1.val <= l2.val) {
                current.next = l1;
                l1 = l1.next;
            } else {
                current.next = l2;
                l2 = l2.next;
            }
            current = current.next;
        }
        
        current.next = (l1 != null) ? l1 : l2;
        return dummy.next;
    }
    
    // Approach 3: Merge one by one
    public ListNode mergeKListsOneByOne(ListNode[] lists) {
        if (lists == null || lists.length == 0) {
            return null;
        }
        
        ListNode result = lists[0];
        for (int i = 1; i < lists.length; i++) {
            result = mergeTwoLists(result, lists[i]);
        }
        
        return result;
    }
    
    // Helper methods
    private static ListNode createLinkedList(int[] values) {
        if (values.length == 0) {
            return null;
        }
        
        ListNode dummy = new ListNode(0);
        ListNode current = dummy;
        for (int val : values) {
            current.next = new ListNode(val);
            current = current.next;
        }
        
        return dummy.next;
    }
    
    private static List<Integer> linkedListToArray(ListNode head) {
        List<Integer> result = new ArrayList<>();
        while (head != null) {
            result.add(head.val);
            head = head.next;
        }
        return result;
    }
    
    // Test cases
    public static void main(String[] args) {
        Solution solution = new Solution();
        
        // Test case 1
        ListNode[] lists1 = {
            createLinkedList(new int[]{1, 4, 5}),
            createLinkedList(new int[]{1, 3, 4}),
            createLinkedList(new int[]{2, 6})
        };
        System.out.println("Input: lists = [[1,4,5],[1,3,4],[2,6]]");
        ListNode result1 = solution.mergeKLists(lists1);
        System.out.println("Output: " + linkedListToArray(result1));
        System.out.println("Expected: [1,1,2,3,4,4,5,6]\n");
        
        // Test case 2
        ListNode[] lists2 = {};
        System.out.println("Input: lists = []");
        ListNode result2 = solution.mergeKLists(lists2);
        System.out.println("Output: " + linkedListToArray(result2));
        System.out.println("Expected: []\n");
        
        // Test case 3
        ListNode[] lists3 = {createLinkedList(new int[]{})};
        System.out.println("Input: lists = [[]]");
        ListNode result3 = solution.mergeKLists(lists3);
        System.out.println("Output: " + linkedListToArray(result3));
        System.out.println("Expected: []\n");
        
        // Test case 4
        ListNode[] lists4 = {createLinkedList(new int[]{1, 2, 3})};
        System.out.println("Input: lists = [[1,2,3]]");
        ListNode result4 = solution.mergeKLists(lists4);
        System.out.println("Output: " + linkedListToArray(result4));
        System.out.println("Expected: [1,2,3]\n");
        
        // Compare approaches
        System.out.println("Compare approaches:");
        ListNode[] lists5_heap = {
            createLinkedList(new int[]{1, 4, 5}),
            createLinkedList(new int[]{1, 3, 4}),
            createLinkedList(new int[]{2, 6})
        };
        System.out.println("Min Heap: " + linkedListToArray(solution.mergeKLists(lists5_heap)));
        
        ListNode[] lists5_dc = {
            createLinkedList(new int[]{1, 4, 5}),
            createLinkedList(new int[]{1, 3, 4}),
            createLinkedList(new int[]{2, 6})
        };
        System.out.println("Divide & Conquer: " + linkedListToArray(solution.mergeKListsDivideConquer(lists5_dc)));
        
        ListNode[] lists5_one = {
            createLinkedList(new int[]{1, 4, 5}),
            createLinkedList(new int[]{1, 3, 4}),
            createLinkedList(new int[]{2, 6})
        };
        System.out.println("One by One: " + linkedListToArray(solution.mergeKListsOneByOne(lists5_one)));
    }
}