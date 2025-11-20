/*
Problem: 49 - Group Anagrams
Difficulty: Medium
Link: https://leetcode.com/problems/group-anagrams/

Problem Statement:
Group anagrams together from an array of strings.

Approach:
Use Hash Map with sorted string as key or character count as key.

Time Complexity: O(N * K log K) where N = number of strings, K = max string length
Space Complexity: O(N * K) for storing results
*/

import java.util.*;

class Solution {
    // Approach 1: Hash map with sorted string as key
    public List<List<String>> groupAnagrams(String[] strs) {
        Map<String, List<String>> anagramMap = new HashMap<>();
        
        for (String s : strs) {
            // Sort string to get key
            char[] chars = s.toCharArray();
            Arrays.sort(chars);
            String key = new String(chars);
            
            anagramMap.putIfAbsent(key, new ArrayList<>());
            anagramMap.get(key).add(s);
        }
        
        return new ArrayList<>(anagramMap.values());
    }
    
    // Approach 2: Using character count as key
    public List<List<String>> groupAnagramsCount(String[] strs) {
        Map<String, List<String>> anagramMap = new HashMap<>();
        
        for (String s : strs) {
            // Count characters (26 lowercase letters)
            int[] count = new int[26];
            for (char c : s.toCharArray()) {
                count[c - 'a']++;
            }
            
            // Build key from count array
            StringBuilder keyBuilder = new StringBuilder();
            for (int i = 0; i < 26; i++) {
                keyBuilder.append('#');
                keyBuilder.append(count[i]);
            }
            String key = keyBuilder.toString();
            
            anagramMap.putIfAbsent(key, new ArrayList<>());
            anagramMap.get(key).add(s);
        }
        
        return new ArrayList<>(anagramMap.values());
    }
    
    // Approach 3: Using prime number multiplication
    public List<List<String>> groupAnagramsPrime(String[] strs) {
        int[] primes = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 
                       59, 61, 67, 71, 73, 79, 83, 89, 97, 101};
        
        Map<Long, List<String>> anagramMap = new HashMap<>();
        
        for (String s : strs) {
            long key = 1;
            for (char c : s.toCharArray()) {
                key *= primes[c - 'a'];
            }
            
            anagramMap.putIfAbsent(key, new ArrayList<>());
            anagramMap.get(key).add(s);
        }
        
        return new ArrayList<>(anagramMap.values());
    }
    
    // Helper method to print result
    private static void printResult(List<List<String>> result) {
        System.out.print("[");
        for (int i = 0; i < result.size(); i++) {
            System.out.print(result.get(i));
            if (i < result.size() - 1) {
                System.out.print(",");
            }
        }
        System.out.println("]");
    }
    
    // Test cases
    public static void main(String[] args) {
        Solution solution = new Solution();
        
        // Test case 1
        String[] strs1 = {"eat","tea","tan","ate","nat","bat"};
        System.out.println("Input: strs = " + Arrays.toString(strs1));
        System.out.print("Output: ");
        printResult(solution.groupAnagrams(strs1));
        System.out.println("Expected: [[bat],[nat,tan],[ate,eat,tea]] (any order)\n");
        
        // Test case 2
        String[] strs2 = {""};
        System.out.println("Input: strs = " + Arrays.toString(strs2));
        System.out.print("Output: ");
        printResult(solution.groupAnagrams(strs2));
        System.out.println("Expected: [[\"\"]]\n");
        
        // Test case 3
        String[] strs3 = {"a"};
        System.out.println("Input: strs = " + Arrays.toString(strs3));
        System.out.print("Output: ");
        printResult(solution.groupAnagrams(strs3));
        System.out.println("Expected: [[a]]\n");
        
        // Test case 4
        String[] strs4 = {"abc","def","ghi"};
        System.out.println("Input: strs = " + Arrays.toString(strs4));
        System.out.print("Output: ");
        printResult(solution.groupAnagrams(strs4));
        System.out.println("Expected: [[abc],[def],[ghi]]\n");
        
        // Compare approaches
        String[] strs5 = {"eat","tea","tan","ate","nat","bat"};
        System.out.println("Input: strs = " + Arrays.toString(strs5));
        System.out.print("Sorted Key: ");
        printResult(solution.groupAnagrams(strs5));
        System.out.print("Count Key: ");
        printResult(solution.groupAnagramsCount(strs5));
        System.out.print("Prime Key: ");
        printResult(solution.groupAnagramsPrime(strs5));
    }
}