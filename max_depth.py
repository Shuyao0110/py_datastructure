class Solution:
    def max_depth(self, root):
        self.res = 0
        self.helper(root, 1)
        return self.res
    # 每次调用helper，形成单独的函数执行上下文
    # 相当于每个节点有自己的depth属性，root属性
    # 因为depth不是全局变量，不会一直自增的

    def helper(self,root, depth):
        if root is None:
            return
        # 这句才是真正函数体，如果depth比原来大，就会更新res
        self.res = max(self.res, depth)
        self.helper(root.left, depth+1)
        self.helper(root.right, depth+1)

