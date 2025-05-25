class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        last_occurrence = {c: i for i, c in enumerate(s)}  # last index of each char
        stack = []
        seen = set()

        for i, c in enumerate(s):
            if c not in seen:
                # Pop characters that are bigger than current char and appear later again
                while stack and c < stack[-1] and i < last_occurrence[stack[-1]]:
                    removed = stack.pop()
                    seen.remove(removed)
                stack.append(c)
                seen.add(c)
        return ''.join(stack)
