-- LeetCode Problem 180: Consecutive Numbers

-- Difficulty: Medium
-- Link: https://leetcode.com/problems/consecutive-numbers/

-- PROBLEM DESCRIPTION:
-- Write a SQL query to find all numbers that appear at least 
-- three times consecutively.

-- TABLE:
-- Logs
-- +-------------+---------+
-- | Column Name | Type    |
-- +-------------+---------+
-- | id          | int     |
-- | num         | varchar |
-- +-------------+---------+
-- id is the primary key and auto-increment
--
-- EXAMPLE:
-- Input: 
-- Logs table:
-- +----+-----+
-- | id | num |
-- +----+-----+
-- | 1  | 1   |
-- | 2  | 1   |
-- | 3  | 1   |
-- | 4  | 2   |
-- | 5  | 1   |
-- | 6  | 2   |
-- | 7  | 2   |
-- +----+-----+
-- Output: 
-- +-----------------+
-- | ConsecutiveNums |
-- +-----------------+
-- | 1               |
-- +-----------------+


-- SOLUTION 1: Using self-joins
SELECT DISTINCT l1.num AS ConsecutiveNums
FROM Logs l1
INNER JOIN Logs l2 ON l1.id = l2.id - 1
INNER JOIN Logs l3 ON l1.id = l3.id - 2
WHERE l1.num = l2.num 
  AND l2.num = l3.num;

-- SOLUTION 2: Using LAG window function
SELECT DISTINCT num AS ConsecutiveNums
FROM (
    SELECT num,
           LAG(num, 1) OVER (ORDER BY id) AS prev_num,
           LAG(num, 2) OVER (ORDER BY id) AS prev_prev_num
    FROM Logs
) t
WHERE num = prev_num 
  AND num = prev_prev_num;

-- EXPLANATION:
-- Solution 1 (Self-joins):
-- - Join table with itself three times
-- - l1 represents current row
-- - l2 represents next row (id - 1)
-- - l3 represents row after next (id - 2)
-- - Check if all three have same number
--
-- Solution 2 (Window function):
-- - LAG(num, 1): Get number from previous row
-- - LAG(num, 2): Get number from 2 rows back
-- - Compare current with both previous values
-- - DISTINCT removes duplicate results

-- KEY CONCEPTS:
-- - Self JOIN: Comparing consecutive rows
-- - LAG(): Access previous row values
-- - Window functions: Accessing multiple rows
-- - DISTINCT: Removing duplicates

-- TIME COMPLEXITY: O(n) for window function, O(n^2) for joins
-- SPACE COMPLEXITY: O(n)