# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode | None) -> list[int]:

        def preorder(root,result):
            if root is None:
                return

            result.append(root.val)
            preorder(root.left,result)
            preorder(root.right,result)

        output = []
        preorder(root,output)
        return output

        