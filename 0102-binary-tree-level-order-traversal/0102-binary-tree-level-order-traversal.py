# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode | None) -> list[list[int]]:
        queue = deque()
        output = []

        if root is None:
            return output

        queue.append(root)
        while queue:

            n = len(queue)
            sublist = []

            for i in range(n):

                node = queue.popleft()

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

                sublist.append(node.val)

            
            output.append(sublist)

        return output
        