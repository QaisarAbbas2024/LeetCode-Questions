class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        changed = False

        for i in range(len(nums) - 1):
            if nums[i] <= nums[i + 1]:
                continue
            if changed:
                return False

            # We want to decrease left element
            # Example: [4, 2, 3]
            if i == 0 or nums[i + 1] >= nums[i - 1]:
                nums[i] = nums[i + 1]
            else:
                nums[i + 1] = nums[i]
            changed = True
        return True    