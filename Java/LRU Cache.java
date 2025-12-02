/*
Problem: 146 - LRU Cache
Difficulty: Medium
Link: https://leetcode.com/problems/lru-cache/
Problem Statement:
Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.
- get(key): Return the value of the key if key exists in cache, else return -1.
- put(key, value): Update the value if key exists, or insert the key if not.
- When cache reaches capacity, the least recently used item should be evicted.
Approach:
Use HashMap for O(1) lookup.
Use Doubly LinkedList to maintain order (most recent at tail, least recent at head).
Combine both for O(1) get, put, and remove operations.
Time Complexity: O(1) for both get and put
Space Complexity: O(capacity)
*/
import java.util.*;

class LRUCache {
    private static class Node {
        int key, value;
        Node prev, next;
        
        Node(int key, int value) {
            this.key = key;
            this.value = value;
        }
    }
    
    private int capacity;
    private Map<Integer, Node> cache;
    private Node head, tail;  // Dummy nodes
    
    public LRUCache(int capacity) {
        this.capacity = capacity;
        this.cache = new HashMap<>();
        
        // Initialize dummy nodes
        this.head = new Node(0, 0);
        this.tail = new Node(0, 0);
        head.next = tail;
        tail.prev = head;
    }
    
    // Add node right after head (most recent)
    private void addToHead(Node node) {
        node.next = head.next;
        node.prev = head;
        head.next.prev = node;
        head.next = node;
    }
    
    // Remove node from list
    private void removeNode(Node node) {
        node.prev.next = node.next;
        node.next.prev = node.prev;
    }
    
    // Move node to head (mark as recently used)
    private void moveToHead(Node node) {
        removeNode(node);
        addToHead(node);
    }
    
    // Remove least recently used (before tail)
    private Node removeLRU() {
        Node lru = tail.prev;
        removeNode(lru);
        return lru;
    }
    
    public int get(int key) {
        if (!cache.containsKey(key)) {
            return -1;
        }
        
        Node node = cache.get(key);
        moveToHead(node);  // Mark as recently used
        return node.value;
    }
    
    public void put(int key, int value) {
        if (cache.containsKey(key)) {
            // Update existing key
            Node node = cache.get(key);
            node.value = value;
            moveToHead(node);
        } else {
            // Add new key
            Node newNode = new Node(key, value);
            cache.put(key, newNode);
            addToHead(newNode);
            
            // Evict LRU if capacity exceeded
            if (cache.size() > capacity) {
                Node lru = removeLRU();
                cache.remove(lru.key);
            }
        }
    }
    
    // Test cases
    public static void main(String[] args) {
        // Test 1
        LRUCache lru1 = new LRUCache(2);
        lru1.put(1, 1);
        lru1.put(2, 2);
        System.out.println("get(1): " + lru1.get(1));  // 1
        lru1.put(3, 3);  // Evicts key 2
        System.out.println("get(2): " + lru1.get(2));  // -1
        lru1.put(4, 4);  // Evicts key 1
        System.out.println("get(1): " + lru1.get(1));  // -1
        System.out.println("get(3): " + lru1.get(3));  // 3
        System.out.println("get(4): " + lru1.get(4));  // 4
        
        System.out.println();
        
        // Test 2
        LRUCache lru2 = new LRUCache(1);
        lru2.put(2, 1);
        System.out.println("get(2): " + lru2.get(2));  // 1
        lru2.put(3, 2);  // Evicts key 2
        System.out.println("get(2): " + lru2.get(2));  // -1
    }
}