/*
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
   Time: O(N log N), Space: O(N)

2. Hash Map - Count character frequencies
   Time: O(N), Space: O(1) for lowercase English letters (max 26 chars)

3. Array counting - Use fixed-size array for ASCII/lowercase letters
   Time: O(N), Space: O(1)

Time Complexity: O(N) - Hash map/array approach
Space Complexity: O(1) - At most 26 characters for lowercase English
*/

import java.util.*;

class Solution {
    // Approach 1: Array counting (most efficient for lowercase English letters)
    public boolean isAnagram(String s, String t) {
        // Different lengths can't be anagrams
        if (s.length() != t.length()) {
            return false;
        }
        
        // Array for 26 lowercase English letters
        int[] count = new int[26];
        
        // Count characters in s and t simultaneously
        for (int i = 0; i < s.length(); i++) {
            count[s.charAt(i) - 'a']++;
            count[t.charAt(i) - 'a']--;
        }
        
        // Check if all counts are zero
        for (int c : count) {
            if (c != 0) {
                return false;
            }
        }
        
        return true;
    }
    
    // Approach 2: Using HashMap
    public boolean isAnagramHashMap(String s, String t) {
        if (s.length() != t.length()) {
            return false;
        }
        
        Map<Character, Integer> countMap = new HashMap<>();
        
        // Count characters in s
        for (char c : s.toCharArray()) {
            countMap.put(c, countMap.getOrDefault(c, 0) + 1);
        }
        
        // Decrement count for characters in t
        for (char c : t.toCharArray()) {
            if (!countMap.containsKey(c)) {
                return false;
            }
            countMap.put(c, countMap.get(c) - 1);
            if (countMap.get(c) < 0) {
                return false;
            }
        }
        
        return true;
    }
    
    // Approach 3: Sorting
    public boolean isAnagramSorting(String s, String t) {
        // Different lengths can't be anagrams
        if (s.length() != t.length()) {
            return false;
        }
        
        // Convert to char arrays and sort
        char[] sArray = s.toCharArray();
        char[] tArray = t.toCharArray();
        
        Arrays.sort(sArray);
        Arrays.sort(tArray);
        
        // Compare sorted arrays
        return Arrays.equals(sArray, tArray);
    }
    
    // Approach 4: Using two arrays (alternative to single array)
    public boolean isAnagramTwoArrays(String s, String t) {
        if (s.length() != t.length()) {
            return false;
        }
        
        int[] sCount = new int[26];
        int[] tCount = new int[26];
        
        for (int i = 0; i < s.length(); i++) {
            sCount[s.charAt(i) - 'a']++;
            tCount[t.charAt(i) - 'a']++;
        }
        
        return Arrays.equals(sCount, tCount);
    }
    
    // Test cases
    public static void main(String[] args) {
        Solution solution = new Solution();
        
        // Test case 1
        String s1 = "anagram", t1 = "nagaram";
        System.out.println("Input: s = \"" + s1 + "\", t = \"" + t1 + "\"");
        System.out.println("Output: " + solution.isAnagram(s1, t1));
        System.out.println("Expected: true\n");
        
        // Test case 2
        String s2 = "rat", t2 = "car";
        System.out.println("Input: s = \"" + s2 + "\", t = \"" + t2 + "\"");
        System.out.println("Output: " + solution.isAnagram(s2, t2));
        System.out.println("Expected: false\n");
        
        // Test case 3
        String s3 = "listen", t3 = "silent";
        System.out.println("Input: s = \"" + s3 + "\", t = \"" + t3 + "\"");
        System.out.println("Output: " + solution.isAnagram(s3, t3));
        System.out.println("Expected: true\n");
        
        // Test case 4: Different lengths
        String s4 = "a", t4 = "ab";
        System.out.println("Input: s = \"" + s4 + "\", t = \"" + t4 + "\"");
        System.out.println("Output: " + solution.isAnagram(s4, t4));
        System.out.println("Expected: false\n");
        
        // Test case 5: Empty strings
        String s5 = "", t5 = "";
        System.out.println("Input: s = \"" + s5 + "\", t = \"" + t5 + "\"");
        System.out.println("Output: " + solution.isAnagram(s5, t5));
        System.out.println("Expected: true\n");
        
        // Compare all approaches
        String s6 = "triangle", t6 = "integral";
        System.out.println("Input: s = \"" + s6 + "\", t = \"" + t6 + "\"");
        System.out.println("Array: " + solution.isAnagram(s6, t6));
        System.out.println("HashMap: " + solution.isAnagramHashMap(s6, t6));
        System.out.println("Sorting: " + solution.isAnagramSorting(s6, t6));
        System.out.println("Two Arrays: " + solution.isAnagramTwoArrays(s6, t6));
        System.out.println("Expected: true");
    }
}