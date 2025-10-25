/*
Problem: 56 - Merge Intervals
Difficulty: Medium
Link: https://leetcode.com/problems/merge-intervals/

Problem Statement:
Given an array of intervals where intervals[i] = [start_i, end_i], 
merge all overlapping intervals, and return an array of the non-overlapping 
intervals that cover all the intervals in the input.

Approach:
1. Sort intervals by start time
2. Iterate through sorted intervals
3. If current interval overlaps with last merged interval, merge them
   (overlap exists if: current_start <= last_end)
4. Otherwise, add current interval to result

Two intervals [a,b] and [c,d] overlap if: c <= b

Time Complexity: O(N log N) - Dominated by sorting
Space Complexity: O(N) - For storing result (or O(log N) for sorting)
*/

import java.util.*;

class Solution {
    public int[][] merge(int[][] intervals) {
        // Edge case: empty or single interval
        if (intervals.length <= 1) {
            return intervals;
        }
        
        // Sort intervals by start time
        Arrays.sort(intervals, (a, b) -> Integer.compare(a[0], b[0]));
        
        // List to store merged intervals
        List<int[]> merged = new ArrayList<>();
        
        // Add first interval
        int[] currentInterval = intervals[0];
        merged.add(currentInterval);
        
        // Process each interval
        for (int i = 1; i < intervals.length; i++) {
            int currentStart = intervals[i][0];
            int currentEnd = intervals[i][1];
            int lastEnd = currentInterval[1];
            
            // Check if intervals overlap
            if (currentStart <= lastEnd) {
                // Merge: extend the end of current interval
                currentInterval[1] = Math.max(lastEnd, currentEnd);
            } else {
                // No overlap: add new interval
                currentInterval = intervals[i];
                merged.add(currentInterval);
            }
        }
        
        // Convert list to array
        return merged.toArray(new int[merged.size()][]);
    }
    
    // Alternative: Using LinkedList for better performance
    public int[][] mergeLinkedList(int[][] intervals) {
        if (intervals.length <= 1) {
            return intervals;
        }
        
        Arrays.sort(intervals, (a, b) -> a[0] - b[0]);
        
        LinkedList<int[]> merged = new LinkedList<>();
        
        for (int[] interval : intervals) {
            // If list is empty or no overlap
            if (merged.isEmpty() || merged.getLast()[1] < interval[0]) {
                merged.add(interval);
            } else {
                // Merge with last interval
                merged.getLast()[1] = Math.max(merged.getLast()[1], interval[1]);
            }
        }
        
        return merged.toArray(new int[merged.size()][]);
    }
    
    // Helper method to print 2D array
    public static void printIntervals(int[][] intervals) {
        System.out.print("[");
        for (int i = 0; i < intervals.length; i++) {
            System.out.print("[" + intervals[i][0] + "," + intervals[i][1] + "]");
            if (i < intervals.length - 1) {
                System.out.print(",");
            }
        }
        System.out.println("]");
    }
    
    // Test cases
    public static void main(String[] args) {
        Solution solution = new Solution();
        
        // Test case 1
        int[][] intervals1 = {{1,3}, {2,6}, {8,10}, {15,18}};
        System.out.print("Input: ");
        printIntervals(intervals1);
        int[][] result1 = solution.merge(intervals1);
        System.out.print("Output: ");
        printIntervals(result1);
        System.out.println("Expected: [[1,6],[8,10],[15,18]]\n");
        
        // Test case 2
        int[][] intervals2 = {{1,4}, {4,5}};
        System.out.print("Input: ");
        printIntervals(intervals2);
        int[][] result2 = solution.merge(intervals2);
        System.out.print("Output: ");
        printIntervals(result2);
        System.out.println("Expected: [[1,5]]\n");
        
        // Test case 3
        int[][] intervals3 = {{1,4}, {0,4}};
        System.out.print("Input: ");
        printIntervals(intervals3);
        int[][] result3 = solution.merge(intervals3);
        System.out.print("Output: ");
        printIntervals(result3);
        System.out.println("Expected: [[0,4]]\n");
        
        // Test case 4
        int[][] intervals4 = {{1,4}, {2,3}};
        System.out.print("Input: ");
        printIntervals(intervals4);
        int[][] result4 = solution.merge(intervals4);
        System.out.print("Output: ");
        printIntervals(result4);
        System.out.println("Expected: [[1,4]]\n");
        
        // Test case 5: Multiple overlapping
        int[][] intervals5 = {{1,3}, {2,4}, {3,5}, {6,7}};
        System.out.print("Input: ");
        printIntervals(intervals5);
        int[][] result5 = solution.mergeLinkedList(intervals5);
        System.out.print("Output (LinkedList): ");
        printIntervals(result5);
        System.out.println("Expected: [[1,5],[6,7]]");
    }
}