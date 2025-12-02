/*
Problem: 127 - Word Ladder
Difficulty: Hard
Link: https://leetcode.com/problems/word-ladder/
Problem Statement:
Given two words, beginWord and endWord, and a dictionary wordList, return the 
number of words in the shortest transformation sequence from beginWord to 
endWord, or 0 if no such sequence exists.
You may assume that beginWord is not in wordList.
One letter can be changed at a time, and each transformed word must exist in 
the word list.
Approach:
Use BFS (Breadth-First Search) to find shortest path.
For each word, generate all possible neighbors (one letter change).
Use a visited set to avoid revisiting words.
Time Complexity: O(N * L * 26) where N is word count, L is word length
Space Complexity: O(N)
*/
import java.util.*;

class Solution {
    public int ladderLength(String beginWord, String endWord, List<String> wordList) {
        // Convert list to set for O(1) lookup
        Set<String> wordSet = new HashSet<>(wordList);
        
        // If endWord not in set, no solution
        if (!wordSet.contains(endWord)) {
            return 0;
        }
        
        // BFS
        Queue<String> queue = new LinkedList<>();
        Set<String> visited = new HashSet<>();
        
        queue.offer(beginWord);
        visited.add(beginWord);
        int level = 1;
        
        while (!queue.isEmpty()) {
            int size = queue.size();
            
            // Process all words at current level
            for (int i = 0; i < size; i++) {
                String word = queue.poll();
                
                // If reached endWord
                if (word.equals(endWord)) {
                    return level;
                }
                
                // Generate all neighbors (one letter change)
                for (String neighbor : getNeighbors(word, wordSet)) {
                    if (!visited.contains(neighbor)) {
                        visited.add(neighbor);
                        queue.offer(neighbor);
                    }
                }
            }
            
            level++;
        }
        
        return 0;  // No path found
    }
    
    // Get all valid neighbors (one letter change)
    private List<String> getNeighbors(String word, Set<String> wordSet) {
        List<String> neighbors = new ArrayList<>();
        char[] chars = word.toCharArray();
        
        // Try changing each position
        for (int i = 0; i < chars.length; i++) {
            char original = chars[i];
            
            // Try all 26 letters
            for (char c = 'a'; c <= 'z'; c++) {
                if (c == original) continue;
                
                chars[i] = c;
                String neighbor = new String(chars);
                
                if (wordSet.contains(neighbor)) {
                    neighbors.add(neighbor);
                }
            }
            
            chars[i] = original;
        }
        
        return neighbors;
    }
    
    // Test cases
    public static void main(String[] args) {
        Solution sol = new Solution();
        
        // Test 1
        String beginWord1 = "hit";
        String endWord1 = "cog";
        List<String> wordList1 = Arrays.asList("hot", "dot", "dog", "lot", "log", "cog");
        System.out.println("Output: " + sol.ladderLength(beginWord1, endWord1, wordList1));
        // Expected: 5 (hit -> hot -> dot -> dog -> cog)
        
        // Test 2
        String beginWord2 = "hit";
        String endWord2 = "cog";
        List<String> wordList2 = Arrays.asList("hot", "dot", "dog", "lot", "log");
        System.out.println("Output: " + sol.ladderLength(beginWord2, endWord2, wordList2));
        // Expected: 0 (no path)
        
        // Test 3
        String beginWord3 = "a";
        String endWord3 = "c";
        List<String> wordList3 = Arrays.asList("a", "b", "c");
        System.out.println("Output: " + sol.ladderLength(beginWord3, endWord3, wordList3));
        // Expected: 2 (a -> c)
    }
}