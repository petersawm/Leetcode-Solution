/*
 * LeetCode Problem: 601 - Human Traffic of Stadium
 * Difficulty: Hard
 * Link: https://leetcode.com/problems/human-traffic-of-stadium/
 * 
 * Problem Statement:
 * Display the records with three or more rows with consecutive id's, and the number 
 * of people is greater than or equal to 100 (inclusive) for each.
 * 
 * Return the result table ordered by visit_date in ascending order.
 * 
 * Table: Stadium
 * +---------------+---------+
 * | Column Name   | Type    |
 * +---------------+---------+
 * | id            | int     |
 * | visit_date    | date    |
 * | people        | int     |
 * +---------------+---------+
 * visit_date is the primary key for this table.
 * Each row contains the visit date and visit id to the stadium with the number of people during the visit.
 * No two rows will have the same visit_date, and as the id increases, the dates increase as well.
 * 
 * Example:
 * Input:
 * Stadium table:
 * +------+------------+-----------+
 * | id   | visit_date | people    |
 * +------+------------+-----------+
 * | 1    | 2017-01-01 | 10        |
 * | 2    | 2017-01-02 | 109       |
 * | 3    | 2017-01-03 | 150       |
 * | 4    | 2017-01-04 | 99        |
 * | 5    | 2017-01-05 | 145       |
 * | 6    | 2017-01-06 | 1455      |
 * | 7    | 2017-01-07 | 199       |
 * | 8    | 2017-01-09 | 188       |
 * +------+------------+-----------+
 * 
 * Output:
 * +------+------------+-----------+
 * | id   | visit_date | people    |
 * +------+------------+-----------+
 * | 5    | 2017-01-05 | 145       |
 * | 6    | 2017-01-06 | 1455      |
 * | 7    | 2017-01-07 | 199       |
 * | 8    | 2017-01-09 | 188       |
 * +------+------------+-----------+
 * 
 * Explanation:
 * The four rows with ids 5, 6, 7, and 8 have consecutive ids and each of them has >= 100 people attended.
 * Note that row 8 was included even though the visit_date was not the next day after row 7.
 * The rows with ids 2 and 3 are not included because we need at least three consecutive ids.
 */

-- ============================================
-- SOLUTION 1: Islands and Gaps (Best)
-- ============================================

/*
 * Approach: Group consecutive high-traffic days into "islands"
 * 
 * Time Complexity: O(n log n) - sorting and grouping
 * Space Complexity: O(n)
 * 
 * Key Insights:
 * - Filter people >= 100 first
 * - Use (id - ROW_NUMBER()) to create group identifiers for consecutive IDs
 * - Count records in each group
 * - Return groups with count >= 3
 */

WITH HighTraffic AS (
    SELECT 
        id,
        visit_date,
        people,
        id - ROW_NUMBER() OVER (ORDER BY id) AS grp
    FROM Stadium
    WHERE people >= 100
)
SELECT 
    id,
    visit_date,
    people
FROM HighTraffic
WHERE grp IN (
    SELECT grp
    FROM HighTraffic
    GROUP BY grp
    HAVING COUNT(*) >= 3
)
ORDER BY visit_date;


-- ============================================
-- SOLUTION 2: LAG/LEAD Window Functions
-- ============================================

/*
 * Approach: Check if current and 2 neighbors all meet criteria
 * 
 * Checks three patterns:
 * 1. Current, Next, Next+1 all >= 100
 * 2. Previous, Current, Next all >= 100
 * 3. Previous-1, Previous, Current all >= 100
 */

SELECT DISTINCT
    s1.id,
    s1.visit_date,
    s1.people
FROM (
    SELECT 
        id,
        visit_date,
        people,
        LAG(people, 1) OVER (ORDER BY id) AS prev1_people,
        LAG(people, 2) OVER (ORDER BY id) AS prev2_people,
        LEAD(people, 1) OVER (ORDER BY id) AS next1_people,
        LEAD(people, 2) OVER (ORDER BY id) AS next2_people,
        LAG(id, 1) OVER (ORDER BY id) AS prev1_id,
        LAG(id, 2) OVER (ORDER BY id) AS prev2_id,
        LEAD(id, 1) OVER (ORDER BY id) AS next1_id,
        LEAD(id, 2) OVER (ORDER BY id) AS next2_id
    FROM Stadium
) s1
WHERE 
    -- Pattern 1: Current is start of 3 consecutive
    (people >= 100 AND next1_people >= 100 AND next2_people >= 100
     AND id + 1 = next1_id AND id + 2 = next2_id)
    OR
    -- Pattern 2: Current is middle of 3 consecutive
    (people >= 100 AND prev1_people >= 100 AND next1_people >= 100
     AND id - 1 = prev1_id AND id + 1 = next1_id)
    OR
    -- Pattern 3: Current is end of 3 consecutive
    (people >= 100 AND prev1_people >= 100 AND prev2_people >= 100
     AND id - 1 = prev1_id AND id - 2 = prev2_id)
ORDER BY visit_date;


-- ============================================
-- SOLUTION 3: Self JOIN (Traditional)
-- ============================================

/*
 * Approach: Join table with itself multiple times
 * Check all possible 3-consecutive patterns
 */

SELECT DISTINCT s1.*
FROM Stadium s1, Stadium s2, Stadium s3
WHERE 
    s1.people >= 100 AND s2.people >= 100 AND s3.people >= 100
    AND (
        -- Pattern 1: s1, s2, s3 consecutive
        (s1.id + 1 = s2.id AND s2.id + 1 = s3.id)
        OR
        -- Pattern 2: s2, s1, s3 consecutive
        (s2.id + 1 = s1.id AND s1.id + 1 = s3.id)
        OR
        -- Pattern 3: s3, s2, s1 consecutive
        (s3.id + 1 = s2.id AND s2.id + 1 = s1.id)
    )
ORDER BY s1.visit_date;


-- ============================================
-- SOLUTION 4: Using Variables (MySQL)
-- ============================================

/*
 * Approach: Track consecutive count dynamically
 */

SELECT id, visit_date, people
FROM (
    SELECT 
        id,
        visit_date,
        people,
        @cnt := IF(@prev = id - 1 AND people >= 100, @cnt + 1, IF(people >= 100, 1, 0)) AS cnt,
        @prev := id,
        @grp := IF(people >= 100, IF(@prev_cnt = id - 1, @grp, @grp + 1), @grp) AS grp,
        @prev_cnt := id
    FROM Stadium, (SELECT @cnt := 0, @prev := 0, @grp := 0, @prev_cnt := 0) vars
    ORDER BY id
) t
WHERE cnt >= 3 OR id IN (
    SELECT id FROM (
        SELECT 
            id,
            @c := IF(@p = id - 1 AND people >= 100, @c + 1, IF(people >= 100, 1, 0)) AS c,
            @p := id
        FROM Stadium, (SELECT @c := 0, @p := 0) v
        ORDER BY id
    ) t2
    WHERE c >= 3
)
ORDER BY visit_date;



-- TEST DATA SETUP


DROP TABLE IF EXISTS Stadium;

CREATE TABLE Stadium (
    id INT PRIMARY KEY,
    visit_date DATE,
    people INT
);

INSERT INTO Stadium VALUES
(1, '2017-01-01', 10),
(2, '2017-01-02', 109),
(3, '2017-01-03', 150),
(4, '2017-01-04', 99),
(5, '2017-01-05', 145),
(6, '2017-01-06', 1455),
(7, '2017-01-07', 199),
(8, '2017-01-09', 188);

-- Expected output: ids 5, 6, 7, 8



-- VERIFICATION QUERIES


-- Visualize the grouping logic
SELECT 
    id,
    visit_date,
    people,
    CASE WHEN people >= 100 THEN '✓' ELSE '✗' END as meets_threshold,
    id - ROW_NUMBER() OVER (ORDER BY id) AS all_grp,
    CASE 
        WHEN people >= 100 
        THEN id - ROW_NUMBER() OVER (ORDER BY CASE WHEN people >= 100 THEN id END) 
        ELSE NULL 
    END as high_traffic_grp
FROM Stadium
ORDER BY id;

-- Show consecutive sequences
WITH HighTraffic AS (
    SELECT 
        id,
        visit_date,
        people,
        id - ROW_NUMBER() OVER (ORDER BY id) AS grp
    FROM Stadium
    WHERE people >= 100
),
GroupCounts AS (
    SELECT 
        grp,
        COUNT(*) as cnt,
        MIN(id) as start_id,
        MAX(id) as end_id,
        GROUP_CONCAT(id ORDER BY id) as ids
    FROM HighTraffic
    GROUP BY grp
)
SELECT 
    grp,
    cnt as consecutive_days,
    ids,
    CASE WHEN cnt >= 3 THEN '✓ INCLUDE' ELSE '✗ EXCLUDE' END as status
FROM GroupCounts
ORDER BY grp;



-- MANUAL CALCULATION


/*
 * Step-by-step analysis:
 * 
 * id | people | >= 100? | ROW_NUMBER | id - ROW_NUMBER | Group
 * ---|--------|---------|------------|-----------------|-------
 * 1  | 10     | No      | -          | -               | -
 * 2  | 109    | Yes     | 1          | 2-1=1           | A
 * 3  | 150    | Yes     | 2          | 3-2=1           | A (same group!)
 * 4  | 99     | No      | -          | -               | -
 * 5  | 145    | Yes     | 3          | 5-3=2           | B
 * 6  | 1455   | Yes     | 4          | 6-4=2           | B (same group!)
 * 7  | 199    | Yes     | 5          | 7-5=2           | B (same group!)
 * 8  | 188    | Yes     | 6          | 8-6=2           | B (same group!)
 * 
 * Groups:
 * - Group A: ids 2,3 (count=2) → EXCLUDE (< 3)
 * - Group B: ids 5,6,7,8 (count=4) → INCLUDE (>= 3)
 * 
 * Result: 5,6,7,8
 */



-- EXTENDED TEST CASES


-- Test case 2: Multiple qualifying groups
DELETE FROM Stadium;
INSERT INTO Stadium VALUES
(1, '2017-01-01', 100),
(2, '2017-01-02', 200),
(3, '2017-01-03', 300),
(4, '2017-01-04', 50),
(5, '2017-01-05', 150),
(6, '2017-01-06', 160),
(7, '2017-01-07', 170),
(8, '2017-01-08', 180);
-- Expected: 1,2,3 and 5,6,7,8


-- Test case 3: Exactly 3 consecutive
DELETE FROM Stadium;
INSERT INTO Stadium VALUES
(1, '2017-01-01', 50),
(2, '2017-01-02', 100),
(3, '2017-01-03', 110),
(4, '2017-01-04', 120),
(5, '2017-01-05', 50);
-- Expected: 2,3,4


-- Test case 4: Gap in IDs but still consecutive in sequence
DELETE FROM Stadium;
INSERT INTO Stadium VALUES
(1, '2017-01-01', 100),
(2, '2017-01-02', 110),
(5, '2017-01-03', 120),
(6, '2017-01-04', 130),
(7, '2017-01-05', 140);
-- Expected: Different groups due to ID gap


-- Test case 5: All days qualify
DELETE FROM Stadium;
INSERT INTO Stadium VALUES
(1, '2017-01-01', 100),
(2, '2017-01-02', 110),
(3, '2017-01-03', 120),
(4, '2017-01-04', 130),
(5, '2017-01-05', 140);
-- Expected: All records (1,2,3,4,5)


-- ============================================
-- COMMON MISTAKES TO AVOID
-- ============================================

-- ❌ MISTAKE 1: Not checking consecutive IDs
WITH HighTraffic AS (
    SELECT * FROM Stadium WHERE people >= 100
)
SELECT * FROM HighTraffic  -- Wrong! Doesn't check if IDs are consecutive
LIMIT 3;


-- ❌ MISTAKE 2: Using LEAD/LAG without checking ID gaps
SELECT *
FROM (
    SELECT 
        *,
        LAG(people, 1) OVER (ORDER BY id) as prev1,
        LAG(people, 2) OVER (ORDER BY id) as prev2
    FROM Stadium
) t
WHERE people >= 100 AND prev1 >= 100 AND prev2 >= 100;
-- Problem: Doesn't verify IDs are actually consecutive


-- ❌ MISTAKE 3: Forgetting DISTINCT in self-join
SELECT s1.* FROM Stadium s1, Stadium s2, Stadium s3
WHERE s1.people >= 100 AND s2.people >= 100 AND s3.people >= 100
AND (s1.id + 1 = s2.id AND s2.id + 1 = s3.id);
-- Problem: Returns duplicates for records that match multiple patterns


-- ❌ MISTAKE 4: Not including all records in qualifying sequence
SELECT * FROM Stadium
WHERE people >= 100
AND id IN (
    SELECT id FROM Stadium WHERE people >= 100
    GROUP BY id HAVING COUNT(*) >= 3
);
-- Problem: GROUP BY id makes no sense (each id is unique)



-- INTERVIEW DISCUSSION POINTS


/*
 * When discussing this problem:
 * 
 * 1. Clarify requirements:
 *    Q: "Should consecutive mean consecutive IDs or consecutive dates?"
 *    A: Consecutive IDs (as stated in problem)
 *    
 *    Q: "If we have 5 consecutive high-traffic days, do we include all 5?"
 *    A: Yes, all records in sequences of 3+ consecutive IDs
 *    
 *    Q: "What if there are gaps in IDs (1,2,5,6,7)?"
 *    A: 1,2 is one group (too small), 5,6,7 is another group (valid if >= 3)
 * 
 * 2. Discuss the "Islands and Gaps" technique:
 *    "This is a classic 'islands' problem. The trick is:
 *    
 *    id - ROW_NUMBER() creates a group identifier
 *    
 *    Example:
 *    id=2 → ROW_NUMBER=1 → group = 2-1 = 1
 *    id=3 → ROW_NUMBER=2 → group = 3-2 = 1 (same!)
 *    id=5 → ROW_NUMBER=3 → group = 5-3 = 2 (new!)
 *    
 *    Consecutive IDs produce the same group number."
 * 
 * 3. Compare approaches:
 *    "Three main approaches:
 *    
 *    a) Islands/Gaps (Best): O(n log n)
 *       - Elegant and efficient
 *       - Easy to extend (e.g., >= 5 consecutive)
 *       - Recommended solution
 *    
 *    b) LAG/LEAD: O(n)
 *       - More explicit logic
 *       - Harder to extend beyond 3
 *       - Good for fixed N
 *    
 *    c) Self-join: O(n³) without index
 *       - Traditional approach
 *       - Very slow for large datasets
 *       - Avoid unless necessary"
 * 
 * 4. Edge cases:
 *    - Empty table → No results
 *    - All days < 100 people → No results
 *    - Exactly 3 consecutive → Include all 3
 *    - Multiple separate groups → Include all qualifying groups
 *    - Gaps in IDs → Treat as separate sequences
 * 
 * 5. Optimization:
 *    "Add index on id for faster sorting and grouping.
 *    The islands approach is already optimal at O(n log n).
 *    For very large datasets, could partition by year/month."
 */



-- BONUS: Generalized N Consecutive


-- Find sequences of N or more consecutive high-traffic days
-- Replace @min_consecutive with desired threshold

SET @min_consecutive = 4;

WITH HighTraffic AS (
    SELECT 
        id,
        visit_date,
        people,
        id - ROW_NUMBER() OVER (ORDER BY id) AS grp
    FROM Stadium
    WHERE people >= 100
)
SELECT 
    id,
    visit_date,
    people
FROM HighTraffic
WHERE grp IN (
    SELECT grp
    FROM HighTraffic
    GROUP BY grp
    HAVING COUNT(*) >= @min_consecutive
)
ORDER BY visit_date;


-- Find longest consecutive high-traffic sequence
WITH HighTraffic AS (
    SELECT 
        id,
        visit_date,
        people,
        id - ROW_NUMBER() OVER (ORDER BY id) AS grp
    FROM Stadium
    WHERE people >= 100
),
GroupStats AS (
    SELECT 
        grp,
        COUNT(*) as sequence_length,
        MIN(visit_date) as start_date,
        MAX(visit_date) as end_date,
        AVG(people) as avg_people
    FROM HighTraffic
    GROUP BY grp
)
SELECT *
FROM GroupStats
ORDER BY sequence_length DESC, avg_people DESC
LIMIT 1;