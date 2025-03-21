# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def calculate(root , sum_):
            if root is None:
                return 0

            sum_ =( sum_ *10) + root.val
            if not root.left and not root.right:
                return sum_

            right = calculate(root.right , sum_)
            left  = calculate(root.left , sum_)
            return left + right
        return calculate(root , 0)

            

            