# 102. Binary Tree Level Order Traversal
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        queue=[root]
        result=[]
        while queue:
            level=[]
            for _ in range(len(queue)):
                # 此处不能用 for node in queue
                # 因为queue在不断加入新节点，但是此时的len(queue)是确定的
                node=queue.pop(0)
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(level)
        return result

    def levelOrder_2queue(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        queue=[root]
        result=[]
        while queue:
            next_queue=[]
            result.append([node.val for node in queue])
            for node in queue:
                # 此处不能用 for node in queue
                # 因为queue在不断加入新节点，但是此时的len(queue)是确定的
                node=queue.pop(0)
                if node.left:
                    next_queue.append(node.left)
                if node.right:
                    next_queue.append(node.right)
            queue=next_queue
        return result

    def levelOrder_dummyNode(self,root):
        if not root:
            return []
        queue,result,level=[root,None],[],[]
        while queue:
            node=queue.pop(0)
            if node is None:
                result.append(level)
                level=[]
                if queue:
                    queue.append(None)
            level.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return results

# 133. Clone Graph
# Given a reference of a node in a connected undirected graph.
# Return a deep copy (clone) of the graph.
# Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors.

# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

import collections
from collections import deque
class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        if node is None:
            return None
        graph_nodes=self.find_nodes(node)
        nodes_mapping=self.copy_nodes(graph_nodes)
        self.copy_edges(graph_nodes,nodes_mapping)
        return nodes_mapping.get(node)

    # step1: BFS traversal all nodes
    def find_nodes(self,node):
        queue=collections.deque([node])
        # 用集合保存所有点，不重复，不遗漏
        visited=set([node])
        while queue:
            curr_node=queue.popleft()
            # 当前节点的所有邻居入队，入集
            for neighbor in curr_node.neighbors:
                if neighbor in visited:
                    continue
                queue.append(neighbor)
                visited.add(neighbor)
        return list(visited)

    # step2: duplicate all nodes
    def copy_nodes(self,nodes):
        mapping={}
        for node in nodes:
            mapping[node]=Node(node.val)
        return mapping

    # step3: duplicate all links
    def copy_links(self,nodes,mapping):
        for node in nodes:
            new_node=mapping[node]
            for neighbor in node.neighbors:
                new_neighbor=mapping[neighbor]
                new_node.neighbors.append(new_neighbor)

# 127. Word Ladder
# A transformation sequence from word beginWord to word endWord using a dictionary wordList 
# is a sequence of words beginWord -> s1 -> s2 -> ... -> sk such that:
# Every adjacent pair of words differs by a single letter.
# Every si for 1 <= i <= k is in wordList. 
# Note that beginWord does not need to be in wordList.
# sk == endWord
# Given two words, beginWord and endWord, and a dictionary wordList, 
# return the number of words in the shortest transformation sequence 
# from beginWord to endWord, or 0 if no such sequence exists.
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """

# 200. Number of Islands
# Given an m x n 2D binary grid grid 
# which represents a map of '1's (land) and '0's (water), 
# eturn the number of islands.
# An island is surrounded by water 
# and is formed by connecting adjacent lands horizontally or vertically. 
# You may assume all four edges of the grid are all surrounded by water.
from collections import deque
# 四个方向的偏移量
DIRECTIONS=[(1,0),(0,-1),(-1,0),(0,1)]
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid or not grid[0]:
            return 0
        island_num=0
        visited=set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                # 先判断是不是陆地，再判断是否被访问过
                if int(grid[i][j]) and (i,j) not in visited:
                    self.BFS(grid,i,j,visited)
                    island_num+=1
        return island_num

    def BFS(self,grid,x,y,visited):
        queue=deque([(x,y)])
        visited.add((x,y))
        while queue:
            x,y=queue.popleft()
            # 遍历上下左右四个方向
            for delta_x,delta_y in DIRECTIONS:
                next_x=x+delta_x
                next_y=y+delta_y
                if not self.is_valid(grid,next_x,next_y,visited):
                    continue
                queue.append((next_x,next_y))
                visited.add((next_x,next_y))
    
    # 规定遍历坐标范围和是否需要被遍历
    def is_valid(self,grid,x,y,visited):
        n,m=len(grid),len(grid[0])
        # 出界
        if not (0<=x<n and 0<=y<m):
            return False
        # 已经被遍历过的点直接跳过，防止：死循环，冗余的变量
        if (x,y) in visited:
            return False
        # 0，1自动隐式转换为boolean
        return int(grid[x][y])

grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
my_solution=Solution()
my_solution.numIslands(grid)
