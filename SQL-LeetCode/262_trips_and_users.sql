/*
 * LeetCode Problem: 262 - Trips and Users
 * Difficulty: Hard
 * Link: https://leetcode.com/problems/trips-and-users/
 * 
 * Problem Statement:
 * The cancellation rate is computed by dividing the number of canceled (by client or driver) 
 * requests with unbanned users by the total number of requests with unbanned users on that day.
 * 
 * Write a SQL query to find the cancellation rate for each day between "2013-10-01" and "2013-10-03". 
 * Round the cancellation rate to two decimal points.
 * 
 * Return the result table in any order.
 * 
 * Tables:
 * 
 * Trips table:
 * +-------------+----------+
 * | Column Name | Type     |
 * +-------------+----------+
 * | id          | int      |
 * | client_id   | int      |
 * | driver_id   | int      |
 * | city_id     | int      |
 * | status      | enum     | ('completed', 'cancelled_by_driver', 'cancelled_by_client')
 * | request_at  | date     |
 * +-------------+----------+
 * 
 * Users table:
 * +-------------+----------+
 * | Column Name | Type     |
 * +-------------+----------+
 * | users_id    | int      |
 * | banned      | enum     | ('Yes', 'No')
 * | role        | enum     | ('client', 'driver', 'partner')
 * +-------------+----------+
 * 
 * Example:
 * Input: 
 * Trips:
 * +----+-----------+-----------+---------+---------------------+------------+
 * | id | client_id | driver_id | city_id | status              | request_at |
 * +----+-----------+-----------+---------+---------------------+------------+
 * | 1  | 1         | 10        | 1       | completed           | 2013-10-01 |
 * | 2  | 2         | 11        | 1       | cancelled_by_driver | 2013-10-01 |
 * | 3  | 3         | 12        | 6       | completed           | 2013-10-01 |
 * | 4  | 4         | 13        | 6       | cancelled_by_client | 2013-10-01 |
 * | 5  | 1         | 10        | 1       | completed           | 2013-10-02 |
 * | 6  | 2         | 11        | 6       | completed           | 2013-10-02 |
 * | 7  | 3         | 12        | 6       | completed           | 2013-10-02 |
 * | 8  | 2         | 12        | 12      | completed           | 2013-10-03 |
 * | 9  | 3         | 10        | 12      | completed           | 2013-10-03 |
 * | 10 | 4         | 13        | 12      | cancelled_by_driver | 2013-10-03 |
 * +----+-----------+-----------+---------+---------------------+------------+
 * 
 * Users:
 * +----------+--------+--------+
 * | users_id | banned | role   |
 * +----------+--------+--------+
 * | 1        | No     | client |
 * | 2        | Yes    | client |
 * | 3        | No     | client |
 * | 4        | No     | client |
 * | 10       | No     | driver |
 * | 11       | No     | driver |
 * | 12       | No     | driver |
 * | 13       | No     | driver |
 * +----------+--------+--------+
 * 
 * Output:
 * +------------+-------------------+
 * | Day        | Cancellation Rate |
 * +------------+-------------------+
 * | 2013-10-01 | 0.33              |
 * | 2013-10-02 | 0.00              |
 * | 2013-10-03 | 0.50              |
 * +------------+-------------------+
 * 
 * Explanation:
 * October 1, 2013:
 *   - There were 4 requests in total, 2 of which were canceled.
 *   - However, the request with Id=2 was made by a banned client (User_Id=2), so it is ignored.
 *   - Hence there are 3 unbanned requests in total, 1 of which was canceled.
 *   - The Cancellation Rate is (1 / 3) = 0.33
 * 
 * October 2, 2013:
 *   - There were 3 requests in total, 0 of which were canceled.
 *   - The request with Id=6 was made by a banned client, so it is ignored.
 *   - Hence there are 2 unbanned requests in total, 0 of which were canceled.
 *   - The Cancellation Rate is (0 / 2) = 0.00
 * 
 * October 3, 2013:
 *   - There were 3 requests in total, 1 of which was canceled.
 *   - The request with Id=8 was made by a banned client, so it is ignored.
 *   - Hence there are 2 unbanned requests in total, 1 of which was canceled.
 *   - The Cancellation Rate is (1 / 2) = 0.50
 */

-- SOLUTION 1: Using JOIN and CASE (Recommended)

/*
 * Approach: JOIN to filter unbanned users, then calculate rate
 * 
 * Time Complexity: O(n * log n) - joins with indexes
 * Space Complexity: O(n) - for grouped results
 * 
 * Key Insights:
 * - Must filter out banned users (both clients AND drivers)
 * - Need to count cancelled trips vs total trips per day
 * - Use CASE to count cancelled trips
 * - Use ROUND for 2 decimal places
 */

SELECT 
    t.request_at AS Day,
    ROUND(
        SUM(CASE 
            WHEN t.status LIKE 'cancelled%' THEN 1 
            ELSE 0 
        END) / COUNT(*),
        2
    ) AS 'Cancellation Rate'
FROM 
    Trips t
    INNER JOIN Users c ON t.client_id = c.users_id AND c.banned = 'No'
    INNER JOIN Users d ON t.driver_id = d.users_id AND d.banned = 'No'
WHERE 
    t.request_at BETWEEN '2013-10-01' AND '2013-10-03'
GROUP BY 
    t.request_at
ORDER BY 
    t.request_at;


-- SOLUTION 2: Using Subquery (Alternative)

/*
 * Approach: Filter in WHERE clause using subqueries
 * More readable for some, slightly less efficient
 */

SELECT 
    request_at AS Day,
    ROUND(
        SUM(IF(status != 'completed', 1, 0)) / COUNT(*),
        2
    ) AS 'Cancellation Rate'
FROM 
    Trips
WHERE 
    client_id NOT IN (SELECT users_id FROM Users WHERE banned = 'Yes')
    AND driver_id NOT IN (SELECT users_id FROM Users WHERE banned = 'Yes')
    AND request_at BETWEEN '2013-10-01' AND '2013-10-03'
GROUP BY 
    request_at
ORDER BY 
    request_at;


-- SOLUTION 3: Using CTE (Most Readable)

/*
 * Approach: Common Table Expression for clarity
 * Best for production code - highly maintainable
 */

WITH UnbannedTrips AS (
    SELECT 
        t.id,
        t.status,
        t.request_at
    FROM 
        Trips t
        INNER JOIN Users c ON t.client_id = c.users_id
        INNER JOIN Users d ON t.driver_id = d.users_id
    WHERE 
        c.banned = 'No'
        AND d.banned = 'No'
        AND t.request_at BETWEEN '2013-10-01' AND '2013-10-03'
)
SELECT 
    request_at AS Day,
    ROUND(
        SUM(CASE WHEN status != 'completed' THEN 1 ELSE 0 END) * 1.0 / COUNT(*),
        2
    ) AS 'Cancellation Rate'
FROM 
    UnbannedTrips
GROUP BY 
    request_at
ORDER BY 
    request_at;


-- SOLUTION 4: Detailed with Comments (Learning)

SELECT 
    t.request_at AS Day,
    
    -- Calculate cancellation rate: cancelled / total
    ROUND(
        -- Count cancelled trips (status starts with 'cancelled')
        SUM(
            CASE 
                WHEN t.status LIKE 'cancelled%' THEN 1  -- Cancelled trip
                ELSE 0                                   -- Completed trip
            END
        ) 
        / 
        -- Divide by total trips for that day
        COUNT(*),  -- COUNT(*) includes all rows for this day
        
        -- Round to 2 decimal places
        2
    ) AS 'Cancellation Rate'
    
FROM 
    Trips t
    
    -- JOIN with Users table to check if CLIENT is banned
    INNER JOIN Users c 
        ON t.client_id = c.users_id 
        AND c.banned = 'No'  -- Only unbanned clients
    
    -- JOIN with Users table again to check if DRIVER is banned
    INNER JOIN Users d 
        ON t.driver_id = d.users_id 
        AND d.banned = 'No'  -- Only unbanned drivers
    
WHERE 
    -- Filter date range
    t.request_at BETWEEN '2013-10-01' AND '2013-10-03'
    
GROUP BY 
    -- Group by day to calculate rate per day
    t.request_at
    
ORDER BY 
    -- Sort by date
    t.request_at;


-- TEST DATA SETUP

-- Create tables
CREATE TABLE IF NOT EXISTS Trips (
    id INT PRIMARY KEY,
    client_id INT,
    driver_id INT,
    city_id INT,
    status ENUM('completed', 'cancelled_by_driver', 'cancelled_by_client'),
    request_at DATE
);

CREATE TABLE IF NOT EXISTS Users (
    users_id INT PRIMARY KEY,
    banned ENUM('Yes', 'No'),
    role ENUM('client', 'driver', 'partner')
);

-- Insert test data
INSERT INTO Trips VALUES
(1, 1, 10, 1, 'completed', '2013-10-01'),
(2, 2, 11, 1, 'cancelled_by_driver', '2013-10-01'),
(3, 3, 12, 6, 'completed', '2013-10-01'),
(4, 4, 13, 6, 'cancelled_by_client', '2013-10-01'),
(5, 1, 10, 1, 'completed', '2013-10-02'),
(6, 2, 11, 6, 'completed', '2013-10-02'),
(7, 3, 12, 6, 'completed', '2013-10-02'),
(8, 2, 12, 12, 'completed', '2013-10-03'),
(9, 3, 10, 12, 'completed', '2013-10-03'),
(10, 4, 13, 12, 'cancelled_by_driver', '2013-10-03');

INSERT INTO Users VALUES
(1, 'No', 'client'),
(2, 'Yes', 'client'),
(3, 'No', 'client'),
(4, 'No', 'client'),
(10, 'No', 'driver'),
(11, 'No', 'driver'),
(12, 'No', 'driver'),
(13, 'No', 'driver');


-- VERIFICATION QUERIES

-- Check what trips are included per day
SELECT 
    t.request_at,
    t.id,
    t.client_id,
    c.banned AS client_banned,
    t.driver_id,
    d.banned AS driver_banned,
    t.status,
    CASE 
        WHEN c.banned = 'Yes' OR d.banned = 'Yes' THEN 'EXCLUDED'
        ELSE 'INCLUDED'
    END AS trip_status
FROM 
    Trips t
    LEFT JOIN Users c ON t.client_id = c.users_id
    LEFT JOIN Users d ON t.driver_id = d.users_id
WHERE 
    t.request_at BETWEEN '2013-10-01' AND '2013-10-03'
ORDER BY 
    t.request_at, t.id;


-- Manual calculation for 2013-10-01:
-- Trip 1: client=1(No), driver=10(No), status=completed ✓ INCLUDED
-- Trip 2: client=2(Yes), driver=11(No), status=cancelled ✗ EXCLUDED (banned client)
-- Trip 3: client=3(No), driver=12(No), status=completed ✓ INCLUDED
-- Trip 4: client=4(No), driver=13(No), status=cancelled ✓ INCLUDED
-- Result: 1 cancelled / 3 total = 0.33


-- COMMON MISTAKES TO AVOID


-- ❌ MISTAKE 1: Forgetting to check BOTH client AND driver
-- This only checks client:
-- SELECT ... FROM Trips t
-- INNER JOIN Users u ON t.client_id = u.users_id AND u.banned = 'No'
-- Missing driver check!

-- ❌ MISTAKE 2: Wrong division (integer division)
-- SUM(...) / COUNT(*) might give 0 in some SQL dialects
-- Fix: Multiply by 1.0 or use CAST to DECIMAL

-- ❌ MISTAKE 3: Not using LIKE for status matching
-- status = 'cancelled' won't match 'cancelled_by_driver'
-- Use: status LIKE 'cancelled%' or status != 'completed'

-- ❌ MISTAKE 4: Including banned users in ANY role
-- Must filter BOTH client_id AND driver_id against banned users
