# 120. Triangle
# Given a triangle array, return the minimum path sum from top to bottom.
# For each step, you may move to an adjacent number of the row below. 
# More formally, if you are on index i on the current row, 
# you may move to either index i or index i + 1 on the next row.
# Example 1:
# Input: triangle = [[2],[3,4],[6,5,7],[4,1,8,3]] Output: 11
# Explanation: The triangle looks like:
#    2
#   3 4
#  6 5 7
# 4 1 8 3
# The minimum path sum from top to bottom is 2 + 3 + 5 + 1 = 11 (underlined above).
import sys
class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        self.minimum = sys.maxsize
        self.traverse(triangle,0,0,0)
        return self.minimum

    # 数字三角形：以数组的形式存放
    #遍历法O(2^N)
    def traverse(self,triangle,x,y,path_sum):
        # 到达最底层
        if x == len(triangle):
            self.minimum = min(path_sum,self.minimum)
            return
        # x: 层数; y:当前层的第几位
        # 向下一个
        self.traverse(triangle,x+1,y,path_sum+triangle[x][y])
        # 向下向右一个
        self.traverse(triangle,x+1,y+1,path_sum+triangle[x][y])

    # 分治法O(2^N)
    def minimum(self,triangle):
        return self.divide_conquer(triangle,0,0)

    def divide_conquer(self,triangle,x,y):
        if x== len(triangle):
            return 0

        left = self.devide_conquer(triangle,x+1,y)
        right = self.devide_conquer(triangle,x+1,y+1)
        return min(left,right)+triangle[x][y]
    
    # 记忆化搜索：O(N^2) 
    # Devide & Conquer + HashMap
    def mini(self,triangle):
        return divide_conquer(triangle,0,0,{})
    # 函数返回从x，y触发，走到最底层的最短路径值
    # memo中key为二元组（x，y）
    # memo中value为从x，y走到最底层的最短路径值
    def divide_conquer(self,triangle,x,y,memo):
        if x==len(triangle):
            return 0
        
        if (x,y) in memo:
            return memo[(x,y)]
        
        left = self.divide_conquer(triangle,x+1,y,memo)
        right = self.divide_conquer(triangle,x+1,y+1,memo)

        memo[(x,y)] = min(left,right) + triangle[x][y]
        return memo[(x,y)]
