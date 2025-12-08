lesson02_xg_overperformance/README.md

Lesson 02 — xG Overperformance (Functions & Numeric Logic)

What This Lesson Teaches

- How to write a Python function
- How to use parameters and default values
- Basic numeric logic
- How to convert a real-world football concept into code
- Returning simple category labels for modelling
- Strengthening analytic thinking

The Football Problem (Explained Simply)

In football analytics, overperformance measures whether a team is scoring more goals than expected from their xG.

This tells us:

- Which teams are finishing clinically
- Which teams are scoring unsustainably
- Whether a team’s goal return matches the quality of chances created

We encode this using your established system:
Overperformance Rule

Let:

- goals = goals scored
- xg = expected goals
- tolerance = how close is “close enough” (default 0.25)

| Meaning                                   | Return Value |
| ----------------------------------------- | ------------ |
| Team scored **more** than xG predicts     | `1`          |
| Team scored **less** than xG predicts     | `-1`         |
| Team’s goals and xG are **roughly equal** | `0`          |

The Decision Logic (Human Words → Code)

If goals > xG + tolerance → clear overperformance → return 1
Else if abs(goals - xG) <= tolerance → basically equal → return 0
Else → underperformance → return -1

This is a perfect function example because you can teach:

- parameters
- comparisons
- return values
- logic branching
- real-world interpretation

Final Code (Used in This Lesson)

def xg_overperformance(goals, xg, tolerance=0.25):
    """
    Determine whether a team overperformed or underperformed their xG.

    Returns:
        1  -> goals > xg + tolerance (clear overperformance)
        0  -> abs(goals - xg) <= tolerance (performance matches chance quality)
        -1 -> goals < xg - tolerance (underperformance)
    """

    if goals > xg + tolerance:
        return 1
    elif abs(goals - xg) <= tolerance:
        return 0
    else:
        return -1


# Example test cases
print(xg_overperformance(2, 0.9))    # 1 -> overperformed
print(xg_overperformance(1, 1.05))   # 0 -> equal
print(xg_overperformance(0, 0.8))    # -1 -> underperformed

How You Would Teach This
This function converts a football performance concept into a simple classification model.
We use tolerance to avoid mislabeling small differences as meaningful.
The function returns clean numeric categories (-1, 0, 1) which can be used in further modelling, rolling averages, and weighted rating systems.

This lesson introduces how parameters and return values work, and how functions provide reusable logic when analysing multiple matches or teams.
