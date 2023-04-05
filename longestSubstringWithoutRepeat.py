class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        long = []
        char_set = []
        if len(s) == 0:
            return 0
        else:
            for l in s:
                if char_set.count(l) is not 0:
                    long.append(len(char_set))
                    # 在循环中修改原数组或字典，则每轮循环都是按更新后的数组来
                    # 比如pop了首位元素，则遍历时每次都是按新数组，进位时会跳过中间一个元素
                    # for char in char_set:
                    #     if char is not l :
                    #         char_set.pop(0)
                    #     else:
                    #         break
                    while char_set[0] is not l:
                        char_set.pop(0)
                    char_set.pop(0)
                char_set.append(l)
            long.append(len(char_set))
            return max(long)


my_solution = Solution()
print(my_solution.lengthOfLongestSubstring("ohvhjdml"))
