class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        magic = 665772
        return sum(
            (magic >> num.bit_count()) & 1
            for num in range(left, right + 1)
        )