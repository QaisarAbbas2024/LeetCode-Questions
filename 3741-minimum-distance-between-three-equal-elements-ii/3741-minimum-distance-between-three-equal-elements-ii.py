class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        idx = sorted(range(len(nums)), key=lambda i: nums[i])
        return  int(min(
            (b-a for i in range(len(idx)-2) 
                 if  nums[a:=idx[i]] == nums[b:=idx[i+2]]),
            default=-0.5
        ) *2)
        