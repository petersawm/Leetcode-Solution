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
import java.util.*;

/**
 * Definition for singly-linked list.
 */
class ListNode {
    int val;
    ListNode next;
    ListNode() {}
    ListNode(int val) { this.val = val; }
    ListNode(int val, ListNode next) { this.val = val; this.next = next; }
}

class Solution {
    public ListNode mergeKLists(ListNode[] lists) {
        if (lists == null || lists.length == 0) {
            return null;
        }
        
        // Min heap to store nodes, ordered by value
        PriorityQueue<ListNode> minHeap = new PriorityQueue<>((a, b) -> a.val - b.val);
        
        // Add first node of each list to heap
        for (ListNode list : lists) {
            if (list != null) {
                minHeap.offer(list);
            }
        }
        
        // Create dummy node
        ListNode dummy = new ListNode(0);
        ListNode current = dummy;
        
        // Process heap
        while (!minHeap.isEmpty()) {
            // Get minimum node
            ListNode minNode = minHeap.poll();
            current.next = minNode;
            current = current.next;
            
            // Add next node to heap if exists
            if (minNode.next != null) {
                minHeap.offer(minNode.next);
            }
        }
        
        return dummy.next;
    }
    
    // Alternative approach: Divide and Conquer
    public ListNode mergeKLists_DivideAndConquer(ListNode[] lists) {
        if (lists == null || lists.length == 0) {
            return null;
        }
        
        return mergeListsHelper(lists, 0, lists.length - 1);
    }
    
    private ListNode mergeListsHelper(ListNode[] lists, int left, int right) {
        // Base case
        if (left == right) {
            return lists[left];
        }
        
        if (left > right) {
            return null;
        }
        
        // Divide
        int mid = left + (right - left) / 2;
        ListNode leftMerged = mergeListsHelper(lists, left, mid);
        ListNode rightMerged = mergeListsHelper(lists, mid + 1, right);
        
        // Conquer: merge two lists
        return merge2Lists(leftMerged, rightMerged);
    }
    
    private ListNode merge2Lists(ListNode l1, ListNode l2) {
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
        
        current.next = l1 != null ? l1 : l2;
        return dummy.next;
    }
    
    // Helper method to create linked list from array
    private ListNode createList(int[] arr) {
        if (arr == null || arr.length == 0) return null;
        ListNode head = new ListNode(arr[0]);
        ListNode current = head;
        for (int i = 1; i < arr.length; i++) {
            current.next = new ListNode(arr[i]);
            current = current.next;
        }
        return head;
    }
    
    // Helper method to print linked list
    private void printList(ListNode head) {
        List<Integer> result = new ArrayList<>();
        while (head != null) {
            result.add(head.val);
            head = head.next;
        }
        System.out.println(result);
    }
    
    // Test cases
    public static void main(String[] args) {
        Solution sol = new Solution();
        
        // Test 1
        ListNode[] lists1 = {
            sol.createList(new int[]{1, 4, 5}),
            sol.createList(new int[]{1, 3, 4}),
            sol.createList(new int[]{2, 6})
        };
        System.out.print("Output (Min Heap): ");
        sol.printList(sol.mergeKLists(lists1));
        
        // Test 2
        ListNode[] lists2 = {};
        System.out.print("Output (Empty): ");
        sol.printList(sol.mergeKLists(lists2));
        // Expected: []
        
        // Test 3
        ListNode[] lists3 = {
            sol.createList(new int[]{})
        };
        System.out.print("Output (Single Empty): ");
        sol.printList(sol.mergeKLists(lists3));
        // Expected: []
    }
}