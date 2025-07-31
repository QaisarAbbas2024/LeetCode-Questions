from typing import List

class Solution:
    def subarrayBitwiseORs(self, arr: List[int]) -> int:
        s = []
        l = 0

        for a in arr:
            r = len(s)
            s.append(a)
            # s[l:r] are values generated in the previous iteration
            for i in range(l, r):
                if s[-1] != (s[i] | a):
                    s.append(s[i] | a)
            l = r

        return len(set(s))
