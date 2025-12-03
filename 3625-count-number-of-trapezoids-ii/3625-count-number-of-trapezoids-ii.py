import collections

class Solution(object):
    def countTrapezoids(self, points):
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return abs(a) if a != 0 else abs(b)

        lookup_slope = collections.defaultdict(int)
        lookup_line = collections.defaultdict(int)
        lookup_slope_length = collections.defaultdict(int)
        lookup_line_length = collections.defaultdict(int)

        result = 0
        same = 0

        for i in range(len(points)):
            x1, y1 = points[i]
            for j in range(i):  # fixed xrange → range
                x2, y2 = points[j]
                dx, dy = x2 - x1, y2 - y1

                g = gcd(dx, dy)
                if g == 0:  # safeguard for identical points (should not happen)
                    continue
                a, b = dx // g, dy // g

                # normalize slope direction
                if a < 0 or (a == 0 and b < 0):
                    a, b = -a, -b

                # line constant c for (a,b)
                c = b * x1 - a * y1

                # count new trapezoids
                result += lookup_slope[(a, b)] - lookup_line[(a, b, c)]
                lookup_slope[(a, b)] += 1
                lookup_line[(a, b, c)] += 1

                # parallelogram correction (segments of equal length on parallel lines)
                l = dx * dx + dy * dy
                same += lookup_slope_length[(a, b, l)] - lookup_line_length[(a, b, c, l)]
                lookup_slope_length[(a, b, l)] += 1
                lookup_line_length[(a, b, c, l)] += 1

        return result - same // 2
