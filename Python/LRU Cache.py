"""
Problem: 146 - LRU Cache
Difficulty: Medium
Link: https://leetcode.com/problems/lru-cache/
Problem Statement:
Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.
- get(key): Return the value of the key if key exists in cache, else return -1.
- put(key, value): Update the value if key exists, or insert the key if not.
- When cache reaches capacity, the least recently used item should be evicted.
Approach:
Use dictionary for O(1) lookup.
Use Doubly LinkedList to maintain order (most recent at tail, least recent at head).
Combine both for O(1) get, put, and remove operations.
Time Complexity: O(1) for both get and put
Space Complexity: O(capacity)
"""

class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        
        # Initialize dummy nodes
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head
    
    # Add node right after head (most recent)
    def add_to_head(self, node):
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node
    
    # Remove node from list
    def remove_node(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
    
    # Move node to head (mark as recently used)
    def move_to_head(self, node):
        self.remove_node(node)
        self.add_to_head(node)
    
    # Remove least recently used (before tail)
    def remove_lru(self):
        lru = self.tail.prev
        self.remove_node(lru)
        return lru
    
    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        
        node = self.cache[key]
        self.move_to_head(node)  # Mark as recently used
        return node.value
    
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # Update existing key
            node = self.cache[key]
            node.value = value
            self.move_to_head(node)
        else:
            # Add new key
            new_node = Node(key, value)
            self.cache[key] = new_node
            self.add_to_head(new_node)
            
            # Evict LRU if capacity exceeded
            if len(self.cache) > self.capacity:
                lru = self.remove_lru()
                del self.cache[lru.key]


# Alternative: Using OrderedDict (simpler)
from collections import OrderedDict

class LRUCacheSimple:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = OrderedDict()
    
    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        
        # Move to end (mark as recently used)
        self.cache.move_to_end(key)
        return self.cache[key]
    
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # Update and move to end
            self.cache[key] = value
            self.cache.move_to_end(key)
        else:
            # Add new key
            self.cache[key] = value
            
            # Evict LRU if capacity exceeded
            if len(self.cache) > self.capacity:
                self.cache.popitem(last=False)


# Test cases
if __name__ == "__main__":
    # Test 1 - Manual implementation
    print("=== Manual Implementation ===")
    lru1 = LRUCache(2)
    lru1.put(1, 1)
    lru1.put(2, 2)
    print("get(1):", lru1.get(1))  # 1
    lru1.put(3, 3)  # Evicts key 2
    print("get(2):", lru1.get(2))  # -1
    lru1.put(4, 4)  # Evicts key 1
    print("get(1):", lru1.get(1))  # -1
    print("get(3):", lru1.get(3))  # 3
    print("get(4):", lru1.get(4))  # 4
    
    print()
    
    # Test 2 - Using OrderedDict
    print("=== OrderedDict Implementation ===")
    lru2 = LRUCacheSimple(2)
    lru2.put(1, 1)
    lru2.put(2, 2)
    print("get(1):", lru2.get(1))  # 1
    lru2.put(3, 3)  # Evicts key 2
    print("get(2):", lru2.get(2))  # -1
    lru2.put(4, 4)  # Evicts key 1
    print("get(1):", lru2.get(1))  # -1
    print("get(3):", lru2.get(3))  # 3
    print("get(4):", lru2.get(4))  # 4