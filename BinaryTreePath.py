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


my_solution = Solution()
my_solution.binaryTreePaths(node1)
