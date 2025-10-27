-- LeetCode Problem 178: Rank Scores

-- Difficulty: Medium
-- Link: https://leetcode.com/problems/rank-scores/

-- PROBLEM DESCRIPTION:
-- Write a SQL query to rank scores from highest to lowest.
-- If there is a tie, assign the same rank. The next rank should
-- be the next consecutive integer (dense rank).
--
-- TABLE:
-- Scores
-- +-------------+---------+
-- | Column Name | Type    |
-- +-------------+---------+
-- | id          | int     |
-- | score       | decimal |
-- +-------------+---------+
-- id is the primary key
--
-- EXAMPLE:
-- Input: 
-- Scores table:
-- +----+-------+
-- | id | score |
-- +----+-------+
-- | 1  | 3.50  |
-- | 2  | 3.65  |
-- | 3  | 4.00  |
-- | 4  | 3.85  |
-- | 5  | 4.00  |
-- | 6  | 3.65  |
-- +----+-------+
-- Output: 
-- +-------+------+
-- | score | rank |
-- +-------+------+
-- | 4.00  | 1    |
-- | 4.00  | 1    |
-- | 3.85  | 2    |
-- | 3.65  | 3    |
-- | 3.65  | 3    |
-- | 3.50  | 4    |
-- +-------+------+


-- SOLUTION:
SELECT 
    score,
    DENSE_RANK() OVER (ORDER BY score DESC) AS 'rank'
FROM Scores;

-- EXPLANATION:
-- 1. DENSE_RANK(): Window function for ranking
-- 2. OVER (ORDER BY score DESC): Partition and order specification
-- 3. DESC: Order from highest to lowest
--
-- DENSE_RANK vs RANK vs ROW_NUMBER:
-- Example scores: 100, 100, 90, 80
-- - DENSE_RANK: 1, 1, 2, 3 (no gaps)
-- - RANK:       1, 1, 3, 4 (gaps after ties)
-- - ROW_NUMBER: 1, 2, 3, 4 (unique numbers, no ties)

-- KEY CONCEPTS:
-- - Window Functions: Functions that operate on a set of rows
-- - DENSE_RANK(): Ranking with no gaps
-- - OVER clause: Defines the window specification

-- ALTERNATIVE SOLUTION (Without window functions):
-- SELECT s1.score,
--        (SELECT COUNT(DISTINCT s2.score) 
--         FROM Scores s2 
--         WHERE s2.score >= s1.score) AS 'rank'
-- FROM Scores s1
-- ORDER BY s1.score DESC;

-- TIME COMPLEXITY: O(n log n) for sorting
-- SPACE COMPLEXITY: O(n) for window function processing