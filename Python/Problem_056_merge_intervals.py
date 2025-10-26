"""
LeetCode Problem: 56 - Merge Intervals
Difficulty: Medium
Link: https://leetcode.com/problems/merge-intervals/

Problem Statement:
Given an array of intervals where intervals[i] = [start_i, end_i], merge all 
overlapping intervals, and return an array of the non-overlapping intervals 
that cover all the intervals in the input.

Examples:
Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].

Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.

Constraints:
- 1 <= intervals.length <= 10^4
- intervals[i].length == 2
- 0 <= start_i <= end_i <= 10^4
"""

from typing import List


class Solution:
    """
    Approach: Sort and Merge
    
    Time Complexity: O(n log n) - dominated by sorting
    Space Complexity: O(n) - for output array (or O(log n) if considering sort space)
    
    Key Insights:
    - Sort intervals by start time
    - After sorting, overlapping intervals are adjacent
    - Two intervals [a,b] and [c,d] overlap if c <= b (when a <= c)
    - Merge by taking min(start) and max(end) of overlapping intervals
    """
    
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        Merge all overlapping intervals.
        
        Args:
            intervals: List of [start, end] pairs
            
        Returns:
            List of merged non-overlapping intervals
        """
        # Edge case: empty or single interval
        if len(intervals) <= 1:
            return intervals
        
        # Sort by start time
        intervals.sort(key=lambda x: x[0])
        
        merged = []
        current_start, current_end = intervals[0]
        
        for start, end in intervals[1:]:
            # Check if current interval overlaps with next
            if start <= current_end:
                # Merge: extend current_end to max of both ends
                current_end = max(current_end, end)
            else:
                # No overlap: save current and start new interval
                merged.append([current_start, current_end])
                current_start, current_end = start, end
        
        # Don't forget the last interval
        merged.append([current_start, current_end])
        
        return merged


class SolutionAlternative:
    """
    Alternative: Using stack-like approach with result array
    
    Same complexity but slightly different style
    """
    
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """Merge using result array as stack."""
        if not intervals:
            return []
        
        intervals.sort()
        merged = [intervals[0]]
        
        for start, end in intervals[1:]:
            # Check if overlaps with last interval in merged
            if start <= merged[-1][1]:
                # Merge by updating end of last interval
                merged[-1][1] = max(merged[-1][1], end)
            else:
                # No overlap: add new interval
                merged.append([start, end])
        
        return merged


# TEST CASES

def test_solution():
    """Test cases with assertions."""
    sol = Solution()
    
    # Test case 1: Example from problem
    assert sol.merge([[1,3],[2,6],[8,10],[15,18]]) == [[1,6],[8,10],[15,18]], "Test 1 failed"
    
    # Test case 2: Adjacent intervals (touching)
    assert sol.merge([[1,4],[4,5]]) == [[1,5]], "Test 2 failed"
    
    # Test case 3: Single interval
    assert sol.merge([[1,4]]) == [[1,4]], "Test 3 failed"
    
    # Test case 4: No overlaps
    assert sol.merge([[1,2],[3,4],[5,6]]) == [[1,2],[3,4],[5,6]], "Test 4 failed"
    
    # Test case 5: All overlap into one
    assert sol.merge([[1,4],[2,3]]) == [[1,4]], "Test 5 failed"
    
    # Test case 6: Unsorted input
    assert sol.merge([[2,3],[4,5],[1,2]]) == [[1,3],[4,5]], "Test 6 failed"
    
    # Test case 7: Contained intervals
    assert sol.merge([[1,10],[2,3],[4,5],[6,7]]) == [[1,10]], "Test 7 failed"
    
    # Test case 8: Multiple merges
    assert sol.merge([[1,3],[2,4],[3,5],[4,6]]) == [[1,6]], "Test 8 failed"
    
    print("✅ All tests passed!")


def trace_example():
    """Trace through merge process step by step."""
    intervals = [[1,3],[2,6],[8,10],[15,18]]
    
    print(f"\nTracing: {intervals}")
    print("="*70)
    
    # Sort first
    intervals.sort()
    print(f"After sorting: {intervals}")
    print("="*70)
    print(f"{'Step':<6} {'Current':<15} {'Next':<15} {'Action':<30}")
    print("="*70)
    
    merged = []
    current_start, current_end = intervals[0]
    
    print(f"{'0':<6} {str([current_start, current_end]):<15} {'':<15} {'Start with first interval':<30}")
    
    for i, (start, end) in enumerate(intervals[1:], 1):
        action = ""
        if start <= current_end:
            new_end = max(current_end, end)
            action = f"Overlap! Merge to [{current_start},{new_end}]"
            current_end = new_end
        else:
            action = f"No overlap. Save [{current_start},{current_end}]"
            merged.append([current_start, current_end])
            current_start, current_end = start, end
        
        print(f"{i:<6} {str([current_start, current_end]):<15} {str([start, end]):<15} {action:<30}")
    
    merged.append([current_start, current_end])
    
    print("="*70)
    print(f"Final result: {merged}")


def visualize_intervals():
    """Visualize intervals on a timeline."""
    def draw_timeline(intervals, title):
        print(f"\n{title}")
        print("="*60)
        
        # Find range
        all_nums = [num for interval in intervals for num in interval]
        min_val, max_val = min(all_nums), max(all_nums)
        
        # Draw each interval
        for i, (start, end) in enumerate(intervals):
            line = [' '] * (max_val + 1)
            for j in range(start, end + 1):
                line[j] = '█'
            print(f"Interval {i+1}: {start:2d} {' '.join(line[min_val:max_val+1])} {end:2d}")
        
        # Draw scale
        scale = [str(i % 10) for i in range(min_val, max_val + 1)]
        print(f"Scale:      {' '.join(scale)}")
    
    # Before merge
    intervals_before = [[1,3],[2,6],[8,10],[15,18]]
    draw_timeline(intervals_before, "Before Merge")
    
    # After merge
    sol = Solution()
    intervals_after = sol.merge(intervals_before)
    draw_timeline(intervals_after, "After Merge")


def edge_cases():
    """Test various edge cases."""
    sol = Solution()
    
    print("\n" + "="*50)
    print("Edge Cases:")
    print("="*50)
    
    test_cases = [
        ([[0,0]], "Single point interval"),
        ([[1,2],[2,3],[3,4]], "Chain of touching intervals"),
        ([[1,100],[2,3],[4,5]], "Small intervals inside large"),
        ([[1,4],[0,4]], "Unsorted with complete overlap"),
        ([[1,4],[0,0]], "Point and range"),
    ]
    
    for intervals, description in test_cases:
        result = sol.merge(intervals)
        print(f"{description:40} {intervals} → {result}")


if __name__ == "__main__":
    test_solution()
    trace_example()
    visualize_intervals()
    edge_cases()
