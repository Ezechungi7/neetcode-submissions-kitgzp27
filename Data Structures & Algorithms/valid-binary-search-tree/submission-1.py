# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node,left,right):
            if not node:
                return True
            if not (left < node.val < right):
                return False
            
            return dfs(node.left,left,node.val) and dfs(node.right, node.val, right)
        return dfs(root, float("-inf"), float("inf"))
        
        '''
        comp = 
        def dfs(root):
            if root is None:
                return True
            if root.left:
                if root.left.val < root.val:
                    dfs(root.left)
                else:
                    raise ValueError()
            if root.right:
                if root.right.val > root.val:
                    dfs(root.right)
                else:
                    raise ValueError()
            
            
            #if root.left.val < root.val and root.right.val > root.val:
                #dfs(root.left)
                #dfs(root.right)
            #else:
                #raise ValueError()
            #return True
        try:
            dfs(root)
        except ValueError:
            return False
        return True
        '''