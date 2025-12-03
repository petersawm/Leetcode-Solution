import collections
from typing import List, Dict, Tuple, Set

class TrieNode:
    def __init__(self):
        self.children: Dict[str, TrieNode] = {}
        self.sentences: Set[str] = set()

class AutocompleteSystem:
    def __init__(self, sentences: List[str], times: List[int]):
        self.hot_degrees: Dict[str, int] = {}
        for sentence, time in zip(sentences, times):
            self.hot_degrees[sentence] = time
        
        self.root = TrieNode()
        self.current_prefix: str = ""
        self.current_node: TrieNode = self.root
        
        for sentence in sentences:
            self._insert_sentence(sentence, self.root)

    def _insert_sentence(self, sentence: str, root_node: TrieNode) -> None:
        node = root_node
        for char in sentence:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
            node.sentences.add(sentence)

    def _get_candidates(self, start_node: TrieNode) -> List[str]:
        return list(start_node.sentences)

    def input(self, c: str) -> List[str]:
        if c == '#':
            sentence_to_store = self.current_prefix
            
            self.hot_degrees[sentence_to_store] = self.hot_degrees.get(sentence_to_store, 0) + 1
            
            if sentence_to_store not in self.root.sentences:
                 self._insert_sentence(sentence_to_store, self.root)
            
            self.current_prefix = ""
            self.current_node = self.root
            return []

        else:
            self.current_prefix += c
            
            if c in self.current_node.children:
                self.current_node = self.current_node.children[c]
                
                candidates = self._get_candidates(self.current_node)
                
                matches: List[Tuple[int, str]] = [
                    (-self.hot_degrees[s], s) for s in candidates
                ]
                
                matches.sort()
                
                result: List[str] = [sentence for _, sentence in matches[:3]]
                return result
            else:
                self.current_node = TrieNode()
                return []


# Your AutocompleteSystem object will be instantiated and called as such:
# obj = AutocompleteSystem(sentences, times)
# param_1 = obj.input(c)