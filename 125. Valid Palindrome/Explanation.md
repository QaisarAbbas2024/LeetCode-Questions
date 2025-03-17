### **✅ Two-Pointer Approach for Checking a Palindrome**  
This approach is **simple and memory-efficient**. We use **two pointers** to check if the string is a palindrome **without creating extra copies** of the string.

---

### **📝 Step-by-Step Explanation**  

1. **Convert the string to lowercase** (so "A" and "a" are treated the same).  
2. **Use two pointers**:  
   - One starts from the **left** (`left = 0`).  
   - One starts from the **right** (`right = last index`).  
3. **Skip non-alphanumeric characters** (ignore spaces, punctuation).  
4. **Compare characters** from both ends:  
   - If they match, move both pointers inward.  
   - If they don’t match, return `False` (not a palindrome).  
5. If all characters match, return `True`.

---

### **💻 Code:**
```python
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # Step 1: Convert to lowercase
        s = s.lower()

        # Step 2: Initialize two pointers
        left, right = 0, len(s) - 1

        # Step 3: Loop until pointers meet
        while left < right:
            # Ignore non-alphanumeric characters
            while left < right and not s[left].isalnum():
                left += 1  # Move left pointer forward
            while left < right and not s[right].isalnum():
                right -= 1  # Move right pointer backward

            # Compare letters from both ends
            if s[left] != s[right]:
                return False  # Not a palindrome
            
            # Move pointers inward
            left += 1
            right -= 1
        
        return True  # It's a palindrome!
```

---

### **🔍 Example Walkthrough**
#### **Example 1:**
```python
s = "A man, a plan, a canal: Panama"
```
#### **How It Works**
| Step | Left Pointer (Letter) | Right Pointer (Letter) | Are They Equal? | Move Pointers? |
|------|---------------------|---------------------|----------------|---------------|
| 1  | 'a' (index 0)  | 'a' (index 29)  | ✅ Yes | Move both |
| 2  | 'm' (index 1)  | 'm' (index 28)  | ✅ Yes | Move both |
| 3  | 'a' (index 2)  | 'a' (index 27)  | ✅ Yes | Move both |
| ... | ... | ... | ... | ... |
| Last  | 'n' (index 14) | 'n' (index 15) | ✅ Yes | Move both |

✅ **Final Answer:** `True` (Palindrome!)

---

### **📊 Time & Space Complexity**
| Approach | Time Complexity | Space Complexity |
|----------|---------------|----------------|
| Two-Pointer | **O(n)** (Scan once) | **O(1)** (No extra memory) |

---

### **🎯 Why This is the Best Approach?**
✅ No extra strings are created (saves memory).  
✅ Only **two variables (`left`, `right`)** are used.  
✅ Works efficiently for **large** strings.

***
### **Why `while left < right`?**  

This condition **ensures that we only check characters until the two pointers meet or cross each other**. Let’s break it down **step by step** in an easy way.  

---

### **🔍 What Does `while left < right` Mean?**  
- **`left` starts from the beginning** of the string (index `0`).  
- **`right` starts from the end** of the string (last index).  
- **We compare characters at `left` and `right`.**  
- **If they match, we move `left` forward (`+1`) and `right` backward (`-1`).**  
- **If `left >= right`, it means we’ve checked everything, and we can stop.**

---

### **📝 Example to Understand**
Let's say we have this string:  
```python
s = "racecar"
```
Here’s how `left` and `right` move:

| Step | Left Pointer (`left`) | Right Pointer (`right`) | Left Char | Right Char | Comparison |
|------|-----------------|-----------------|----------|-----------|------------|
| 1    | `0`            | `6`            | 'r'      | 'r'       | ✅ Match, move in |
| 2    | `1`            | `5`            | 'a'      | 'a'       | ✅ Match, move in |
| 3    | `2`            | `4`            | 'c'      | 'c'       | ✅ Match, move in |
| 4    | `3`            | `3`            | 'e'      | 'e'       | ✅ Middle reached, stop |

#### **Why stop when `left == right`?**
- When `left` reaches `right`, we have checked **all** necessary characters.  
- If all comparisons matched, **it’s a palindrome**.  
- If at any step `s[left] != s[right]`, we return `False`.  

---

### **⛔ What If We Used `while left <= right`?**
This would cause **extra unnecessary work** because:
- If `left == right`, we're checking the **middle character** alone.
- The middle character **does not matter** (it's always the same when reading forward and backward).
- The loop should **stop when `left == right` or crosses it**.

---

### **✅ Summary**
👉 **`while left < right` ensures that we only compare needed characters.**  
👉 **It prevents unnecessary checks and makes the solution efficient.**  
👉 **Once `left` reaches `right`, we are done checking the string.**  

Would you like me to run a visual simulation for another example? 😊
