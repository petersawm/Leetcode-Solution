"""
Problem: 146 - LRU Cache
Difficulty: Medium
Link: https://leetcode.com/problems/lru-cache/

Problem Statement:
Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Implement the LRUCache class:
- LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
- int get(int key) Return the value of the key if the key exists, otherwise return -1.
- void put(int key, int value) Update the value of the key if the key exists. Otherwise, 
  add the key-value pair to the cache. If the number of keys exceeds the capacity from this 
  operation, evict the least recently used key.

The functions get and put must each run in O(1) average time complexity.

Approach:
Use combination of Hash Map + Doubly Linked List:
- Hash Map: For O(1) key lookup
- Doubly Linked List: To maintain order (most recent at head, least recent at tail)

Operations:
- get: Move node to head
- put: Add to head, remove tail if over capacity

Time Complexity: O(1) for both get and put
Space Complexity: O(capacity) for storing key-value pairs
"""

class Node:
    """Doubly Linked List Node"""
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}  # key -> Node mapping
        
        # Dummy head and tail for easier manipulation
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def get(self, key: int) -> int:
        """Get value and move to most recent"""
        if key not in self.cache:
            return -1
        
        node = self.cache[key]
        # Move to head (most recently used)
        self._remove(node)
        self._add_to_head(node)
        
        return node.value
    
    def put(self, key: int, value: int) -> None:
        """Put key-value pair"""
        if key in self.cache:
            # Update existing key
            node = self.cache[key]
            node.value = value
            # Move to head
            self._remove(node)
            self._add_to_head(node)
        else:
            # Add new key
            node = Node(key, value)
            self.cache[key] = node
            self._add_to_head(node)
            
            # Check capacity
            if len(self.cache) > self.capacity:
                # Remove least recently used (tail)
                lru = self.tail.prev
                self._remove(lru)
                del self.cache[lru.key]
    
    def _add_to_head(self, node: Node) -> None:
        """Add node right after head"""
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node
    
    def _remove(self, node: Node) -> None:
        """Remove node from list"""
        node.prev.next = node.next
        node.next.prev = node.prev


# Alternative: Using OrderedDict (Python-specific)
from collections import OrderedDict

class LRUCacheOrderedDict:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = OrderedDict()
    
    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        
        # Move to end (most recent)
        self.cache.move_to_end(key)
        return self.cache[key]
    
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # Update and move to end
            self.cache.move_to_end(key)
        
        self.cache[key] = value
        
        # Check capacity
        if len(self.cache) > self.capacity:
            # Remove first item (least recent)
            self.cache.popitem(last=False)


# Test cases
if __name__ == "__main__":
    print("=== LRU Cache (Doubly Linked List) ===")
    lru = LRUCache(2)
    
    lru.put(1, 1)  # cache: {1=1}
    lru.put(2, 2)  # cache: {1=1, 2=2}
    print(f"get(1): {lru.get(1)}")  # returns 1, cache: {2=2, 1=1}
    
    lru.put(3, 3)  # evicts key 2, cache: {1=1, 3=3}
    print(f"get(2): {lru.get(2)}")  # returns -1 (not found)
    
    lru.put(4, 4)  # evicts key 1, cache: {3=3, 4=4}
    print(f"get(1): {lru.get(1)}")  # returns -1 (not found)
    print(f"get(3): {lru.get(3)}")  # returns 3
    print(f"get(4): {lru.get(4)}")  # returns 4
    
    print("\n=== LRU Cache (OrderedDict) ===")
    lru2 = LRUCacheOrderedDict(2)
    
    lru2.put(1, 1)
    lru2.put(2, 2)
    print(f"get(1): {lru2.get(1)}")  # returns 1
    
    lru2.put(3, 3)  # evicts key 2
    print(f"get(2): {lru2.get(2)}")  # returns -1
    
    lru2.put(4, 4)  # evicts key 1
    print(f"get(1): {lru2.get(1)}")  # returns -1
    print(f"get(3): {lru2.get(3)}")  # returns 3
    print(f"get(4): {lru2.get(4)}")  # returns 4
    
    # Test case 2
    print("\n=== Test Case 2 ===")
    lru3 = LRUCache(1)
    lru3.put(2, 1)
    print(f"get(2): {lru3.get(2)}")  # returns 1
    lru3.put(3, 2)  # evicts key 2
    print(f"get(2): {lru3.get(2)}")  # returns -1
    print(f"get(3): {lru3.get(3)}")  # returns 2