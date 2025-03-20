### **Leetcode 232: Implement Queue using Stacks**  
We need to implement a **First In, First Out (FIFO) queue** using only two **Last In, First Out (LIFO) stacks**.

---

## **🔹 Problem Statement**
Implement the following operations using **only stacks**:
1. `push(x)` → Pushes `x` to the back of the queue.
2. `pop()` → Removes and returns the element from the front of the queue.
3. `peek()` → Returns the front element.
4. `empty()` → Returns `True` if the queue is empty, else `False`.

---

## **🔹 Approach: Using Two Stacks**
We will use:
- **`stack1` (input stack)** → Stores elements in LIFO order.
- **`stack2` (output stack)** → Stores elements in FIFO order.

### **Steps:**
- **Push(x):** Push elements into `stack1`.
- **Pop():** If `stack2` is empty, transfer all elements from `stack1` to `stack2` and pop the top element.
- **Peek():** If `stack2` is empty, transfer all elements from `stack1` to `stack2` and return the top element.
- **Empty():** Return `True` if both stacks are empty.

---

## **🔹 Python Code (Two Stack Approach)**
```python
class MyQueue(object):

    def __init__(self):
        self.stack1 = []  # Input stack (used for push)
        self.stack2 = []  # Output stack (used for pop/peek)

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.stack1.append(x)  # Always push to stack1

    def pop(self):
        """
        :rtype: int
        """
        self._move_stack1_to_stack2()  # Move elements if stack2 is empty
        return self.stack2.pop() if self.stack2 else None

    def peek(self):
        """
        :rtype: int
        """
        self._move_stack1_to_stack2()  # Move elements if stack2 is empty
        return self.stack2[-1] if self.stack2 else None

    def empty(self):
        """
        :rtype: bool
        """
        return not self.stack1 and not self.stack2  # True if both stacks are empty

    def _move_stack1_to_stack2(self):
        """ Move elements from stack1 to stack2 if stack2 is empty. """
        if not self.stack2:  # Only transfer if stack2 is empty
            while self.stack1:
                self.stack2.append(self.stack1.pop())  # Reverse order
```

---

## **🔹 Explanation of Code**
### **`push(x)`**
- Simply push `x` into `stack1`.
- **Example:**  
  ```python
  q.push(1)  # stack1 = [1], stack2 = []
  q.push(2)  # stack1 = [1, 2], stack2 = []
  ```

### **`pop()`**
- If `stack2` is empty, move all elements from `stack1` to `stack2`.
- Pop the top element from `stack2`.
- **Example:**  
  ```python
  q.pop()   # Moves [1,2] -> [2,1] in stack2, then pops 1
  ```

### **`peek()`**
- If `stack2` is empty, move all elements from `stack1` to `stack2`.
- Return the top element of `stack2` without removing it.
- **Example:**  
  ```python
  q.peek()  # Returns 2 without popping
  ```

### **`empty()`**
- If both `stack1` and `stack2` are empty, return `True`, else `False`.

---

## **🔹 Time Complexity Analysis**
| Operation | Average Time Complexity | Explanation |
|-----------|------------------------|-------------|
| `push(x)` | **O(1)** | Directly appends to `stack1`. |
| `pop()` | **O(1) (Amortized)** | Moves elements from `stack1` to `stack2` **only when needed**. |
| `peek()` | **O(1) (Amortized)** | Moves elements only if `stack2` is empty. |
| `empty()` | **O(1)** | Simple check on both stacks. |

✅ **All operations are **O(1) amortized** time complexity!**

---

## **🔹 Follow-up: Why is it O(1) Amortized?**
- In the worst case, `pop()` or `peek()` moves **n elements** from `stack1` to `stack2`, which is **O(n)**.
- However, each element is moved **only once** in its lifetime.
- Over `n` operations, each element is pushed and popped **once**, so the **average cost per operation is O(1)**.

---

## **🔹 Summary**
| Approach | Pros | Cons |
|----------|------|------|
| **Two Stack (Lazy Transfer)** | O(1) amortized operations | Slightly more complex implementation |
| **Single Stack (Not Possible)** | - | Cannot maintain FIFO order |

This **two-stack** approach is optimal and widely used in real-world scenarios.

Happy Coding 🚀
