-- LeetCode Problem 626: Exchange Seats

-- Difficulty: Medium
-- Link: https://leetcode.com/problems/exchange-seats/

-- PROBLEM DESCRIPTION:
-- Write a SQL query to swap the seat id of every two consecutive 
-- students. If the number of students is odd, the id of the last 
-- student is not swapped.

-- TABLE:
-- Seat
-- +-------------+---------+
-- | Column Name | Type    |
-- +-------------+---------+
-- | id          | int     |
-- | student     | varchar |
-- +-------------+---------+
-- id is the primary key and continuous (1, 2, 3, ...)
--
-- EXAMPLE:
-- Input: 
-- Seat table:
-- +----+---------+
-- | id | student |
-- +----+---------+
-- | 1  | Abbot   |
-- | 2  | Doris   |
-- | 3  | Emerson |
-- | 4  | Green   |
-- | 5  | Jeames  |
-- +----+---------+
-- Output: 
-- +----+---------+
-- | id | student |
-- +----+---------+
-- | 1  | Doris   |
-- | 2  | Abbot   |
-- | 3  | Green   |
-- | 4  | Emerson |
-- | 5  | Jeames  |
-- +----+---------+


-- SOLUTION:
SELECT 
    CASE
        WHEN id % 2 = 1 AND id != (SELECT MAX(id) FROM Seat) THEN id + 1
        WHEN id % 2 = 0 THEN id - 1
        ELSE id
    END AS id,
    student
FROM Seat
ORDER BY id;

-- EXPLANATION:
-- Logic breakdown:
-- 1. If id is odd AND not the last seat: swap with next (id + 1)
-- 2. If id is even: swap with previous (id - 1)
-- 3. If id is odd AND is the last seat: keep same (else id)
--
-- Examples:
-- - id=1 (odd, not last): becomes 2
-- - id=2 (even): becomes 1
-- - id=5 (odd, last): stays 5

-- KEY CONCEPTS:
-- - CASE WHEN: Conditional logic in SQL
-- - Modulo operator (%): Check odd/even
-- - Subquery: Find maximum id
-- - ORDER BY: Sort final results

-- ALTERNATIVE SOLUTION (Using LAG/LEAD):
-- SELECT id,
--        CASE
--            WHEN id % 2 = 1 THEN COALESCE(LEAD(student) OVER (ORDER BY id), student)
--            ELSE LAG(student) OVER (ORDER BY id)
--        END AS student
-- FROM Seat;

-- TIME COMPLEXITY: O(n log n) for sorting
-- SPACE COMPLEXITY: O(1)