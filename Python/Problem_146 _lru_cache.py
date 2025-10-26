"""
LeetCode Problem: 146 - LRU Cache
Difficulty: Medium
Link: https://leetcode.com/problems/lru-cache/

Problem Statement:
Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Implement the LRUCache class:
- LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
- int get(int key) Return the value of the key if exists, otherwise return -1.
- void put(int key, int value) Update the value of the key if exists. Otherwise, 
  add the key-value pair. If the number of keys exceeds capacity, evict the LRU key.

The functions get and put must each run in O(1) average time complexity.

Example:
Input:
["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]

Output:
[null, null, null, 1, null, -1, null, -1, 3, 4]

Explanation:
LRUCache lRUCache = new LRUCache(2);
lRUCache.put(1, 1); // cache is {1=1}
lRUCache.put(2, 2); // cache is {1=1, 2=2}
lRUCache.get(1);    // return 1
lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
lRUCache.get(2);    // returns -1 (not found)
lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
lRUCache.get(1);    // return -1 (not found)
lRUCache.get(3);    // return 3
lRUCache.get(4);    // return 4

Constraints:
- 1 <= capacity <= 3000
- 0 <= key <= 10^4
- 0 <= value <= 10^5
- At most 2 * 10^5 calls will be made to get and put
"""


class DLLNode:
    """Doubly Linked List Node for LRU Cache."""
    def __init__(self, key: int = 0, value: int = 0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:
    """
    Approach: Hash Map + Doubly Linked List
    
    Time Complexity: O(1) for both get and put
    Space Complexity: O(capacity)
    
    Key Insights:
    - Hash map provides O(1) lookup
    - Doubly linked list maintains order (most recent to least recent)
    - Most recent items at head, least recent at tail
    - Use dummy head and tail nodes to simplify edge cases
    
    Structure:
    Head (dummy) <-> [most recent] <-> ... <-> [least recent] <-> Tail (dummy)
    """
    
    def __init__(self, capacity: int):
        """
        Initialize LRU cache with given capacity.
        
        Args:
            capacity: Maximum number of items cache can hold
        """
        self.capacity = capacity
        self.cache = {}  # key -> DLLNode
        
        # Dummy head and tail for easier manipulation
        self.head = DLLNode()
        self.tail = DLLNode()
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def _add_to_head(self, node: DLLNode) -> None:
        """Add node right after head (most recent position)."""
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node
    
    def _remove_node(self, node: DLLNode) -> None:
        """Remove node from its current position."""
        node.prev.next = node.next
        node.next.prev = node.prev
    
    def _move_to_head(self, node: DLLNode) -> None:
        """Move existing node to head (mark as most recently used)."""
        self._remove_node(node)
        self._add_to_head(node)
    
    def _remove_tail(self) -> DLLNode:
        """Remove and return least recently used node (before tail)."""
        lru_node = self.tail.prev
        self._remove_node(lru_node)
        return lru_node
    
    def get(self, key: int) -> int:
        """
        Get value by key and mark as recently used.
        
        Args:
            key: Key to lookup
            
        Returns:
            Value if found, -1 otherwise
        """
        if key not in self.cache:
            return -1
        
        node = self.cache[key]
        self._move_to_head(node)  # Mark as recently used
        return node.value
    
    def put(self, key: int, value: int) -> None:
        """
        Put key-value pair, evicting LRU if necessary.
        
        Args:
            key: Key to insert/update
            value: Value to store
        """
        if key in self.cache:
            # Update existing key
            node = self.cache[key]
            node.value = value
            self._move_to_head(node)
        else:
            # Add new key
            new_node = DLLNode(key, value)
            self.cache[key] = new_node
            self._add_to_head(new_node)
            
            # Check capacity
            if len(self.cache) > self.capacity:
                # Evict LRU
                lru_node = self._remove_tail()
                del self.cache[lru_node.key]


class LRUCacheOrderedDict:
    """
    Alternative: Using Python's OrderedDict
    
    Simpler but uses built-in data structure.
    Good for production, but may not be accepted in interviews.
    """
    
    from collections import OrderedDict
    
    def __init__(self, capacity: int):
        self.cache = self.OrderedDict()
        self.capacity = capacity
    
    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        self.cache.move_to_end(key)  # Mark as recently used
        return self.cache[key]
    
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)  # Remove oldest


# TEST CASES

def test_solution():
    """Test cases from problem."""
    print("Testing LRU Cache Implementation")
    print("="*50)
    
    # Test case 1: Basic operations
    cache = LRUCache(2)
    
    cache.put(1, 1)
    assert cache.get(1) == 1, "Test 1.1 failed"
    
    cache.put(2, 2)
    assert cache.get(1) == 1, "Test 1.2 failed"
    assert cache.get(2) == 2, "Test 1.3 failed"
    
    cache.put(3, 3)  # Evicts key 1
    assert cache.get(1) == -1, "Test 1.4 failed"
    assert cache.get(2) == 2, "Test 1.5 failed"
    
    cache.put(4, 4)  # Evicts key 2
    assert cache.get(2) == -1, "Test 1.6 failed"
    assert cache.get(3) == 3, "Test 1.7 failed"
    assert cache.get(4) == 4, "Test 1.8 failed"
    
    print("✅ Test 1 passed: Basic operations")
    
    # Test case 2: Update existing key
    cache2 = LRUCache(2)
    cache2.put(1, 1)
    cache2.put(2, 2)
    cache2.put(1, 10)  # Update key 1
    assert cache2.get(1) == 10, "Test 2.1 failed"
    cache2.put(3, 3)  # Should evict key 2, not key 1
    assert cache2.get(2) == -1, "Test 2.2 failed"
    assert cache2.get(1) == 10, "Test 2.3 failed"
    
    print("✅ Test 2 passed: Update existing key")
    
    # Test case 3: Single capacity
    cache3 = LRUCache(1)
    cache3.put(1, 1)
    cache3.put(2, 2)  # Evicts 1
    assert cache3.get(1) == -1, "Test 3.1 failed"
    assert cache3.get(2) == 2, "Test 3.2 failed"
    
    print("✅ Test 3 passed: Single capacity")
    
    print("\n✅ All tests passed!")


def trace_operations():
    """Trace through operations to show cache state."""
    cache = LRUCache(2)
    
    def show_cache_state():
        """Display current cache state."""
        items = []
        node = cache.head.next
        while node != cache.tail:
            items.append(f"{node.key}:{node.value}")
            node = node.next
        print(f"  Cache state (MRU→LRU): [{', '.join(items)}]")
    
    print("\nTracing LRU Cache Operations:")
    print("="*50)
    
    print("1. put(1, 1)")
    cache.put(1, 1)
    show_cache_state()
    
    print("\n2. put(2, 2)")
    cache.put(2, 2)
    show_cache_state()
    
    print("\n3. get(1) → returns 1")
    result = cache.get(1)
    print(f"  Returned: {result}")
    show_cache_state()
    print("  (key 1 moved to front)")
    
    print("\n4. put(3, 3) → evicts key 2")
    cache.put(3, 3)
    show_cache_state()
    
    print("\n5. get(2) → returns -1")
    result = cache.get(2)
    print(f"  Returned: {result} (not found)")
    show_cache_state()
    
    print("\n6. put(4, 4) → evicts key 1")
    cache.put(4, 4)
    show_cache_state()


def performance_test():
    """Test performance with many operations."""
    import time
    
    cache = LRUCache(1000)
    
    # Fill cache
    start = time.time()
    for i in range(1000):
        cache.put(i, i * 10)
    fill_time = time.time() - start
    
    # Random access
    start = time.time()
    for i in range(10000):
        cache.get(i % 1000)
    get_time = time.time() - start
    
    # Mixed operations
    start = time.time()
    for i in range(5000):
        if i % 2 == 0:
            cache.get(i % 1000)
        else:
            cache.put(i + 1000, i)
    mixed_time = time.time() - start
    
    print("\nPerformance Test:")
    print("="*50)
    print(f"Fill 1000 items:     {fill_time*1000:8.4f}ms")
    print(f"10000 get ops:       {get_time*1000:8.4f}ms ({10000/get_time:.0f} ops/sec)")
    print(f"5000 mixed ops:      {mixed_time*1000:8.4f}ms")
    print(f"Average get time:    {get_time/10000*1000000:8.4f}μs")


if __name__ == "__main__":
    test_solution()
    trace_operations()
    performance_test()
