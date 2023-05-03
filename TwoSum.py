class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        #创建字典
        dic_nums={}
        for i in range (len(nums)):
            dic_nums[nums[i]]=i
        for j in range (len(nums)):
            res=target-nums[j]
            if dic_nums.get(res):
                #排除这个元素本身
                if dic_nums[res]==j:
                    continue
                return [j,dic_nums[res]]
        
        #哈希表法
        harshset=set()
        for num in nums:
            if target-num in harshset:
                return num, target-num
            harshset.add(num)
        return None

        #双指针法：先给数组排序提高效率
        if nums is None:
            return None
        # enumerate给liest内的元素加上索引
        new_nums = []
        for index, num in enumerate(nums):
            new_nums.append((num, index))
        new_nums.sort()
        # tuple比较大小时按第一位，所以把num放在前
        left, right = 0, len(new_nums)-1
        while left < right:
            if new_nums[left][0]+new_nums[right][0] > target:
                right -= 1
            elif new_nums[left][0]+new_nums[right][0] < target:
                left += 1
            else:
                # 把返回的索引排序，防止顺序错误
                # sort()只能传入一个list，要把索引放入一个数组再排序
                return sorted([new_nums[left][1], new_nums[right][1]])
        return None


my_solution = Solution()
print(my_solution.twoSum([2, 7, 11, 15], 9))
