## 📝 Problem Description
Given two strings `s` and `t`, determine if they are **anagrams** of each other.
An anagram is formed by rearranging the letters of one string to match another, using all the original letters exactly once.

**Example:**
```python
Input: s = "listen", t = "silent"
Output: True
```

---

## 🚀 Solution Approach
- **Frequency Count:** Use a dictionary or an array to count the occurrences of each character in both strings.
- **Comparison:** If the frequency counts match, the strings are anagrams.
- **Edge Cases:** Handle strings of unequal length (immediately return `False`) and ignore spaces/punctuation if needed.
- **Time Complexity:** O(n), where `n` is the length of the strings.

---

## 🧪 How to Run
1. **Run the function directly:**
   ```python
   from two_anagrams import is_anagram
   print(is_anagram("listen", "silent"))  # Output: True
   ```

2. **Run tests:**
   ```bash
   pytest test_two_anagrams.py -v
   ```

---

## **Project Structure**
```
two_anagrams/
├── two_anagrams.py      # Core implementation
├── test_two_anagrams.py # Test cases
└── README.md            # Documentation
```

---

## 📚 Learning Points
- **Hash Maps:** Efficiently count character frequencies using dictionaries.
- **String Manipulation:** Practice iterating and comparing strings.
- **Edge Cases:** Learn to handle empty strings, different lengths, and case sensitivity.
- **Optimization:** Understand the trade-off between time and space complexity.
```
