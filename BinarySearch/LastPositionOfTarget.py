class Solution:
    def lastPositionOfTarget(self, nums, target):
        if nums is None or len(nums) == 0:
            return None

        start, end = 0, len(nums)-1
        while start+1 < end:
            mid = (start+end)/2
            if nums[mid] < target:
                start = mid+1
            elif nums[mid] > target:
                end = mid-1
            else:
                start = mid

        if nums[end] == target:
            return end
        if nums[start] == target:
            return start

        return-1
