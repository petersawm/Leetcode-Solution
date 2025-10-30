/*
Problem: 146 - LRU Cache
Difficulty: Medium
Link: https://leetcode.com/problems/lru-cache/

Problem Statement:
Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Implement the LRUCache class with get and put methods that run in O(1) time.

Approach:
Use combination of unordered_map + list (doubly linked list):
- unordered_map: For O(1) key lookup
- list: To maintain order (most recent at front, least recent at back)

Time Complexity: O(1) for both get and put
Space Complexity: O(capacity) for storing key-value pairs
*/

#include <unordered_map>
#include <list>
#include <iostream>

using namespace std;

class LRUCache {
private:
    int capacity;
    list<pair<int, int>> cache;  // list of (key, value) pairs
    unordered_map<int, list<pair<int, int>>::iterator> map;  // key -> iterator mapping
    
public:
    LRUCache(int capacity) {
        this->capacity = capacity;
    }
    
    int get(int key) {
        if (map.find(key) == map.end()) {
            return -1;
        }
        
        // Move to front (most recently used)
        auto it = map[key];
        int value = it->second;
        cache.erase(it);
        cache.push_front({key, value});
        map[key] = cache.begin();
        
        return value;
    }
    
    void put(int key, int value) {
        if (map.find(key) != map.end()) {
            // Update existing key
            cache.erase(map[key]);
        } else if (cache.size() >= capacity) {
            // Remove least recently used (back)
            int lru_key = cache.back().first;
            cache.pop_back();
            map.erase(lru_key);
        }
        
        // Add to front (most recently used)
        cache.push_front({key, value});
        map[key] = cache.begin();
    }
};

// Alternative implementation with Node class
class Node {
public:
    int key;
    int value;
    Node* prev;
    Node* next;
    
    Node(int k = 0, int v = 0) : key(k), value(v), prev(nullptr), next(nullptr) {}
};

class LRUCacheNode {
private:
    int capacity;
    unordered_map<int, Node*> cache;
    Node* head;
    Node* tail;
    
    void addToHead(Node* node) {
        node->prev = head;
        node->next = head->next;
        head->next->prev = node;
        head->next = node;
    }
    
    void remove(Node* node) {
        node->prev->next = node->next;
        node->next->prev = node->prev;
    }
    
public:
    LRUCacheNode(int capacity) {
        this->capacity = capacity;
        head = new Node();
        tail = new Node();
        head->next = tail;
        tail->prev = head;
    }
    
    int get(int key) {
        if (cache.find(key) == cache.end()) {
            return -1;
        }
        
        Node* node = cache[key];
        // Move to head
        remove(node);
        addToHead(node);
        
        return node->value;
    }
    
    void put(int key, int value) {
        if (cache.find(key) != cache.end()) {
            // Update existing key
            Node* node = cache[key];
            node->value = value;
            // Move to head
            remove(node);
            addToHead(node);
        } else {
            // Add new key
            Node* node = new Node(key, value);
            cache[key] = node;
            addToHead(node);
            
            // Check capacity
            if (cache.size() > capacity) {
                // Remove least recently used
                Node* lru = tail->prev;
                remove(lru);
                cache.erase(lru->key);
                delete lru;
            }
        }
    }
    
    ~LRUCacheNode() {
        // Clean up
        Node* curr = head;
        while (curr) {
            Node* next = curr->next;
            delete curr;
            curr = next;
        }
    }
};

int main() {
    cout << "=== LRU Cache (list + unordered_map) ===" << endl;
    LRUCache lru(2);
    
    lru.put(1, 1);  // cache: {1=1}
    lru.put(2, 2);  // cache: {1=1, 2=2}
    cout << "get(1): " << lru.get(1) << endl;  // returns 1
    
    lru.put(3, 3);  // evicts key 2
    cout << "get(2): " << lru.get(2) << endl;  // returns -1
    
    lru.put(4, 4);  // evicts key 1
    cout << "get(1): " << lru.get(1) << endl;  // returns -1
    cout << "get(3): " << lru.get(3) << endl;  // returns 3
    cout << "get(4): " << lru.get(4) << endl;  // returns 4
    
    cout << "\n=== LRU Cache (Node-based) ===" << endl;
    LRUCacheNode lru2(2);
    
    lru2.put(1, 1);
    lru2.put(2, 2);
    cout << "get(1): " << lru2.get(1) << endl;  // returns 1
    
    lru2.put(3, 3);  // evicts key 2
    cout << "get(2): " << lru2.get(2) << endl;  // returns -1
    
    lru2.put(4, 4);  // evicts key 1
    cout << "get(1): " << lru2.get(1) << endl;  // returns -1
    cout << "get(3): " << lru2.get(3) << endl;  // returns 3
    cout << "get(4): " << lru2.get(4) << endl;  // returns 4
    
    // Test case 2
    cout << "\n=== Test Case 2 ===" << endl;
    LRUCache lru3(1);
    lru3.put(2, 1);
    cout << "get(2): " << lru3.get(2) << endl;  // returns 1
    lru3.put(3, 2);  // evicts key 2
    cout << "get(2): " << lru3.get(2) << endl;  // returns -1
    cout << "get(3): " << lru3.get(3) << endl;  // returns 2
    
    return 0;
}