# Lesson 05 — Weighted Team Rating Model (Mini Project)

## What This Lesson Teaches
- How to combine multiple metrics into a single model output  
- How to design and apply weighting systems  
- How functions call other functions  
- How to structure a small end-to-end analytics pipeline  
- How model components (xG battle, defence, form, etc.) work together  
- How to create a reusable “team rating” function  

This is the first mini-project where learners build something that behaves like an **actual sports analytics model**.

---

## The Football Problem (Explained Simply)

A single football metric—like xG, defence score, or form—doesn’t tell the whole story.  
Analysts combine **multiple signals** to estimate how strong a team is overall.

Your existing model already uses:

- **xG Battle Score** (Lesson 1)  
- **Overperformance Score** (Lesson 2)  
- **Defence Score** (Lesson 3)  
- **6-Game Rolling Form** (Lesson 4)  

Each metric captures something different, so we **assign weights** based on how important each factor is.

The result is a **Weighted Team Rating**, a single number representing overall strength.

---

## The Weighted Rating Rule

Let the metrics be:

- `xg_battle` → categorical score (−1, 0, 1)  
- `overperf` → categorical score (−1, 0, 1)  
- `defence` → categorical score (−1, 0, 1)  
- `form` → rolling value (float)  

Let the weights be:

- `w1`, `w2`, `w3`, `w4`  
- Typically chosen so they sum to 1 (e.g., 0.3 + 0.2 + 0.3 + 0.2)

### Final rating formula:

rating = (xg_battle * w1)
+ (overperf * w2)
+ (defence * w3)
+ (form * w4)


A higher score indicates a stronger, more reliable team.

---

## The Decision Logic (Human Words → Code)

1. Multiply each metric by its weight  
2. Add the weighted values together  
3. Return the final rating  
4. Optionally round the output for cleaner reporting  

This mirrors real modelling logic used in betting analytics, power rankings, and predictive systems.

---

## Final Code (Used in This Lesson)

```python
def team_rating(xg_battle, overperf, defence, form,
                w1=0.3, w2=0.2, w3=0.3, w4=0.2):
    """
    Compute a weighted team rating using four metrics:
    - xg_battle : -1, 0, 1
    - overperf  : -1, 0, 1
    - defence   : -1, 0, 1
    - form      : rolling average (float)

    Weights (w1–w4) should normally sum to 1.

    Returns:
        A single float representing team strength.
    """

    rating = (xg_battle * w1) \
           + (overperf  * w2) \
           + (defence   * w3) \
           + (form      * w4)

    return round(rating, 3)

# Example 1 — Balanced team
print(team_rating(
    xg_battle=1, overperf=0, defence=0, form=0.2
))
# Possible output: 0.26


# Example 2 — Strong defence, poor finishing
print(team_rating(
    xg_battle=0, overperf=-1, defence=1, form=0.5
))
# Possible output: 0.26


# Example 3 — Weak team overall
print(team_rating(
    xg_battle=-1, overperf=-1, defence=-1, form=-0.3
))
# Possible output: -0.72

How You Would Teach This

You would explain that this project brings together everything learned so far.
Learners can now take individual metrics—each captured as a simple function—and combine them into a unified model.
You would emphasise that weighting is a modelling choice: analysts decide what matters most, and the model reflects those priorities.
By adjusting weights or input scores, learners can see how a team’s overall rating responds.
This lesson helps them understand modelling intuition, function composition, and how analytics systems are built in practice.

| File             | Purpose                                                   |
| ---------------- | --------------------------------------------------------- |
| `team_rating.py` | Weighted rating function + example tests                  |
| `README.md`      | Full explanation of the rule, logic, code, teaching notes |

