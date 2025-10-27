-- LeetCode Problem 176: Second Highest Salary

-- Difficulty: Medium
-- Link: https://leetcode.com/problems/second-highest-salary/
--
-- PROBLEM DESCRIPTION:
-- Write a SQL query to find the second highest salary from Employee table.
-- If there is no second highest salary, return null.

-- TABLE:
-- Employee
-- +-------------+------+
-- | Column Name | Type |
-- +-------------+------+
-- | id          | int  |
-- | salary      | int  |
-- +-------------+------+
-- id is the primary key
--
-- EXAMPLE:
-- Input: 
-- Employee table:
-- +----+--------+
-- | id | salary |
-- +----+--------+
-- | 1  | 100    |
-- | 2  | 200    |
-- | 3  | 300    |
-- +----+--------+
-- Output: 
-- +---------------------+
-- | SecondHighestSalary |
-- +---------------------+
-- | 200                 |
-- +---------------------+
--
-- Example 2:
-- Input: 
-- Employee table:
-- +----+--------+
-- | id | salary |
-- +----+--------+
-- | 1  | 100    |
-- +----+--------+
-- Output: 
-- +---------------------+
-- | SecondHighestSalary |
-- +---------------------+
-- | null                |
-- +---------------------+


-- SOLUTION 1: Using MAX with subquery
SELECT MAX(salary) AS SecondHighestSalary
FROM Employee
WHERE salary < (SELECT MAX(salary) FROM Employee);

-- SOLUTION 2: Using LIMIT and OFFSET with IFNULL
SELECT IFNULL(
    (SELECT DISTINCT salary 
     FROM Employee 
     ORDER BY salary DESC 
     LIMIT 1 OFFSET 1),
    NULL
) AS SecondHighestSalary;

-- EXPLANATION:
-- Solution 1:
-- - Inner query finds the highest salary
-- - Outer query finds MAX of all salaries less than the highest
-- - Returns NULL if no such salary exists
--
-- Solution 2:
-- - ORDER BY salary DESC: Sort salaries in descending order
-- - DISTINCT: Handle duplicate salaries
-- - LIMIT 1 OFFSET 1: Skip first (highest) and take second
-- - IFNULL: Return NULL if no second highest exists

-- KEY CONCEPTS:
-- - Nested subqueries
-- - LIMIT and OFFSET for pagination
-- - IFNULL for NULL handling
-- - DISTINCT for removing duplicates

-- TIME COMPLEXITY: O(n log n) due to sorting
-- SPACE COMPLEXITY: O(1)