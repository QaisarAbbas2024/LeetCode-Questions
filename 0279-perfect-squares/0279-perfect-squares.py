import math
class Solution:
    def numSquares(self, n: int) -> int:
        # Step 1: Check if n is a perfect square
        if int(math.sqrt(n))**2 == n:
            return 1
        
        # Step 2: Check if n can be written as the sum of 2 squares
        for i in range(1, int(math.sqrt(n)) + 1):
            remainder = n - i*i
            if int(math.sqrt(remainder))**2 == remainder:
                return 2
        
        # Step 3: Reduce n by removing factors of 4
        while n % 4 == 0:
            n //= 4
        
        # Step 4: Check Legendre's condition
        if n % 8 == 7:
            return 4
        
        # Else, return 3
        return 3
