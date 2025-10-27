-- LeetCode Problem 183: Customers Who Never Order

-- Difficulty: Easy
-- Link: https://leetcode.com/problems/customers-who-never-order/
--
-- PROBLEM DESCRIPTION:
-- Write a SQL query to find all customers who never order anything.
--
-- TABLES:
-- Customers
-- +-------------+---------+
-- | Column Name | Type    |
-- +-------------+---------+
-- | id          | int     |
-- | name        | varchar |
-- +-------------+---------+
-- id is the primary key
--
-- Orders
-- +-------------+------+
-- | Column Name | Type |
-- +-------------+------+
-- | id          | int  |
-- | customerId  | int  |
-- +-------------+------+
-- id is the primary key
-- customerId is a foreign key to Customers.id
--
-- EXAMPLE:
-- Input: 
-- Customers table:
-- +----+-------+
-- | id | name  |
-- +----+-------+
-- | 1  | Joe   |
-- | 2  | Henry |
-- | 3  | Sam   |
-- | 4  | Max   |
-- +----+-------+
-- Orders table:
-- +----+------------+
-- | id | customerId |
-- +----+------------+
-- | 1  | 3          |
-- | 2  | 1          |
-- +----+------------+
-- Output: 
-- +-----------+
-- | Customers |
-- +-----------+
-- | Henry     |
-- | Max       |
-- +-----------+


-- SOLUTION 1: Using NOT IN
SELECT name AS Customers
FROM Customers
WHERE id NOT IN (
    SELECT customerId 
    FROM Orders
);

-- SOLUTION 2: Using LEFT JOIN
SELECT c.name AS Customers
FROM Customers c
LEFT JOIN Orders o ON c.id = o.customerId
WHERE o.id IS NULL;

-- EXPLANATION:
-- Solution 1: NOT IN approach
-- - Subquery finds all customerIds that have orders
-- - Main query selects customers NOT in that list
--
-- Solution 2: LEFT JOIN approach
-- - LEFT JOIN keeps all customers
-- - WHERE o.id IS NULL filters customers with no matching orders
-- - This is often more efficient than NOT IN

-- KEY CONCEPTS:
-- - NOT IN: Excluding values from a list
-- - LEFT JOIN: Finding non-matching rows
-- - NULL checking: Identifying missing relationships

-- TIME COMPLEXITY: O(n * m) for NOT IN, O(n + m) for LEFT JOIN
-- SPACE COMPLEXITY: O(k) where k is number of unique customerIds