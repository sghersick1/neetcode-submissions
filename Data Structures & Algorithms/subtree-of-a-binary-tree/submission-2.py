# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # 1. Scale tree to find where a node matches root of subroot
        if subRoot is None:
            return True
            
        def dfs(dRoot):
            if dRoot is None:
                return False
            elif dRoot.val == subRoot.val:
                # check subtree match
                valid = self.checkSubtree(dRoot, subRoot)
                if valid: return True

            return dfs(dRoot.left) or dfs(dRoot.right)

        return dfs(root)

    def checkSubtree(self, root: TreeNode, subRoot: TreeNode):
        if root is None and subRoot is None:
            return True
        elif root is None or subRoot is None:
            return False
        elif root.val != subRoot.val:
            return False
            
        return self.checkSubtree(root.right, subRoot.right) and self.checkSubtree(root.left, subRoot.left)