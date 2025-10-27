-- LeetCode Problem 182: Duplicate Emails

-- Difficulty: Easy
-- Link: https://leetcode.com/problems/duplicate-emails/
--
-- PROBLEM DESCRIPTION:
-- Write a SQL query to report all duplicate emails.
--
-- TABLE:
-- Person
-- +-------------+---------+
-- | Column Name | Type    |
-- +-------------+---------+
-- | id          | int     |
-- | email       | varchar |
-- +-------------+---------+
-- id is the primary key
--
-- EXAMPLE:
-- Input: 
-- Person table:
-- +----+---------+
-- | id | email   |
-- +----+---------+
-- | 1  | a@b.com |
-- | 2  | c@d.com |
-- | 3  | a@b.com |
-- +----+---------+
-- Output: 
-- +---------+
-- | Email   |
-- +---------+
-- | a@b.com |
-- +---------+
-- =====================================================

-- SOLUTION:
SELECT email AS Email
FROM Person
GROUP BY email
HAVING COUNT(email) > 1;

-- EXPLANATION:
-- 1. GROUP BY email: Groups all rows with the same email together
-- 2. HAVING COUNT(email) > 1: Filters groups that have more than 1 occurrence
-- 3. HAVING vs WHERE: HAVING is used after GROUP BY for aggregate conditions

-- KEY CONCEPTS:
-- - GROUP BY: Grouping rows with same values
-- - HAVING clause: Filtering grouped results
-- - COUNT function: Counting occurrences

-- TIME COMPLEXITY: O(n) for grouping and counting
-- SPACE COMPLEXITY: O(n) for storing grouped results