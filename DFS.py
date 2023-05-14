
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
        self.DFS(unique_sorted_nums,0,[].target,results)
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