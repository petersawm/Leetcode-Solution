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

import java.util.*;

// Node class for Trie
class TrieNode {
    Map<Character, TrieNode> children;
    boolean isEndOfWord;
    
    public TrieNode() {
        children = new HashMap<>();
        isEndOfWord = false;
    }
}

// Main Trie implementation
class Trie {
    private TrieNode root;
    
    public Trie() {
        root = new TrieNode();
    }
    
    public void insert(String word) {
        TrieNode node = root;
        
        for (char c : word.toCharArray()) {
            // Create new node if character doesn't exist
            if (!node.children.containsKey(c)) {
                node.children.put(c, new TrieNode());
            }
            
            // Move to child node
            node = node.children.get(c);
        }
        
        // Mark end of word
        node.isEndOfWord = true;
    }
    
    public boolean search(String word) {
        TrieNode node = root;
        
        for (char c : word.toCharArray()) {
            if (!node.children.containsKey(c)) {
                return false;
            }
            node = node.children.get(c);
        }
        
        // Word exists only if we reach end of word marker
        return node.isEndOfWord;
    }
    
    public boolean startsWith(String prefix) {
        TrieNode node = root;
        
        for (char c : prefix.toCharArray()) {
            if (!node.children.containsKey(c)) {
                return false;
            }
            node = node.children.get(c);
        }
        
        // If we successfully traversed all characters, prefix exists
        return true;
    }
}

// Alternative: Array-based implementation
class TrieNodeArray {
    TrieNodeArray[] children;
    boolean isEndOfWord;
    
    public TrieNodeArray() {
        children = new TrieNodeArray[26]; // For lowercase English letters
        isEndOfWord = false;
    }
}

class TrieArray {
    private TrieNodeArray root;
    
    public TrieArray() {
        root = new TrieNodeArray();
    }
    
    public void insert(String word) {
        TrieNodeArray node = root;
        
        for (char c : word.toCharArray()) {
            int index = c - 'a';
            
            if (node.children[index] == null) {
                node.children[index] = new TrieNodeArray();
            }
            
            node = node.children[index];
        }
        
        node.isEndOfWord = true;
    }
    
    public boolean search(String word) {
        TrieNodeArray node = root;
        
        for (char c : word.toCharArray()) {
            int index = c - 'a';
            
            if (node.children[index] == null) {
                return false;
            }
            
            node = node.children[index];
        }
        
        return node.isEndOfWord;
    }
    
    public boolean startsWith(String prefix) {
        TrieNodeArray node = root;
        
        for (char c : prefix.toCharArray()) {
            int index = c - 'a';
            
            if (node.children[index] == null) {
                return false;
            }
            
            node = node.children[index];
        }
        
        return true;
    }
}

// Enhanced Trie with additional methods
class TrieEnhanced {
    private TrieNode root;
    
    public TrieEnhanced() {
        root = new TrieNode();
    }
    
    public void insert(String word) {
        TrieNode node = root;
        for (char c : word.toCharArray()) {
            node.children.putIfAbsent(c, new TrieNode());
            node = node.children.get(c);
        }
        node.isEndOfWord = true;
    }
    
    public boolean search(String word) {
        TrieNode node = root;
        for (char c : word.toCharArray()) {
            if (!node.children.containsKey(c)) {
                return false;
            }
            node = node.children.get(c);
        }
        return node.isEndOfWord;
    }
    
    public boolean startsWith(String prefix) {
        TrieNode node = root;
        for (char c : prefix.toCharArray()) {
            if (!node.children.containsKey(c)) {
                return false;
            }
            node = node.children.get(c);
        }
        return true;
    }
    
    public List<String> getAllWords() {
        List<String> words = new ArrayList<>();
        dfs(root, new StringBuilder(), words);
        return words;
    }
    
    private void dfs(TrieNode node, StringBuilder current, List<String> words) {
        if (node.isEndOfWord) {
            words.add(current.toString());
        }
        
        for (Map.Entry<Character, TrieNode> entry : node.children.entrySet()) {
            current.append(entry.getKey());
            dfs(entry.getValue(), current, words);
            current.deleteCharAt(current.length() - 1);
        }
    }
    
    public List<String> autocomplete(String prefix) {
        TrieNode node = root;
        
        // Navigate to prefix
        for (char c : prefix.toCharArray()) {
            if (!node.children.containsKey(c)) {
                return new ArrayList<>();
            }
            node = node.children.get(c);
        }
        
        // Collect all words from that point
        List<String> words = new ArrayList<>();
        dfs(node, new StringBuilder(prefix), words);
        return words;
    }
}

// Test class
class ImplementTrie {
    public static void main(String[] args) {
        // Test basic Trie
        System.out.println("=== Basic Trie ===");
        Trie trie = new Trie();
        
        trie.insert("apple");
        System.out.println("search(\"apple\"): " + trie.search("apple"));  // true
        System.out.println("search(\"app\"): " + trie.search("app"));  // false
        System.out.println("startsWith(\"app\"): " + trie.startsWith("app"));  // true
        
        trie.insert("app");
        System.out.println("search(\"app\"): " + trie.search("app"));  // true
        
        // Test array-based Trie
        System.out.println("\n=== Array-based Trie ===");
        TrieArray trie2 = new TrieArray();
        trie2.insert("hello");
        trie2.insert("help");
        System.out.println("search(\"hello\"): " + trie2.search("hello"));  // true
        System.out.println("search(\"hel\"): " + trie2.search("hel"));  // false
        System.out.println("startsWith(\"hel\"): " + trie2.startsWith("hel"));  // true
        
        // Test enhanced Trie
        System.out.println("\n=== Enhanced Trie ===");
        TrieEnhanced trie3 = new TrieEnhanced();
        String[] words = {"apple", "app", "apricot", "banana", "band"};
        for (String word : words) {
            trie3.insert(word);
        }
        
        System.out.println("All words: " + trie3.getAllWords());
        System.out.println("Autocomplete \"ap\": " + trie3.autocomplete("ap"));
        System.out.println("Autocomplete \"ban\": " + trie3.autocomplete("ban"));
    }
}