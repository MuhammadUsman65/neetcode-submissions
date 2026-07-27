# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        same = [True]
        
        def helper (root1,root2):
            if not root1 and not root2:
                return True

            if (root1 and not root2) or (root2 and not root1):
                same[0] = False
                return
            
            if root1.val == root2.val:
                helper(root1.left,root2.left)
                helper(root1.right,root2.right)
            
            else:
                same[0]=False
                return

        helper(p,q)
        return same[0]
