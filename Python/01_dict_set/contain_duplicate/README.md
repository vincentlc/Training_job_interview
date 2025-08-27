---

# Contain Duplicate

A Python solution to the **Contain Duplicate** problem: Given an array of integers, return `True` if any value appears at least twice, otherwise return `False`.

## **Problem Statement**
Given an integer array `nums`, return `True` if any value appears **at least twice** in the array, and return `False` if all elements are distinct.

**Example:**
```python
Input: nums = [1, 2, 3, 1]
Output: True
```

---

## **Features**
- Efficient solution using a hash set (O(n) time complexity).
- Type hints for clarity.
- Comprehensive test cases.

---

## **Installation**
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/contain_duplicate.git
   cd contain_duplicate
   ```

2. Install dependencies (if any):
   ```bash
   pip install pytest  # Only needed for running tests
   ```

---

## **Usage**
### **As a Function**
```python
from contain_duplicate import contains_duplicate

nums = [1, 2, 3, 1]
print(contains_duplicate(nums))  # Output: True
```

### **As a Class**
```python
from contain_duplicate import Solution

solution = Solution()
nums = [1, 2, 3, 4]
print(solution.containsDuplicate(nums))  # Output: False
```

---

## **Running Tests**
Run the test suite with `pytest`:
```bash
pytest test_contain_duplicate.py -v
```

---

## **Time Complexity**
- **O(n)**: We use a hash set to track seen elements, ensuring linear time complexity.

---

## **Project Structure**
```
contain_duplicate/
├── contain_duplicate.py   # Implementation
├── test_contain_duplicate.py  # Tests
└── README.md               # Documentation
```
---

