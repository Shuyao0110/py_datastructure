# 264.Ugly number II
# An ugly number is a positive integer whose prime factors are limited to 2, 3, and 5.
# Given an integer n, return the nth ugly number.
# Example 1:
# Input: n = 10 Output: 12
# Explanation: [1, 2, 3, 4, 5, 6, 8, 9, 10, 12] is the sequence of the first 10 ugly numbers.
# time complexity：O(NlogN)加入一个数：O(logN)
# space complexity：O(N)

import heapq

class Solution(object):
    # 最小堆（min heap）+set
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        heap=[1]
        seen = set([1])
        curr_ugly=1
        for _ in range(n):
            curr_ugly = heapq.heappop(heap)
            for factor in [2,3,5]:
                new_ugly = curr_ugly*factor
                if new_ugly not in seen:
                    seen.add(new_ugly)
                    heapq.heappush(heap,new_ugly)
        return curr_ugly
    #动态规划解法
    #O(N)
    def nthUglyNumberDP(self,n):
        dp = [0]* n
        dp[0] = 1
        l2,l3,l5 =0,0,0
        for i in range(1,n):
            dp[i] == min(2*dp[l2], 3*dp[l3],5*dp[l5])
            if dp[i] == 2* dp[l2]:
                l2+=1
            if dp[i] == 3* dp[l3]:
                l3+=1
            if dp[i] == 5* dp[l5]:
                l5+=1
        return dp[n-1]

# 263. Ugly Number
# An ugly number is a positive integer whose prime factors are limited to 2, 3, and 5.
# Given an integer n, return true if n is an ugly number.
# Example 1:
# Input: n = 6 Output: true
# Explanation: 6 = 2 × 3
class Solution(object):
    def isUgly(self, n):
        """
        :type n: int
        :rtype: bool
        """
    if n == 0:
        return False
    for factor in [2,3,5]:
        while n % factor == 0:
            n=n/factor
    return n==1

# 973. K Closest Points to Origin
# Given an array of points where points[i] = [xi, yi] 
# represents a point on the X-Y plane and an integer k, 
# return the k closest points to the origin (0, 0).
# The distance between two points on the X-Y plane is the Euclidean distance 
# (i.e., √(x1 - x2)2 + (y1 - y2)2).
# You may return the answer in any order. 
# The answer is guaranteed to be unique (except for the order that it is in).
# Input: points = [[1,3],[-2,2]], k = 1 Output: [[-2,2]]
# Explanation:
# The distance between (1, 3) and the origin is sqrt(10).
# The distance between (-2, 2) and the origin is sqrt(8).
# Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
# We only want the closest k = 1 points from the origin, so the answer is just [[-2,2]].
class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        self.heap=[]
        for point in points:
            distdance = self.getDistance(point)
            heapq.heappush(self.heap,(distance,point[0],point[1]))
        
        result=[]
        i=0
        while len(self.heap) >0 and i<k:
            _, x, y = heapq.heappop(self.heap)
            result.append([x,y])
            i+=1
        return result
    
    def getDistance(self,point):
        return (point[0])**2+(point[1])**2

# 545.Top k Largest Numbers II
# Implement a adata structure, provide two interfaces:
# add(number).Add a new number in data structure.
# topk().Return the top k largest numbers in this data structure. 
# k is given when we create the data structure.
class Solution:
    """
    @param: k: An integer
    """
    def __init__(self,k):
        #do initialization if necessary
        self.k = k
        self.heap=[]
    """
    @param: num: Number to be added
    @return: nothing
    """
    def add(self,num):
        #write your code here
        heapq.heappush(self.heap,num)
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)
    """
    @return: Top k element
    """
    def topk(self):
        #write your code here
        return sorted(self.heap,reverse=True)