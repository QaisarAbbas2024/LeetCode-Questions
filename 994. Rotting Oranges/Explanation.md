## **994. Rotting Oranges Problem** 
---

### **1️⃣ Understanding the Problem**  

Imagine a **grid (a 2D table)** where:
- `0` means **empty cell** (nothing is there).
- `1` means **a fresh orange** (good, but can rot).
- `2` means **a rotten orange** (already bad and can spread rot).

#### **How Rotting Works**:
- Every **minute**, a rotten orange will **spread the rot** to any fresh oranges **next to it** (up, down, left, or right).
- **This continues until** all fresh oranges either rot or are trapped.

### **Example 1**
#### **Input Grid:**
```
2 1 1
1 1 0
0 1 1
```
#### **Minute 1:**
```
2 2 1
2 1 0
0 1 1
```
(The rotten orange at **(0,0)** spreads to **(0,1) and (1,0)**.)

#### **Minute 2:**
```
2 2 2
2 2 0
0 1 1
```
(Oranges at **(0,1) and (1,0) rot their neighbors**.)

#### **Minute 3:**
```
2 2 2
2 2 0
0 2 1
```
(Orange at **(1,1) rot its neighbor (1,2)**.)

#### **Minute 4:**
```
2 2 2
2 2 0
0 2 2
```
(Last fresh orange rots.)

✅ **Output: 4 minutes**

---

### **Example 2 (Impossible Case)**
#### **Input Grid:**
```
2 1 1
0 1 1
1 0 1
```
- Some fresh oranges **cannot be reached**.
- **Output:** `-1` (Not all oranges can rot).

---

### **Example 3 (Already Rotten)**
#### **Input Grid:**
```
0 2
```
- No fresh oranges exist.
- **Output:** `0` (Nothing to rot).

---

## **2️⃣ What is BFS (Breadth-First Search)?**  

BFS is a method used in **graph traversal**.  

### **Understanding of BFS**
- Imagine you **drop a water droplet** in the center of a pond.
- The water **spreads outward in layers**.
- This is how **BFS spreads information**.

In this problem:
- **Rotten oranges are the "water droplet"**, spreading rot to fresh oranges.
- The **spread happens layer by layer** (minute by minute).
- **We use a queue** (a data structure) to keep track of which oranges will rot next.

---

## **3️⃣ Step-by-Step Approach to Solve the Problem**  

### **Step 1: Store Initial Rotten Oranges**
- We first **find all rotten oranges** (`2s`) in the grid.
- Store them in a **queue** to process them first.

### **Step 2: Count Fresh Oranges**
- We count **how many fresh oranges (`1s`)** exist.

### **Step 3: Use BFS to Rot Fresh Oranges**
- **Take rotten oranges from the queue**.
- **Spread the rot to neighbors** (up, down, left, right).
- **Add newly rotten oranges back to the queue**.
- **Repeat until all oranges are processed**.

### **Step 4: Check if All Fresh Oranges are Rotten**
- If **some fresh oranges are still left**, return `-1`.
- Otherwise, return the **time it took**.

---

## **4️⃣ Python Code (Step-by-Step)**
```python
from collections import deque

def orangesRotting(grid):
    rows, cols = len(grid), len(grid[0])  # Get grid size
    queue = deque()  # Queue to store rotten oranges
    fresh_count = 0  # Count fresh oranges
    minutes = 0  # Timer for rotting process

    # Step 1: Find all rotten oranges and count fresh ones
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 2:  # Rotten orange
                queue.append((r, c, 0))  # (row, col, time)
            elif grid[r][c] == 1:  # Fresh orange
                fresh_count += 1

    # Step 2: Define directions for moving (Right, Left, Down, Up)
    directions = [(0,1), (0,-1), (1,0), (-1,0)]  

    # Step 3: Start BFS
    while queue:
        r, c, time = queue.popleft()  # Process one rotten orange
        minutes = time  # Update minutes with last rotting time

        # Check all 4 possible directions
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                grid[nr][nc] = 2  # Rot the fresh orange
                fresh_count -= 1   # Reduce fresh orange count
                queue.append((nr, nc, time + 1))  # Add to queue with updated time

    # Step 4: If any fresh oranges are left, return -1, else return minutes
    return minutes if fresh_count == 0 else -1
```

---

## **5️⃣ Breaking Down the Code in Detail**
### **Step 1: Initialize Variables**
```python
    rows, cols = len(grid), len(grid[0])  # Get grid size
    queue = deque()  # Queue to store rotten oranges
    fresh_count = 0  # Count fresh oranges
    minutes = 0  # Timer for rotting process
```
- We get the **number of rows and columns** in the grid.
- We create a **queue** to store rotten oranges.
- We set `fresh_count` to **track the number of fresh oranges**.

---

### **Step 2: Find Rotten and Fresh Oranges**
```python
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 2:  # Rotten orange
                queue.append((r, c, 0))  # (row, col, time)
            elif grid[r][c] == 1:  # Fresh orange
                fresh_count += 1
```
- We **scan the entire grid**:
  - **Rotten oranges** are added to the **queue**.
  - **Fresh oranges** are **counted**.

---

### **Step 3: Start the BFS Process**
```python
    directions = [(0,1), (0,-1), (1,0), (-1,0)]  
```
- These represent **right, left, down, and up** movements.

```python
    while queue:
        r, c, time = queue.popleft()  # Process one rotten orange
        minutes = time  # Update minutes with last rotting time
```
- **Process each rotten orange one by one**.
- **Update the time** (so we can return the total minutes later).

```python
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                grid[nr][nc] = 2  # Rot the fresh orange
                fresh_count -= 1   # Reduce fresh orange count
                queue.append((nr, nc, time + 1))  # Add to queue with updated time
```
- **For each rotten orange**:
  - Check **all 4 directions**.
  - If **neighboring cell has a fresh orange**, **make it rotten**.
  - **Reduce fresh count**.
  - **Add it back to queue** with an **incremented time**.

---

### **Step 4: Check if All Fresh Oranges are Rotten**
```python
    return minutes if fresh_count == 0 else -1
```
- If all fresh oranges have **rotted**, return `minutes`.
- Otherwise, return `-1`.

---

## **6️⃣ Final Thoughts**
✅ **BFS spreads the rot level by level (minute by minute).**  
✅ **Using a queue ensures all rotten oranges spread simultaneously.**  
✅ **If any fresh oranges remain, return `-1`.**  

🔥 Hence, that was a **detailed explanation** of BFS and solution of this problem! 🚀
