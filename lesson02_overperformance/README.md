# Lesson 02 — xG Overperformance (Functions & Numeric Logic)

## What This Lesson Teaches
- How to write a Python function  
- How to use parameters and default values  
- How to compare numerical values  
- How to convert a real-world football concept into code  
- Returning simple numeric labels for modelling  
- Strengthening analytics thinking  

---

## The Football Problem (Explained Simply)

In football analytics, **overperformance** measures whether a team is scoring more goals than expected from their xG.

This tells us:

- Which teams are finishing clinically  
- Which teams are scoring *unsustainably*  
- Whether recent goal output matches the quality of chances created  

We encode this using a simple rule: **Overperformance Rule**

Let:

- `goals` = goals scored  
- `xg` = expected goals  
- `tolerance` = "how close is close enough" (default 0.25)

| Meaning | Return Value |
|--------|--------------|
| Team scored more than xG predicts | 1 |
| Team scored less than xG predicts | -1 |
| Team’s goals & xG are roughly equal | 0 |

---

## The Decision Logic (Human Words → Code)

1. If `goals > xg + tolerance` → **overperformance** → return `1`  
2. If `abs(goals - xg) <= tolerance` → **roughly equal** → return `0`  
3. Else → **underperformance** → return `-1`  

This lesson is perfect for exploring:

- comparison  
- parameters  
- return values  
- tolerance thresholds  
- real-world interpretation  

---

## Final Code (Used in This Lesson)

```python
def xg_overperformance(goals, xg, tolerance=0.25):
    """
    Determine whether a team overperformed or underperformed their xG.

    Returns:
        1  -> team scored more than expected (clear overperformance)
        0  -> abs(goals - xg) <= tolerance (roughly equal)
        -1 -> team scored less than expected (clear underperformance)
    """

    if goals > xg + tolerance:
        return 1
    elif abs(goals - xg) <= tolerance:
        return 0
    else:
        return -1

print(xg_overperformance(2.0, 1.7))    # 1
print(xg_overperformance(1.0, 1.0))    # 0
print(xg_overperformance(0.8, 1.3))    # -1

How You Would Teach This

I frame the function as a translation of a real football performance concept into a small, reusable decision tool.
I highlight how tolerance prevents misclassification, and why the numeric return values (-1, 0, 1) are ideal for modelling.
I guide learners through parameters and return values using the PiLORS framework so they can clearly see the structure.
Finally, I show how this function can feed into larger analytics workflows like rolling form, slicing averages, and weighted models.

| File                    | Purpose                                                   |
| ----------------------- | --------------------------------------------------------- |
| `xg_overperformance.py` | The function + test cases                                 |
| `README.md`             | Explanation of rule, logic, code, and teaching reflection |

