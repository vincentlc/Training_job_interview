---

````markdown
# 📘 Exercise: First Unique Character in a String

## 📝 Problem Description
Given a string, return the index of the **first non-repeating character**.  
If no such character exists, return `-1`.

**Examples:**
- Input: `"leetcode"` → Output: `0`  
- Input: `"loveleetcode"` → Output: `2`  
- Input: `"aabb"` → Output: `-1`

---

## 🚀 Solution Approach
- ✅ Use a **dictionary** to count character frequencies.  
- ✅ First pass: count occurrences of each character.  
- ✅ Second pass: find the first character with count = 1.  
- ✅ Time Complexity: **O(n)** (two passes over the string).  
- ✅ Space Complexity: **O(1)** (since only lowercase letters, max 26 counts).  

---

## 🧪 How to Run

### Python
```bash
pytest test_uniqueString.py
````

---

## 📚 Learning Points

* [x] Practiced using a **dictionary** for frequency counting.
* [x] Applied the **two-pass scanning pattern** (count then check).
* [x] Wrote a **pytest test file** before implementing (TDD).
* [x] Focused on **clear naming** and clean return values.

---

## ✅ Example Run

Input:

```
"loveleetcode"
```

Output:

```
2
```

```

---


