# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode | None) -> bool:

        def heightBalanced(root):

            if root is None:
                return 0

            left = heightBalanced(root.left)
            right = heightBalanced(root.right)

            if abs(left - right) > 1:
                return -1

            if left == -1 or right == -1:
                return -1

            return 1 + max(left,right)


        return heightBalanced(root) != -1
        