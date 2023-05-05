# Sort Colors II
# O(nlgk)
# n elements including k kinds of colors
# sort the elements by colors
# return a list in color sequence, such as [1,1,3,5,5,5,6]
# 四根指针，分别是颜色的pivot（由from和to决定，时间复杂度logk）
# list的左右指针负责调换，时间复杂度n

class Solution:
    def sortColors(self, colors, k):
        self.partition(colors, 0, k, 0, len(colors)-1)

    def partition(self, colors, color_from, color_to, index_from, index_to):
        if color_to == color_from or left == right:
            return
        pivot = (color_from+color_to)//2

        left, right = index_from, index_to
        while left <= right:
            while left <= right and colors[left] <= k:
                left += 1
            while left <= right and colors[right] >= k:
                right -= 1
            if left <= right:
                colors[left], colors[right] = colors[right], colors[left]
                left += 1
                right -= 1

        self.partition(colors, color_from, pivot, index_from, left)
        self.partition(colors, pivot, left, index_to)
