from collections import Counter

class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        count = Counter(words)
        res = 0
        central = False

        for word in count:
            rev = word[::-1]
            if word == rev:
                pairs = count[word] // 2
                res += pairs * 4
                if count[word] % 2 == 1:
                    central = True
            elif word < rev:
                res += 4 * min(count[word], count[rev])
        
        if central:
            res += 2

        return res
