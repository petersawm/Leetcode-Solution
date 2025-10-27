-- LeetCode Problem 196: Delete Duplicate Emails

-- Difficulty: Easy
-- Link: https://leetcode.com/problems/delete-duplicate-emails/
--
-- PROBLEM DESCRIPTION:
-- Write a SQL query to delete all duplicate emails, keeping only 
-- the one with the smallest id.
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
-- +----+------------------+
-- | id | email            |
-- +----+------------------+
-- | 1  | john@example.com |
-- | 2  | bob@example.com  |
-- | 3  | john@example.com |
-- +----+------------------+
-- Output: 
-- +----+------------------+
-- | id | email            |
-- +----+------------------+
-- | 1  | john@example.com |
-- | 2  | bob@example.com  |
-- +----+------------------+


-- SOLUTION:
DELETE p1 
FROM Person p1
INNER JOIN Person p2 
WHERE p1.email = p2.email 
  AND p1.id > p2.id;

-- EXPLANATION:
-- 1. Self-join Person table (p1 and p2)
-- 2. Match rows with same email
-- 3. Keep the one with smaller id (delete where p1.id > p2.id)
-- 4. DELETE p1 removes the duplicate with larger id

-- IMPORTANT NOTES:
-- - This modifies the table permanently
-- - Always backup data before running DELETE queries
-- - Some databases require different DELETE syntax

-- KEY CONCEPTS:
-- - DELETE with JOIN: Removing rows based on join conditions
-- - Self JOIN: Comparing rows within the same table
-- - Duplicate removal: Keeping records based on criteria

-- TIME COMPLEXITY: O(n^2) for self-join
-- SPACE COMPLEXITY: O(1) - in-place deletion