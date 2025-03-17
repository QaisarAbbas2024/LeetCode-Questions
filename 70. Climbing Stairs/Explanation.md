## **Solution for Climbing Stairs (Leetcode 70)**  
This problem is a **dynamic programming (DP)** problem that follows the **Fibonacci sequence** pattern. Let’s break it down step by step.

---

### **🔹 Understanding the Problem**
Each time, you can take **1 step** or **2 steps**. You need to find the number of ways to reach the **n-th step**.

### **Example 1**  
#### **Input:**
```python
n = 2
```
#### **Explanation:**
1. `1 step + 1 step`
2. `2 steps`

✅ **Output:**
```python
2
```

---

### **Example 2**  
#### **Input:**
```python
n = 3
```
#### **Explanation:**
1. `1 step + 1 step + 1 step`
2. `1 step + 2 steps`
3. `2 steps + 1 step`

✅ **Output:**
```python
3
```

---

### **🔹 Observing the Pattern**
If we look at the ways to reach each step:

| `n` | Ways to Climb |
|----|--------------|
| `1` | `1` |
| `2` | `2` |
| `3` | `3` |
| `4` | `5` |
| `5` | `8` |
| `6` | `13` |
| `7` | `21` |

It follows the **Fibonacci sequence**:  
`ways(n) = ways(n-1) + ways(n-2)`

---

## **🔹 Optimized Approach: Dynamic Programming (O(N) Time, O(1) Space)**
Instead of using recursion (which is slow), we use an **iterative approach** with two variables.

### **✅ Python Code**
```python
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        if n == 2:
            return 2

        first, second = 1, 2  # Base cases for n=1 and n=2
        
        for _ in range(3, n + 1):
            third = first + second  # Fibonacci relation
            first, second = second, third  # Move forward
        
        return second
```

---

## **🔍 How Does It Work?**
1. **Base Cases:**  
   - If `n = 1`, return `1`.  
   - If `n = 2`, return `2`.  
2. **Iterate from 3 to n:**  
   - Use two variables (`first` and `second`) to store previous values.
   - Compute the next value using:  
     `third = first + second`
   - Shift values forward.

---

## **🔹 Time & Space Complexity**
| Approach | Time Complexity | Space Complexity |
|----------|---------------|----------------|
| **Optimized DP Approach** | `O(N)` | `O(1)` (only 3 variables used) |

💡 **Why is this better than recursion?**  
- **Recursion** has **exponential** `O(2^N)` complexity (slow).  
- **This DP approach** runs in **linear** `O(N)` time and **constant** `O(1)` space.

---

## **🚀 Alternative: Formula-Based Fibonacci (O(log N) Time)**
We can also use the **Fibonacci formula** (Binet’s formula) to solve it in `O(log N)` time using **matrix exponentiation**.
