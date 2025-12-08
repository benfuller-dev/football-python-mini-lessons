# Lesson 03 — Defence Thresholds (Comparisons & Lists)

## What This Lesson Teaches
- How to classify values using numeric thresholds  
- How to apply comparisons in Python  
- How to encode football analytics logic into simple return values  
- How to iterate over a list of match statistics  
- How to build reusable classification functions  

---

## The Football Problem (Explained Simply)

In football analytics, **defensive strength** can be measured by how much xG a team *concedes* per match.  
Lower xG conceded means the defence is limiting high-quality chances; higher xG conceded suggests defensive weaknesses.

To make this usable in modelling, we convert raw xG conceded into a **simple 3-category score**:

- **1** → strong defence  
- **0** → average defence  
- **-1** → weak defence  

This allows you to compare teams consistently and use the results in later models.

---

## Defence Classification Rule

Let:

- `xg_conceded` = the expected goals conceded in a match  
- Thresholds based on typical Premier League defensive profiles  

| Meaning | Condition | Return Value |
|--------|-----------|--------------|
| Strong defence | `xg_conceded < 0.4` | **1** |
| Average defence | `0.4 <= xg_conceded <= 1.1` | **0** |
| Weak defence | `xg_conceded > 1.1` | **-1** |

These thresholds reflect meaningful cut-offs for how effectively a team restricts opposition chances.

---

## The Decision Logic (Human Words → Code)

1. If `xg_conceded < 0.4` → the defence limited chances extremely well → return **1**  
2. If `0.4 <= xg_conceded <= 1.1` → the defence performed reasonably → return **0**  
3. If `xg_conceded > 1.1` → the defence allowed too many chances → return **-1**  

In this lesson, you also iterate over a list of xG conceded values and classify each match using your function.

---

## Final Code (Used in This Lesson)

```python
def classify_defence(xg_conceded):
    """
    Classify defensive strength based on xG conceded.

    Returns:
        1  -> xg_conceded < 0.4       (strong defence)
        0  -> 0.4 <= xg_conceded <= 1.1 (average defence)
       -1  -> xg_conceded > 1.1       (weak defence)
    """
    if xg_conceded < 0.4:
        return 1
    elif 0.4 <= xg_conceded <= 1.1:
        return 0
    else:
        return -1


def classify_defence_list(values):
    """
    Apply the defence classification to a list of xG conceded values.
    Returns a list of encoded results.
    """
    results = []
    for v in values:
        results.append(classify_defence(v))
    return results

Example Test Cases

print(classify_defence(0.22))   # 1  (strong)
print(classify_defence(0.85))   # 0  (average)
print(classify_defence(1.43))   # -1 (weak)

sample_xg_conceded = [0.3, 0.6, 1.2, 0.95, 1.5]
print(classify_defence_list(sample_xg_conceded))
# Output: [1, 0, -1, 0, -1]

How You Would Teach This

You would introduce this lesson as a way of simplifying defensive performance into clear categories that a model can use.
You can show learners how threshold-based classification works in real analytics, then guide them through the comparisons in the function.
Using a list of matches helps demonstrate iteration and reinforces how functions apply across datasets.
By the end, learners understand how numeric conditions translate into labelled outcomes and how these labels feed into larger models (like the weighted rating system later in the course).

Files in This Lesson

| File                  | Purpose                                                                |
| --------------------- | ---------------------------------------------------------------------- |
| `classify_defence.py` | Contains both classification functions + test cases                    |
| `README.md`           | Rule explanation, decision logic, code, tests, and teaching reflection |
