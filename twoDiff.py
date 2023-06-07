# Binary Search + Two Pointers

# given a sorted array, find the two numbers, 
# the differece of which equals the target value
# no extra space
# Input: nums=[2,7,15,24], target = 5
# Output: [2,7]
# Solution: 
# 1.binary search O(nlogn) 
# 2.hash map
def twoSum(self,nums,target):
    if not nums or len(nums)<2:
        return [-1,-1]
    # 特殊情况：target为负时，转换成绝对值
    target = abs(target)
    for i in range(len(nums)):
        # 对于每个i，找到j，使得nums[j]-nums[i] = target
        j=self.binary_search(nums, i+1, len(nums) -1, target + nums[i])
        if j != -1:
            return [nums[i], nums[j]]

def binary_search(self, nums, start, end, target):
    while start+1 < end:
        mid=(start+end)//2
        if nums[mid] < target:
            start=mid
        else:
            end = mid
    if nums[start] == target:
        return start
    if nums[end] == target:
        return end
    
    return -1

# optimization O(n)
# j  只向右不会想左走回头路，因为i在变大
def optimized_twoSum(self,nums,target):
    if not nums:
        return [-1,-1]
    
    target = abs(target)
    j = 1
    for i in range(len(nums)):
        # 防止出现i在j右侧的情况：[0,1,2,2] target=0
        j=max(j,i+1)
        while j < len(nums) and nums[j] - nums[i] < target:
            j += 1
        if j >= len(nums):
            break
        if nums[j] - nums[i] == target:
            return [nums[i], nums[j]]

    return [-1, -1]

