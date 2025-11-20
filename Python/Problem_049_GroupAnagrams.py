"""
Problem: 49 - Group Anagrams
Difficulty: Medium
Link: https://leetcode.com/problems/group-anagrams/

Problem Statement:
Given an array of strings strs, group the anagrams together. You can return the answer 
in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or 
phrase, typically using all the original letters exactly once.

Example: ["eat","tea","tan","ate","nat","bat"] → [["bat"],["nat","tan"],["ate","eat","tea"]]

Approach:
Use Hash Map with sorted string as key:
1. For each string, sort it to get a key
2. Use key to group anagrams together
3. Return all groups

Alternative: Use character count as key

Time Complexity: O(N * K log K) where N = number of strings, K = max string length
Space Complexity: O(N * K) for storing results
"""

from typing import List
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """Hash map with sorted string as key"""
        anagram_map = defaultdict(list)
        
        for s in strs:
            # Sort string to get key
            key = ''.join(sorted(s))
            anagram_map[key].append(s)
        
        return list(anagram_map.values())
    
    # Using character count as key
    def groupAnagramsCount(self, strs: List[str]) -> List[List[str]]:
        """Hash map with character count as key"""
        anagram_map = defaultdict(list)
        
        for s in strs:
            # Count characters (26 lowercase letters)
            count = [0] * 26
            for char in s:
                count[ord(char) - ord('a')] += 1
            
            # Use tuple of counts as key
            key = tuple(count)
            anagram_map[key].append(s)
        
        return list(anagram_map.values())
    
    # Using prime number multiplication (mathematical approach)
    def groupAnagramsPrime(self, strs: List[str]) -> List[List[str]]:
        """Prime number product as key"""
        # Map each letter to a prime number
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101]
        
        anagram_map = defaultdict(list)
        
        for s in strs:
            # Calculate product of primes
            key = 1
            for char in s:
                key *= primes[ord(char) - ord('a')]
            
            anagram_map[key].append(s)
        
        return list(anagram_map.values())
    
    # Using Counter from collections
    def groupAnagramsCounter(self, strs: List[str]) -> List[List[str]]:
        """Using Counter for character frequency"""
        from collections import Counter
        
        anagram_map = defaultdict(list)
        
        for s in strs:
            # Use frozenset of Counter items as key
            # frozenset is hashable unlike dict
            key = frozenset(Counter(s).items())
            anagram_map[key].append(s)
        
        return list(anagram_map.values())


# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1
    strs1 = ["eat","tea","tan","ate","nat","bat"]
    print(f"Input: strs = {strs1}")
    print(f"Output: {solution.groupAnagrams(strs1)}")
    print(f"Expected: [['bat'],['nat','tan'],['ate','eat','tea']] (any order)\n")
    
    # Test case 2: Empty string
    strs2 = [""]
    print(f"Input: strs = {strs2}")
    print(f"Output: {solution.groupAnagrams(strs2)}")
    print(f"Expected: [['']]\n")
    
    # Test case 3: Single character
    strs3 = ["a"]
    print(f"Input: strs = {strs3}")
    print(f"Output: {solution.groupAnagrams(strs3)}")
    print(f"Expected: [['a']]\n")
    
    # Test case 4: No anagrams
    strs4 = ["abc","def","ghi"]
    print(f"Input: strs = {strs4}")
    print(f"Output: {solution.groupAnagrams(strs4)}")
    print(f"Expected: [['abc'],['def'],['ghi']]\n")
    
    # Test case 5: All anagrams
    strs5 = ["abc","bca","cab","acb","bac","cba"]
    print(f"Input: strs = {strs5}")
    print(f"Output: {solution.groupAnagrams(strs5)}")
    print(f"Expected: All in one group\n")
    
    # Compare approaches
    strs6 = ["eat","tea","tan","ate","nat","bat"]
    print(f"Input: strs = {strs6}")
    print(f"Sorted Key: {solution.groupAnagrams(strs6)}")
    print(f"Count Key: {solution.groupAnagramsCount(strs6)}")
    print(f"Prime Key: {solution.groupAnagramsPrime(strs6)}")
    print(f"Counter Key: {solution.groupAnagramsCounter(strs6)}")