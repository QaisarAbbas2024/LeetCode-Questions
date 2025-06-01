class Solution:
    def integerBreak(self, n: int) -> int:
        if n == 2:
            return 1
        if n == 3:
            return 2

        three = n // 3
        remainder = n % 3

        if remainder == 1:
            three -= 1
            remainder += 3
        elif remainder == 0:
            remainder = 1

        max_product = 3**three * remainder

        return max_product