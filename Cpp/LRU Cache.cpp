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
Use unordered_map for O(1) lookup.
Use Doubly LinkedList to maintain order (most recent at tail, least recent at head).
Combine both for O(1) get, put, and remove operations.
Time Complexity: O(1) for both get and put
Space Complexity: O(capacity)
*/
#include <iostream>
#include <unordered_map>
using namespace std;

struct Node {
    int key, value;
    Node* prev;
    Node* next;
    
    Node(int key, int value) : key(key), value(value), prev(nullptr), next(nullptr) {}
};

class LRUCache {
private:
    int capacity;
    unordered_map<int, Node*> cache;
    Node* head;
    Node* tail;
    
    // Add node right after head (most recent)
    void addToHead(Node* node) {
        node->next = head->next;
        node->prev = head;
        head->next->prev = node;
        head->next = node;
    }
    
    // Remove node from list
    void removeNode(Node* node) {
        node->prev->next = node->next;
        node->next->prev = node->prev;
    }
    
    // Move node to head (mark as recently used)
    void moveToHead(Node* node) {
        removeNode(node);
        addToHead(node);
    }
    
    // Remove least recently used (before tail)
    Node* removeLRU() {
        Node* lru = tail->prev;
        removeNode(lru);
        return lru;
    }
    
public:
    LRUCache(int capacity) : capacity(capacity) {
        // Initialize dummy nodes
        head = new Node(0, 0);
        tail = new Node(0, 0);
        head->next = tail;
        tail->prev = head;
    }
    
    int get(int key) {
        if (cache.find(key) == cache.end()) {
            return -1;
        }
        
        Node* node = cache[key];
        moveToHead(node);  // Mark as recently used
        return node->value;
    }
    
    void put(int key, int value) {
        if (cache.find(key) != cache.end()) {
            // Update existing key
            Node* node = cache[key];
            node->value = value;
            moveToHead(node);
        } else {
            // Add new key
            Node* newNode = new Node(key, value);
            cache[key] = newNode;
            addToHead(newNode);
            
            // Evict LRU if capacity exceeded
            if (cache.size() > capacity) {
                Node* lru = removeLRU();
                cache.erase(lru->key);
                delete lru;
            }
        }
    }
    
    ~LRUCache() {
        Node* current = head;
        while (current) {
            Node* temp = current;
            current = current->next;
            delete temp;
        }
    }
};

// Test cases
int main() {
    // Test 1
    LRUCache lru1(2);
    lru1.put(1, 1);
    lru1.put(2, 2);
    cout << "get(1): " << lru1.get(1) << endl;  // 1
    lru1.put(3, 3);  // Evicts key 2
    cout << "get(2): " << lru1.get(2) << endl;  // -1
    lru1.put(4, 4);  // Evicts key 1
    cout << "get(1): " << lru1.get(1) << endl;  // -1
    cout << "get(3): " << lru1.get(3) << endl;  // 3
    cout << "get(4): " << lru1.get(4) << endl;  // 4
    
    cout << endl;
    
    // Test 2
    LRUCache lru2(1);
    lru2.put(2, 1);
    cout << "get(2): " << lru2.get(2) << endl;  // 1
    lru2.put(3, 2);  // Evicts key 2
    cout << "get(2): " << lru2.get(2) << endl;  // -1
    
    return 0;
}