# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        ptr = [True]
        self.depth(root, ptr)
        return ptr[0]

    # find depth
    def depth(self, root: TreeNode, ptr: List[bool]) -> int:
        # base case
        if root is None or ptr[0] == False:
            return 0

        l = self.depth(root.left, ptr)
        r = self.depth(root.right, ptr)

        if abs(l - r) > 1:
            ptr[0] = False 

        return 1 + max(l, r) 