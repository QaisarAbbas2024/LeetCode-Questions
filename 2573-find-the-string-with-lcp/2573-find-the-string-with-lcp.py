from typing import List

class Solution:
    def findTheString(self, lcp: List[List[int]]) -> str:
        n = len(lcp)
        non_letter = chr(ord('a') - 1)  # character before 'a'
        c = non_letter
        word = [non_letter] * n

        for i in range(n):
            if word[i] != non_letter:
                continue
            # move to next character
            c = chr(ord(c) + 1)
            if c > 'z':  # ran out of letters
                return ""
            for j in range(i, n):
                if lcp[i][j] > 0:
                    word[j] = c

        # validate the constructed word
        for i in range(n):
            for j in range(n):
                if i + 1 < n and j + 1 < n:
                    next_lcp = lcp[i + 1][j + 1]
                else:
                    next_lcp = 0

                curr_lcp = 1 + next_lcp if word[i] == word[j] else 0

                if lcp[i][j] != curr_lcp:
                    return ""

        return "".join(word)