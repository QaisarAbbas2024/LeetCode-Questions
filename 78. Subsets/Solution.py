class Solution:
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []  # To store all subsets
        
        def backtrack(start, path):
            """
            start: The index from where we pick elements
            path: The current subset being built
            """
            result.append(path[:])  # Add a copy of path to result
            
            for i in range(start, len(nums)):  
                path.append(nums[i])  # Include nums[i] in subset
                backtrack(i + 1, path)  # Move to the next element
                path.pop()  # Undo (Backtrack) to try other possibilities

        backtrack(0, [])  # Start with an empty subset
        return result
