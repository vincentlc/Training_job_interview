# Intersection of Two Arrays II

## 📝 Problem Description
Given two integer arrays `nums1` and `nums2`, return an array of their **intersection**. Each element in the result must appear as many times as it shows in both arrays, and you can return the result in **any order**.

**Example:**
```python
Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]
```

---

## 🚀 Solution Approach
- **Frequency Count:** Use a dictionary to count occurrences of each element in the smaller array.
- **Comparison:** Iterate through the larger array and check if elements exist in the frequency dictionary. If they do, add them to the result and decrement the count.
- **Edge Cases:** Handle empty arrays and arrays with no intersection.
- **Time Complexity:** O(n + m), where `n` and `m` are the lengths of `nums1` and `nums2`.
- **Space Complexity:** O(min(n, m)) for storing the frequency count.

---

## 🧪 How to Run
1. **Run the function directly:**
   ```python
   from intersection_two_arrays import intersect
   print(intersect([1, 2, 2, 1], [2, 2]))  # Output: [2, 2]
   ```

2. **Run tests:**
   ```bash
   pytest test_intersection_two_arrays.py -v
   ```

---

## **Project Structure**
```
intersection-two-arrays/
├── intersection_two_arrays.py  # Core implementation
├── test_intersection_two_arrays.py  # Test cases
└── README.md                    # Documentation
```

---

## 📚 Learning Points
- **Hash Maps:** Efficiently count and compare element frequencies using dictionaries.
- **Two-Pointer Technique:** Alternative approach for sorted arrays (O(n log n) time due to sorting).
- **Edge Cases:** Handle empty arrays, no intersection, and duplicate values.
- **Optimization:** Understand the trade-off between time and space complexity.
```
