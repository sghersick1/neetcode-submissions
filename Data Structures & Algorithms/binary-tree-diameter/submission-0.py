# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # Calculate based on left_depth, + right_depth
        # recursively check, only returning the max of left/right
        ptr = [0] 
        self.maxDepth(root, ptr)
        return ptr[0]
            
    # return depth of tree, number of edges
    def maxDepth(self, root: TreeNode, ptr: List[int]) -> int:
        # base case
        if root is None:
            return 0
        
        dLeft = self.maxDepth(root.left, ptr)
        dRight = self.maxDepth(root.right, ptr)

        ptr[0] = max(ptr[0], dRight + dLeft)
        return 1 + max(dLeft, dRight)
