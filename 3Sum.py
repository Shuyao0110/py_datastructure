class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        result = []
        for tar in range(len(nums)):
            # target不能和上一个一样，否则会重复
            if tar > 0 and nums[tar] == nums[tar-1]:
                continue
            self.twoSum(nums, tar+1, len(nums)-1, -nums[tar], result)

        return result

    def twoSum(self, nums, left, right, target, result):
        last_pair = None
        while left < right:
            if nums[left]+nums[right] < target:
                left += 1
            elif nums[left]+nums[right] > target:
                right -= 1
            else:
                # 如果满足target，左右指针同时跳，如果只跳一个肯定和原来是不一样的
                # 但是也有可能都和上一组一样
                if (nums[left], nums[right]) != last_pair:
                    result.append([-target, nums[left], nums[right]])
                last_pair = (nums[left], nums[right])
                right -= 1
                left += 1
