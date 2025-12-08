# Lesson 07 — Match Outcome Prediction (TypeScript Function)

## What This Lesson Teaches
- How to write a simple TypeScript function  
- How to define input types (`number`, `interface`, etc.)  
- How to use thresholds to determine predictions  
- How to return categorical outcomes (“win”, “draw”, “loss”)  
- How to translate a Python-based model into TypeScript syntax  
- How modelling logic can be used in front-end or tooling applications  

This lesson shows learners how analytics logic moves from Python → TypeScript and into production-friendly environments.

---

## The Football Problem (Explained Simply)

Once you have a **team rating** (from Lesson 05), you often want to make a basic prediction:

- Will the team likely **win**?
- Will the match be **close**?
- Is the team likely to **struggle**?

We can convert the rating into a simple 3-way match prediction using two thresholds:

- A **win threshold** (e.g., 0.5)  
- A **draw margin** (range near zero, e.g., ±0.2)  

This creates an interpretable prediction rule used in many basic models.

---

## The Prediction Rule

Let:

- `rating` = the team’s overall strength score  
- `winThreshold` = minimum value to predict a win  
- `drawMargin` = the “close enough” band around zero  

### We return:

| Meaning | Condition | Return Value |
|--------|-----------|--------------|
| Likely win | `rating > winThreshold` | `"win"` |
| Likely loss | `rating < -winThreshold` | `"loss"` |
| Close match / balanced | `abs(rating) <= drawMargin` | `"draw"` |

This produces a simple, readable 3-category prediction.

---

## The Decision Logic (Human Words → Code)

1. If rating is comfortably above the win threshold → return `"win"`  
2. If rating is comfortably below the loss threshold → return `"loss"`  
3. If rating is near zero (within the draw margin) → return `"draw"`  
4. Return the result as a string for use in UI tools or further models  

This is a clean example of TypeScript being used for deterministic modelling.

---

## Final Code (Used in This Lesson)

```typescript
function predictOutcome(
    rating: number,
    winThreshold: number = 0.5,
    drawMargin: number = 0.2
): "win" | "draw" | "loss" {

    if (rating > winThreshold) {
        return "win";
    } else if (rating < -winThreshold) {
        return "loss";
    } else if (Math.abs(rating) <= drawMargin) {
        return "draw";
    } else {
        // Slight lean but outside draw margin
        return rating > 0 ? "win" : "loss";
    }
}

Example Test Cases

console.log(predictOutcome(0.82));     // "win"
console.log(predictOutcome(-0.77));    // "loss"
console.log(predictOutcome(0.05));     // "draw"
console.log(predictOutcome(0.25));     // "win" (slight edge)
console.log(predictOutcome(-0.28));    // "loss" (slight edge)

This helps learners see how threshold tuning affects model behaviour.

This helps learners see how threshold tuning affects model behaviour.

How You Would Teach This

You would explain that this lesson completes the modelling pipeline.
Learners have built metrics, a rating system, and now a prediction function written in TypeScript.
You can show them how TypeScript adds type safety, especially useful in UI tools or web apps.
The lesson highlights how the same logic used in Python can be reused across languages, reinforcing transferable modelling skills.
By adjusting thresholds, learners can see how prediction confidence changes, deepening their understanding of evaluation logic.

Files in This Lesson

| File                | Purpose                                                            |
| ------------------- | ------------------------------------------------------------------ |
| `predictOutcome.ts` | TypeScript prediction function + example tests                     |
| `README.md`         | Rule explanation, TypeScript logic, thresholds, and teaching notes |

