-- LeetCode Problem 175: Combine Two Tables

-- Difficulty: Easy
-- Link: https://leetcode.com/problems/combine-two-tables/
--
-- PROBLEM DESCRIPTION:
-- Write a SQL query to report the firstName, lastName, city, and state 
-- of each person in the Person table. If the address of a personId is 
-- not present in the Address table, report null instead.
--
-- TABLES:
-- Person
-- +-------------+---------+
-- | Column Name | Type    |
-- +-------------+---------+
-- | personId    | int     |
-- | firstName   | varchar |
-- | lastName    | varchar |
-- +-------------+---------+
-- personId is the primary key
--
-- Address
-- +-------------+---------+
-- | Column Name | Type    |
-- +-------------+---------+
-- | addressId   | int     |
-- | personId    | int     |
-- | city        | varchar |
-- | state       | varchar |
-- +-------------+---------+
-- addressId is the primary key
--
-- EXAMPLE:
-- Input: 
-- Person table:
-- +----------+----------+-----------+
-- | personId | lastName | firstName |
-- +----------+----------+-----------+
-- | 1        | Wang     | Allen     |
-- | 2        | Alice    | Bob       |
-- +----------+----------+-----------+
-- Address table:
-- +-----------+----------+---------------+------------+
-- | addressId | personId | city          | state      |
-- +-----------+----------+---------------+------------+
-- | 1         | 2        | New York City | New York   |
-- | 2         | 3        | Leetcode      | California |
-- +-----------+----------+---------------+------------+
-- Output: 
-- +-----------+----------+---------------+----------+
-- | firstName | lastName | city          | state    |
-- +-----------+----------+---------------+----------+
-- | Allen     | Wang     | Null          | Null     |
-- | Bob       | Alice    | New York City | New York |
-- +-----------+----------+---------------+----------+
-- =====================================================

-- SOLUTION:
SELECT 
    p.firstName, 
    p.lastName, 
    a.city, 
    a.state
FROM Person p
LEFT JOIN Address a ON p.personId = a.personId;

-- EXPLANATION:
-- We use LEFT JOIN because we want to include ALL persons from the 
-- Person table, regardless of whether they have a corresponding 
-- address in the Address table. When there's no match, the city 
-- and state columns will automatically be NULL.

-- KEY CONCEPTS:
-- - LEFT JOIN: Keeps all rows from the left table (Person)
-- - NULL handling: Automatically returns NULL for non-matching rows

-- TIME COMPLEXITY: O(n + m) where n = Person rows, m = Address rows
-- SPACE COMPLEXITY: O(1) - no additional space required