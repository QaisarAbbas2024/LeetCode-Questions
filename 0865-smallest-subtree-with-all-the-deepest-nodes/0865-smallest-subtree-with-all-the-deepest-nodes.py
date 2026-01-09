# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        return self.dfs(root)[0]

    def dfs(self, root):
        # returns (lca, depth)
        if root is None:
            return (None, 0)

        left_lca, left_depth = self.dfs(root.left)
        right_lca, right_depth = self.dfs(root.right)

        if left_depth > right_depth:
            return (left_lca, left_depth + 1)
        if left_depth < right_depth:
            return (right_lca, right_depth + 1)

        return (root, left_depth + 1)
