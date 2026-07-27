# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def sameTree(root,subRoot):
            if not root and not subRoot:
                return True

            if (root and not subRoot) or (subRoot and not root):
                return False

            if root.val != subRoot.val:
                return False

            return sameTree(root.left,subRoot.left) and sameTree(root.right,subRoot.right)

        def has_subTree(root):
            if not root:
                return False

            if sameTree(root,subRoot):
                return True

            return has_subTree(root.left) or has_subTree(root.right)

        return has_subTree(root)

            
        