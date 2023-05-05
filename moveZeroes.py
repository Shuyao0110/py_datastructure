class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        slow, fast = 0, 0
        # while fast < len(nums):
        #     if nums[fast] != 0:
        #         nums[slow] = nums[fast]
        #         slow += 1
        #     fast += 1

        # while slow < len(nums):
        #     nums[slow] = 0
        #     slow += 1

        while fas

