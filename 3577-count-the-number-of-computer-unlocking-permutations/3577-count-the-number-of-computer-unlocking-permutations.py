class Solution:
    def countPermutations(self, complexity: list[int]) -> int:
        MOD = 10**9 + 7
        n = len(complexity)

        # if any computer i>0 has complexity <= complexity[0], it's impossible to unlock it
        for i in range(1, n):
            if complexity[i] <= complexity[0]:
                return 0

        # otherwise, all (n-1)! permutations of [1..n-1] are valid unlock orders
        ans = 1
        for i in range(1, n):
            ans = ans * i % MOD
        return ans
