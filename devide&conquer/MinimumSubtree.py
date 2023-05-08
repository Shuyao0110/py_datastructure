class Solution:
    # 需要全局变量的版本
    def findSubtree(self, root):
        self.mini_weight = float('inf')
        self.mini_subtree_root = None
        self.getTreeSum(root)
        return self.mini_subtree_root

    def getTreeSum(self, root):
        if root is None:
            return 0
        left_weight = self.getTreeSum(root.left)
        right_weight = self.getTreeSum(root.right)
        root_weight = left_weight+right_weight+root.val

        if root_weight < self.mini_weight:
            self.mini_weight = root_weight
            self.mini_subtree_root = root

        return root_weight

    # def min_sub_tree(self,root):

    # 没有全局变量的版本
    def get_min_sum(self, root):
        if root is None:
            # 正无穷，none，0:分别是用来做比较，传递最小值根节点，传值给父节点用来计算
            return float('int'), None, 0

        left_minimum, left_subtree, left_sum = self.get_min_sum(root.left)
        right_minimum, right_subtree, right_sum = self.get_min_sum(root.right)
        sum_of_root = left_minimum+right_minimum+root.val

        if left_minimum == min(left_minimum, right_minimum, sum_of_root):
            return left_minimum, left_subtree, sum_of_root
        if right_minimum == min(left_minimum, right_minimum, sum_of_root):
            return right_minimum, right_subtree, sum_of_root
        return sum_of_root, root, sum_of_root
