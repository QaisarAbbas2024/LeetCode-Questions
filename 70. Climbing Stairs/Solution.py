class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        if n == 2:
            return 2

        first, second = 1, 2  # Base cases for n=1 and n=2
        
        for _ in range(3, n + 1):
            third = first + second  # Fibonacci relation
            first, second = second, third  # Move forward
        
        return second
