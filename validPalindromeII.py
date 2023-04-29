class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # 去掉一个字符后是回文串
        # 1def 找到不同，返回当前索引
        # 2def 判断回文，返回boolean
        # 3找到不同，左or右进一位，是回文串

        if s is None:
            return False

        left, right = self.findDifference(s, 0, len(s)-1)
        if left >= right:
            return True
        return self.isPalindrome(s, left+1, right) or self.isPalindrome(s, left, right-1)

    def isPalindrome(self, s, left, right):
        left, right = self.findDifference(s, left, right)
        return left >= right

    def findDifference(self, s, left, right):
        while left < right:
            if s[left] != s[right]:
                return left, right
            left += 1
            right -= 1
        return left, right
