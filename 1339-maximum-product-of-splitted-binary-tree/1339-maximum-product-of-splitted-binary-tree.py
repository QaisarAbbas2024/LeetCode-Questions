# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: 'TreeNode') -> int:
        MOD = 1_000_000_007
        self.all_sums = []

        total_sum = self.treeSum(root)

        ans = 0
        for s in self.all_sums:
            ans = max(ans, s * (total_sum - s))

        return ans % MOD

    def treeSum(self, root: 'TreeNode') -> int:
        if not root:
            return 0

        left_sum = self.treeSum(root.left)
        right_sum = self.treeSum(root.right)

        subtree_sum = root.val + left_sum + right_sum
        self.all_sums.append(subtree_sum)

        return subtree_sum
