# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode | None) -> bool:

        left = []
        right = []

        def preorderleft(root,arr):

            if root is None:
                arr.append(None)
                return

            arr.append(root.val)
            preorderleft(root.left,arr)
            preorderleft(root.right,arr)

        def preorderright(root,arr):

            if root is None:
                arr.append(None)
                return

            arr.append(root.val)
            preorderright(root.right,arr)
            preorderright(root.left,arr)


        preorderleft(root.left,left)
        preorderright(root.right,right)

        print(left)
        print(right)

        return left == right




        