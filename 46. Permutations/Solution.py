class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []  # List to store permutations
        
        def backtrack(path, choices):
            if not choices:  # Base case: all numbers used
                result.append(path[:])  # Store a copy of path
                return
            
            for i in range(len(choices)):  
                path.append(choices[i])  # Pick a number
                backtrack(path, choices[:i] + choices[i+1:])  # Recur without picked number
                path.pop()  # Undo last choice (backtrack)
        
        backtrack([], nums)  # Start with an empty path
        return result
