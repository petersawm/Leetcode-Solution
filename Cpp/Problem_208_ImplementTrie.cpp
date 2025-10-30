/*
Problem: 208 - Implement Trie (Prefix Tree)
Difficulty: Medium
Link: https://leetcode.com/problems/implement-trie-prefix-tree/

Problem Statement:
Implement the Trie class:
- Trie() Initializes the trie object.
- void insert(String word) Inserts the string word into the trie.
- boolean search(String word) Returns true if the string word is in the trie.
- boolean startsWith(String prefix) Returns true if there is a word with the prefix.

Time Complexity:
- insert: O(M) where M is word length
- search: O(M) where M is word length
- startsWith: O(M) where M is prefix length

Space Complexity: O(N × M) where N is number of words, M is average word length
*/

#include <string>
#include <unordered_map>
#include <vector>
#include <iostream>

using namespace std;

// Node class for Trie
class TrieNode {
public:
    unordered_map<char, TrieNode*> children;
    bool isEndOfWord;
    
    TrieNode() {
        isEndOfWord = false;
    }
};

// Main Trie implementation
class Trie {
private:
    TrieNode* root;
    
public:
    Trie() {
        root = new TrieNode();
    }
    
    void insert(string word) {
        TrieNode* node = root;
        
        for (char c : word) {
            // Create new node if character doesn't exist
            if (node->children.find(c) == node->children.end()) {
                node->children[c] = new TrieNode();
            }
            
            // Move to child node
            node = node->children[c];
        }
        
        // Mark end of word
        node->isEndOfWord = true;
    }
    
    bool search(string word) {
        TrieNode* node = root;
        
        for (char c : word) {
            if (node->children.find(c) == node->children.end()) {
                return false;
            }
            node = node->children[c];
        }
        
        // Word exists only if we reach end of word marker
        return node->isEndOfWord;
    }
    
    bool startsWith(string prefix) {
        TrieNode* node = root;
        
        for (char c : prefix) {
            if (node->children.find(c) == node->children.end()) {
                return false;
            }
            node = node->children[c];
        }
        
        // If we successfully traversed all characters, prefix exists
        return true;
    }
    
    ~Trie() {
        deleteTrie(root);
    }
    
private:
    void deleteTrie(TrieNode* node) {
        for (auto& pair : node->children) {
            deleteTrie(pair.second);
        }
        delete node;
    }
};

// Alternative: Array-based implementation
class TrieNodeArray {
public:
    TrieNodeArray* children[26];
    bool isEndOfWord;
    
    TrieNodeArray() {
        for (int i = 0; i < 26; i++) {
            children[i] = nullptr;
        }
        isEndOfWord = false;
    }
};

class TrieArray {
private:
    TrieNodeArray* root;
    
public:
    TrieArray() {
        root = new TrieNodeArray();
    }
    
    void insert(string word) {
        TrieNodeArray* node = root;
        
        for (char c : word) {
            int index = c - 'a';
            
            if (node->children[index] == nullptr) {
                node->children[index] = new TrieNodeArray();
            }
            
            node = node->children[index];
        }
        
        node->isEndOfWord = true;
    }
    
    bool search(string word) {
        TrieNodeArray* node = root;
        
        for (char c : word) {
            int index = c - 'a';
            
            if (node->children[index] == nullptr) {
                return false;
            }
            
            node = node->children[index];
        }
        
        return node->isEndOfWord;
    }
    
    bool startsWith(string prefix) {
        TrieNodeArray* node = root;
        
        for (char c : prefix) {
            int index = c - 'a';
            
            if (node->children[index] == nullptr) {
                return false;
            }
            
            node = node->children[index];
        }
        
        return true;
    }
    
    ~TrieArray() {
        deleteTrieArray(root);
    }
    
private:
    void deleteTrieArray(TrieNodeArray* node) {
        for (int i = 0; i < 26; i++) {
            if (node->children[i] != nullptr) {
                deleteTrieArray(node->children[i]);
            }
        }
        delete node;
    }
};

// Enhanced Trie with additional methods
class TrieEnhanced {
private:
    TrieNode* root;
    
    void dfs(TrieNode* node, string current, vector<string>& words) {
        if (node->isEndOfWord) {
            words.push_back(current);
        }
        
        for (auto& pair : node->children) {
            dfs(pair.second, current + pair.first, words);
        }
    }
    
public:
    TrieEnhanced() {
        root = new TrieNode();
    }
    
    void insert(string word) {
        TrieNode* node = root;
        for (char c : word) {
            if (node->children.find(c) == node->children.end()) {
                node->children[c] = new TrieNode();
            }
            node = node->children[c];
        }
        node->isEndOfWord = true;
    }
    
    bool search(string word) {
        TrieNode* node = root;
        for (char c : word) {
            if (node->children.find(c) == node->children.end()) {
                return false;
            }
            node = node->children[c];
        }
        return node->isEndOfWord;
    }
    
    bool startsWith(string prefix) {
        TrieNode* node = root;
        for (char c : prefix) {
            if (node->children.find(c) == node->children.end()) {
                return false;
            }
            node = node->children[c];
        }
        return true;
    }
    
    vector<string> getAllWords() {
        vector<string> words;
        dfs(root, "", words);
        return words;
    }
    
    vector<string> autocomplete(string prefix) {
        TrieNode* node = root;
        
        // Navigate to prefix
        for (char c : prefix) {
            if (node->children.find(c) == node->children.end()) {
                return vector<string>();
            }
            node = node->children[c];
        }
        
        // Collect all words from that point
        vector<string> words;
        dfs(node, prefix, words);
        return words;
    }
    
    ~TrieEnhanced() {
        deleteTrie(root);
    }
    
private:
    void deleteTrie(TrieNode* node) {
        for (auto& pair : node->children) {
            deleteTrie(pair.second);
        }
        delete node;
    }
};

// Helper function to print vector
void printVector(const vector<string>& arr) {
    cout << "[";
    for (int i = 0; i < arr.size(); i++) {
        cout << "\"" << arr[i] << "\"";
        if (i < arr.size() - 1) cout << ",";
    }
    cout << "]";
}

int main() {
    // Test basic Trie
    cout << "=== Basic Trie ===" << endl;
    Trie trie;
    
    trie.insert("apple");
    cout << "search(\"apple\"): " << (trie.search("apple") ? "true" : "false") << endl;
    cout << "search(\"app\"): " << (trie.search("app") ? "true" : "false") << endl;
    cout << "startsWith(\"app\"): " << (trie.startsWith("app") ? "true" : "false") << endl;
    
    trie.insert("app");
    cout << "search(\"app\"): " << (trie.search("app") ? "true" : "false") << endl;
    
    // Test array-based Trie
    cout << "\n=== Array-based Trie ===" << endl;
    TrieArray trie2;
    trie2.insert("hello");
    trie2.insert("help");
    cout << "search(\"hello\"): " << (trie2.search("hello") ? "true" : "false") << endl;
    cout << "search(\"hel\"): " << (trie2.search("hel") ? "true" : "false") << endl;
    cout << "startsWith(\"hel\"): " << (trie2.startsWith("hel") ? "true" : "false") << endl;
    
    // Test enhanced Trie
    cout << "\n=== Enhanced Trie ===" << endl;
    TrieEnhanced trie3;
    vector<string> words = {"apple", "app", "apricot", "banana", "band"};
    for (const string& word : words) {
        trie3.insert(word);
    }
    
    cout << "All words: ";
    printVector(trie3.getAllWords());
    cout << endl;
    
    cout << "Autocomplete \"ap\": ";
    printVector(trie3.autocomplete("ap"));
    cout << endl;
    
    cout << "Autocomplete \"ban\": ";
    printVector(trie3.autocomplete("ban"));
    cout << endl;
    
    return 0;
}