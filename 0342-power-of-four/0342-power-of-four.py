class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        # A power of four must be positive
        if n <= 0:
            return False
        # Check if n is a power of two (only one bit set)
        if n & (n - 1) != 0:
            return False
        # For power of four, the only set bit must be in an odd position (0-indexed)
        # 0x55555555 in binary has bits set at positions 0, 2, 4, ... (odd powers of two)
        return (n & 0x55555555) != 0
