/*
Problem: 127 - Word Ladder
Difficulty: Hard
Link: https://leetcode.com/problems/word-ladder/
Problem Statement:
Given two words, beginWord and endWord, and a dictionary wordList, return the 
number of words in the shortest transformation sequence from beginWord to 
endWord, or 0 if no such sequence exists.
One letter can be changed at a time, and each transformed word must exist in 
the word list.
Approach:
Use BFS (Breadth-First Search) to find shortest path.
For each word, generate all possible neighbors (one letter change).
Use a visited set to avoid revisiting words.
Time Complexity: O(N * L * 26) where N is word count, L is word length
Space Complexity: O(N)
*/
#include <iostream>
#include <vector>
#include <unordered_set>
#include <queue>
using namespace std;

class Solution {
public:
    int ladderLength(string beginWord, string endWord, vector<string>& wordList) {
        // Convert vector to set for O(1) lookup
        unordered_set<string> wordSet(wordList.begin(), wordList.end());
        
        // If endWord not in set, no solution
        if (wordSet.find(endWord) == wordSet.end()) {
            return 0;
        }
        
        // BFS
        queue<string> q;
        unordered_set<string> visited;
        
        q.push(beginWord);
        visited.insert(beginWord);
        int level = 1;
        
        while (!q.empty()) {
            int size = q.size();
            
            // Process all words at current level
            for (int i = 0; i < size; i++) {
                string word = q.front();
                q.pop();
                
                // If reached endWord
                if (word == endWord) {
                    return level;
                }
                
                // Generate all neighbors (one letter change)
                vector<string> neighbors = getNeighbors(word, wordSet);
                for (const string& neighbor : neighbors) {
                    if (visited.find(neighbor) == visited.end()) {
                        visited.insert(neighbor);
                        q.push(neighbor);
                    }
                }
            }
            
            level++;
        }
        
        return 0;  // No path found
    }
    
private:
    // Get all valid neighbors (one letter change)
    vector<string> getNeighbors(string word, const unordered_set<string>& wordSet) {
        vector<string> neighbors;
        
        // Try changing each position
        for (int i = 0; i < word.length(); i++) {
            char original = word[i];
            
            // Try all 26 letters
            for (char c = 'a'; c <= 'z'; c++) {
                if (c == original) continue;
                
                word[i] = c;
                
                if (wordSet.find(word) != wordSet.end()) {
                    neighbors.push_back(word);
                }
            }
            
            word[i] = original;
        }
        
        return neighbors;
    }
};

// Test cases
int main() {
    Solution sol;
    
    // Test 1
    string beginWord1 = "hit";
    string endWord1 = "cog";
    vector<string> wordList1 = {"hot", "dot", "dog", "lot", "log", "cog"};
    cout << "Output: " << sol.ladderLength(beginWord1, endWord1, wordList1) << endl;
    // Expected: 5 (hit -> hot -> dot -> dog -> cog)
    
    // Test 2
    string beginWord2 = "hit";
    string endWord2 = "cog";
    vector<string> wordList2 = {"hot", "dot", "dog", "lot", "log"};
    cout << "Output: " << sol.ladderLength(beginWord2, endWord2, wordList2) << endl;
    // Expected: 0 (no path)
    
    // Test 3
    string beginWord3 = "a";
    string endWord3 = "c";
    vector<string> wordList3 = {"a", "b", "c"};
    cout << "Output: " << sol.ladderLength(beginWord3, endWord3, wordList3) << endl;
    // Expected: 2 (a -> c)
    
    return 0;
}