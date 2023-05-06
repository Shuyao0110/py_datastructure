# Binary Search in Unsorted Array
class Solution:
    # 先升后降，没有重复数字，呈山峰状，找到最大值
    def mountainSequence(self, nums):
        start, end = 0, len(nums)-1
        while start+1 < end:
            mid = (start+end)/2
            if nums[mid] > nums[mid+1]:
                end = mid
            else:
                start = mid
        return max(nums[start], nums[end])

    # 循环有序数组rotated sorted array
    # 方法一：两轮二分，找到最小值的位置，在子区间再二分
    def find_min_index(self, nums):
        start, end = 0, len(nums)-1
        while start+1 < end:
            mid = (start+end)/2
            if nums[mid] < nums[-1]:
                end = mid
            else:
                start = mid
        if nums[start] < nums[end]:
            return start
        return end

    def binary_search(self, nums, target):
        start, end = 0, len(nums)-1
        while start+1 < end:
            mid = (start+end)/2
            if nums[mid] >= nums[0]:
                start = mid
            else:
                end = mid
        if nums[start] == target:
            return start
        return end

    def search_in_rotated(self, nums, target):
        min_index = self.find_min_index(nums)
        if nums[min_index] <= target <= nums[-1]:
            return self.binary_search(nums[min_index:-2], target)
        return self.binary_search(nums[0:min_index+1], target)

    # 方法二：一轮二分，分类讨论，列出所有可能情况
    def search(self, nums, target):
        start, end = 0, len(nums)-1

        while start+1 < end:
            mid = (start+end)/2
            if nums[mid] >= nums[0]:
                if nums[start] <= target <= nums[mid]:
                    end = mid
                else:
                    start = mid
            else:
                if nums[mid] <= target <= nums[end]:
                    start = mid
                else:
                    end = mid
        if nums[start] == target:
            return start
        if nums[end] == target:
            return end
        return -1

    # 未排序数组找任一波峰,所有元素相邻不相等
    def find_peak(self, nums):
        start, end = 0, len(nums)-2
        while start+1 < end:
            mid = (start+end)/2
            if nums[mid] < nums[mid+1]:
                start = mid
            elif nums[mid] < nums[mid-1]:
                end = mid
            else:
                return mid
        if nums[start] < nums[end]:
            return end
        return start

    # 将一些原木切成k段长为l的小木头，l最长？
    def wood_cut(self, L, k):
        start, end = 1, max(L)
        while start+1 < end:
            mid = (start+end)/2
            if self.pieces(L, mid) < k:
                end = mid
            else:
                start = mid
        if self.pieces(L, end) >= k:
            return end
        if self.pieces(L, start) >= k:
            return start
        return 0

    def pieces(self, L, length):
        result = 0
        for i in range(len(L)):
            result += L[i]/length
        return result
