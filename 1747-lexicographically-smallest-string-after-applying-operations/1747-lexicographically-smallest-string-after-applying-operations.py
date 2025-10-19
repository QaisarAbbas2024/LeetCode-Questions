class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        ans = s
        seen = set()

        def add(s: str, a: int) -> str:
            s = list(s)
            for i in range(1, len(s), 2):
                s[i] = str((int(s[i]) + a) % 10)
            return ''.join(s)

        def rotate(s: str, b: int) -> str:
            n = len(s)
            return s[-b:] + s[:-b]

        def dfs(s: str):
            nonlocal ans
            if s in seen:
                return
            seen.add(s)
            ans = min(ans, s)
            dfs(add(s, a))
            dfs(rotate(s, b))

        dfs(s)
        return ans
