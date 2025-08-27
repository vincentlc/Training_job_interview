# 📘 Exercise: Two Sum

## 📝 Problem Description
Given an array of integers `nums` and an integer `target`, return the **indices** of the two numbers that add up to `target`.  
Assume that each input has exactly one solution, and you cannot use the same element twice.

**Example:**
- Input: `nums = [2,7,11,15], target = 9` → Output: `[0,1]`
- Input: `nums = [3,2,4], target = 6` → Output: `[1,2]`

---

## 🚀 Solution Approach
- Use a **dictionary** to store numbers and their indices.
- For each number `n`, check if `target - n` exists in the dictionary.
- If found, return the indices.
- Time Complexity: O(n), Space Complexity: O(n).

---

## 🧪 How to Run
```bash
pytest test_two_sum.py -v
```

---

## 📚 Learning Points
- Practiced **hashmap lookups** for constant-time checks.
- Applied **problem-solving patterns** (search + complement).
- Used **TDD** with pytest.
