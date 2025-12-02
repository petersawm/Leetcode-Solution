"""
Problem: 49 - Group Anagrams
Difficulty: Medium
Link: https://leetcode.com/problems/group-anagrams/
Problem Statement:
Given an array of strings strs, group the anagrams together. You can return 
the answer in any order.
Approach:
Sort each string's characters and use as key in dictionary.
Strings with same characters (anagrams) will have same sorted key.
Time Complexity: O(N * K log K) where N is number of strings, K is max length
Space Complexity: O(N * K)
"""
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        # Dictionary to store {sorted_key: list_of_anagrams}
        map_dict = defaultdict(list)
        
        # Iterate through each string
        for str_val in strs:
            # Sort characters in string
            sorted_key = ''.join(sorted(str_val))
            
            # Add to corresponding group
            map_dict[sorted_key].append(str_val)
        
        # Return all groups
        return list(map_dict.values())


# Test cases
if __name__ == "__main__":
    sol = Solution()
    
    # Test 1
    strs1 = ["eat", "tea", "ate", "eat", "tan", "nat", "bat"]
    print("Output:", sol.groupAnagrams(strs1))
    # Expected: [["eat","tea","ate"], ["tan","nat"], ["bat"]]
    # Order may vary
    
    # Test 2
    strs2 = [""]
    print("Output:", sol.groupAnagrams(strs2))
    # Expected: [[""]]
    
    # Test 3
    strs3 = ["a"]
    print("Output:", sol.groupAnagrams(strs3))
    # Expected: [["a"]]