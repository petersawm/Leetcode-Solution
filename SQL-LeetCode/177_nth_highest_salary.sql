/*
 * LeetCode Problem: 177 - Nth Highest Salary
 * Difficulty: Medium
 * Link: https://leetcode.com/problems/nth-highest-salary/
 * 
 * Problem Statement:
 * Write a SQL query to get the nth highest salary from the Employee table.
 * If there is no nth highest salary, the query should return null.
 * 
 * Table: Employee
 * +-------------+------+
 * | Column Name | Type |
 * +-------------+------+
 * | id          | int  |
 * | salary      | int  |
 * +-------------+------+
 * id is the primary key column for this table.
 * Each row contains information about the salary of an employee.
 * 
 * Example 1:
 * Input:
 * Employee table:
 * +----+--------+
 * | id | salary |
 * +----+--------+
 * | 1  | 100    |
 * | 2  | 200    |
 * | 3  | 300    |
 * +----+--------+
 * n = 2
 * 
 * Output:
 * +------------------------+
 * | getNthHighestSalary(2) |
 * +------------------------+
 * | 200                    |
 * +------------------------+
 * 
 * Example 2:
 * Input:
 * Employee table:
 * +----+--------+
 * | id | salary |
 * +----+--------+
 * | 1  | 100    |
 * +----+--------+
 * n = 2
 * 
 * Output:
 * +------------------------+
 * | getNthHighestSalary(2) |
 * +------------------------+
 * | null                   |
 * +------------------------+
 */


-- SOLUTION 1: DENSE_RANK with Function (Best)


/*
 * Approach: Use DENSE_RANK to handle ties properly
 * 
 * Time Complexity: O(n log n) - sorting
 * Space Complexity: O(n)
 * 
 * Key Insights:
 * - DENSE_RANK handles duplicate salaries correctly
 * - Must use DISTINCT to get unique salaries
 * - LIMIT 1 gets the specific rank
 * - Returns NULL if N is out of range
 */

CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  RETURN (
      SELECT DISTINCT salary
      FROM (
          SELECT 
              salary,
              DENSE_RANK() OVER (ORDER BY salary DESC) as rnk
          FROM Employee
      ) ranked
      WHERE rnk = N
      LIMIT 1
  );
END



-- SOLUTION 2: OFFSET Method (Elegant)


/*
 * Approach: Order by salary DESC, skip N-1 rows
 * 
 * Pros: Very clean and readable
 * Cons: Need to handle N=0 edge case
 */

CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  DECLARE M INT;
  SET M = N - 1;
  RETURN (
      SELECT DISTINCT salary
      FROM Employee
      ORDER BY salary DESC
      LIMIT 1 OFFSET M
  );
END



-- SOLUTION 3: Subquery Counting (Traditional)


/*
 * Approach: Count how many DISTINCT salaries are higher
 * 
 * Time Complexity: O(n²)
 * Pros: Works on older SQL versions
 * Cons: Slower for large datasets
 */

CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  RETURN (
      SELECT MAX(salary)
      FROM Employee
      WHERE (
          SELECT COUNT(DISTINCT e2.salary)
          FROM Employee e2
          WHERE e2.salary > Employee.salary
      ) = N - 1
  );
END



-- SOLUTION 4: Using CTE (Most Readable)


/*
 * Approach: Step-by-step with Common Table Expression
 */

CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  RETURN (
      WITH RankedSalaries AS (
          SELECT DISTINCT
              salary,
              DENSE_RANK() OVER (ORDER BY salary DESC) as salary_rank
          FROM Employee
      )
      SELECT salary
      FROM RankedSalaries
      WHERE salary_rank = N
      LIMIT 1
  );
END



-- SOLUTION 5: Without Function (For Testing)


/*
 * If you can't create functions, use this standalone query
 * Replace @N with your desired rank
 */

SET @N = 2;

SELECT DISTINCT salary AS SecondHighestSalary
FROM (
    SELECT 
        salary,
        DENSE_RANK() OVER (ORDER BY salary DESC) as rnk
    FROM Employee
) ranked
WHERE rnk = @N;



-- TEST DATA SETUP


DROP TABLE IF EXISTS Employee;

CREATE TABLE Employee (
    id INT PRIMARY KEY AUTO_INCREMENT,
    salary INT
);

-- Test case 1: Normal case with distinct salaries
INSERT INTO Employee (salary) VALUES
(100),
(200),
(300);

-- Test the function
SELECT getNthHighestSalary(1) AS '1st Highest';  -- Should return 300
SELECT getNthHighestSalary(2) AS '2nd Highest';  -- Should return 200
SELECT getNthHighestSalary(3) AS '3rd Highest';  -- Should return 100
SELECT getNthHighestSalary(4) AS '4th Highest';  -- Should return NULL



-- EXTENDED TEST CASES


-- Test case 2: Duplicate salaries
DELETE FROM Employee;
INSERT INTO Employee (salary) VALUES
(100),
(200),
(200),
(300),
(300),
(300);

SELECT getNthHighestSalary(1);  -- Should return 300 (highest)
SELECT getNthHighestSalary(2);  -- Should return 200 (2nd highest)
SELECT getNthHighestSalary(3);  -- Should return 100 (3rd highest)
SELECT getNthHighestSalary(4);  -- Should return NULL (doesn't exist)


-- Test case 3: All same salary
DELETE FROM Employee;
INSERT INTO Employee (salary) VALUES
(100),
(100),
(100);

SELECT getNthHighestSalary(1);  -- Should return 100
SELECT getNthHighestSalary(2);  -- Should return NULL


-- Test case 4: Single employee
DELETE FROM Employee;
INSERT INTO Employee (salary) VALUES (500);

SELECT getNthHighestSalary(1);  -- Should return 500
SELECT getNthHighestSalary(2);  -- Should return NULL


-- Test case 5: Empty table
DELETE FROM Employee;

SELECT getNthHighestSalary(1);  -- Should return NULL



-- VERIFICATION QUERIES


-- View all salaries with ranks
SELECT 
    id,
    salary,
    DENSE_RANK() OVER (ORDER BY salary DESC) as dense_rank,
    RANK() OVER (ORDER BY salary DESC) as rank_func,
    ROW_NUMBER() OVER (ORDER BY salary DESC) as row_num
FROM Employee
ORDER BY salary DESC;

-- Count distinct salaries
SELECT 
    COUNT(DISTINCT salary) as unique_salaries,
    COUNT(*) as total_employees,
    MAX(salary) as highest,
    MIN(salary) as lowest
FROM Employee;



-- VISUAL DEMONSTRATION


-- Show why DENSE_RANK is correct
DELETE FROM Employee;
INSERT INTO Employee (salary) VALUES
(500),
(400),
(400),
(300),
(200);

SELECT 
    salary,
    DENSE_RANK() OVER (ORDER BY salary DESC) as 'DENSE_RANK (✓)',
    RANK() OVER (ORDER BY salary DESC) as 'RANK (✗)',
    ROW_NUMBER() OVER (ORDER BY salary DESC) as 'ROW_NUMBER (✗)'
FROM Employee;

/*
 * Results:
 * salary | DENSE_RANK | RANK | ROW_NUMBER
 * -------|------------|------|------------
 * 500    | 1          | 1    | 1
 * 400    | 2          | 2    | 2
 * 400    | 2          | 2    | 3  ← Duplicate
 * 300    | 3          | 4    | 4  ← RANK skips 3!
 * 200    | 4          | 5    | 5
 * 
 * For N=3:
 * - DENSE_RANK: Returns 300 ✓ (correct - 3rd unique salary)
 * - RANK: Would skip to 4th
 * - ROW_NUMBER: Would return 400 (wrong!)
 */



-- COMMON MISTAKES TO AVOID


-- ❌ MISTAKE 1: Forgetting DISTINCT
CREATE FUNCTION Wrong1(N INT) RETURNS INT
BEGIN
  RETURN (
      SELECT salary  -- Missing DISTINCT!
      FROM Employee
      ORDER BY salary DESC
      LIMIT 1 OFFSET N-1
  );
END
-- Problem: With duplicates [300,300,200], N=2 returns 300 (wrong!)
-- Fix: Add DISTINCT


-- ❌ MISTAKE 2: Using RANK instead of DENSE_RANK
CREATE FUNCTION Wrong2(N INT) RETURNS INT
BEGIN
  RETURN (
      SELECT salary
      FROM (
          SELECT salary, RANK() OVER (ORDER BY salary DESC) as rnk
          FROM Employee
      ) ranked
      WHERE rnk = N
  );
END
-- Problem: RANK skips numbers after ties
-- Fix: Use DENSE_RANK


-- ❌ MISTAKE 3: Not handling NULL case
CREATE FUNCTION Wrong3(N INT) RETURNS INT
BEGIN
  RETURN (
      SELECT salary
      FROM Employee
      ORDER BY salary DESC
      LIMIT 1 OFFSET N-1
  );
END
-- Problem: Returns empty result instead of NULL when N out of range
-- Fix: Ensure function returns NULL, or wrap in COALESCE


-- ❌ MISTAKE 4: Off-by-one error with OFFSET
CREATE FUNCTION Wrong4(N INT) RETURNS INT
BEGIN
  RETURN (
      SELECT DISTINCT salary
      FROM Employee
      ORDER BY salary DESC
      LIMIT 1 OFFSET N  -- Should be N-1!
  );
END
-- Problem: OFFSET N skips N rows, but we want the Nth row
-- Fix: Use OFFSET N-1



-- PERFORMANCE COMPARISON


-- Create large test table
DELETE FROM Employee;

-- Insert 10000 employees with random salaries
DELIMITER //
CREATE PROCEDURE GenerateTestData()
BEGIN
    DECLARE i INT DEFAULT 1;
    WHILE i <= 10000 DO
        INSERT INTO Employee (salary) VALUES (FLOOR(RAND() * 10000));
        SET i = i + 1;
    END WHILE;
END//
DELIMITER ;

CALL GenerateTestData();

-- Test query performance
-- Method 1: DENSE_RANK (Fast - O(n log n))
SELECT COUNT(*) FROM (
    SELECT DISTINCT salary, DENSE_RANK() OVER (ORDER BY salary DESC) as rnk
    FROM Employee
) ranked WHERE rnk = 100;

-- Method 2: Subquery (Slow - O(n²))
SELECT COUNT(*) FROM Employee e1
WHERE (SELECT COUNT(DISTINCT salary) FROM Employee e2 WHERE e2.salary > e1.salary) = 99;



-- INTERVIEW DISCUSSION POINTS


/*
 * When discussing this problem:
 * 
 * 1. Clarify requirements:
 *    Q: "What should we return if N is larger than the number of employees?"
 *    A: Return NULL
 *    
 *    Q: "How do we handle duplicate salaries?"
 *    A: Count unique salaries only (use DISTINCT)
 *    
 *    Q: "What if N is 0 or negative?"
 *    A: Return NULL (though problem usually assumes N >= 1)
 * 
 * 2. Discuss approaches:
 *    "I can think of three approaches:
 *    
 *    a) DENSE_RANK: Rank all salaries, filter by rank N
 *       - O(n log n) time
 *       - Handles duplicates correctly
 *       - Modern SQL approach
 *    
 *    b) OFFSET: Order DESC, skip N-1 rows
 *       - Very clean code
 *       - Must use DISTINCT for duplicates
 *       - Simple to understand
 *    
 *    c) Correlated subquery: Count higher salaries
 *       - O(n²) time
 *       - Works on older SQL versions
 *       - Slower for large datasets
 *    
 *    I'll use DENSE_RANK for optimal performance."
 * 
 * 3. Why DENSE_RANK vs others:
 *    "DENSE_RANK is correct because:
 *    - Handles ties properly (doesn't skip ranks)
 *    - With salaries [300,200,200,100], ranks are [1,2,2,3]
 *    - RANK would give [1,2,2,4] - skips 3
 *    - ROW_NUMBER would give [1,2,3,4] - treats duplicates as different
 *    
 *    We want DENSE_RANK because we're looking for the Nth UNIQUE salary."
 * 
 * 4. Edge cases to mention:
 *    - Empty table → NULL
 *    - N larger than distinct salaries → NULL
 *    - All same salary → 1st returns that salary, 2nd+ returns NULL
 *    - Duplicate salaries → Count as one rank
 * 
 * 5. Optimization:
 *    "For very large tables, I'd:
 *    - Add index on salary column: CREATE INDEX idx_salary ON Employee(salary DESC)
 *    - Consider caching if this query runs frequently
 *    - For millions of rows, DENSE_RANK is still efficient O(n log n)"
 */



-- RELATED PROBLEMS


/*
 * Once you understand this, try:
 * 
 * - Problem 176: Second Highest Salary (easier - just N=2)
 * - Problem 178: Rank Scores (similar ranking logic)
 * - Problem 184: Department Highest Salary (ranking within groups)
 * - Problem 185: Department Top Three Salaries (top N per group)
 */



-- BONUS: Generic Top N Query


-- If you need multiple Nth values at once:
SELECT 
    1 as N, getNthHighestSalary(1) as salary
UNION ALL
SELECT 
    2 as N, getNthHighestSalary(2) as salary
UNION ALL
SELECT 
    3 as N, getNthHighestSalary(3) as salary
UNION ALL
SELECT 
    4 as N, getNthHighestSalary(4) as salary
UNION ALL
SELECT 
    5 as N, getNthHighestSalary(5) as salary;

-- Or show all ranks at once:
SELECT 
    salary,
    DENSE_RANK() OVER (ORDER BY salary DESC) as rank
FROM Employee
GROUP BY salary
ORDER BY salary DESC
LIMIT 10;