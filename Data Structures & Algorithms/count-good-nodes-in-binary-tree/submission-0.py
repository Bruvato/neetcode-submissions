# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0

        if not root.left and not root.right:
            return 1

        self.res = 0

        def dfs(root: TreeNode, maxVal: int):
            if root.val >= maxVal:
                self.res += 1
            
            if root.val > maxVal:
                maxVal = root.val

            if root.left:
                dfs(root.left, maxVal)
            if root.right:
                dfs(root.right, maxVal)
        
        dfs(root, root.val)

        return self.res