# Lesson 01 — xG Battle (Conditionals & Threshold Logic)

## What This Lesson Teaches
- How to use `if / elif / else`  
- How to compare numerical values  
- How to apply a tolerance buffer to avoid false classification  
- How to encode football logic into simple return values (-1, 0, 1)  
- How conditionals translate real-world decision rules into Python  

This is the foundational lesson for your analytics model.

---

## The Football Problem (Explained Simply)

In football analytics, the **xG battle** tells us which team created the better quality chances in a match.  
But xG values can be very close, so small differences shouldn’t always decide the “winner”.

To avoid misclassification, we use a **tolerance value** (0.25).  
This treats xG values within a small range as “effectively equal”.

---

## The xG Battle Rule

Let:

- `team_xg` = the team’s expected goals  
- `opp_xg` = opponent’s expected goals  
- `tolerance` = buffer for treating small differences as equal (default 0.25)

We return:

| Meaning | Condition | Return Value |
|--------|-----------|--------------|
| Team clearly won the xG battle | `team_xg > opp_xg + tolerance` | **1** |
| Too close to call | `abs(team_xg - opp_xg) <= tolerance` | **0** |
| Team clearly lost the xG battle | otherwise | **-1** |

This encoding is perfect for modelling and classification tasks.

---

## The Decision Logic (Human Words → Code)

1. If `team_xg > opp_xg + tolerance` → clear win → return **1**  
2. If the values are within tolerance → treat as equal → return **0**  
3. Otherwise → clear loss → return **-1**  

This introduces the idea of **threshold-based logic**, a foundation for future lessons.

---

## Final Code (Used in This Lesson)

```python
def xg_battle(team_xg, opp_xg, tolerance=0.25):
    """
    Determine the outcome of the xG battle.

    Returns:
        1  -> team_xg > opp_xg + tolerance (clear win)
        0  -> abs(team_xg - opp_xg) <= tolerance (effectively equal)
       -1  -> team_xg < opp_xg - tolerance (clear loss)
    """

    if team_xg > opp_xg + tolerance:
        return 1
    elif abs(team_xg - opp_xg) <= tolerance:
        return 0
    else:
        return -1

Example Test Cases
print(xg_battle(0.67, 1.6))   # -1 (clear loss)
print(xg_battle(1.8, 0.4))    # 1  (clear win)
print(xg_battle(0.96, 1.1))   # 0  (equal within tolerance)

These examples show all three possible outcomes.

How You Would Teach This

You would explain that conditionals allow us to encode decision rules exactly as analysts reason about them.
Learners see how the tolerance prevents overreacting to small differences, and how the numeric encoding (-1, 0, 1) supports modelling later.
You would walk learners through each condition, helping them understand why the order matters and how Python evaluates each branch.
This lesson sets the foundation for overperformance scoring, defence classification, form tracking, and the final rating model built in later lessons.

| File           | Purpose                                                   |
| -------------- | --------------------------------------------------------- |
| `xg_battle.py` | Function + test cases                                     |
| `README.md`    | Full explanation of rule, logic, code, and teaching notes |

