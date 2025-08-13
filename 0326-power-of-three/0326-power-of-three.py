class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        # Keep dividing n by 3 if divisible
        while n > 1 and n % 3 == 0:
            n //= 3
        # True if reduced to 1
        return n == 1
