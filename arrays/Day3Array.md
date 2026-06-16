# Day 3 - Arrays

## Problem: Product of Array Except Self

Today I solved the **Product of Array Except Self** problem.

### My Thought Process

My initial approach was a **brute-force solution**. For each element, I calculated the product of all other elements in the array. While this worked correctly, it required traversing the array multiple times, resulting in a time complexity of **O(n²)**.

After analyzing the repeated calculations, I looked for a more efficient approach and discovered the **Prefix-Suffix Technique**.

### Optimized Approach: Prefix & Suffix Products

The idea is to precompute:

- **Prefix Product:** Product of all elements to the left of the current index.
- **Suffix Product:** Product of all elements to the right of the current index.

For each index:

```text
answer[i] = prefix[i] * suffix[i]
```

This eliminates redundant calculations and reduces the overall complexity to **O(n)**.

### Complexity Analysis

| Approach | Time Complexity | Space Complexity |
|-----------|----------------|------------------|
| Brute Force | O(n²) | O(1) |
| Prefix-Suffix | O(n) | O(n) |

### Key Learning

- Identified inefficiencies in a brute-force solution.
- Learned how precomputation can significantly improve performance.
- Practiced the Prefix-Suffix pattern, which is useful for many array-based problems.

### Takeaway

A common optimization strategy is to identify repeated computations and store intermediate results. The Prefix-Suffix technique is a great example of converting a quadratic-time solution into a linear-time solution.

---
**Day 3 Complete ✅**

#DSA #Arrays #LeetCode #ProblemSolving #100DaysOfCode
