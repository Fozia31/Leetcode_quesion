# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if not root:
            return []

        result = []
        queue = deque([root]) 
        left = True  

        while queue:
            size = len(queue)
            level_nodes = deque()  

            for _ in range(size):
                node = queue.popleft()  
                
                if left:
                    level_nodes.append(node.val)  
                else:
                    level_nodes.appendleft(node.val)  

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            result.append(list(level_nodes))
            left = not left 
        return result
