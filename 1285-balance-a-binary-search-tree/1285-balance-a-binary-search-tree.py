# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        list_num = []
        def inorder(root):
            if root is None:
                return []

            left = inorder(root.left)
            list_num.append(root.val)
            right = inorder(root.right)
    
            return list_num
        print (inorder(root))

        def balancer(list_num):
            if len(list_num) == 0:
                return None

            mid = len(list_num) // 2
            root = TreeNode(list_num[mid])

            root.left = balancer(list_num[ : mid])
            root.right = balancer(list_num[mid + 1 : ])

            return root
        return balancer(list_num)
