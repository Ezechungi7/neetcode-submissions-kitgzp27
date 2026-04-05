# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = 0
        now = 0
        def dfs(root):
            nonlocal res
            nonlocal now
            if not root:
                return
            dfs(root.left)
            now += 1
            print(now)
            if now == k:
                res = root.val
            dfs(root.right)    
            return
        dfs(root)
        return res

        '''
        Works its O(n + k log n) so its O(n)
        l = []
        res = 0
        def dfs(root):
            if not root:
                return
            dfs(root.left)
            dfs(root.right)
            l.append(root.val)
            return
        dfs(root)
        heapq.heapify(l)
        for i in range(k):
            res = heapq.heappop(l)
        return(res)
        '''
        '''
        #Works but its nlogn
        l = []
        def dfs(root):
            if not root:
                return
            dfs(root.left)
            dfs(root.right)
            l.append(root.val)
            return
        dfs(root)
        l.sort()
        return(l[k-1])
        '''