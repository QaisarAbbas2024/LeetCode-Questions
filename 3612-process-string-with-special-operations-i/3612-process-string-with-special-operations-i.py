class Solution:
    def processStr(self, s: str) -> str:
        ans = []
        for ch in s:
            if ch.isalpha(): ## Used if the character is letter for this problem
                ans.append(ch)
            elif ch == "*":
                if ans:
                    ans.pop()
            elif ch == "#":
                ans.extend(ans)
            elif ch == "%":
                ans.reverse()
        return "".join(ans)