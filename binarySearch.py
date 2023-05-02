# Given an array of integers nums which is sorted in ascending order,
# and an integer target, write a function to search target in nums.
# If target exists, then return its index. Otherwise, return -1.
# You must write an algorithm with O(log n) runtime complexity.
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # recursion
        return self.helper(nums,0,len(nums)-1,target)
        
        def helper(self，nums,start,end,target):
            if start>end:
                return -1
            if nums[start]==target:
                return start
            return self.helper(nums,start+1,len(nums)-1,target)
        
        ####################################################################

        # recursion + binary search
        self.middle = 0
        def helper(nums, start, end, target):
            if start > end:
                self.middle = -1
                return
            #如果（start+end）/2太大，可能会超出范围，这种写法比较周全
            self.middle = start+(end-start)//2
            if nums[self.middle] > target:
                helper(nums, start, self.middle-1, target)
            if nums[self.middle] < target:
                helper(nums, self.middle+1, end, target)
        helper(nums, 0, len(nums)-1, target)
        return self.middle

        ####################################################################
    
        # itertation
        start = 0
        end = len(nums)-1
        # middle=end//2
        # <=：nums长度为1，且有值时，不能返回-1
        while start <= end:
            middle = (start+end)//2
            if nums[middle] == target:
                return middle
            # start和end差1时，会死循环：start一直被等于middle，所以要+1和-1
            if nums[middle] > target:
                end = middle-1
            if nums[middle] < target:
                start = middle+1
        return -1
