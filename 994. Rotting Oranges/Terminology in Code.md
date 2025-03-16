## Terminology in Code

## **1️⃣ What is `deque`? (Why This Word?)**
### 🔹 **Meaning of `deque`**
- **Full form:** **D**ouble-**E**nded **Que**ue (**deque**).
- It is a special type of **queue** that allows **fast adding and removing** elements **from both ends** (front and back).
- **Why use `deque` instead of a normal list?**  
  - **Faster**: Removing from the front (`popleft()`) in a list takes **O(n)** time, while in `deque` it takes **O(1)** time.
  - **Efficient for BFS (Breadth-First Search)**.

### 🔹 **Example Usage**
```python
from collections import deque

queue = deque()  # Create an empty deque
queue.append(1)  # Add 1 to the queue
queue.append(2)  # Add 2 to the queue
print(queue)  # Output: deque([1, 2])

queue.popleft()  # Remove the first element (1)
print(queue)  # Output: deque([2])
```
- **Appending (`append()`) adds to the back.**
- **`popleft()` removes from the front efficiently.**

---

## **2️⃣ What are `r, c`?**
### 🔹 **Meaning of `r, c`**
- `r` stands for **row number**.
- `c` stands for **column number**.
- Since we are working with a **2D grid (matrix)**, each cell is identified by **(row, column)**.

### 🔹 **Example**
Consider this grid:
```
  0   1   2   (Columns)
----------------
0 | 2 | 1 | 1 |
1 | 1 | 1 | 0 |   (Rows)
2 | 0 | 1 | 1 |
```
- The **top-left** orange is at `(r=0, c=0)`.
- The **bottom-right** orange is at `(r=2, c=2)`.

### 🔹 **Usage in Code**
```python
for r in range(rows):    # Loop through rows
    for c in range(cols):  # Loop through columns
        if grid[r][c] == 2:  # If the cell contains a rotten orange
            queue.append((r, c, 0))  # Store its position in the queue
```
- **`r, c` help us track the position of each orange** in the grid.

---

## **3️⃣ What is `queue.popleft()`?**
### 🔹 **Meaning**
- **Removes the first (oldest) element from the queue**.
- It ensures that we **process rotten oranges in the order they were added** (FIFO – First In, First Out).

### 🔹 **Example**
```python
queue = deque([(0, 0), (1, 2), (2, 1)])  # Queue has some positions
print(queue.popleft())  # Removes (0,0) -> Output: (0, 0)
print(queue)  # Output: deque([(1, 2), (2, 1)])
```
- This is useful in **BFS** because we always process the **oldest rotten orange first** before newer ones.

---

## **4️⃣ What are `dr, dc`?**
### 🔹 **Meaning**
- `dr` = **Change in row** (delta row).
- `dc` = **Change in column** (delta column).
- These are used to **move in four directions** in the grid.

### 🔹 **Directions We Need**
```python
directions = [(0,1), (0,-1), (1,0), (-1,0)]
```
- `(0,1)` → Move **right** (same row, next column).
- `(0,-1)` → Move **left** (same row, previous column).
- `(1,0)` → Move **down** (next row, same column).
- `(-1,0)` → Move **up** (previous row, same column).

---

## **5️⃣ What are `nr, nc`?**
### 🔹 **Meaning**
- `nr` = **New row number** (next position after moving).
- `nc` = **New column number** (next position after moving).

### 🔹 **Usage in Code**
```python
for dr, dc in directions:
    nr, nc = r + dr, c + dc  # Calculate new row and column position
```
- `nr` and `nc` help us check the **new position** of an orange **after moving**.

### 🔹 **Example Calculation**
Imagine `r=1, c=1` (middle orange) and we check all directions:
| Direction | `(dr, dc)` | `(nr, nc)` Calculation | New Position |
|-----------|------------|------------------------|--------------|
| Right     | `(0,1)`    | `(1+0, 1+1)` = `(1,2)` | (1,2) |
| Left      | `(0,-1)`   | `(1+0, 1-1)` = `(1,0)` | (1,0) |
| Down      | `(1,0)`    | `(1+1, 1+0)` = `(2,1)` | (2,1) |
| Up        | `(-1,0)`   | `(1-1, 1+0)` = `(0,1)` | (0,1) |

---

## **6️⃣ What is `queue.append()`?**
### 🔹 **Meaning**
- **Adds an element to the end of the queue**.
- Used to **store new rotten oranges** after they spread rot.

### 🔹 **Usage in Code**
```python
queue.append((nr, nc, time + 1))  # Add new rotten orange
```
- This adds a **new rotten orange's position** `(nr, nc)` to the queue.
- **`time + 1` keeps track of minutes passed.**

---

## **🔹 Full Code Explanation with Comments**
```python
from collections import deque  # Import deque for fast queue operations

def orangesRotting(grid):
    rows, cols = len(grid), len(grid[0])  # Get grid size
    queue = deque()  # Create a queue to store rotten oranges
    fresh_count = 0  # Count of fresh oranges
    minutes = 0  # Track time

    # Step 1: Find all rotten oranges and count fresh ones
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 2:  # Rotten orange
                queue.append((r, c, 0))  # Store (row, col, time)
            elif grid[r][c] == 1:  # Fresh orange
                fresh_count += 1  # Count fresh oranges

    # Step 2: Define movement directions (Right, Left, Down, Up)
    directions = [(0,1), (0,-1), (1,0), (-1,0)]  

    # Step 3: BFS to spread rot
    while queue:
        r, c, time = queue.popleft()  # Get the next rotten orange
        minutes = time  # Update time with last rotten orange

        # Check all 4 directions
        for dr, dc in directions:
            nr, nc = r + dr, c + dc  # Compute new row, column
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                grid[nr][nc] = 2  # Rot the fresh orange
                fresh_count -= 1  # Reduce fresh count
                queue.append((nr, nc, time + 1))  # Add to queue with time

    # Step 4: If fresh oranges remain, return -1; otherwise, return minutes
    return minutes if fresh_count == 0 else -1
```

---

## **🎯 Summary**
| Term | Meaning |
|------|---------|
| `deque` | **Double-ended queue** for efficient popping from the front (`O(1)`) |
| `queue.popleft()` | **Removes the first element** from the queue |
| `queue.append(x)` | **Adds an element** to the queue |
| `r, c` | **Current row and column position** |
| `dr, dc` | **Direction to move in the grid** |
| `nr, nc` | **New row and column after moving** |

