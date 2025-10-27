-- LeetCode Problem 184: Department Highest Salary

-- Difficulty: Medium
-- Link: https://leetcode.com/problems/department-highest-salary/

-- PROBLEM DESCRIPTION:
-- Write a SQL query to find employees who have the highest salary 
-- in each department.

-- TABLES:
-- Employee
-- +--------------+---------+
-- | Column Name  | Type    |
-- +--------------+---------+
-- | id           | int     |
-- | name         | varchar |
-- | salary       | int     |
-- | departmentId | int     |
-- +--------------+---------+
-- id is the primary key
--
-- Department
-- +--------------+---------+
-- | Column Name  | Type    |
-- +--------------+---------+
-- | id           | int     |
-- | name         | varchar |
-- +--------------+---------+
-- id is the primary key
--
-- EXAMPLE:
-- Input: 
-- Employee table:
-- +----+-------+--------+--------------+
-- | id | name  | salary | departmentId |
-- +----+-------+--------+--------------+
-- | 1  | Joe   | 70000  | 1            |
-- | 2  | Jim   | 90000  | 1            |
-- | 3  | Henry | 80000  | 2            |
-- | 4  | Sam   | 60000  | 2            |
-- | 5  | Max   | 90000  | 1            |
-- +----+-------+--------+--------------+
-- Department table:
-- +----+-------+
-- | id | name  |
-- +----+-------+
-- | 1  | IT    |
-- | 2  | Sales |
-- +----+-------+
-- Output: 
-- +------------+----------+--------+
-- | Department | Employee | Salary |
-- +------------+----------+--------+
-- | IT         | Jim      | 90000  |
-- | Sales      | Henry    | 80000  |
-- | IT         | Max      | 90000  |
-- +------------+----------+--------+


-- SOLUTION:
SELECT 
    d.name AS Department, 
    e.name AS Employee, 
    e.salary AS Salary
FROM Employee e
INNER JOIN Department d ON e.departmentId = d.id
WHERE (e.departmentId, e.salary) IN (
    SELECT departmentId, MAX(salary)
    FROM Employee
    GROUP BY departmentId
);

-- EXPLANATION:
-- 1. Subquery finds the highest salary for each department
-- 2. Returns pairs of (departmentId, max_salary)
-- 3. Main query joins Employee and Department tables
-- 4. Filters employees whose (departmentId, salary) matches the subquery result
-- 5. This handles cases where multiple employees have the same max salary

-- KEY CONCEPTS:
-- - Subquery with tuple comparison: (col1, col2) IN (subquery)
-- - GROUP BY with aggregate functions
-- - JOIN to get department names
-- - Handling ties (multiple employees with same max salary)

-- ALTERNATIVE SOLUTION (Using window function):
-- SELECT Department, Employee, Salary
-- FROM (
--     SELECT d.name AS Department,
--            e.name AS Employee,
--            e.salary AS Salary,
--            RANK() OVER (PARTITION BY e.departmentId ORDER BY e.salary DESC) AS rnk
--     FROM Employee e
--     JOIN Department d ON e.departmentId = d.id
-- ) ranked
-- WHERE rnk = 1;

-- TIME COMPLEXITY: O(n) for grouping and filtering
-- SPACE COMPLEXITY: O(k) where k is number of departments