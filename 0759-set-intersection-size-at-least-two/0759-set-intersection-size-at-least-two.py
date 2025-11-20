class Solution:
    def intersectionSizeTwo(self, intervals):
        # Sort by end ascending, start descending
        intervals.sort(key=lambda x: (x[1], -x[0]))

        ans = 0
        mx = -1
        secondMax = -1

        for start, end in intervals:
            # If both numbers already satisfy the interval
            if mx >= start and secondMax >= start:
                continue

            if mx >= start:
                # Only mx satisfies; add one new point
                ans += 1
                secondMax = mx
                mx = end
            else:
                # Need to add two new points
                ans += 2
                mx = end
                secondMax = end - 1

        return ans
