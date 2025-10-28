"""
Problem: 21 - Merge Two Sorted Lists
Difficulty: Easy
Link: https://leetcode.com/problems/merge-two-sorted-lists/

Problem Statement:
You are given the heads of two sorted linked lists list1 and list2.
Merge the two lists into one sorted list.

Approach:
Use a dummy node to simplify edge cases.
Compare nodes from both lists and attach the smaller one.
Continue until one list is exhausted, then attach the remainder.

Time Complexity: O(N + M) - where N, M are lengths of lists
Space Complexity: O(1) - only pointers used
"""
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], 
                      list2: Optional[ListNode]) -> Optional[ListNode]:
        # Dummy node to simplify logic
        dummy = ListNode(0)
        current = dummy
        
        # Merge while both lists have nodes
        while list1 and list2:
            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next
        
        # Attach remaining nodes
        current.next = list1 if list1 else list2
        
        return dummy.next

# Helper functions
def create_list(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    curr = head
    for val in arr[1:]:
        curr.next = ListNode(val)
        curr = curr.next
    return head

def list_to_array(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result

# Test
if __name__ == "__main__":
    solution = Solution()
    
    list1 = create_list([1, 2, 4])
    list2 = create_list([1, 3, 4])
    merged = solution.mergeTwoLists(list1, list2)
    print(f"Output: {list_to_array(merged)}")  # [1,1,2,3,4,4]