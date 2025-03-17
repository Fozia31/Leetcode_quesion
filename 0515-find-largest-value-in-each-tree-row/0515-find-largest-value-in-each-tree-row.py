# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        ans = []
        que = deque([root])
        while que:
            row_max = que[0].val
            len_ = len(que)
            for _ in range(len_):
                poped = que.popleft()
                row_max = max(row_max ,poped.val)
                if poped.left:
                    que.append(poped.left)
                if poped.right:
                    que.append(poped.right)
            
            ans.append(row_max)
        return ans

        