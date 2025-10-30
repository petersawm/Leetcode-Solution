/*
Problem: 146 - LRU Cache
Difficulty: Medium
Link: https://leetcode.com/problems/lru-cache/

Problem Statement:
Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Implement the LRUCache class with get and put methods that run in O(1) time.

Approach:
Use combination of Hash Map + Doubly Linked List:
- Hash Map: For O(1) key lookup
- Doubly Linked List: To maintain order (most recent at head, least recent at tail)

Time Complexity: O(1) for both get and put
Space Complexity: O(capacity) for storing key-value pairs
*/

import java.util.*;

// Node class for doubly linked list
class Node {
    int key;
    int value;
    Node prev;
    Node next;
    
    public Node(int key, int value) {
        this.key = key;
        this.value = value;
    }
}

// Main LRU Cache implementation
class LRUCache {
    private int capacity;
    private Map<Integer, Node> cache;
    private Node head;
    private Node tail;
    
    public LRUCache(int capacity) {
        this.capacity = capacity;
        this.cache = new HashMap<>();
        
        // Dummy head and tail for easier manipulation
        this.head = new Node(0, 0);
        this.tail = new Node(0, 0);
        head.next = tail;
        tail.prev = head;
    }
    
    public int get(int key) {
        if (!cache.containsKey(key)) {
            return -1;
        }
        
        Node node = cache.get(key);
        // Move to head (most recently used)
        remove(node);
        addToHead(node);
        
        return node.value;
    }
    
    public void put(int key, int value) {
        if (cache.containsKey(key)) {
            // Update existing key
            Node node = cache.get(key);
            node.value = value;
            // Move to head
            remove(node);
            addToHead(node);
        } else {
            // Add new key
            Node node = new Node(key, value);
            cache.put(key, node);
            addToHead(node);
            
            // Check capacity
            if (cache.size() > capacity) {
                // Remove least recently used (tail)
                Node lru = tail.prev;
                remove(lru);
                cache.remove(lru.key);
            }
        }
    }
    
    private void addToHead(Node node) {
        node.prev = head;
        node.next = head.next;
        head.next.prev = node;
        head.next = node;
    }
    
    private void remove(Node node) {
        node.prev.next = node.next;
        node.next.prev = node.prev;
    }
}

// Alternative: Using LinkedHashMap
class LRUCacheLinkedHashMap extends LinkedHashMap<Integer, Integer> {
    private int capacity;
    
    public LRUCacheLinkedHashMap(int capacity) {
        super(capacity, 0.75f, true);  // true for access-order
        this.capacity = capacity;
    }
    
    public int get(int key) {
        return super.getOrDefault(key, -1);
    }
    
    public void put(int key, int value) {
        super.put(key, value);
    }
    
    @Override
    protected boolean removeEldestEntry(Map.Entry<Integer, Integer> eldest) {
        return size() > capacity;
    }
}

// Test class
class LRUCacheTest {
    public static void main(String[] args) {
        System.out.println("=== LRU Cache (Doubly Linked List) ===");
        LRUCache lru = new LRUCache(2);
        
        lru.put(1, 1);  // cache: {1=1}
        lru.put(2, 2);  // cache: {1=1, 2=2}
        System.out.println("get(1): " + lru.get(1));  // returns 1
        
        lru.put(3, 3);  // evicts key 2
        System.out.println("get(2): " + lru.get(2));  // returns -1
        
        lru.put(4, 4);  // evicts key 1
        System.out.println("get(1): " + lru.get(1));  // returns -1
        System.out.println("get(3): " + lru.get(3));  // returns 3
        System.out.println("get(4): " + lru.get(4));  // returns 4
        
        System.out.println("\n=== LRU Cache (LinkedHashMap) ===");
        LRUCacheLinkedHashMap lru2 = new LRUCacheLinkedHashMap(2);
        
        lru2.put(1, 1);
        lru2.put(2, 2);
        System.out.println("get(1): " + lru2.get(1));  // returns 1
        
        lru2.put(3, 3);  // evicts key 2
        System.out.println("get(2): " + lru2.get(2));  // returns -1
        
        lru2.put(4, 4);  // evicts key 1
        System.out.println("get(1): " + lru2.get(1));  // returns -1
        System.out.println("get(3): " + lru2.get(3));  // returns 3
        System.out.println("get(4): " + lru2.get(4));  // returns 4
        
        // Test case 2
        System.out.println("\n=== Test Case 2 ===");
        LRUCache lru3 = new LRUCache(1);
        lru3.put(2, 1);
        System.out.println("get(2): " + lru3.get(2));  // returns 1
        lru3.put(3, 2);  // evicts key 2
        System.out.println("get(2): " + lru3.get(2));  // returns -1
        System.out.println("get(3): " + lru3.get(3));  // returns 2
    }
}