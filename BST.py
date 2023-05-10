# 230. Kth Smallest Element in a BST
# Given the root of a binary search tree, and an integer k, 
# return the kth smallest value (1-indexed) of all the values of the nodes in the tree.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        stack=[]
        while root is not None:
            stack.append(root)
            root=root.left
        
        for i in range(k-1):
            node=stack.pop()
            if node.right:
                node=node.right
                while node:
                    stack.append(node)
                    node=node.left
        
        return stack[-1].val

# 270. Closest Binary Search Tree Value
# Given the root of a binary search tree and a target value, 
# return the value in the BST that is closest to the target.
# If there are multiple answers, print the smallest.

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def closestValue(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        lowerNode=self.lower_bound(root,target,None)
        upperNode=self.upper_bound(root,target,None)
        if lowerNode and upperNode:
            if target-lowerNode.val>upperNode.val-target:
                return upperNode.val
            return lowerNode.val
        if lowerNode:
            return lowerNode
        return upperNode

    # 越向下层意味着数字的分区间隔越小，越向下越精细，越向上越笼统
    # 所以要尽可能的向下层迭代，目的是找到距离更近的数字
    def lower_bound(self,root,target,lowerNode):
        # 一层一层向下在尽可能大的基础上:root->right->left
        # 找到<target的，直到遇到一个大的，然后返回上一层根节点
        if root is None:
            return lowerNode
        if target<root.val:
            lowerNode=self.lower_bound(root.left,target,lowerNode)
        else:
            lowerNode=self.lower_bound(root.right,target,root)
        return lowerNode

    def upper_bound(self,root,target,upperNode):
        if root is None:
            return upperNode
        if target>root.val:
            upperNode=self.upper_bound(root.right,target,upperNode)
        else:
            upperNode=self.upper_bound(root.left,target,root)
        return upperNode

node5 = TreeNode(5)
node3 = TreeNode(3)
node2 = TreeNode(2)
node1 = TreeNode(1)
node2.left=node1
node2.right=node3
node3.right=node5
my_solution=Solution()
my_solution.closestValue(node2,3.5)