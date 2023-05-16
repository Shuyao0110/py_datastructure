
# 17. Letter Combinations of a Phone Number(全排列)
# Given a string containing digits from 2-9 inclusive, 
# return all possible letter combinations that the number could represent. 
# Return the answer in any order.
# A mapping of digits to letters (just like on the telephone buttons) 
# is given below. Note that 1 does not map to any letters.
# Input: digits = "23"
# Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
KEYBOARD={
    '2':'abc',
    '3':'def',
    '4':'ghi',
    '5':'jkl',
    '6':'mno',
    '7':'pqrs',
    '8':'tuv',
    '9':'wxyz'
}
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits: 
            return []
        combinations=[]
        self.DFS(digits,0,[],combinations)
        return combinations

    def DFS(self,digits,index,combination,combinations):
        if index==len(digits):
            combinations.append(''.join(combination))
            return
        # 遍历同一个digits数字的所有字母，abc，def...
        for letter in KEYBOARD[digits[index]]:
            combination.append(letter)
            self.DFS(digits,index+1,combination,combinations)
            # backtracking,进入上一层的for循环，尝试下一个组合字母
            combination.pop()


# 560. Subarray Sum Equals K
# Given an array of integers nums and an integer k, 
# return the total number of subarrays whose sum equals to k.
# A subarray is a contiguous non-empty sequence of elements within an array.
# Input: nums = [1,1,1], k = 2
# Output: 2
# Input: nums = [1,2,3], k = 3
# Output: 2
class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        subsets=[]
        self.DFS(nums,0,2,K,[],subsets)
        return subsets

    def kSumII(self,A,k,target):
        A.sort()
        subsets=[]
        self.DFS(A,0,k,right_max,[],subsets)
        return subsets
        
    # A原数组
    # index代表树的第几层
    # k代表元素个数
    # target目标值
    # subset局部变量，临时存放当前的组合
    # subsets全局变量，存放总结果
    def DFS(self,A,index,k,target,subset,subsets):
        if k==0 and target==0:
            sebsets.append(list(subset))
            # 如果题目是有正有负，不限制元素个数，就不需要return
            return
        if k==0 or target<=0:
            return
        # 从index到len(A)是为了防止和之前产生重复:组合数
        for i in range(index,len(A)):
            subset.append(A[i])
            self.DFS(A,i+1,k-1,target-A[i],subset,subsets)
            subset.pop()

# 39. Combination Sum
# Given an array of distinct integers candidates and a target integer target, 
# return a list of all unique combinations of candidates 
# where the chosen numbers sum to target. 
# You may return the combinations in any order.
# The same number may be chosen 
# from candidates an unlimited number of times. 
# Two combinations are unique if the 
# frequency of at least one of the chosen numbers is different.
# The test cases are generated such that the number of unique combinations 
# that sum up to target is less than 150 combinations for the given input.
# Input: candidates = [2,3,6,7], target = 7
# Output: [[2,2,3],[7]]
class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        results=[]
        if not candidates:
            return results
        # 去重：减少重复的组合
        # 排序：要求返回值是非降序的
        unique_sorted_nums=sorted(list(set(candidates)))
        self.DFS(unique_sorted_nums,0,[],target,results)
        return results

    def DFS(self,nums,index,current_result,remain_target,results):
        if remain_target==0:
            return results.append(list(current_result))
        for i in range(index,len(nums)):
            if remain_target<nums[i]:
                return
            current_result.append(nums[i])
            # 这里传入index是i而不是i+1，因为下一层的dfs可以重复使用当前位置的数字
            self.DFS(nums,i,current_result,remain_target-nums[i],results)
            current_result.pop()

# [1,2,3]的不同排列
class Sloution:
    def permute(self,nums):
        if nums is None:
            return []
        results=[]
        used=set()
        self.build_permutation()
        return results
    
    def build_permutation(self,nums,used,path,results):
        if len(nums)==len(path):
            # 复制path里的内容append到results后面
            results.append(path[:])
            return
        for i in range(len((nums))):
            if i in used:
                continue
            path.append(nums[i])
            used.add(i)
            self.build_permutation(nums,used,path,results)
            used.remove(i)
            path.pop()
    
# 47. Permutations II
# Given a collection of numbers, nums, that might contain duplicates, 
# return all possible unique permutations in any order.
# Input: nums = [1,1,2]
# Output:
# [[1,1,2],
#  [1,2,1],
#  [2,1,1]]
class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if nums is None:
            return
        nums.sort()
        visited=[False]*len(nums)
        permutations=[]
        self.DFS(nums,visited,[],permutations)
        return permutations

    def DFS(self,nums,visited,permutation,permutations):
        if len(permutation)==len(nums):
            permutations.append(list(permutation))
            return
        for i in range(len(nums)):
            # 同一个位置上的字符不能重复用
            if visited[i]:
                continue
            # 和上一个重复的字符只有上一个被访问才能被用
            if i>0 and nums[i-1]==nums[i] and not visited[i-1]:
                continue
            visited[i]=True
            permutation.append(nums[i])
            self.DFS(nums,visited,permutation,permutations)
            permutation.pop()
            visited[i]=False
    
# 79. Word Search
# Given an m x n grid of characters board and a string word, 
# return true if word exists in the grid.
# The word can be constructed from letters of sequentially adjacent cells, 
# where adjacent cells are horizontally or vertically neighboring. 
# The same letter cell may not be used more than once.
# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], 
# word = "ABCCED"
# Output: true


# 212. Word Search II
# Given an m x n board of characters and a list of strings words, 
# return all words on the board.
# Each word must be constructed from letters of sequentially adjacent cells, 
# where adjacent cells are horizontally or vertically neighboring. 
# The same letter cell may not be used more than once in a word.
DIRECTIONS=[(0,-1),(0,1),(-1,0),(1,0)]
class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        if board is None or len(board)==0:
            return []
        word_set=set(words)
        prefix_set=set()
        for word in words:
            for i in range(len(word)):
                prefix_set.add(word[:i+1])

        result_set=set()

        for i in range(len(board)):
            for j in range(len(board[0])):
                self.search(
                    board,
                    i,
                    j,
                    board[i][j],
                    word_set,
                    prefix_set,
                    set([(i,j)]),
                    result_set,
                )
        return list(result_set)
    
    def search(self,board,x,y,word,word_set,prefix_set,visited,result_set):
        if word not in prefix_set:
            return
        
        if word in word_set:
            result_set.add(word)
        for dx,dy in DIRECTIONS:
            x_=x+dx
            y_=y+dy
            if not self.inside(board,x_,y_) or (x_,y_) in visited:
                continue
            visited.add((x_,y_))
            self.search(
                board,
                x_,
                y_,
                word+board[x_][y_],
                word_set,
                prefix_set,
                visited,
                result_set,
            )
            visited.remove((x_,y_))

    def inside(self,board,x,y):
        return 0<=x<len(board) and 0<=y<len(board[0])