class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        #  忽略大小写和非法字符后，判断一个字符串是否回文
        left, right = 0, len(s)-1
        while left < right:
            # 异常情况检测：全都是非法字符时，left值会出界，导致s[left]报错
            while left < right and not self.is_valid(s[left]):
                left += 1
            while left < right and not self.is_valid(s[right]):
                right -= 1
            if left < right and s[left].lower() == s[right].lower():
                left += 1
                right -= 1
            else:
                return False
        return True

    def is_valid(self, char):
        return char.isdigit() or char.isalpha()


my_solution = Solution()
print(my_solution.isPalindrome('A man, a canama'))
