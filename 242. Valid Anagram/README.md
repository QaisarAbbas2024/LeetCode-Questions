## **📝 Solution for "Valid Anagram" (Leetcode 242)**
Following is solution of the problem:
---

## **✅ Understanding the Problem**
Two strings are **anagrams** if one string can be rearranged to form the other.

### **Example 1**
#### **Input**
```python
s = "anagram"
t = "nagaram"
```
#### **Explanation**
Both strings have the **same characters** with the **same frequency**.

#### **Output**
```python
True
```

### **Example 2**
#### **Input**
```python
s = "rat"
t = "car"
```
#### **Explanation**
- `s` has `"r", "a", "t"`
- `t` has `"c", "a", "r"`
- `"c"` is extra, and `"t"` is missing.

#### **Output**
```python
False
```

---

## **🔹 Optimized Approach Using Hash Map (Dictionary)**
### **🔑 Key Idea**
1. Both strings **must have the same length**.
2. Count the **frequency of characters** in `s` and `t`.
3. If both frequency counts are the **same**, then `t` is an anagram of `s`.

---

### **✅ Python Code (Optimized Hash Map Approach)**
```python
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False  # If lengths are different, they can't be anagrams
        
        char_count = {}  # Dictionary to store character frequency
        
        # Count frequency of characters in string 's'
        for char in s:
            char_count[char] = char_count.get(char, 0) + 1
        
        # Reduce the frequency based on string 't'
        for char in t:
            if char in char_count:
                char_count[char] -= 1
                if char_count[char] == 0:
                    del char_count[char]  # Remove if count reaches zero
            else:
                return False  # If character is not in 's', return False
        
        return len(char_count) == 0  # If dictionary is empty, it's an anagram
```

---

## **🔍 How Does This Work?**
### **Example 1**
#### **Input**  
```python
s = "anagram"
t = "nagaram"
```
#### **Processing Steps**
| Character | Count in `s` | Count in `t` | After Processing |
|-----------|-------------|-------------|-----------------|
| a | 3 | 3 | ✅ |
| n | 1 | 1 | ✅ |
| g | 1 | 1 | ✅ |
| r | 1 | 1 | ✅ |
| m | 1 | 1 | ✅ |

Since all character counts match, **it is an anagram**.

#### **Output**
```python
True
```

---

### **Example 2**
#### **Input**
```python
s = "rat"
t = "car"
```
#### **Processing Steps**
| Character | Count in `s` | Count in `t` | After Processing |
|-----------|-------------|-------------|-----------------|
| r | 1 | 1 | ✅ |
| a | 1 | 1 | ✅ |
| t | 1 | 0 | ❌ (Mismatch) |

Since counts **do not match**, `t` is **not** an anagram of `s`.

#### **Output**
```python
False
```

---

## **🔹 Time & Space Complexity**
| Approach | Time Complexity | Space Complexity |
|----------|---------------|----------------|
| **Optimized Hash Map Approach** | `O(N)` | `O(1)` (At most 26 keys for English letters) |

- **Time Complexity:** `O(N)` → We iterate over both strings **once**.
- **Space Complexity:** `O(1)` → We store at most **26 letters** in the dictionary.

---

## **✅ Alternative Approach (Sorting)**
We can also check if two strings are anagrams by **sorting** both strings.

```python
class Solution(object):
    def isAnagram(self, s, t):
        return sorted(s) == sorted(t)
```

### **⏳ Time Complexity**
- **Sorting takes** `O(N log N)`, which is **slower** than `O(N)`.
- **Uses extra space** due to sorting.

⚠️ **Not recommended for large inputs!**

---

## **🚀 Handling Unicode Characters (Follow-up Question)**
If the input contains **Unicode characters** (e.g., `é, ç, ñ`), the same **hash map approach** works **without changes**.

However, **sorting** may behave differently in different languages due to Unicode encoding.

🔹 **Best approach** → Hash map (same as above) ✅

---

## **🎯 Conclusion**
1️⃣ **Best Approach:** Use **hash map (dictionary)** for `O(N)` time.  
2️⃣ **Sorting Approach:** `O(N log N)`, not efficient for large inputs.  
3️⃣ **Handles Unicode Characters** → No extra modifications needed.  
***
