# Lesson 06 — SQL Basics for Football Analytics (Queries, Filtering & Aggregation)

## What This Lesson Teaches
- How SQL is used to query and analyse structured data  
- How to SELECT, FILTER, ORDER, and AGGREGATE match data  
- How to JOIN tables to build richer analytics views  
- How football metrics (xG battle, overperformance, defence score, form) translate into SQL queries  
- How to think like an analyst working with a dataset instead of a Python list  

This lesson shows how your football model naturally becomes a SQL-friendly dataset.

---

## The Football Problem (Explained Simply)

Once football performance data is stored in a table, analysts need ways to:

- filter matches  
- find specific conditions (e.g., who won the xG battle)  
- calculate averages  
- join statistics across teams  
- generate reports  

SQL provides the exact tools needed to do this at scale.

For example:

- “Show all matches where a team won the xG battle”  
- “Calculate each team’s average xG conceded”  
- “Find teams with a rolling form > 0.5”  
- “Join match-level data with team-level ratings”  

This lesson introduces the core SQL concepts needed for these tasks.

---

## The SQL Logic for This Lesson

We imagine a basic table called **matches** containing:

| Column | Description |
|--------|-------------|
| team | team name |
| opponent | opponent name |
| goals | goals scored |
| xg | expected goals |
| xg_against | xG conceded |
| xg_battle | -1/0/1 result from Lesson 1 |
| overperf | -1/0/1 from Lesson 2 |
| defence | -1/0/1 from Lesson 3 |
| form | rolling form score (Lesson 4) |

This allows us to use SQL to query your entire analytics model.

---

## Core SQL Patterns Demonstrated

### 1. **Selecting Rows**
```sql
SELECT * FROM matches;

Filtering (WHERE)

Find all matches where the team won the xG battle:

SELECT team, opponent, xg, xg_battle
FROM matches
WHERE xg_battle = 1;

Find weak defensive performances:

SELECT team, opponent, xg_against, defence
FROM matches
WHERE defence = -1;

Sorting (ORDER BY)

Find matches where the team conceded the most xG:
SELECT team, xg_against
FROM matches
ORDER BY xg_against DESC;

Aggregating (AVG, COUNT, SUM)

Average xG scored by each team:

SELECT team, AVG(xg) AS avg_xg
FROM matches
GROUP BY team;

SELECT team, AVG(xg) AS avg_xg
FROM matches
GROUP BY team;

Count how many matches each team won the xG battle:

SELECT team, COUNT(*) AS xg_battle_wins
FROM matches
WHERE xg_battle = 1
GROUP BY team;

Joining Tables (If using multiple tables)

Imagine a second table:

team_ratings
(team, rating)

Join it with match results:

SELECT m.team, m.opponent, m.xg_battle, t.rating
FROM matches m
JOIN team_ratings t
  ON m.team = t.team;

This demonstrates how SQL supports richer combined analytics.

How You Would Teach This

You would explain that SQL is simply a way of “asking questions” of a structured dataset.
Because your football model already uses encoded metrics and rolling averages, it translates naturally into SQL queries.
Learners can see how conditionals become WHERE clauses, how rolling averages become AVG(), and how JOINs combine multiple sources.
This lesson helps them recognise how Python logic and SQL logic complement each other in real analytics workflows, preparing them for more advanced modelling.

| File                 | Purpose                                            |
| -------------------- | -------------------------------------------------- |
| `sample_queries.sql` | Example SQL queries for common analytics tasks     |
| `README.md`          | Explanation of SQL logic, examples, teaching notes |



