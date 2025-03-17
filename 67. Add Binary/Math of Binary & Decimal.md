### **Understanding the 8421 Rule in Binary Conversion**  

The **8421 rule** is a simple way to understand how **binary numbers** work. It helps you **convert** between **binary (base-2)** and **decimal (base-10)** by breaking numbers into powers of **2**.  

Each digit (bit) in a **4-bit binary number** represents a specific **power of 2**:  

| **8**  | **4**  | **2**  | **1**  |  
|--------|--------|--------|--------|  
| \(2³\) | \(2²\) | \(2¹\) | \(2⁰\) |  

This means:
- The **leftmost bit (8)** is worth **8** if it’s **1**, otherwise **0**.
- The **next bit (4)** is worth **4** if it’s **1**, otherwise **0**.
- The **next bit (2)** is worth **2** if it’s **1**, otherwise **0**.
- The **rightmost bit (1)** is worth **1** if it’s **1**, otherwise **0**.

---

### **📝 8421 Table for Binary to Decimal Conversion**  

| **Binary** | **8 (2³)** | **4 (2²)** | **2 (2¹)** | **1 (2⁰)** | **Decimal Value** |
|------------|------------|------------|------------|------------|----------------|
| 0000       | 0          | 0          | 0          | 0          | 0              |
| 0001       | 0          | 0          | 0          | 1          | 1              |
| 0010       | 0          | 0          | 1          | 0          | 2              |
| 0011       | 0          | 0          | 1          | 1          | 3              |
| 0100       | 0          | 1          | 0          | 0          | 4              |
| 0101       | 0          | 1          | 0          | 1          | 5              |
| 0110       | 0          | 1          | 1          | 0          | 6              |
| 0111       | 0          | 1          | 1          | 1          | 7              |
| 1000       | 1          | 0          | 0          | 0          | 8              |
| 1001       | 1          | 0          | 0          | 1          | 9              |
| 1010       | 1          | 0          | 1          | 0          | 10             |
| 1011       | 1          | 0          | 1          | 1          | 11             |
| 1100       | 1          | 1          | 0          | 0          | 12             |
| 1101       | 1          | 1          | 0          | 1          | 13             |
| 1110       | 1          | 1          | 1          | 0          | 14             |
| 1111       | 1          | 1          | 1          | 1          | 15             |

---

### **🛠 How to Use the 8421 Rule to Convert Binary to Decimal**
1️⃣ **Write down the binary number and align it with 8421.**  
2️⃣ **Multiply each binary digit (bit) by its corresponding power of 2.**  
3️⃣ **Add the values together to get the decimal number.**  

### **Example 1: Convert 1011 (Binary) to Decimal**
```
1 × 8  =  8
0 × 4  =  0
1 × 2  =  2
1 × 1  =  1
-------------
Total   = 11 (Decimal)
```
✅ **1011 (Binary) = 11 (Decimal)**  

---

### **Example 2: Convert 1100 (Binary) to Decimal**
```
1 × 8  =  8
1 × 4  =  4
0 × 2  =  0
0 × 1  =  0
-------------
Total   = 12 (Decimal)
```
✅ **1100 (Binary) = 12 (Decimal)**  

---

### **🎯 Key Takeaways**
✔ The **8421 rule** assigns each bit a value from the **powers of 2**.  
✔ To convert, **multiply each bit by its place value** and **sum** the results.  
✔ Works best for **4-bit binary numbers** but can be extended for larger numbers.  

***
