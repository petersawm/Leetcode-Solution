-- LeetCode Problem 262: Trips and Users

-- Difficulty: Hard
-- Link: https://leetcode.com/problems/trips-and-users/

-- PROBLEM DESCRIPTION:
-- Write a SQL query to find the cancellation rate of requests with 
-- unbanned users (both client and driver must not be banned) for 
-- each day between "2013-10-01" and "2013-10-03". Round the result 
-- to two decimal places.
--
-- TABLES:
-- Trips
-- +-------------+----------+
-- | Column Name | Type     |
-- +-------------+----------+
-- | id          | int      |
-- | client_id   | int      |
-- | driver_id   | int      |
-- | city_id     | int      |
-- | status      | enum     |
-- | request_at  | date     |
-- +-------------+----------+
-- id is the primary key
-- status is ENUM ('completed', 'cancelled_by_driver', 'cancelled_by_client')
--
-- Users
-- +-------------+----------+
-- | Column Name | Type     |
-- +-------------+----------+
-- | users_id    | int      |
-- | banned      | enum     |
-- | role        | enum     |
-- +-------------+----------+
-- users_id is the primary key
-- banned is ENUM ('Yes', 'No')
-- role is ENUM ('client', 'driver', 'partner')
--
-- EXAMPLE:
-- Input: 
-- Trips table:
-- +----+-----------+-----------+---------+---------------------+------------+
-- | id | client_id | driver_id | city_id | status              | request_at |
-- +----+-----------+-----------+---------+---------------------+------------+
-- | 1  | 1         | 10        | 1       | completed           | 2013-10-01 |
-- | 2  | 2         | 11        | 1       | cancelled_by_driver | 2013-10-01 |
-- | 3  | 3         | 12        | 6       | completed           | 2013-10-01 |
-- | 4  | 4         | 13        | 6       | cancelled_by_client | 2013-10-01 |
-- | 5  | 1         | 10        | 1       | completed           | 2013-10-02 |
-- | 6  | 2         | 11        | 6       | completed           | 2013-10-02 |
-- | 7  | 3         | 12        | 6       | completed           | 2013-10-02 |
-- | 8  | 2         | 12        | 12      | completed           | 2013-10-03 |
-- | 9  | 3         | 10        | 12      | completed           | 2013-10-03 |
-- | 10 | 4         | 13        | 12      | cancelled_by_driver | 2013-10-03 |
-- +----+-----------+-----------+---------+---------------------+------------+
-- Users table:
-- +----------+--------+--------+
-- | users_id | banned | role   |
-- +----------+--------+--------+
-- | 1        | No     | client |
-- | 2        | Yes    | client |
-- | 3        | No     | client |
-- | 4        | No     | client |
-- | 10       | No     | driver |
-- | 11       | No     | driver |
-- | 12       | No     | driver |
-- | 13       | No     | driver |
-- +----------+--------+--------+
-- Output: 
-- +------------+-------------------+
-- | Day        | Cancellation Rate |
-- +------------+-------------------+
-- | 2013-10-01 | 0.33              |
-- | 2013-10-02 | 0.00              |
-- | 2013-10-03 | 0.50              |
-- +------------+-------------------+


-- SOLUTION:
SELECT 
    request_at AS Day,
    ROUND(
        SUM(CASE WHEN status LIKE 'cancelled%' THEN 1 ELSE 0 END) / COUNT(*),
        2
    ) AS 'Cancellation Rate'
FROM Trips t
WHERE client_id NOT IN (
        SELECT users_id 
        FROM Users 
        WHERE banned = 'Yes'
    )
  AND driver_id NOT IN (
        SELECT users_id 
        FROM Users 
        WHERE banned = 'Yes'
    )
  AND request_at BETWEEN '2013-10-01' AND '2013-10-03'
GROUP BY request_at
ORDER BY request_at;

-- EXPLANATION:
-- 1. Filter trips where BOTH client and driver are NOT banned
-- 2. Filter by date range (2013-10-01 to 2013-10-03)
-- 3. Group by request date
-- 4. Calculate cancellation rate:
--    - Numerator: Count trips with status starting with 'cancelled'
--    - Denominator: Total trips for that day
-- 5. ROUND to 2 decimal places
--
-- CASE WHEN logic:
-- - status LIKE 'cancelled%' matches both:
--   * 'cancelled_by_driver'
--   * 'cancelled_by_client'
-- - Returns 1 for cancelled, 0 for completed
-- - SUM gives total cancelled trips

-- KEY CONCEPTS:
-- - NOT IN with subquery: Filtering banned users
-- - LIKE operator: Pattern matching
-- - CASE WHEN: Conditional aggregation
-- - GROUP BY with date: Daily aggregation
-- - ROUND: Formatting decimal results
-- - Multiple WHERE conditions: Complex filtering

-- ALTERNATIVE SOLUTION (Using JOINs):
-- SELECT 
--     t.request_at AS Day,
--     ROUND(
--         SUM(IF(t.status != 'completed', 1, 0)) / COUNT(*),
--         2
--     ) AS 'Cancellation Rate'
-- FROM Trips t
-- JOIN Users c ON t.client_id = c.users_id AND c.banned = 'No'
-- JOIN Users d ON t.driver_id = d.users_id AND d.banned = 'No'
-- WHERE t.request_at BETWEEN '2013-10-01' AND '2013-10-03'
-- GROUP BY t.request_at
-- ORDER BY t.request_at;

-- TIME COMPLEXITY: O(n) for filtering and grouping
-- SPACE COMPLEXITY: O(k) where k is number of distinct dates

-- IMPORTANT NOTES:
-- - Must filter BOTH client and driver for banned status
-- - Use LIKE 'cancelled%' to catch all cancellation types
-- - Round to 2 decimal places as required
-- - Handle division by zero (if no trips on a day)