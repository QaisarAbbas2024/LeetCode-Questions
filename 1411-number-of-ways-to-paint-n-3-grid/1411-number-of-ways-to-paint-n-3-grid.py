class Solution:
    def numOfWays(self, n: int) -> int:
        MOD = 1_000_000_007
        color2 = 6  # 121, 131, 212, 232, 313, 323
        color3 = 6  # 123, 132, 213, 231, 312, 321

        for _ in range(1, n):
            nextColor2 = color2 * 3 + color3 * 2
            nextColor3 = color2 * 2 + color3 * 2
            color2 = nextColor2 % MOD
            color3 = nextColor3 % MOD

        return (color2 + color3) % MOD
