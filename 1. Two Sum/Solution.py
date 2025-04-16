class Solution:
    def twoSum(self, nums, target):
        # This dictionary will store numbers and their indices
        memory = {}

        # Loop through the list using index
        for index in range(len(nums)):
            # Find the number we need to complete the target
            needed = target - nums[index]

            # If the needed number is already in memory, we found a match!
            if needed in memory:
                return [memory[needed], index]

            # Store the current number and its index for future reference
            memory[nums[index]] = index
