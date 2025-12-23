"""
Problem: 23 - Merge K Sorted Lists
Difficulty: Hard
Link: https://leetcode.com/problems/merge-k-sorted-lists/
Problem Statement:
You are given an array of k linked-lists lists, each linked-list is sorted 
in ascending order.
Merge all the linked-lists into one sorted linked-list and return it.
Approach 1: Min Heap (Priority Queue)
Add first node of each list to heap
Pop minimum, add its next node to heap
Continue until all nodes are processed
Time Complexity: O(N * k * log k) where N = total nodes
Space Complexity: O(k) for heap

Approach 2: Divide and Conquer
Recursively divide lists in half
Merge pairs of lists
Time Complexity: O(N * log k)
Space Complexity: O(log k) for recursion
"""
import heapq
from typing import List, Optional

# Definition for singly-linked list node.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # Approach 1: Min Heap
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        
        # Min heap with (value, counter, node) to break ties
        min_heap = []
        counter = 0
        
        # Add first node of each list to heap
        for lst in lists:
            if lst:
                # Use counter to ensure stable ordering for tie-breaking
                heapq.heappush(min_heap, (lst.val, counter, lst))
                counter += 1
        
        # Create dummy node
        dummy = ListNode(0)
        current = dummy
        
        # Process heap
        while min_heap:
            # Get minimum node
            _, _, min_node = heapq.heappop(min_heap)
            current.next = min_node
            current = current.next
            
            # Add next node to heap if exists
            if min_node.next:
                heapq.heappush(min_heap, (min_node.next.val, counter, min_node.next))
                counter += 1
        
        return dummy.next
    
    # Approach 2: Divide and Conquer
    def mergeKLists_DivideAndConquer(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        
        return self.mergeListsHelper(lists, 0, len(lists) - 1)
    
    def mergeListsHelper(self, lists: List[Optional[ListNode]], left: int, right: int) -> Optional[ListNode]:
        # Base cases
        if left == right:
            return lists[left]
        
        if left > right:
            return None
        
        # Divide
        mid = (left + right) // 2
        left_merged = self.mergeListsHelper(lists, left, mid)
        right_merged = self.mergeListsHelper(lists, mid + 1, right)
        
        # Conquer: merge two lists
        return self.merge2Lists(left_merged, right_merged)
    
    def merge2Lists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
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
        
        current.next = l1 if l1 else l2
        return dummy.next
    
    # Approach 3: Iterative Merge
    def mergeKLists_Iterative(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        
        # Keep merging pairs until only one list remains
        while len(lists) > 1:
            merged_lists = []
            
            # Merge pairs of lists
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if i + 1 < len(lists) else None
                merged_lists.append(self.merge2Lists(l1, l2))
            
            lists = merged_lists
        
        return lists[0]
    
    # Helper method to create linked list from list
    @staticmethod
    def createList(arr: List[int]) -> Optional[ListNode]:
        if not arr:
            return None
        head = ListNode(arr[0])
        current = head
        for val in arr[1:]:
            current.next = ListNode(val)
            current = current.next
        return head
    
    # Helper method to print linked list
    @staticmethod
    def printList(head: Optional[ListNode]) -> None:
        result = []
        while head:
            result.append(head.val)
            head = head.next
        print(result)


# Test cases
if __name__ == "__main__":
    sol = Solution()
    
    # Test 1
    lists1 = [
        Solution.createList([1, 4, 5]),
        Solution.createList([1, 3, 4]),
        Solution.createList([2, 6])
    ]
    print("Test 1 - Min Heap: ", end="")
    sol.printList(sol.mergeKLists(lists1))
    
    lists1_copy = [
        Solution.createList([1, 4, 5]),
        Solution.createList([1, 3, 4]),
        Solution.createList([2, 6])
    ]
    print("Test 1 - Divide and Conquer: ", end="")
    sol.printList(sol.mergeKLists_DivideAndConquer(lists1_copy))
    
    lists1_copy2 = [
        Solution.createList([1, 4, 5]),
        Solution.createList([1, 3, 4]),
        Solution.createList([2, 6])
    ]
    print("Test 1 - Iterative: ", end="")
    sol.printList(sol.mergeKLists_Iterative(lists1_copy2))
    
    # Test 2
    lists2 = []
    print("Test 2 - Empty: ", end="")
    sol.printList(sol.mergeKLists(lists2))
    
    # Test 3
    lists3 = [Solution.createList([])]
    print("Test 3 - Single Empty: ", end="")
    sol.printList(sol.mergeKLists(lists3))