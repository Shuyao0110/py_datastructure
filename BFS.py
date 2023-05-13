# 分层遍历：clone graph
# 最短路径：word ladder
# 连通块：num of island
# 拓扑排序：course schedule
# 102. Binary Tree Level Order Traversal
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution102(object):
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
class Solution133(object):
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
class Solution127(object):
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
class Solution200(object):
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

# 1197. Minimum Knight Moves
# A knight has 8 possible moves it can make, as illustrated below. 
# Each move is two squares in a cardinal direction, then one square in an orthogonal direction.
# Return the minimum number of steps needed to move the knight 
# to the square [x, y]. It is guaranteed the answer exists.
# In an infinite chess board with coordinates 
# from -infinity to +infinity, you have a knight at square [0, 0].

OFFSETS=[(-2,-1),(-2,1),(-1,2),(1,2),(2,1),(2,-1),(1,-2),(-1,-2)]
from collections import deque
class Solution1197(object):
    def minKnightMoves(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        queue=deque([(0,0)])
        diatance_map={(0,0):0}

        while queue:
            (m,n)=queue.popleft()
            if (m,n)==(x,y):
                return distance_map[(m,n)]
            for dm,dn in OFFSETS:
                next_m,next_n=m+dm,n+dn
                if (next_m,next_n) in distance_map:
                    continue
                queue.append((next_m,next_n))
                distance_map[(next_m,next_n)]=distance_map[(m,n)]+1
        return -1

class Solution:
    def shortestPath(self,grid,start,destination):
        queue=deque([(start.x,start.y)])
        # 去重同时记录路线长度
        distance_map={(start.x,start.y):0}
        
        while queue:
            (x,y)=queue.popleft()
            if (x,y)==(destination.x,destination.y):
                return distance_map=[(x,y)]
            
            for dx,dy in OFFSETS:
                next_x, next_y = x + dx, y + dy
                if not self.is_valid(next_x,next_y,grid):
                    continue
                if (next_x,next_y) in distance_map:
                    continue
                queue.append((next_x,next_y))
                distance[(next_x,next_y)]=distance[(x,y)]+1
                
        return -1
    
    def is_valid(self,x,y,grid):
        n,m=len(grid),len(grid[0])
        if x<0 or x>=n or y<0 or y>=m:
            return False
        return not grid[x][y]


# 210. Course Schedule II
# There are a total of numCourses courses you have to take, 
# labeled from 0 to numCourses - 1. 
# You are given an array prerequisites where prerequisites[i] = [ai, bi] 
# indicates that you must take course bi first if you want to take course ai.
# For example, the pair [0, 1], indicates that to take course 0 
# you have to first take course 1.
# Return the ordering of courses you should take to finish all courses. 
# If there are many valid answers, return any of them. 
# If it is impossible to finish all courses, return an empty array.
# Input: numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
# Output: [0,2,1,3]
class Solution210(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        # 构建图记录课程和指向映进行射
        graph=[[] for i in range[numCourses]]
        # 统计每个点的入度
        # in_degree是一个单独的列表，实时更新入度
        in_degree=[0]*numCourses
        # node_in箭头的头
        # node_out箭头的尾
        for node_in, node_out in prerequisites:
            graph[node_out].append(node_in)
            in_degree[node_in]+=1

        queue=deque()
        # 将入度为0的点放入队列作为起始节点
        for i in range(numCourses):
            if in_degree[i]==0:
                queue.append(i)

        num_choose=0
        topo_order=[]
        
        while queue:
            now_pos=queue.popleft()
            topo_order.append(now_pos)
            num_choose+=1
            for next_pos in graph[now_pos]:
                in_degree[next_pos]-=1
                if in_degree[next_pos]==0:
                    queue.append(next_pos)
        return topo_order if num_choose==numCourses else []

# 269. Alien Dictionary
# There is a new alien language that uses the English alphabet. 
# However, the order among the letters is unknown to you.
# You are given a list of strings words from the alien language's dictionary, 
# where the strings in words are 
# sorted lexicographically by the rules of this new language.
# Return a string of the unique letters in the new alien language sorted 
# in lexicographically increasing order by the new language's rules. 
# If there is no solution, return "". 
# If there are multiple solutions, return any of them.
# Input: words = ["wrt","wrf","er","ett","rftt"]
# Output: "wertf"

from heapq import heappush, heappop, heapify
class Solution(object):
    def alienOrder(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        graph=self.build_graph(words)
        if not graph:
            return ""
        return self.topological_sort(graph)
    
    def build_graph(self,words):
        graph={}
        # 生成所有点
        for word in words:
            for character in words:
                if character not in graph:
                    # 生成这个set可以表示箭头指向，每个set只存放一个衔接的字母
                    graph[character]=set()
        n=len(words)
        # 生成所有边
        for i in range(n-1):
            for j in range(min(len(words[i],len(words[i+1])))):
                if words[i][j]!=words[i+1][j]:
                    graph[words[i][j]].add(words[i+1][j])
                    break
                # 比如"abc"在"ab"之前，不合法 
                if j==min(len(words[i]),len(words[i+1]))-1:
                    if len(words[i])>len(words[i+1]):
                        return None
        return graph

    def topological_sort(self,graph):
        # 统计元素入度
        in_degree=self.get_indegree(graph)
        queue=[node for node in graph if in_degree[node]==0]
        # 堆化后每次取出都是按从小到大的顺序（针对无法得知先后顺循的字母，按地球顺序来）
        heapify(queue)
        topo_order=""
        while queue:
            node=heappop(queue)
            topo_order+=node
            for neighbor in graph[node]:
                in_degree[neighbor]-=1
                if in_degree[neighbor]==0:
                    heappush(queue,neighbor)
        return topo_order if len(topo_order)==len(graph) else ""

    def get_indegree(self,graph):
        in_degree={node:0 for node in praph}
         for node in graph:
            for neighbor in graph[node]:
                in_degree[neighbor]=in_degree[neighbor]+1
        return in_degree