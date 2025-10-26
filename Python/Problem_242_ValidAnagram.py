"""
Problem: 242 - Valid Anagram
Difficulty: Easy
Link: https://leetcode.com/problems/valid-anagram/

Problem Statement:
Given two strings s and t, return true if t is an anagram of s, and false otherwise.
An Anagram is a word or phrase formed by rearranging the letters of a different word 
or phrase, typically using all the original letters exactly once.

Approach:
Multiple approaches:

1. Sorting - Sort both strings and compare
   Time: O(N log N), Space: O(1) or O(N) depending on sort

2. Hash Map/Counter - Count character frequencies
   Time: O(N), Space: O(1) for lowercase English letters (max 26 chars)

3. Array counting - Use fixed-size array for ASCII/lowercase letters
   Time: O(N), Space: O(1)

Time Complexity: O(N) - Hash map approach
Space Complexity: O(1) - At most 26 characters for lowercase English
"""

from typing import Dict
from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """Hash Map approach - Most intuitive"""
        # Different lengths can't be anagrams
        if len(s) != len(t):
            return False
        
        # Count character frequencies
        count = {}
        
        for char in s:
            count[char] = count.get(char, 0) + 1
        
        for char in t:
            if char not in count:
                return False
            count[char] -= 1
            if count[char] < 0:
                return False
        
        return True
    
    # Pythonic approach using Counter
    def isAnagramCounter(self, s: str, t: str) -> bool:
        """Using Counter from collections"""
        return Counter(s) == Counter(t)
    
    # Sorting approach
    def isAnagramSorting(self, s: str, t: str) -> bool:
        """Sort both strings and compare"""
        return sorted(s) == sorted(t)
    
    # Array counting approach (for lowercase English letters)
    def isAnagramArray(self, s: str, t: str) -> bool:
        """Using array for counting (lowercase English letters only)"""
        if len(s) != len(t):
            return False
        
        # Array for 26 lowercase English letters
        count = [0] * 26
        
        for i in range(len(s)):
            count[ord(s[i]) - ord('a')] += 1
            count[ord(t[i]) - ord('a')] -= 1
        
        # Check if all counts are zero
        return all(c == 0 for c in count)
    
    # One-liner pythonic
    def isAnagramOneLiner(self, s: str, t: str) -> bool:
        """One-liner solution"""
        return len(s) == len(t) and all(s.count(c) == t.count(c) for c in set(s))


# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1
    s1, t1 = "anagram", "nagaram"
    print(f'Input: s = "{s1}", t = "{t1}"')
    print(f"Output: {solution.isAnagram(s1, t1)}")
    print(f"Expected: True\n")
    
    # Test case 2
    s2, t2 = "rat", "car"
    print(f'Input: s = "{s2}", t = "{t2}"')
    print(f"Output: {solution.isAnagram(s2, t2)}")
    print(f"Expected: False\n")
    
    # Test case 3
    s3, t3 = "listen", "silent"
    print(f'Input: s = "{s3}", t = "{t3}"')
    print(f"Output: {solution.isAnagram(s3, t3)}")
    print(f"Expected: True\n")
    
    # Test case 4: Different lengths
    s4, t4 = "a", "ab"
    print(f'Input: s = "{s4}", t = "{t4}"')
    print(f"Output: {solution.isAnagram(s4, t4)}")
    print(f"Expected: False\n")
    
    # Test case 5: Empty strings
    s5, t5 = "", ""
    print(f'Input: s = "{s5}", t = "{t5}"')
    print(f"Output: {solution.isAnagram(s5, t5)}")
    print(f"Expected: True\n")
    
    # Compare all approaches
    s6, t6 = "triangle", "integral"
    print(f'Input: s = "{s6}", t = "{t6}"')
    print(f"HashMap: {solution.isAnagram(s6, t6)}")
    print(f"Counter: {solution.isAnagramCounter(s6, t6)}")
    print(f"Sorting: {solution.isAnagramSorting(s6, t6)}")
    print(f"Array: {solution.isAnagramArray(s6, t6)}")
    print(f"OneLiner: {solution.isAnagramOneLiner(s6, t6)}")
    print(f"Expected: True")