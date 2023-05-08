# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


node5 = TreeNode(5)
node3 = TreeNode(3)
node2 = TreeNode(2, None, node5)
node1 = TreeNode(1, node2, node3)


class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        paths = []
        if not root:
            return paths
        if not root.left and not root.right:
            return [str(root.val)]

        for path in self.binaryTreePaths(root.left):
            paths.append(str(root.val)+'->'+path)
        for path in self.binaryTreePaths(root.right):
            paths.append(str(root.val)+'->'+path)

        return paths


    def findPath(self,node,path,paths):
        if not node:
            return 
        if not node.left and not node.right:
            paths.append('->'.join(str(n.val) for n in path))
            return
        # path是每个节点自带的notebook，遍历到每个节点时把值记录到本上
        path.append(node.left)
        self.findPath(node.left,path,paths)
        path.pop()

        path.append(node.right)
        self.findPath(node.right,path,paths)
        path.pop()

        return paths
path=[]
paths=[]
my_solution = Solution()
my_solution.binaryTreePaths(node1)