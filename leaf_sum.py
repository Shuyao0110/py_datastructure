class Solution:
    # self.可以变成类的属性，在此类中都可以用res
    def leaf_sum(self,root):
        self.res=0
        self.helper(root)
        return self.res

    def helper(self,root):
        if root is None:
            return
        # 压栈时判断是否是叶子结点并更新res值
        if root.left is None and root.right is None:
            self.res+=root.val
        self.helper(root.left)
        self.helper(root.right)

        