# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        visited_p, visited_q = [], []
        p_ptr = q_ptr = root
        self.findVisited(visited_p, p_ptr, p)
        self.findVisited(visited_q, q_ptr, q)

        start = min(len(visited_p), len(visited_q)) - 1
        for i in range(start, -1, -1):
            if visited_p[i] == visited_q[i]:
                return visited_p[i]

        # unreachable 
        return None

    # Traverse tree until target found
    # Create array of visited nodes
    def findVisited(self, visited: List[TreeNode], root: TreeNode, target: TreeNode):
        visited.append(root)

        if target == root or target.val == root.val:
            return
        elif target.val < root.val:
            self.findVisited(visited, root.left, target)
        else:
            self.findVisited(visited, root.right, target)

        