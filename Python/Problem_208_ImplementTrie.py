"""
Problem: 208 - Implement Trie (Prefix Tree)
Difficulty: Medium
Link: https://leetcode.com/problems/implement-trie-prefix-tree/

Problem Statement:
A trie (pronounced as "try") or prefix tree is a tree data structure used to efficiently 
store and retrieve keys in a dataset of strings. There are various applications of this 
data structure, such as autocomplete and spellchecker.

Implement the Trie class:
- Trie() Initializes the trie object.
- void insert(String word) Inserts the string word into the trie.
- boolean search(String word) Returns true if the string word is in the trie, and false otherwise.
- boolean startsWith(String prefix) Returns true if there is a previously inserted string word 
  that has the prefix, and false otherwise.

Approach:
Use a tree where each node represents a character:
- Each node has children (up to 26 for lowercase English letters)
- Each node has a boolean flag indicating if it's end of a word

Time Complexity:
- insert: O(M) where M is word length
- search: O(M) where M is word length
- startsWith: O(M) where M is prefix length

Space Complexity: O(N × M) where N is number of words, M is average word length
"""

class TrieNode:
    """Node in the Trie"""
    def __init__(self):
        self.children = {}  # Dictionary mapping character to TrieNode
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        """Initialize the trie with empty root"""
        self.root = TrieNode()
    
    def insert(self, word: str) -> None:
        """Insert a word into the trie"""
        node = self.root
        
        for char in word:
            # Create new node if character doesn't exist
            if char not in node.children:
                node.children[char] = TrieNode()
            
            # Move to child node
            node = node.children[char]
        
        # Mark end of word
        node.is_end_of_word = True
    
    def search(self, word: str) -> bool:
        """Search if word exists in the trie"""
        node = self.root
        
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        
        # Word exists only if we reach end of word marker
        return node.is_end_of_word
    
    def startsWith(self, prefix: str) -> bool:
        """Check if any word in trie starts with given prefix"""
        node = self.root
        
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        
        # If we successfully traversed all characters, prefix exists
        return True


# Alternative implementation using array instead of dictionary
class TrieNodeArray:
    """Node using array for children (more memory efficient for dense tries)"""
    def __init__(self):
        self.children = [None] * 26  # For lowercase English letters
        self.is_end_of_word = False

class TrieArray:
    def __init__(self):
        self.root = TrieNodeArray()
    
    def insert(self, word: str) -> None:
        node = self.root
        
        for char in word:
            index = ord(char) - ord('a')
            
            if node.children[index] is None:
                node.children[index] = TrieNodeArray()
            
            node = node.children[index]
        
        node.is_end_of_word = True
    
    def search(self, word: str) -> bool:
        node = self.root
        
        for char in word:
            index = ord(char) - ord('a')
            
            if node.children[index] is None:
                return False
            
            node = node.children[index]
        
        return node.is_end_of_word
    
    def startsWith(self, prefix: str) -> bool:
        node = self.root
        
        for char in prefix:
            index = ord(char) - ord('a')
            
            if node.children[index] is None:
                return False
            
            node = node.children[index]
        
        return True


# Enhanced Trie with additional methods
class TrieEnhanced:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True
    
    def search(self, word: str) -> bool:
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_word
    
    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True
    
    def delete(self, word: str) -> bool:
        """Delete a word from trie"""
        def delete_helper(node: TrieNode, word: str, index: int) -> bool:
            if index == len(word):
                if not node.is_end_of_word:
                    return False
                node.is_end_of_word = False
                return len(node.children) == 0
            
            char = word[index]
            if char not in node.children:
                return False
            
            child = node.children[char]
            should_delete_child = delete_helper(child, word, index + 1)
            
            if should_delete_child:
                del node.children[char]
                return len(node.children) == 0 and not node.is_end_of_word
            
            return False
        
        return delete_helper(self.root, word, 0)
    
    def get_all_words(self) -> list:
        """Get all words in the trie"""
        words = []
        
        def dfs(node: TrieNode, current_word: str):
            if node.is_end_of_word:
                words.append(current_word)
            
            for char, child in node.children.items():
                dfs(child, current_word + char)
        
        dfs(self.root, "")
        return words
    
    def autocomplete(self, prefix: str) -> list:
        """Get all words that start with given prefix"""
        # First, navigate to the prefix
        node = self.root
        for char in prefix:
            if char not in node.children:
                return []
            node = node.children[char]
        
        # Then collect all words from that point
        words = []
        
        def dfs(node: TrieNode, current_word: str):
            if node.is_end_of_word:
                words.append(current_word)
            
            for char, child in node.children.items():
                dfs(child, current_word + char)
        
        dfs(node, prefix)
        return words


# Test cases
if __name__ == "__main__":
    # Test basic Trie
    print("=== Basic Trie ===")
    trie = Trie()
    
    trie.insert("apple")
    print(f'search("apple"): {trie.search("apple")}')  # True
    print(f'search("app"): {trie.search("app")}')  # False
    print(f'startsWith("app"): {trie.startsWith("app")}')  # True
    
    trie.insert("app")
    print(f'search("app"): {trie.search("app")}')  # True
    
    # Test array-based Trie
    print("\n=== Array-based Trie ===")
    trie2 = TrieArray()
    trie2.insert("hello")
    trie2.insert("help")
    print(f'search("hello"): {trie2.search("hello")}')  # True
    print(f'search("hel"): {trie2.search("hel")}')  # False
    print(f'startsWith("hel"): {trie2.startsWith("hel")}')  # True
    
    # Test enhanced Trie
    print("\n=== Enhanced Trie ===")
    trie3 = TrieEnhanced()
    words = ["apple", "app", "apricot", "banana", "band"]
    for word in words:
        trie3.insert(word)
    
    print(f"All words: {trie3.get_all_words()}")
    print(f'Autocomplete "ap": {trie3.autocomplete("ap")}')
    print(f'Autocomplete "ban": {trie3.autocomplete("ban")}')
    
    trie3.delete("app")
    print(f'After deleting "app": {trie3.get_all_words()}')