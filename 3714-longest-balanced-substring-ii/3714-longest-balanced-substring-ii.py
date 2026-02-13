class Solution:
    def longestBalanced(self, s: str) -> int:
        n = len(s)
        ans = 0
        
        # ---------- Case 1: Single character ----------
        i = 0
        while i < n:
            j = i
            while j < n and s[j] == s[i]:
                j += 1
            ans = max(ans, j - i)
            i = j
        
        # ---------- Case 2: Two characters ----------
        def two_char(c1, c2):
            nonlocal ans
            diff = 0
            seen = {0: -1}
            
            for i, ch in enumerate(s):
                if ch == c1:
                    diff += 1
                elif ch == c2:
                    diff -= 1
                else:
                    diff = 0
                    seen = {0: i}
                    continue
                
                if diff in seen:
                    ans = max(ans, i - seen[diff])
                else:
                    seen[diff] = i
        
        two_char('a', 'b')
        two_char('a', 'c')
        two_char('b', 'c')
        
        # ---------- Case 3: Three characters ----------
        a = b = c = 0
        seen = {(0, 0): -1}
        
        for i, ch in enumerate(s):
            if ch == 'a':
                a += 1
            elif ch == 'b':
                b += 1
            else:
                c += 1
            
            key = (a - b, a - c)
            
            if key in seen:
                ans = max(ans, i - seen[key])
            else:
                seen[key] = i
        
        return ans
