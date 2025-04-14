## **Leetcode 67: Add Binary**

---

### **💡 Understanding the Problem**
We are given **two binary strings** (`a` and `b`) and we need to **add them** together, just like we do with decimal numbers, but in **binary**.  

#### **Example 1**
```
Input:  a = "11", b = "1"
Output: "100"
Explanation:
   11
 +  1
 ----
  100  (Binary Sum)
```
#### **Example 2**
```
Input:  a = "1010", b = "1011"
Output: "10101"
```

---

### **🔢 How to Solve It?**
1. Convert the **binary strings** into **decimal numbers**.  
2. Add them like normal numbers.  
3. Convert the result back into a **binary string**.  
4. Return the final **binary sum**.  

---

### **🐍 Python Code**
```python
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # Step 1: Convert binary to decimal
        num1 = int(a, 2)  # Convert 'a' to decimal
        num2 = int(b, 2)  # Convert 'b' to decimal
        
        # Step 2: Add the numbers
        total = num1 + num2  # Normal addition in decimal
        
        # Step 3: Convert back to binary and return (removing '0b' prefix)
        return bin(total)[2:]  # bin() gives '0b...' so we remove '0b'
```

---

### **🔍 Step-by-Step Explanation**
#### ✅ **Step 1: Convert Binary to Decimal**
- Python provides a built-in function `int(string, base)`, where:
  - `"11"` in **binary (base 2)** → `int("11", 2) = 3`
  - `"1"` in **binary (base 2)** → `int("1", 2) = 1`
```python
num1 = int(a, 2)  # Convert 'a' from binary to decimal
num2 = int(b, 2)  # Convert 'b' from binary to decimal
```
#### ✅ **Step 2: Add the Numbers**
- Simply add the numbers in decimal:
```python
total = num1 + num2  # Normal addition
```
For `"11" + "1"`, it becomes:
```
3 + 1 = 4
```
#### ✅ **Step 3: Convert the Sum Back to Binary**
- Python provides `bin(number)` to convert decimal to binary.
```python
bin(total)  # Gives '0b100'
```
- The `0b` prefix means it's a binary number. To remove this, we use:
```python
bin(total)[2:]  # Remove the '0b' part
```
- Final output is **"100"**.

---

### **🚀 Example Runs**
#### **Example 1**
```python
a = "11"
b = "1"
Solution().addBinary(a, b)
```
**Output:**
```
"100"
```

#### **Example 2**
```python
a = "1010"
b = "1011"
Solution().addBinary(a, b)
```
**Output:**
```
"10101"
```

---

### **🔥 Why is This the Easiest Approach?**
✔ Uses Python’s built-in **int()** and **bin()** functions.  
✔ **No need to manually calculate carry bits.**  
✔ **Short and readable** – only 3 simple steps.  

---
