/*
 * LeetCode Problem: 197 - Rising Temperature
 * Difficulty: Easy
 * Link: https://leetcode.com/problems/rising-temperature/
 * 
 * Problem Statement:
 * Find all dates' id with higher temperatures compared to its previous dates (yesterday).
 * 
 * Table: Weather
 * +---------------+---------+
 * | Column Name   | Type    |
 * +---------------+---------+
 * | id            | int     |
 * | recordDate    | date    |
 * | temperature   | int     |
 * +---------------+---------+
 * id is the primary key for this table.
 * 
 * Example:
 * Input:
 * Weather table:
 * +----+------------+-------------+
 * | id | recordDate | temperature |
 * +----+------------+-------------+
 * | 1  | 2015-01-01 | 10          |
 * | 2  | 2015-01-02 | 25          |
 * | 3  | 2015-01-03 | 20          |
 * | 4  | 2015-01-04 | 30          |
 * +----+------------+-------------+
 * 
 * Output:
 * +----+
 * | id |
 * +----+
 * | 2  |
 * | 4  |
 * +----+
 * 
 * Explanation:
 * - In 2015-01-02, the temperature was higher than the previous day (25 > 10).
 * - In 2015-01-04, the temperature was higher than the previous day (30 > 20).
 */

-- ============================================
-- SOLUTION 1: LAG Window Function (Best - Modern SQL)
-- ============================================

/*
 * Approach: Use LAG to access previous day's temperature
 * 
 * Time Complexity: O(n log n) - sorting by date
 * Space Complexity: O(n)
 * 
 * Key Insights:
 * - LAG looks at previous row after ordering
 * - DATEDIFF ensures we're comparing consecutive days
 * - Handles gaps in dates correctly
 */

SELECT id
FROM (
    SELECT 
        id,
        recordDate,
        temperature,
        LAG(recordDate, 1) OVER (ORDER BY recordDate) as prev_date,
        LAG(temperature, 1) OVER (ORDER BY recordDate) as prev_temp
    FROM Weather
) w
WHERE 
    DATEDIFF(recordDate, prev_date) = 1
    AND temperature > prev_temp;


-- ============================================
-- SOLUTION 2: Self JOIN (Traditional)
-- ============================================

/*
 * Approach: Join table with itself to compare dates
 * 
 * Time Complexity: O(n²) without index, O(n log n) with index
 * Pros: Works on any SQL version
 * Cons: Slower than window functions
 */

SELECT w1.id
FROM 
    Weather w1
    JOIN Weather w2 ON DATEDIFF(w1.recordDate, w2.recordDate) = 1
WHERE 
    w1.temperature > w2.temperature;


-- ============================================
-- SOLUTION 3: DATE_ADD Method
-- ============================================

/*
 * Approach: Use DATE_SUB to find yesterday's record
 * 
 * Very readable and intuitive
 */

SELECT w1.id
FROM 
    Weather w1
    JOIN Weather w2 ON w1.recordDate = DATE_ADD(w2.recordDate, INTERVAL 1 DAY)
WHERE 
    w1.temperature > w2.temperature;


-- ============================================
-- SOLUTION 4: CTE for Clarity
-- ============================================

/*
 * Approach: Break down logic with Common Table Expression
 */

WITH WeatherWithPrevious AS (
    SELECT 
        id,
        recordDate,
        temperature,
        LAG(recordDate, 1) OVER (ORDER BY recordDate) as prev_date,
        LAG(temperature, 1) OVER (ORDER BY recordDate) as prev_temp
    FROM Weather
)
SELECT id
FROM WeatherWithPrevious
WHERE 
    DATEDIFF(recordDate, prev_date) = 1
    AND temperature > prev_temp;


-- ============================================
-- SOLUTION 5: Subquery Method
-- ============================================

/*
 * Approach: Use subquery to find yesterday's temperature
 */

SELECT w1.id
FROM Weather w1
WHERE w1.temperature > (
    SELECT w2.temperature
    FROM Weather w2
    WHERE w2.recordDate = DATE_SUB(w1.recordDate, INTERVAL 1 DAY)
)
AND EXISTS (
    SELECT 1
    FROM Weather w2
    WHERE w2.recordDate = DATE_SUB(w1.recordDate, INTERVAL 1 DAY)
);


-- ============================================
-- TEST DATA SETUP
-- ============================================

DROP TABLE IF EXISTS Weather;

CREATE TABLE Weather (
    id INT PRIMARY KEY,
    recordDate DATE,
    temperature INT
);

-- Test case 1: Basic example
INSERT INTO Weather VALUES
(1, '2015-01-01', 10),
(2, '2015-01-02', 25),
(3, '2015-01-03', 20),
(4, '2015-01-04', 30);

-- Expected output: 2, 4


-- ============================================
-- VERIFICATION QUERIES
-- ============================================

-- View with previous day comparison
SELECT 
    id,
    recordDate,
    temperature,
    LAG(recordDate, 1) OVER (ORDER BY recordDate) as prev_date,
    LAG(temperature, 1) OVER (ORDER BY recordDate) as prev_temp,
    temperature - LAG(temperature, 1) OVER (ORDER BY recordDate) as temp_diff,
    DATEDIFF(recordDate, LAG(recordDate, 1) OVER (ORDER BY recordDate)) as day_diff,
    CASE 
        WHEN DATEDIFF(recordDate, LAG(recordDate, 1) OVER (ORDER BY recordDate)) = 1
             AND temperature > LAG(temperature, 1) OVER (ORDER BY recordDate)
        THEN '✓ RISING'
        ELSE ''
    END as status
FROM Weather
ORDER BY recordDate;


-- ============================================
-- MANUAL CALCULATION
-- ============================================

/*
 * Walking through the example:
 * 
 * id | date       | temp | prev_date  | prev_temp | diff | consecutive? | rising?
 * ---|------------|------|------------|-----------|------|--------------|--------
 * 1  | 2015-01-01 | 10   | NULL       | NULL      | NULL | N/A          | No
 * 2  | 2015-01-02 | 25   | 2015-01-01 | 10        | +15  | YES          | YES ✓
 * 3  | 2015-01-03 | 20   | 2015-01-02 | 25        | -5   | YES          | No
 * 4  | 2015-01-04 | 30   | 2015-01-03 | 20        | +10  | YES          | YES ✓
 * 
 * Result: IDs 2 and 4
 */


-- ============================================
-- EXTENDED TEST CASES
-- ============================================

-- Test case 2: Gap in dates (important!)
DELETE FROM Weather;
INSERT INTO Weather VALUES
(1, '2015-01-01', 10),
(2, '2015-01-03', 25),  -- Skip Jan 2nd
(3, '2015-01-04', 20);

-- Expected: Only id 3 (Jan 4 > Jan 3)
-- NOT id 2 (Jan 3 is not consecutive to Jan 1)


-- Test case 3: Temperature drops
DELETE FROM Weather;
INSERT INTO Weather VALUES
(1, '2015-01-01', 30),
(2, '2015-01-02', 25),
(3, '2015-01-03', 20),
(4, '2015-01-04', 15);

-- Expected: Empty result (all temperatures dropping)


-- Test case 4: Same temperature
DELETE FROM Weather;
INSERT INTO Weather VALUES
(1, '2015-01-01', 20),
(2, '2015-01-02', 20),
(3, '2015-01-03', 25);

-- Expected: Only id 3 (25 > 20)
-- NOT id 2 (20 = 20, not greater)


-- Test case 5: Single record
DELETE FROM Weather;
INSERT INTO Weather VALUES
(1, '2015-01-01', 20);

-- Expected: Empty result (no previous day to compare)


-- Test case 6: Negative temperatures
DELETE FROM Weather;
INSERT INTO Weather VALUES
(1, '2015-01-01', -10),
(2, '2015-01-02', -5),
(3, '2015-01-03', 0),
(4, '2015-01-04', 5);

-- Expected: 2, 3, 4 (all rising)


-- ============================================
-- COMMON MISTAKES TO AVOID
-- ============================================

-- ❌ MISTAKE 1: Not checking date difference
SELECT w1.id
FROM 
    Weather w1
    JOIN Weather w2 ON w1.id = w2.id + 1  -- Wrong! ID might not be consecutive
WHERE w1.temperature > w2.temperature;
-- Problem: Assumes consecutive IDs mean consecutive dates
-- Fix: Use DATEDIFF or DATE functions


-- ❌ MISTAKE 2: Not handling date gaps
SELECT id
FROM (
    SELECT 
        id,
        temperature,
        LAG(temperature, 1) OVER (ORDER BY recordDate) as prev_temp
    FROM Weather
) w
WHERE temperature > prev_temp;  -- Missing date check!
-- Problem: Compares with previous record even if dates have gaps
-- Fix: Add DATEDIFF(recordDate, prev_date) = 1


-- ❌ MISTAKE 3: Wrong date comparison
SELECT w1.id
FROM Weather w1
JOIN Weather w2 ON w1.recordDate > w2.recordDate  -- Too broad!
WHERE w1.temperature > w2.temperature;
-- Problem: Compares with ALL previous dates, not just yesterday
-- Fix: Use DATEDIFF = 1 or DATE_ADD


-- ❌ MISTAKE 4: Using subtraction for dates (wrong syntax)
SELECT w1.id
FROM Weather w1
JOIN Weather w2 ON w1.recordDate = w2.recordDate + 1  -- Wrong!
WHERE w1.temperature > w2.temperature;
-- Problem: Can't add integer to DATE directly in most SQL dialects
-- Fix: Use DATE_ADD(date, INTERVAL 1 DAY) or DATEDIFF


-- ============================================
-- PERFORMANCE CONSIDERATIONS
-- ============================================

-- Create indexes for faster queries
CREATE INDEX idx_recordDate ON Weather(recordDate);
CREATE INDEX idx_temp ON Weather(temperature);

-- Compound index for join queries
CREATE INDEX idx_date_temp ON Weather(recordDate, temperature);

-- Query execution plan comparison
EXPLAIN SELECT id
FROM (
    SELECT 
        id,
        recordDate,
        temperature,
        LAG(recordDate, 1) OVER (ORDER BY recordDate) as prev_date,
        LAG(temperature, 1) OVER (ORDER BY recordDate) as prev_temp
    FROM Weather
) w
WHERE DATEDIFF(recordDate, prev_date) = 1 AND temperature > prev_temp;


-- ============================================
-- DIFFERENT DATE COMPARISON METHODS
-- ============================================

-- Method 1: DATEDIFF (most reliable)
WHERE DATEDIFF(w1.recordDate, w2.recordDate) = 1

-- Method 2: DATE_ADD
WHERE w1.recordDate = DATE_ADD(w2.recordDate, INTERVAL 1 DAY)

-- Method 3: DATE_SUB (reverse direction)
WHERE w2.recordDate = DATE_SUB(w1.recordDate, INTERVAL 1 DAY)

-- Method 4: ADDDATE (MySQL specific)
WHERE w1.recordDate = ADDDATE(w2.recordDate, 1)

-- All are equivalent, but DATEDIFF is most portable


-- ============================================
-- VISUALIZATION HELPER
-- ============================================

-- Show temperature trends with arrows
SELECT 
    id,
    recordDate,
    temperature,
    LAG(temperature) OVER (ORDER BY recordDate) as prev_temp,
    CASE 
        WHEN temperature > LAG(temperature) OVER (ORDER BY recordDate) THEN '↑ RISING'
        WHEN temperature < LAG(temperature) OVER (ORDER BY recordDate) THEN '↓ FALLING'
        WHEN temperature = LAG(temperature) OVER (ORDER BY recordDate) THEN '→ SAME'
        ELSE 'N/A'
    END as trend,
    temperature - LAG(temperature) OVER (ORDER BY recordDate) as change
FROM Weather
ORDER BY recordDate;


-- ============================================
-- INTERVIEW DISCUSSION POINTS
-- ============================================

/*
 * When discussing this problem:
 * 
 * 1. Clarify requirements:
 *    Q: "Should we only compare consecutive calendar days?"
 *    A: Yes - if data has gaps (missing days), don't compare across gaps
 *    
 *    Q: "What if two records have the same date?"
 *    A: Shouldn't happen per problem constraints (date is implied unique)
 *    
 *    Q: "Do we compare with immediately previous record or previous day?"
 *    A: Previous DAY - must check dates are consecutive
 * 
 * 2. Discuss approaches:
 *    "Two main approaches:
 *    
 *    a) Window function (LAG): Modern, efficient O(n log n)
 *       - Clean code
 *       - Easy to understand
 *       - Requires SQL:2003+
 *    
 *    b) Self-join: Traditional O(n²) or O(n log n) with index
 *       - Works on any SQL version
 *       - More intuitive for some
 *       - Can be slower
 *    
 *    I'll use LAG for better performance."
 * 
 * 3. Key insight - Date checking:
 *    "The tricky part is ensuring we compare CONSECUTIVE days.
 *    Can't just use LAG alone - if Jan 1st and Jan 3rd (missing Jan 2nd),
 *    we shouldn't compare them.
 *    
 *    Solution: DATEDIFF(current_date, prev_date) = 1"
 * 
 * 4. Edge cases:
 *    - First record (no previous) → Exclude from results
 *    - Gaps in dates → Only compare consecutive days
 *    - Same temperature → Not "higher", so exclude
 *    - Negative temps → Works fine with > comparison
 * 
 * 5. Optimization:
 *    "Add index on recordDate for faster ordering and joins.
 *    With millions of records, LAG with proper index is O(n log n).
 *    Self-join benefits from index on recordDate too."
 */


-- ============================================
-- BONUS: Extended Analysis
-- ============================================

-- Find longest streak of rising temperatures
WITH DailyChange AS (
    SELECT 
        id,
        recordDate,
        temperature,
        CASE 
            WHEN temperature > LAG(temperature) OVER (ORDER BY recordDate)
                 AND DATEDIFF(recordDate, LAG(recordDate) OVER (ORDER BY recordDate)) = 1
            THEN 1 
            ELSE 0 
        END as is_rising
    FROM Weather
),
Streaks AS (
    SELECT 
        *,
        SUM(CASE WHEN is_rising = 0 THEN 1 ELSE 0 END) 
            OVER (ORDER BY recordDate) as streak_id
    FROM DailyChange
)
SELECT 
    MIN(recordDate) as streak_start,
    MAX(recordDate) as streak_end,
    COUNT(*) as streak_length
FROM Streaks
WHERE is_rising = 1
GROUP BY streak_id
ORDER BY streak_length DESC
LIMIT 1;


-- Find biggest temperature jump
SELECT 
    w1.id,
    w1.recordDate,
    w1.temperature as current_temp,
    w2.temperature as prev_temp,
    w1.temperature - w2.temperature as temp_jump
FROM 
    Weather w1
    JOIN Weather w2 ON DATEDIFF(w1.recordDate, w2.recordDate) = 1
ORDER BY 
    temp_jump DESC
LIMIT 1;