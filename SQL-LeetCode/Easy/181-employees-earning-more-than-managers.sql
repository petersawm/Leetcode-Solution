-- LeetCode Problem 181: Employees Earning More Than Their Managers
-- Difficulty: Easy
-- Link: https://leetcode.com/problems/employees-earning-more-than-their-managers/

-- PROBLEM DESCRIPTION:
-- Write a SQL query to find employees who earn more than their managers.

-- TABLE:
-- Employee
-- +-------------+---------+
-- | Column Name | Type    |
-- +-------------+---------+
-- | id          | int     |
-- | name        | varchar |
-- | salary      | int     |
-- | managerId   | int     |
-- +-------------+---------+
-- id is the primary key
-- managerId is a foreign key to id
--
-- EXAMPLE:
-- Input: 
-- Employee table:
-- +----+-------+--------+-----------+
-- | id | name  | salary | managerId |
-- +----+-------+--------+-----------+
-- | 1  | Joe   | 70000  | 3         |
-- | 2  | Henry | 80000  | 4         |
-- | 3  | Sam   | 60000  | Null      |
-- | 4  | Max   | 90000  | Null      |
-- +----+-------+--------+-----------+
-- Output: 
-- +----------+
-- | Employee |
-- +----------+
-- | Joe      |
-- +----------+


-- SOLUTION:
SELECT e1.name AS Employee
FROM Employee e1
INNER JOIN Employee e2 ON e1.managerId = e2.id
WHERE e1.salary > e2.salary;

-- EXPLANATION:
-- We perform a self-join where:
-- - e1 represents the employee
-- - e2 represents the manager (e1.managerId = e2.id)
-- Then we filter for cases where employee salary > manager salary

-- KEY CONCEPTS:
-- - Self JOIN: Joining a table with itself
-- - Alias usage: e1 and e2 to distinguish employee from manager

-- TIME COMPLEXITY: O(n^2) worst case for self-join
-- SPACE COMPLEXITY: O(1)