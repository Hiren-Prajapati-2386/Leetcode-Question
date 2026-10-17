# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode | None) -> list[list[int]]:

        if not root:
            return []

        result = []
        flag = 0

        queue = deque()
        queue.append(root)

        while queue:

            level = []
            
            for _ in range(len(queue)):
                node = queue.popleft()
                level.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            
            if flag == 0:
                result.append(level)
                flag = 1
            else:
                result.append(level[::-1])
                flag = 0

        return result

        