from typing import List

class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        n = len(s)
        freq = [0] * 26
        for ch in s:
            freq[ord(ch) - 97] += 1

        # Check if a palindromic permutation exists (at most one odd count)
        odd_count = sum(1 for x in freq if x % 2 == 1)
        if odd_count > 1:
            return ""

        # Build the smallest palindrome from the given frequencies (for reference)
        def build_min_pal(f):
            left = []
            mid = ''
            for c in range(26):
                if f[c] % 2 == 1:
                    mid = chr(97 + c)
                left.append(chr(97 + c) * (f[c] // 2))
            left_str = ''.join(left)
            return left_str + mid + left_str[::-1]

        min_pal = build_min_pal(freq[:])
        if min_pal > target:
            return min_pal

        half = n // 2
        odd_char = -1
        for c in range(26):
            if freq[c] % 2 == 1:
                odd_char = c
                break

        left_half = [''] * half

        # Fill the remaining left_half positions with the smallest possible characters
        def fill_remaining(pos, f):
            for i in range(pos, half):
                for c in range(26):
                    if f[c] >= 2:
                        f[c] -= 2
                        left_half[i] = chr(97 + c)
                        break
                else:
                    return None
            # Build full palindrome
            if n % 2 == 0:
                return ''.join(left_half) + ''.join(reversed(left_half))
            else:
                if odd_char == -1 or f[odd_char] == 0:
                    return None
                f[odd_char] -= 1  # use the middle character
                return ''.join(left_half) + chr(97 + odd_char) + ''.join(reversed(left_half))

        def dfs(pos, f, greater):
            if pos == half:
                # All left half positions filled
                if n % 2 == 0:
                    full = ''.join(left_half) + ''.join(reversed(left_half))
                    return full if full > target else None
                else:
                    if odd_char == -1 or f[odd_char] == 0:
                        return None
                    full = ''.join(left_half) + chr(97 + odd_char) + ''.join(reversed(left_half))
                    return full if full > target else None

            if greater:
                # Already greater, fill rest with smallest possible
                return fill_remaining(pos, f)

            # Try to match target[pos]
            # First try the exact character if available
            c_target = ord(target[pos]) - 97
            if f[c_target] >= 2:
                f[c_target] -= 2
                left_half[pos] = chr(97 + c_target)
                res = dfs(pos + 1, f, False)
                if res is not None:
                    return res
                f[c_target] += 2

            # Try larger characters
            for c in range(c_target + 1, 26):
                if f[c] >= 2:
                    f[c] -= 2
                    left_half[pos] = chr(97 + c)
                    # Now we are greater, fill rest minimally
                    res = fill_remaining(pos + 1, f)
                    if res is not None:
                        # Build the full palindrome from the current prefix and filled rest
                        # We need to construct the full string from left_half and remaining
                        # However fill_remaining builds the full palindrome directly.
                        # So we can just return res.
                        return res
                    f[c] += 2
            return None

        ans = dfs(0, freq, False)
        return ans if ans is not None else ""