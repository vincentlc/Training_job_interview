## 📝 Problem Description
Given a string `s`, find the index of the first non-repeating character. If no such character exists, return `-1`.

A non-repeating character is one that appears only once in the string.

**Example:**
```python
Input: s = "leetcode"
Output: 0

Input: s = "loveleetcode"
Output: 2

Input: s = "aabb"
Output: -1
```

---

## 🚀 Solution Approach
- **Frequency Count:** Use a dictionary to count the occurrences of each character in the string.
- **Index Search:** Iterate through the string to find the first character with a frequency of `1`.
- **Edge Cases:** Handle empty strings (immediately return `-1`) and strings with no unique characters.

**Time Complexity:** O(n), where `n` is the length of the string.

---

## 🧪 How to Run
1. **Run the function directly:**
   ```python
   from first_uniq_char import first_uniq_char
   print(first_uniq_char("leetcode"))  # Output: 0
   ```

2. **Run tests:**
   ```bash
   pytest test_first_uniq_char.py -v
   ```

---

## **Project Structure**
```
first-uniq-char/
├── first_uniq_char.py      # Core implementation
├── test_first_uniq_char.py # Test cases
└── README.md               # Documentation
```

---

## 📚 Learning Points
- **Hash Maps:** Efficiently count character frequencies using dictionaries.
- **String Manipulation:** Practice iterating and comparing strings.
- **Edge Cases:** Learn to handle empty strings and strings with no unique characters.
- **Optimization:** Understand the trade-off between