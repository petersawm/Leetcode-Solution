-- LeetCode Problem 177: Nth Highest Salary

-- Difficulty: Medium
-- Link: https://leetcode.com/problems/nth-highest-salary/
--
-- PROBLEM DESCRIPTION:
-- Write a SQL function to get the Nth highest salary from Employee table.
-- If there is no Nth highest salary, return null.

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
-- n = 2
-- Output: 
-- +------------------------+
-- | getNthHighestSalary(2) |
-- +------------------------+
-- | 200                    |
-- +------------------------+


-- SOLUTION:
CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  DECLARE M INT;
  SET M = N - 1;
  RETURN (
      SELECT IFNULL(
          (SELECT DISTINCT salary 
           FROM Employee 
           ORDER BY salary DESC 
           LIMIT 1 OFFSET M),
          NULL
      )
  );
END;

-- EXPLANATION:
-- 1. Create a function that accepts N as parameter
-- 2. Calculate M = N - 1 (because OFFSET is 0-indexed)
-- 3. ORDER BY salary DESC: Sort salaries highest to lowest
-- 4. DISTINCT: Handle duplicate salaries
-- 5. LIMIT 1 OFFSET M: Skip M rows and take the next one
-- 6. IFNULL: Return NULL if Nth salary doesn't exist
--
-- Why M = N - 1?
-- - OFFSET 0 = 1st highest
-- - OFFSET 1 = 2nd highest
-- - OFFSET 2 = 3rd highest
-- - etc.

-- KEY CONCEPTS:
-- - CREATE FUNCTION: Defining reusable SQL functions
-- - DECLARE and SET: Variable declaration and assignment
-- - OFFSET: Skipping rows in result set
-- - Function parameters and return values

-- TIME COMPLEXITY: O(n log n) for sorting
-- SPACE COMPLEXITY: O(1)

-- USAGE EXAMPLE:
-- SELECT getNthHighestSalary(3) AS ThirdHighestSalary;