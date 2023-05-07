# Given an array nums with n objects colored red, white, or blue,
# sort them in-place so that objects of the same color are adjacent,
# with the colors in the order red, white, and blue.

# We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

# You must solve this problem without using the library's sort function.
class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # nums = self.partition(nums, 0)
        # return self.partition(nums, 1)

    def partition(self, nums, pivot):
        left, right = 0, len(nums)-1
        while left <= right:
            while left <= right and nums[left] <= pivot:
                left += 1
            while left <= right and nums[right] > pivot:
                right -= 1
            if left <= right:
                nums[right], nums[left] = nums[left], nums[right]
                left += 1
                right -= 1
        return nums

    # 三根指针扫描，index，left，right
    # 小于1，给left；大于1，给right
    def sortColors(self, nums):
        left, index, right = 0, 0, len(nums)-1
        while index <= right:
            if nums[index] == 0:
                nums[left], nums[index] = nums[index], nums[left]
                index += 1
                left += 1
            elif nums[index] == 2:
                nums[index], nums[right] = nums[right], nums[index]
                index += 1
                right -= 1
            else:
                index += 1

    # count sort放入字典然后再写出来
    def sortColor(self, nums):
        colors = {0: 0, 1: 0, 2: 0}
        for index in nums:
            colors[index] += 1
        result = []
        self.print_color(0, colors[0], result)
        self.print_color(1, colors[1], result)
        self.print_color(2, colors[2], result)

    def print_color(self, num1, num2, result):
        for i in range(num2+1):
            result.append(num1)
