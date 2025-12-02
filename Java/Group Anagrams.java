/*
Problem: 49 - Group Anagrams
Difficulty: Medium
Link: https://leetcode.com/problems/group-anagrams/
Problem Statement:
Given an array of strings strs, group the anagrams together. You can return 
the answer in any order.
Approach:
Sort each string's characters and use as key in HashMap.
Strings with same characters (anagrams) will have same sorted key.
Time Complexity: O(N * K log K) where N is number of strings, K is max length
Space Complexity: O(N * K)
*/
import java.util.*;

class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        // HashMap to store {sorted_key: list_of_anagrams}
        Map<String, List<String>> map = new HashMap<>();
        
        // Iterate through each string
        for (String str : strs) {
            // Sort characters in string
            char[] chars = str.toCharArray();
            Arrays.sort(chars);
            String sorted = new String(chars);
            
            // Add to corresponding group
            map.putIfAbsent(sorted, new ArrayList<>());
            map.get(sorted).add(str);
        }
        
        // Return all groups
        return new ArrayList<>(map.values());
    }
    
    // Test cases
    public static void main(String[] args) {
        Solution sol = new Solution();
        
        // Test 1
        String[] strs1 = {"eat", "tea", "ate", "eat", "tan", "nat", "bat"};
        System.out.println("Output: " + sol.groupAnagrams(strs1));
        // Expected: [["eat","tea","ate"], ["tan","nat"], ["bat"]]
        // Order may vary
        
        // Test 2
        String[] strs2 = {""};
        System.out.println("Output: " + sol.groupAnagrams(strs2));
        // Expected: [[""]]
        
        // Test 3
        String[] strs3 = {"a"};
        System.out.println("Output: " + sol.groupAnagrams(strs3));
        // Expected: [["a"]]
    }
}