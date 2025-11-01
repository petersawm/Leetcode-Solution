"""
Problem: 23 - Merge k Sorted Lists
Difficulty: Hard
Link: https://leetcode.com/problems/merge-k-sorted-lists/

Problem Statement:
You are given an array of k linked-lists lists, each linked-list is sorted in 
ascending order. Merge all the linked-lists into one sorted linked-list and return it.

Approach:
Multiple approaches:

1. Min Heap (Priority Queue) - Most efficient
   - Add first node of each list to heap
   - Pop smallest, add to result, push next node
   - Time: O(N log k), Space: O(k)

2. Divide and Conquer
   - Merge lists in pairs recursively
   - Time: O(N log k), Space: O(log k)

3. Merge one by one
   - Merge lists sequentially
   - Time: O(N*k), Space: O(1)

Time Complexity: O(N log k) where N = total nodes, k = number of lists
Space Complexity: O(k) for heap
"""

from typing import List, Optional
import heapq

# Definition for singly-linked list
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """Min Heap approach - Most efficient"""
        if not lists:
            return None
        
        # Min heap: (value, index, node)
        # Index is used to break ties for nodes with same value
        min_heap = []
        
        # Add first node of each list to heap
        for i, head in enumerate(lists):
            if head:
                heapq.heappush(min_heap, (head.val, i, head))
        
        # Dummy head for result
        dummy = ListNode(0)
        current = dummy
        
        while min_heap:
            val, i, node = heapq.heappop(min_heap)
            
            # Add to result
            current.next = node
            current = current.next
            
            # Add next node from same list
            if node.next:
                heapq.heappush(min_heap, (node.next.val, i, node.next))
        
        return dummy.next
    
    # Divide and Conquer approach
    def mergeKListsDivideConquer(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """Divide and conquer - merge in pairs"""
        if not lists:
            return None
        if len(lists) == 1:
            return lists[0]
        
        # Merge lists in pairs
        while len(lists) > 1:
            merged = []
            
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if i + 1 < len(lists) else None
                merged.append(self.mergeTwoLists(l1, l2))
            
            lists = merged
        
        return lists[0]
    
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """Merge two sorted lists"""
        dummy = ListNode(0)
        current = dummy
        
        while l1 and l2:
            if l1.val <= l2.val:
                current.next = l1
                l1 = l1.next
            else:
                current.next = l2
                l2 = l2.next
            current = current.next
        
        current.next = l1 or l2
        return dummy.next
    
    # Merge one by one approach
    def mergeKListsOneByOne(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """Merge lists one by one"""
        if not lists:
            return None
        
        result = lists[0]
        for i in range(1, len(lists)):
            result = self.mergeTwoLists(result, lists[i])
        
        return result
    
    # Alternative heap implementation without index
    def mergeKListsSimple(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """Simpler heap approach"""
        # Override comparison for ListNode
        ListNode.__lt__ = lambda self, other: self.val < other.val
        
        min_heap = []
        for head in lists:
            if head:
                heapq.heappush(min_heap, head)
        
        dummy = ListNode(0)
        current = dummy
        
        while min_heap:
            node = heapq.heappop(min_heap)
            current.next = node
            current = current.next
            
            if node.next:
                heapq.heappush(min_heap, node.next)
        
        return dummy.next


# Helper functions
def create_linked_list(values: List[int]) -> Optional[ListNode]:
    """Create linked list from array"""
    if not values:
        return None
    
    dummy = ListNode(0)
    current = dummy
    for val in values:
        current.next = ListNode(val)
        current = current.next
    
    return dummy.next

def linked_list_to_array(head: Optional[ListNode]) -> List[int]:
    """Convert linked list to array"""
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result


# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1
    lists1 = [
        create_linked_list([1, 4, 5]),
        create_linked_list([1, 3, 4]),
        create_linked_list([2, 6])
    ]
    print("Input: lists = [[1,4,5],[1,3,4],[2,6]]")
    result1 = solution.mergeKLists(lists1)
    print(f"Output: {linked_list_to_array(result1)}")
    print(f"Expected: [1,1,2,3,4,4,5,6]\n")
    
    # Test case 2: Empty lists
    lists2 = []
    print("Input: lists = []")
    result2 = solution.mergeKLists(lists2)
    print(f"Output: {linked_list_to_array(result2)}")
    print(f"Expected: []\n")
    
    # Test case 3: Single empty list
    lists3 = [create_linked_list([])]
    print("Input: lists = [[]]")
    result3 = solution.mergeKLists(lists3)
    print(f"Output: {linked_list_to_array(result3)}")
    print(f"Expected: []\n")
    
    # Test case 4: Single list
    lists4 = [create_linked_list([1, 2, 3])]
    print("Input: lists = [[1,2,3]]")
    result4 = solution.mergeKLists(lists4)
    print(f"Output: {linked_list_to_array(result4)}")
    print(f"Expected: [1,2,3]\n")
    
    # Compare approaches
    lists5 = [
        create_linked_list([1, 4, 5]),
        create_linked_list([1, 3, 4]),
        create_linked_list([2, 6])
    ]
    print("Compare approaches:")
    result5_heap = solution.mergeKLists([
        create_linked_list([1, 4, 5]),
        create_linked_list([1, 3, 4]),
        create_linked_list([2, 6])
    ])
    print(f"Min Heap: {linked_list_to_array(result5_heap)}")
    
    result5_dc = solution.mergeKListsDivideConquer([
        create_linked_list([1, 4, 5]),
        create_linked_list([1, 3, 4]),
        create_linked_list([2, 6])
    ])
    print(f"Divide & Conquer: {linked_list_to_array(result5_dc)}")
    
    result5_one = solution.mergeKListsOneByOne([
        create_linked_list([1, 4, 5]),
        create_linked_list([1, 3, 4]),
        create_linked_list([2, 6])
    ])
    print(f"One by One: {linked_list_to_array(result5_one)}")