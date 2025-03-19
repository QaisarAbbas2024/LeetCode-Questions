## **Leetcode 46: Permutations**  
This problem requires generating **all possible permutations** of a given list of numbers. Let's break it down step by step.

---

## **🔹 Understanding the Problem**
**Given:**  
- A list of **distinct integers** `nums`.  
- **Find:** All possible **permutations** (different orders of elements).  

---

### **Example 1**  
#### **Input:**
```python
nums = [1,2,3]
```
#### **Output:**
```python
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
```

---

### **Example 2**  
#### **Input:**
```python
nums = [0,1]
```
#### **Output:**
```python
[
  [0,1],
  [1,0]
]
```

---

## **🔹 Observing the Pattern**
- If `nums = [1]`, output = `[[1]]` (only one way).  
- If `nums = [1, 2]`, output = `[[1,2], [2,1]]`.  
- If `nums = [1,2,3]`, we take each element as **first** and find permutations of the rest.  

💡 **We need to generate all possible orders of elements**.

---

## **🔹 Approach: Backtracking (DFS)**
The most common way to generate permutations is **backtracking** (Depth-First Search).  

### **✅ Python Code**
```python
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []  # List to store permutations
        
        def backtrack(path, choices):
            if not choices:  # Base case: all numbers used
                result.append(path[:])  # Store a copy of path
                return
            
            for i in range(len(choices)):  
                path.append(choices[i])  # Pick a number
                backtrack(path, choices[:i] + choices[i+1:])  # Recur without picked number
                path.pop()  # Undo last choice (backtrack)
        
        backtrack([], nums)  # Start with an empty path
        return result
```

---

## **🔍 How Does It Work?**
- We **build permutations step by step** using recursion.  
- **Each step:**  
  - Choose a number from `nums`.  
  - Remove it from choices and recursively find permutations.  
  - **Undo (backtrack)** by removing the last choice.  

### **Example Walkthrough**
For `nums = [1,2,3]`:
```
Start → [] 
1 → [1] 
    2 → [1,2] 
        3 → [1,2,3] ✅ (store it)
        Backtrack to [1,2]
    3 → [1,3]
        2 → [1,3,2] ✅ (store it)
        Backtrack to [1]
2 → [2]
    1 → [2,1]
        3 → [2,1,3] ✅
    3 → [2,3]
        1 → [2,3,1] ✅
3 → [3]
    1 → [3,1]
        2 → [3,1,2] ✅
    2 → [3,2]
        1 → [3,2,1] ✅
```

---

## **🔹 Time & Space Complexity**
| Approach | Time Complexity | Space Complexity |
|----------|---------------|----------------|
| **Backtracking (DFS)** | `O(N!)` | `O(N!)` |

✅ `O(N!)` is the best possible complexity since there are `N!` (factorial) permutations.  
✅ **Space is also `O(N!)`** because we store all permutations.

---

## **🚀 Alternative Approach: Using itertools (Built-in Python)**
Python has a **built-in function** for permutations:
```python
from itertools import permutations

class Solution(object):
    def permute(self, nums):
        return list(map(list, permutations(nums)))
```
💡 **Pros:** Simple & easy to write.  
💡 **Cons:** Uses extra memory and is **not allowed** in interviews!

---

## **🔹 Summary**
| Approach | Pros | Cons |
|----------|------|------|
| **Backtracking (DFS)** | Efficient, standard approach | Requires recursion |
| **itertools.permutations** | Simple, built-in | Not allowed in coding interviews |

***
