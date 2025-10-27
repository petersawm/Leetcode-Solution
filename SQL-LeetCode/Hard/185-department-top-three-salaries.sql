-- LeetCode Problem 185: Department Top Three Salaries

-- Difficulty: Hard
-- Link: https://leetcode.com/problems/department-top-three-salaries/

-- PROBLEM DESCRIPTION:
-- A company's executives want to see the top 3 earners in each 
-- department. Write a SQL query to find employees who are high 
-- earners in each of the departments.

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
-- | 1  | Joe   | 85000  | 1            |
-- | 2  | Henry | 80000  | 2            |
-- | 3  | Sam   | 60000  | 2            |
-- | 4  | Max   | 90000  | 1            |
-- | 5  | Janet | 69000  | 1            |
-- | 6  | Randy | 85000  | 1            |
-- | 7  | Will  | 70000  | 1            |
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
-- | IT         | Max      | 90000  |
-- | IT         | Joe      | 85000  |
-- | IT         | Randy    | 85000  |
-- | IT         | Will     | 70000  |
-- | Sales      | Henry    | 80000  |
-- | Sales      | Sam      | 60000  |
-- +------------+----------+--------+


-- SOLUTION 1: Using correlated subquery
SELECT 
    d.name AS Department, 
    e.name AS Employee, 
    e.salary AS Salary
FROM Employee e
INNER JOIN Department d ON e.departmentId = d.id
WHERE (
    SELECT COUNT(DISTINCT e2.salary)
    FROM Employee e2
    WHERE e2.departmentId = e.departmentId 
      AND e2.salary >= e.salary
) <= 3
ORDER BY d.name, e.salary DESC;

-- SOLUTION 2: Using DENSE_RANK window function with CTE
WITH RankedSalaries AS (
    SELECT 
        d.name AS Department, 
        e.name AS Employee, 
        e.salary AS Salary,
        DENSE_RANK() OVER (
            PARTITION BY e.departmentId 
            ORDER BY e.salary DESC
        ) AS salary_rank
    FROM Employee e
    INNER JOIN Department d ON e.departmentId = d.id
)
SELECT Department, Employee, Salary
FROM RankedSalaries
WHERE salary_rank <= 3
ORDER BY Department, Salary DESC;

-- EXPLANATION:
-- Solution 1 (Correlated subquery):
-- - For each employee, count how many DISTINCT salaries are >= their salary
-- - If count <= 3, they're in top 3
-- - DISTINCT handles ties (multiple people with same salary)
--
-- Solution 2 (Window function with CTE):
-- - PARTITION BY: Create separate ranking for each department
-- - DENSE_RANK(): Rank salaries without gaps (handles ties properly)
-- - WHERE salary_rank <= 3: Filter top 3 ranks
-- - CTE makes query more readable and maintainable

-- Why DENSE_RANK instead of RANK?
-- Example: 100, 100, 90, 80
-- - DENSE_RANK: 1, 1, 2, 3 (all included in top 3)
-- - RANK:       1, 1, 3, 4 (only first two included)

-- KEY CONCEPTS:
-- - Common Table Expressions (CTE): WITH clause
-- - Window Functions: DENSE_RANK() with PARTITION BY
-- - Correlated subqueries: Subquery referencing outer query
-- - DISTINCT in aggregation: Handling duplicates

-- TIME COMPLEXITY: 
-- - Solution 1: O(n^2) for correlated subquery
-- - Solution 2: O(n log n) for window function
-- SPACE COMPLEXITY: O(n) for intermediate results