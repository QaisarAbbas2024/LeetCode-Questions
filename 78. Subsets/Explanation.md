### **Leetcode 78: Subsets - Python Solution (Backtracking Approach)**  

This problem requires generating all subsets (the power set) of a given list of unique integers.  

---

## **🔹 Python Code**
```python
class Solution:
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []  # To store all subsets
        
        def backtrack(start, path):
            """
            start: The index from where we pick elements
            path: The current subset being built
            """
            result.append(path[:])  # Add a copy of path to result
            
            for i in range(start, len(nums)):  
                path.append(nums[i])  # Include nums[i] in subset
                backtrack(i + 1, path)  # Move to the next element
                path.pop()  # Undo (Backtrack) to try other possibilities

        backtrack(0, [])  # Start with an empty subset
        return result
```

---

## **🔹 Explanation of Code**
### **1️⃣ Understanding the Problem**
- We need **all possible subsets** of `nums`.  
- Example:  
  ```python
  nums = [1, 2, 3]
  ```
  Expected Output:
  ```python
  [[], [1], [2], [1,2], [3], [1,3], [2,3], [1,2,3]]
  ```
  This is called the **power set**.

---

### **2️⃣ Step-by-Step Execution**
#### **📌 `result = []`**
- Stores all the subsets we generate.

#### **📌 `def backtrack(start, path):`**
- `start`: The current index we are picking elements from.  
- `path`: The subset we are currently building.

#### **📌 Base Case**
```python
result.append(path[:])  # Store the current subset
```
- We add a **copy** of `path` to `result` every time.

#### **📌 Loop to Explore Further**
```python
for i in range(start, len(nums)):
    path.append(nums[i])  # Pick the element
    backtrack(i + 1, path)  # Recursive call
    path.pop()  # Backtrack (Undo last step)
```
- We **include `nums[i]`**, then **recursively call** `backtrack`.
- After recursion, we **remove `nums[i]` (Backtrack)** to try new possibilities.

---

## **🔹 Example Walkthrough**
Let's take `nums = [1, 2, 3]` and trace the recursion.

### **Step 1: Start with an Empty Path**
```
[]
```
Store `[]` in `result`.

---

### **Step 2: Pick `1`, Remaining `[2,3]`**
```
[1]
```
Store `[1]` in `result`.

- Pick `2` → `[1,2]`
- Pick `3` → `[1,2,3]` ✅ Store it.
- **Backtrack**: Remove `3`
- **Backtrack**: Remove `2`

Try `3` directly:
```
[1,3]
```
Store `[1,3]`.

---

### **Step 3: Pick `2` Directly**
```
[2]
```
Store `[2]`.

- Pick `3` → `[2,3]`
- **Backtrack**: Remove `3`

---

### **Step 4: Pick `3` Directly**
```
[3]
```
Store `[3]`.

---

**Final Output**:
```python
[[], [1], [2], [1,2], [3], [1,3], [2,3], [1,2,3]]
```
This covers **all possible subsets**.

---

## **🔹 Time Complexity Analysis**
- Since each element has **two choices** (included or not), we generate **\(2^n\) subsets**.
- **Time Complexity = O(2^n)**
- **Space Complexity = O(n)** (for recursion stack).

---

## **🔹 Optimized Iterative Approach**
Instead of recursion, we can **build subsets iteratively**.

```python
class Solution:
    def subsets(self, nums):
        result = [[]]  # Start with an empty subset
        
        for num in nums:  
            new_subsets = [subset + [num] for subset in result]
            result.extend(new_subsets)  
        
        return result
```
🔹 **How it Works?**
- Start with `[[]]` (empty subset).
- For each number, **append it to existing subsets**.

Example:
```python
nums = [1, 2, 3]
Iteration 1: [[]] → [[], [1]]
Iteration 2: [[], [1]] → [[], [1], [2], [1,2]]
Iteration 3: [[], [1], [2], [1,2]] → [[], [1], [2], [1,2], [3], [1,3], [2,3], [1,2,3]]
```
✅ **Same O(2^n) time, but no recursion overhead!**

---

## **🔹 Summary**
- **Backtracking** generates subsets recursively.
- **Iterative approach** builds subsets step by step.
- **Time Complexity:** `O(2^n)`, best possible.
- **Space Complexity:** `O(n)`, for recursion or iteration.

***
Code Concludes with explanation.
