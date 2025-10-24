"""
Problem: 206 - Reverse Linked List
Difficulty: Easy
Link: https://leetcode.com/problems/reverse-linked-list/

Problem Statement:
Given the head of a singly linked list, reverse the list, and return the 
reversed list.

Approach:
Use iterative approach with three pointers:
1. prev - keeps track of the previous node (initially None)
2. curr - current node being processed (starts at head)
3. next_node - temporarily stores the next node before we change the pointer

We iterate through the list, reversing the next pointer of each node to point
to the previous node instead of the next node.

Time Complexity: O(N) - Single pass through the list
Space Complexity: O(1) - Only using three pointer variables
"""

from typing import Optional

# Definition for singly-linked list node
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Initialize pointers
        prev = None
        curr = head
        
        # Iterate through the list
        while curr:
            # Save next node before changing pointer
            next_node = curr.next
            
            # Reverse the pointer
            curr.next = prev
            
            # Move prev and curr one step forward
            prev = curr
            curr = next_node
        
        # prev is now pointing to the new head
        return prev
    
    # Alternative: Recursive approach
    def reverseListRecursive(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Base case: empty list or single node
        if not head or not head.next:
            return head
        
        # Recursively reverse the rest of the list
        new_head = self.reverseListRecursive(head.next)
        
        # Reverse the current connection
        head.next.next = head
        head.next = None
        
        return new_head


# Helper functions for testing
def create_linked_list(values):
    """Create a linked list from a list of values"""
    if not values:
        return None
    
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

def linked_list_to_list(head):
    """Convert linked list to Python list for easy printing"""
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result

# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1
    head1 = create_linked_list([1, 2, 3, 4, 5])
    print("Input: [1,2,3,4,5]")
    reversed1 = solution.reverseList(head1)
    print(f"Output: {linked_list_to_list(reversed1)}")  # Expected: [5,4,3,2,1]
    
    # Test case 2
    head2 = create_linked_list([1, 2])
    print("\nInput: [1,2]")
    reversed2 = solution.reverseList(head2)
    print(f"Output: {linked_list_to_list(reversed2)}")  # Expected: [2,1]
    
    # Test case 3
    head3 = create_linked_list([])
    print("\nInput: []")
    reversed3 = solution.reverseList(head3)
    print(f"Output: {linked_list_to_list(reversed3)}")  # Expected: []
    
    # Test recursive approach
    head4 = create_linked_list([1, 2, 3])
    print("\nInput (Recursive): [1,2,3]")
    reversed4 = solution.reverseListRecursive(head4)
    print(f"Output: {linked_list_to_list(reversed4)}")  # Expected: [3,2,1]