## Brute Force Approach (O(n²))

### 🔧 Code:

```python
class Solution:
    def twoSum(self, nums, target):
        # Try every pair of numbers
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                # Check if the pair sums to target
                if nums[i] + nums[j] == target:
                    return [i, j]
