# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        #each of the nodes in the recursion has a largest_diameter so thats why we make it a list
        largest_diameter = [0]

        def height(node):
            if not node:
                return 0
            
            left_height =height(node.left)
            right_height =height(node.right)

            diamaeter = left_height + right_height
            largest_diameter[0] = max(largest_diameter[0],diamaeter)
            return 1 + max(left_height,right_height)

            
        height(root)
        return largest_diameter[0]
