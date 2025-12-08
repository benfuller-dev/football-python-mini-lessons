# Lesson 04 — Rolling Form (Loops, Slicing & Averages)

## What This Lesson Teaches
- How to extract recent data using list slicing (`values[-6:]`)  
- How to compute averages using a loop or Python’s `sum()` function  
- How to convert match-by-match values into a single performance indicator  
- How rolling metrics are used in real football analytics  
- How to write clean, reusable functions  

---

## The Football Problem (Explained Simply)

A team’s **recent form** is one of the strongest predictors of upcoming performance.

Rather than looking at the whole season, analysts often focus on the **last six matches**, because:

- It reflects current momentum  
- It smooths out one-off results  
- It highlights short-term trends affecting confidence, injuries, or tactical changes  

To measure recent form, we take the **average of the last six match values** (e.g., goals scored, xG, xG battle results, defensive ratings).

---

## The Rolling Form Rule

Let:

- `values` = a list of match metrics (e.g., `[1, -1, 0, 1, 1, -1, …]`)  
- We want to compute the average of the **last six** values  

### Steps

| Step | Explanation |
|------|-------------|
| 1 | Extract last six matches → `recent = values[-6:]` |
| 2 | Compute the total → `sum(recent)` or loop |
| 3 | Divide by 6 to get the average |
| 4 | Return the rolling form as a single number |

This produces a meaningful **6-game form score**, used widely in modelling and betting analytics.

---

## The Decision Logic (Human Words → Code)

1. Take the last 6 values from the list  
2. Add them together  
3. Divide by 6 to compute the average  
4. Return the result  

The logic is simple but extremely powerful—it reduces a sequence of performances into a single indicator of momentum.

---

## Final Code (Used in This Lesson)

```python
def rolling_form(values):
    """
    Calculate the 6-game rolling average for a list of match values.

    Steps:
        - Extract last six matches using slicing
        - Compute their sum
        - Divide by six
    Returns a single numeric value representing recent form.
    """
    
    # Step 1: Get the last six matches
    recent = values[-6:]
    
    # Step 2: Compute the total
    total = sum(recent)
    
    # Step 3: Compute the average
    average = total / 6
    
    return average

Example Test Cases

# Example 1 — Mixed results
matches = [1, 0, -1, 1, 1, 0, -1, 1]
print(rolling_form(matches))
# Last 6 = [-1, 1, 1, 0, -1, 1]
# Average = 1/6 ≈ 0.166...

# Example 2 — Strong recent form
matches = [1, 1, 1, 1, 1, 1, 0]
print(rolling_form(matches))
# Last 6 = [1, 1, 1, 1, 1, 0]
# Average = 5/6 ≈ 0.833...

# Example 3 — Poor recent form
matches = [-1, -1, 0, -1, 0, -1, 1]
print(rolling_form(matches))
# Last 6 = [-1, 0, -1, 0, -1, 1]
# Average = -2/6 ≈ -0.333...

How You Would Teach This

You would explain that rolling form is one of the most intuitive analytics concepts because it aligns with how fans already think about momentum.
Once learners see that values[-6:] pulls out the recent matches, they immediately understand how slicing works.
From there, averaging teaches loops, sum(), and basic numerical reasoning.
This lesson reinforces the idea of turning many match results into one meaningful number, preparing learners for weighting, modelling, and prediction later in the course.

Files in This Lesson

| File              | Purpose                                                 |
| ----------------- | ------------------------------------------------------- |
| `rolling_form.py` | Contains the rolling average function + test cases      |
| `README.md`       | Rule explanation, logic, code, examples, teaching notes |
