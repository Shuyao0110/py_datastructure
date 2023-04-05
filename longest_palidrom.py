class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        # 记录两个指针rp,lp的间隔长度
        # 检查长度是否长于res_len
        # 提取对应位置的字符,并更新到pali上
        # 对于同一个回文中心，包含两种检测：odd偶数；even奇数
        pali=""
        res_len=0
        for i in range(len(s)):
            rp,lp=i,i
            while lp>=0 and rp<len(s) and s[rp]==s[lp]:
                if(rp-lp+1)>res_len:
                    pali=s[lp:rp+1]
                    res_len=rp-lp+1
                rp+=1
                lp-=1
            lp,rp=i,i+1
            while lp>=0 and rp<len(s) and s[rp]==s[lp]:
                if(rp-lp+1)>res_len:
                    pali=s[lp:rp+1]
                    res_len=rp-lp+1
                rp+=1
                lp-=1
        return pali


my_solution=Solution()
print(my_solution.longestPalindrome('babadc'))
                    