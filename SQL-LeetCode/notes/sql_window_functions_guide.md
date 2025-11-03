# SQL Window Functions - Complete Guide for LeetCode

## Overview

Window functions perform calculations across a set of table rows that are related to the current row. Unlike GROUP BY, they don't collapse rows.

**Key Difference:**
```sql
-- GROUP BY: Collapses rows
SELECT department, AVG(salary) FROM employees GROUP BY department;
-- Result: One row per department

-- Window Function: Keeps all rows
SELECT name, salary, AVG(salary) OVER (PARTITION BY department) FROM employees;
-- Result: Original rows + average for each row's department
```

---

## Window Function Syntax

```sql
function_name() OVER (
    [PARTITION BY partition_expression]
    [ORDER BY sort_expression [ASC|DESC]]
    [ROWS or RANGE frame_clause]
)
```

**Components:**
- **Function**: What to calculate (SUM, AVG, RANK, etc.)
- **PARTITION BY**: Divides rows into groups (optional)
- **ORDER BY**: Defines order within partition (optional)
- **Frame**: Defines which rows to include in calculation (optional)

---

## Common Window Functions

### 1. Ranking Functions

#### RANK()
Assigns rank with gaps after ties
```sql
-- Salaries: 100, 90, 90, 80
SELECT salary, RANK() OVER (ORDER BY salary DESC) as rank
FROM employees;
-- Result: 1, 2, 2, 4  (skips 3)
```

#### DENSE_RANK()
Assigns rank without gaps
```sql
-- Salaries: 100, 90, 90, 80
SELECT salary, DENSE_RANK() OVER (ORDER BY salary DESC) as rank
FROM employees;
-- Result: 1, 2, 2, 3  (no skip)
```

#### ROW_NUMBER()
Assigns unique sequential number
```sql
-- Salaries: 100, 90, 90, 80
SELECT salary, ROW_NUMBER() OVER (ORDER BY salary DESC) as row_num
FROM employees;
-- Result: 1, 2, 3, 4  (unique even for ties)
```

**When to use which?**
- **RANK**: When you want to show ties but skip numbers (Olympics style)
- **DENSE_RANK**: When you want consecutive ranks (top N unique values)
- **ROW_NUMBER**: When you need unique numbers (pagination, deduplication)

---

### 2. Aggregate Functions

#### SUM() OVER
```sql
-- Running total
SELECT 
    date,
    amount,
    SUM(amount) OVER (ORDER BY date) as running_total
FROM transactions;
```

#### AVG() OVER
```sql
-- Compare salary to department average
SELECT 
    name,
    salary,
    AVG(salary) OVER (PARTITION BY department) as dept_avg,
    salary - AVG(salary) OVER (PARTITION BY department) as diff
FROM employees;
```

#### COUNT() OVER
```sql
-- Count employees per department (shown on each row)
SELECT 
    name,
    department,
    COUNT(*) OVER (PARTITION BY department) as dept_count
FROM employees;
```

---

### 3. Value Functions

#### LAG()
Access previous row's value
```sql
-- Compare with previous day
SELECT 
    date,
    price,
    LAG(price, 1) OVER (ORDER BY date) as prev_price,
    price - LAG(price, 1) OVER (ORDER BY date) as change
FROM stock_prices;
```

**Parameters:**
- `LAG(column, offset, default)`: Look back N rows
- offset: How many rows back (default: 1)
- default: Value if no row exists (default: NULL)

#### LEAD()
Access next row's value
```sql
-- Compare with next day
SELECT 
    date,
    price,
    LEAD(price, 1) OVER (ORDER BY date) as next_price
FROM stock_prices;
```

#### FIRST_VALUE() / LAST_VALUE()
```sql
-- Compare to first/last in partition
SELECT 
    name,
    salary,
    FIRST_VALUE(salary) OVER (
        PARTITION BY department 
        ORDER BY salary DESC
    ) as highest_in_dept
FROM employees;
```

---

## PARTITION BY Deep Dive

**Purpose:** Divide data into groups for separate calculations

### Example: Salary Comparison Within Departments

```sql
SELECT 
    name,
    department,
    salary,
    
    -- Rank within department
    RANK() OVER (
        PARTITION BY department 
        ORDER BY salary DESC
    ) as dept_rank,
    
    -- Department average
    AVG(salary) OVER (
        PARTITION BY department
    ) as dept_avg,
    
    -- Overall rank (no partition)
    RANK() OVER (ORDER BY salary DESC) as overall_rank
FROM 
    employees;
```

**Result:**
```
name    | dept  | salary | dept_rank | dept_avg | overall_rank
--------|-------|--------|-----------|----------|-------------
Alice   | IT    | 100000 | 1         | 85000    | 1
Bob     | IT    | 90000  | 2         | 85000    | 2
Carol   | Sales | 85000  | 1         | 72500    | 3
Dave    | IT    | 65000  | 3         | 85000    | 5
Eve     | Sales | 60000  | 2         | 72500    | 6
```

---

## Frame Clause

Define **which rows** are included in the calculation.

### Syntax
```sql
ROWS BETWEEN frame_start AND frame_end
```

### Frame Options
- `UNBOUNDED PRECEDING`: From start of partition
- `N PRECEDING`: N rows before current
- `CURRENT ROW`: Current row
- `N FOLLOWING`: N rows after current
- `UNBOUNDED FOLLOWING`: To end of partition

### Common Patterns

#### Running Total
```sql
SELECT 
    date,
    amount,
    SUM(amount) OVER (
        ORDER BY date
        ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
    ) as running_total
FROM transactions;
```

#### Moving Average (3-day)
```sql
SELECT 
    date,
    price,
    AVG(price) OVER (
        ORDER BY date
        ROWS BETWEEN 2 PRECEDING AND CURRENT ROW
    ) as moving_avg_3day
FROM stock_prices;
```

#### Centered Average (before + current + after)
```sql
SELECT 
    date,
    value,
    AVG(value) OVER (
        ORDER BY date
        ROWS BETWEEN 1 PRECEDING AND 1 FOLLOWING
    ) as centered_avg
FROM data;
```

---

## LeetCode Problem Patterns

### Pattern 1: Ranking Within Groups
**Problems:** 185 (Top Three Salaries), 178 (Rank Scores)

```sql
-- Template
SELECT 
    *
FROM (
    SELECT 
        columns,
        DENSE_RANK() OVER (
            PARTITION BY group_column
            ORDER BY sort_column DESC
        ) as rank
    FROM table
) ranked
WHERE rank <= N;
```

### Pattern 2: Comparing Adjacent Rows
**Problems:** 180 (Consecutive Numbers), 197 (Rising Temperature)

```sql
-- Template
SELECT 
    *
FROM (
    SELECT 
        column,
        LAG(column, N) OVER (ORDER BY order_column) as prev
    FROM table
) compared
WHERE current = prev;
```

### Pattern 3: Running Calculations
**Problems:** Running totals, moving averages

```sql
-- Template
SELECT 
    date,
    value,
    SUM(value) OVER (
        ORDER BY date
        ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
    ) as running_sum
FROM table;
```

### Pattern 4: Deduplication
**Problems:** Remove duplicate rows

```sql
-- Template
DELETE FROM table
WHERE id NOT IN (
    SELECT MIN(id)
    FROM table
    GROUP BY unique_columns
);

-- Or with ROW_NUMBER
DELETE FROM table
WHERE id IN (
    SELECT id
    FROM (
        SELECT 
            id,
            ROW_NUMBER() OVER (
                PARTITION BY unique_columns
                ORDER BY id
            ) as rn
        FROM table
    ) t
    WHERE rn > 1
);
```

---

## Performance Tips

### 1. Indexing
```sql
-- Index columns used in:
-- - PARTITION BY
-- - ORDER BY
-- - WHERE clauses

CREATE INDEX idx_dept_salary ON employees(department, salary DESC);
```

### 2. Window Function vs GROUP BY

**Use Window Functions when:**
- Need to keep all rows
- Need multiple aggregations at different levels
- Comparing row values to aggregates

**Use GROUP BY when:**
- Need only aggregated results
- Collapsing rows is desired
- Generally faster for simple aggregations

### 3. Avoid Repeated Window Definitions
```sql
-- ❌ Bad: Repeated window definition
SELECT 
    RANK() OVER (PARTITION BY dept ORDER BY salary DESC),
    DENSE_RANK() OVER (PARTITION BY dept ORDER BY salary DESC)
FROM employees;

-- ✓ Good: Named window
SELECT 
    RANK() OVER w,
    DENSE_RANK() OVER w
FROM employees
WINDOW w AS (PARTITION BY dept ORDER BY salary DESC);
```

---

## Common Mistakes

### Mistake 1: Confusing RANK functions
```sql
-- Problem: Find top 3 unique salaries per department

-- ❌ Wrong: Using ROW_NUMBER
-- Will miss employees with tied salaries
WHERE ROW_NUMBER() OVER (...) <= 3

-- ✓ Correct: Using DENSE_RANK
-- Includes all employees in top 3 salary levels
WHERE DENSE_RANK() OVER (...) <= 3
```

### Mistake 2: Forgetting ORDER BY
```sql
-- ❌ Wrong: No ORDER BY with ranking
SELECT RANK() OVER (PARTITION BY dept) FROM employees;
-- Result: All ranks = 1 (no ordering specified)

-- ✓ Correct
SELECT RANK() OVER (PARTITION BY dept ORDER BY salary DESC) FROM employees;
```

### Mistake 3: Wrong Frame with Aggregates
```sql
-- ❌ Wrong: Default frame might not be what you want
SELECT SUM(amount) OVER (ORDER BY date) FROM transactions;
-- Default: RANGE BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW

-- ✓ Explicit: Be clear about what you want
SELECT SUM(amount) OVER (
    ORDER BY date
    ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
) FROM transactions;
```

---

## Quick Reference Table

| Function | Use Case | Groups? | Order? |
|----------|----------|---------|--------|
| RANK() | Ranking with gaps | Optional | Required |
| DENSE_RANK() | Consecutive ranks | Optional | Required |
| ROW_NUMBER() | Unique numbers | Optional | Required |
| LAG() | Previous row | Optional | Required |
| LEAD() | Next row | Optional | Required |
| SUM() OVER | Running total | Optional | Optional |
| AVG() OVER | Moving average | Optional | Optional |
| FIRST_VALUE() | First in group | Optional | Required |
| LAST_VALUE() | Last in group | Optional | Required |

---

## Practice Problems

**Easy:**
- 176: Second Highest Salary
- 177: Nth Highest Salary
- 178: Rank Scores

**Medium:**
- 180: Consecutive Numbers
- 184: Department Highest Salary
- 626: Exchange Seats

**Hard:**
- 185: Department Top Three Salaries
- 262: Trips and Users
- 601: Human Traffic of Stadium

---

## Summary

**Key Takeaways:**
1. Window functions don't collapse rows (unlike GROUP BY)
2. PARTITION BY divides data into groups
3. ORDER BY defines calculation order
4. Frame clause controls which rows are included
5. Choose right ranking function: RANK vs DENSE_RANK vs ROW_NUMBER
6. LAG/LEAD for comparing adjacent rows
7. Always be explicit with ORDER BY for consistent results

**Interview Tips:**
- Mention window functions early in discussion
- Explain why you chose specific ranking function
- Consider performance with indexes
- Test edge cases (ties, empty partitions)
- Compare to alternative approaches (self-join, subquery)