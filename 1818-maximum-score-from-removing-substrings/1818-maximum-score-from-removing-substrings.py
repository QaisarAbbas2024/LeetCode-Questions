class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        def remove(sub1, sub2, val):
            stack = []
            score = 0
            for ch in s:
                if stack and stack[-1] == sub1 and ch == sub2:
                    stack.pop()
                    score += val
                else:
                    stack.append(ch)
            return ''.join(stack), score

        if x > y:
            s, score1 = remove('a', 'b', x)
            _, score2 = remove('b', 'a', y)
        else:
            s, score1 = remove('b', 'a', y)
            _, score2 = remove('a', 'b', x)
        return score1 + score2
