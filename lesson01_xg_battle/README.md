# Lesson 01 — xG Battle (Conditionals)

## What This Lesson Teaches
- `if / elif / else` conditionals  
- Numeric comparison  
- Working with a tolerance value  
- Writing a simple, testable Python function  
- Translating a real-world rule into code  

---

## The Football Problem (Explained Simply)

In football analytics, the **xG battle** tells us which team created the better chances in a match.

But xG values are often close — so we use a **tolerance of 0.25** to avoid overreacting to small differences.

---

## The Rule

Given:

- `team_xg` — the team’s expected goals  
- `opp_xg` — opponent’s expected goals  
- `tolerance` — small buffer (default `0.25`)  

We encode the result as:

| Meaning                                 | Return Value |
|-----------------------------------------|--------------|
| Team clearly won the xG battle          | 1            |
| xG values effectively equal (tolerance) | 0            |
| Team clearly lost the xG battle         | -1           |

---

## The Decision Logic (Human Words → Code)

1. If `team_xg` is greater than `opp_xg + tolerance` → **clear win → return 1**  
2. Else if the difference is within tolerance → **too close to call → return 0**  
3. Else → **clear loss → return -1**

---

## Final Code (Used in This Lesson)

```python
def xg_battle(team_xg, opp_xg, tolerance=0.25):
    """
    Determine the xG battle outcome.

    Returns:
        1  -> team_xg is greater than opp_xg + tolerance (clear win)
        0  -> abs(team_xg - opp_xg) <= tolerance (effectively equal)
        -1 -> team_xg is lower than opp_xg - tolerance (clear loss)
    """

    if team_xg > opp_xg + tolerance:
        return 1
    elif abs(team_xg - opp_xg) <= tolerance:
        return 0
    else:
        return -1


# Example test cases
print(xg_battle(0.67, 1.6))   # -1
print(xg_battle(1.8, 0.4))    # 1
print(xg_battle(0.96, 1.1))   # 0
