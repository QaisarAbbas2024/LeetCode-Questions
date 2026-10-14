class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        if sum > num * 9:
            return ""

        res = []

        while num > 0:
            if sum >= 9:
                res.append('9')
                sum -= 9
            elif sum == 0:
                res.append('0')
            else:
                res.append(str(sum))
                sum = 0

            num -= 1

        return ''.join(res)