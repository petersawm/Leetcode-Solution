/*
 * LeetCode Problem: 180 - Consecutive Numbers
 * Difficulty: Medium
 * Link: https://leetcode.com/problems/consecutive-numbers/
 * 
 * Problem Statement:
 * Find all numbers that appear at least three times consecutively.
 * 
 * Return the result table in any order.
 * 
 * Table: Logs
 * +-------------+---------+
 * | Column Name | Type    |
 * +-------------+---------+
 * | id          | int     |
 * | num         | varchar |
 * +-------------+---------+
 * id is the primary key for this table.
 * id is an autoincrement column.
 * 
 * Example:
 * Input:
 * Logs table:
 * +----+-----+
 * | id | num |
 * +----+-----+
 * | 1  | 1   |
 * | 2  | 1   |
 * | 3  | 1   |
 * | 4  | 2   |
 * | 5  | 1   |
 * | 6  | 2   |
 * | 7  | 2   |
 * +----+-----+
 * 
 * Output:
 * +-----------------+
 * | ConsecutiveNums |
 * +-----------------+
 * | 1               |
 * +-----------------+
 * 
 * Explanation: 1 is the only number that appears consecutively for at least three times.
 */


-- SOLUTION 1: Self JOIN (Most Intuitive)


/*
 * Approach: Join table with itself three times
 * 
 * Time Complexity: O(n³) in worst case, O(n) with indexes
 * Space Complexity: O(n)
 * 
 * Key Insights:
 * - Use self-join to compare consecutive rows
 * - Check if id values are consecutive (l1.id + 1, l1.id + 2)
 * - Check if num values are the same
 * - Use DISTINCT to avoid duplicates
 */

SELECT DISTINCT
    l1.num AS ConsecutiveNums
FROM
    Logs l1
    JOIN Logs l2 ON l1.id = l2.id - 1
    JOIN Logs l3 ON l1.id = l3.id - 2
WHERE
    l1.num = l2.num 
    AND l2.num = l3.num;



-- SOLUTION 2: Window Functions (Modern SQL)


/*
 * Approach: Use LAG/LEAD to look at adjacent rows
 * 
 * Time Complexity: O(n)
 * Space Complexity: O(n)
 * 
 * Pros: More efficient, cleaner code
 * Cons: Requires SQL:2003 support (most modern databases)
 */

SELECT DISTINCT
    num AS ConsecutiveNums
FROM (
    SELECT 
        num,
        LAG(num, 1) OVER (ORDER BY id) AS prev_num,
        LAG(num, 2) OVER (ORDER BY id) AS prev_prev_num
    FROM 
        Logs
) AS subquery
WHERE 
    num = prev_num 
    AND num = prev_prev_num;



-- SOLUTION 3: LEAD Function (Alternative)


/*
 * Approach: Use LEAD instead of LAG to look ahead
 * Same logic, different direction
 */

SELECT DISTINCT
    num AS ConsecutiveNums
FROM (
    SELECT 
        num,
        LEAD(num, 1) OVER (ORDER BY id) AS next_num,
        LEAD(num, 2) OVER (ORDER BY id) AS next_next_num
    FROM 
        Logs
) AS subquery
WHERE 
    num = next_num 
    AND num = next_next_num;



-- SOLUTION 4: Using Variables (MySQL Specific)


/*
 * Approach: Track consecutive count with user variables
 * 
 * Pros: Efficient, works for any consecutive count (not just 3)
 * Cons: MySQL-specific, requires careful variable initialization
 */

SELECT DISTINCT
    num AS ConsecutiveNums
FROM (
    SELECT 
        num,
        @count := IF(@prev = num, @count + 1, 1) AS count,
        @prev := num
    FROM 
        Logs,
        (SELECT @count := 0, @prev := NULL) AS vars
    ORDER BY 
        id
) AS subquery
WHERE 
    count >= 3;



-- SOLUTION 5: CTE with Window Function (Most Readable)


/*
 * Approach: Break down logic into clear steps
 * Best for production code and interviews
 */

WITH NumberedLogs AS (
    SELECT 
        id,
        num,
        LAG(num, 1) OVER (ORDER BY id) AS prev1,
        LAG(num, 2) OVER (ORDER BY id) AS prev2
    FROM 
        Logs
)
SELECT DISTINCT
    num AS ConsecutiveNums
FROM 
    NumberedLogs
WHERE 
    num = prev1 
    AND num = prev2;



-- TEST DATA SETUP


DROP TABLE IF EXISTS Logs;

CREATE TABLE Logs (
    id INT PRIMARY KEY AUTO_INCREMENT,
    num VARCHAR(10)
);

INSERT INTO Logs (num) VALUES
('1'),
('1'),
('1'),
('2'),
('1'),
('2'),
('2');



-- VERIFICATION QUERIES


-- View all logs
SELECT * FROM Logs;

-- Check consecutive sequences manually
SELECT 
    l1.id AS id1, 
    l1.num AS num1,
    l2.id AS id2, 
    l2.num AS num2,
    l3.id AS id3, 
    l3.num AS num3,
    CASE 
        WHEN l1.num = l2.num AND l2.num = l3.num THEN '✓ CONSECUTIVE'
        ELSE '✗ NOT CONSECUTIVE'
    END AS status
FROM
    Logs l1
    JOIN Logs l2 ON l1.id = l2.id - 1
    JOIN Logs l3 ON l1.id = l3.id - 2
ORDER BY
    l1.id;

-- Visualize with LAG
SELECT 
    id,
    num,
    LAG(num, 1) OVER (ORDER BY id) AS prev1,
    LAG(num, 2) OVER (ORDER BY id) AS prev2,
    CASE 
        WHEN num = LAG(num, 1) OVER (ORDER BY id) 
         AND num = LAG(num, 2) OVER (ORDER BY id)
        THEN '✓ 3 CONSECUTIVE'
        ELSE ''
    END AS consecutive_status
FROM 
    Logs;



-- MANUAL CALCULATION


/*
 * Walking through the example:
 * 
 * id | num | prev1 | prev2 | consecutive?
 * ---|-----|-------|-------|-------------
 * 1  | 1   | NULL  | NULL  | No (need 3)
 * 2  | 1   | 1     | NULL  | No (need 3)
 * 3  | 1   | 1     | 1     | YES! ✓ (1,1,1)
 * 4  | 2   | 1     | 1     | No (2,1,1)
 * 5  | 1   | 2     | 1     | No (1,2,1)
 * 6  | 2   | 1     | 2     | No (2,1,2)
 * 7  | 2   | 2     | 1     | No (2,2,1)
 * 
 * Result: Only "1" appears 3 times consecutively
 */



-- EXTENDED TEST CASES

-- Test case 2: Multiple consecutive sequences
DROP TABLE IF EXISTS Logs;
CREATE TABLE Logs (id INT PRIMARY KEY AUTO_INCREMENT, num VARCHAR(10));
INSERT INTO Logs (num) VALUES ('1'),('1'),('1'),('2'),('2'),('2'),('3');

-- Should return both '1' and '2'

-- Test case 3: Four consecutive numbers
DROP TABLE IF EXISTS Logs;
CREATE TABLE Logs (id INT PRIMARY KEY AUTO_INCREMENT, num VARCHAR(10));
INSERT INTO Logs (num) VALUES ('1'),('1'),('1'),('1'),('2');

-- Should return '1' (appears 4 times consecutively)

-- Test case 4: No consecutive numbers
DROP TABLE IF EXISTS Logs;
CREATE TABLE Logs (id INT PRIMARY KEY AUTO_INCREMENT, num VARCHAR(10));
INSERT INTO Logs (num) VALUES ('1'),('2'),('3'),('1'),('2');

-- Should return empty result



-- COMMON MISTAKES TO AVOID


-- ❌ MISTAKE 1: Forgetting DISTINCT
-- Without DISTINCT, you might get duplicate results if number appears
-- multiple times in different consecutive sequences

-- ❌ MISTAKE 2: Wrong join condition
-- This is WRONG:
-- JOIN Logs l2 ON l1.id = l2.id + 1  (backward)
-- Correct:
-- JOIN Logs l2 ON l1.id = l2.id - 1  (forward)

-- ❌ MISTAKE 3: Not considering gaps in IDs
-- If IDs are not consecutive (1,2,4,5), simple id+1 might fail
-- The problem assumes consecutive IDs, but in real scenarios, consider:
-- ROW_NUMBER() OVER (ORDER BY id) for true consecutive checking

-- ❌ MISTAKE 4: Comparing with wrong number of rows
-- Need to check 3 consecutive: current, prev, prev-prev
-- Don't compare only 2 rows



-- PERFORMANCE CONSIDERATIONS

-- Create index on id for faster joins
CREATE INDEX idx_id ON Logs(id);

-- Create index on num for faster filtering
CREATE INDEX idx_num ON Logs(num);

-- For very large tables (millions of rows):
-- - Window functions are generally faster than self-joins
-- - Consider partitioning if data can be divided logically
-- - Use EXPLAIN to check query execution plan



-- INTERVIEW DISCUSSION POINTS


/*
 * When discussing this problem:
 * 
 * 1. Clarify requirements:
 *    Q: "Are IDs guaranteed to be consecutive?"
 *    Q: "Can numbers appear multiple times non-consecutively?"
 *    Q: "Do we need exactly 3 or at least 3 consecutive?"
 * 
 * 2. Discuss approaches:
 *    "I can think of two main approaches:
 *    - Self-join: Join table 3 times, check consecutive IDs
 *    - Window functions: Use LAG/LEAD to look at adjacent rows
 *    Window functions are more efficient for modern SQL databases."
 * 
 * 3. Mention trade-offs:
 *    "Self-join is easier to understand but less efficient O(n³)
 *    Window functions are O(n) but require SQL:2003 support"
 * 
 * 4. Edge cases:
 *    - What if table is empty? (Return empty)
 *    - What if only 1 or 2 rows? (Return empty)
 *    - What if all numbers are the same? (Return that number)
 *    - What if IDs have gaps? (Problem assumes no gaps)
 * 
 * 5. Scalability:
 *    "For millions of rows, I'd use window functions with proper indexing
 *    on the id column. We could also consider partitioning by date range
 *    if this is time-series data."
 */



-- BONUS: Generalized Solution (N Consecutive)


/*
 * What if we need to find numbers appearing N times consecutively?
 * Using window functions with dynamic N
 */

-- For N = 4 consecutive numbers:
SELECT DISTINCT
    num AS ConsecutiveNums
FROM (
    SELECT 
        num,
        LAG(num, 1) OVER (ORDER BY id) AS prev1,
        LAG(num, 2) OVER (ORDER BY id) AS prev2,
        LAG(num, 3) OVER (ORDER BY id) AS prev3
    FROM 
        Logs
) AS subquery
WHERE 
    num = prev1 
    AND num = prev2
    AND num = prev3;



-- ALTERNATIVE: Group Islands Approach


/*
 * Advanced technique: Find "islands" of consecutive numbers
 * Useful when you need to know WHERE sequences start/end
 */

WITH GroupedLogs AS (
    SELECT 
        id,
        num,
        id - ROW_NUMBER() OVER (PARTITION BY num ORDER BY id) AS grp
    FROM 
        Logs
),
ConsecutiveCounts AS (
    SELECT 
        num,
        grp,
        COUNT(*) AS consecutive_count,
        MIN(id) AS start_id,
        MAX(id) AS end_id
    FROM 
        GroupedLogs
    GROUP BY 
        num, grp
    HAVING 
        COUNT(*) >= 3
)
SELECT DISTINCT
    num AS ConsecutiveNums
FROM 
    ConsecutiveCounts;

-- This also shows START and END of consecutive sequences
SELECT 
    num,
    consecutive_count,
    start_id,
    end_id
FROM 
    ConsecutiveCounts
ORDER BY 
    start_id;