-- LeetCode Problem 197: Rising Temperature

-- Difficulty: Easy
-- Link: https://leetcode.com/problems/rising-temperature/
--
-- PROBLEM DESCRIPTION:
-- Write a SQL query to find all dates with higher temperature 
-- compared to the previous day.

-- TABLE:
-- Weather
-- +---------------+---------+
-- | Column Name   | Type    |
-- +---------------+---------+
-- | id            | int     |
-- | recordDate    | date    |
-- | temperature   | int     |
-- +---------------+---------+
-- id is the primary key
--
-- EXAMPLE:
-- Input: 
-- Weather table:
-- +----+------------+-------------+
-- | id | recordDate | temperature |
-- +----+------------+-------------+
-- | 1  | 2015-01-01 | 10          |
-- | 2  | 2015-01-02 | 25          |
-- | 3  | 2015-01-03 | 20          |
-- | 4  | 2015-01-04 | 30          |
-- +----+------------+-------------+
-- Output: 
-- +----+
-- | id |
-- +----+
-- | 2  |
-- | 4  |
-- +----+


-- SOLUTION:
SELECT w1.id
FROM Weather w1
JOIN Weather w2 
  ON DATEDIFF(w1.recordDate, w2.recordDate) = 1
WHERE w1.temperature > w2.temperature;

-- EXPLANATION:
-- 1. Self-join Weather table
-- 2. DATEDIFF(w1.recordDate, w2.recordDate) = 1 ensures w1 is the next day after w2
-- 3. Compare temperatures: w1.temperature > w2.temperature
-- 4. Return the id of the day with higher temperature

-- KEY CONCEPTS:
-- - DATEDIFF: Calculating difference between dates
-- - Self JOIN: Comparing consecutive rows
-- - Date arithmetic: Working with date types

-- ALTERNATIVE SOLUTION (Using LAG window function):
-- SELECT id
-- FROM (
--     SELECT id,
--            temperature,
--            LAG(temperature) OVER (ORDER BY recordDate) AS prev_temp,
--            DATEDIFF(recordDate, LAG(recordDate) OVER (ORDER BY recordDate)) AS date_diff
--     FROM Weather
-- ) t
-- WHERE temperature > prev_temp AND date_diff = 1;

-- TIME COMPLEXITY: O(n^2) for self-join
-- SPACE COMPLEXITY: O(1)