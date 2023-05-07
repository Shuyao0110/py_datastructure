class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        # 双指针
        
        # 中心点枚举法
        # 背向型 O(n^2)
        # 对于同一个回文中心，包含两种检测：odd偶数；even奇数
        pali=""
        res_len=0
        # 记录长度
        for i in range(len(s)):

            # even number length
            rp,lp=i,i
            while lp>=0 and rp<len(s) and s[rp]==s[lp]:
                if(rp-lp+1)>res_len:
                    pali=s[lp:rp+1]
                    res_len=rp-lp+1
                rp+=1
                lp-=1

            # odd number length
            lp,rp=i,i+1
            while lp>=0 and rp<len(s) and s[rp]==s[lp]:
                if(rp-lp+1)>res_len:
                    pali=s[lp:rp+1]
                    res_len=rp-lp+1
                rp+=1
                lp-=1
        return pali
    
    # 中心点枚举法优化
    # 奇数和偶数有重复的代码，提取公共部分，抽象成get_palindrome_from方法
    def longestPalinAgainst(self,s):
        if not s:
            return s
        # tuple相比于list，它的空间每次更新不会被os回收再创建
        # 内存里的静态资源会被一直保留，便于每次更新
        # tuple比较大小，按位比较，先看第一位，然后再按顺序向后，返回值还是tuple
        answer=(0,0)
        for mid in range(len(s)):
            answer=max(answer,self.get_palidrome_from(s,mid,mid))
            answer=max(answer,self.get_palidrome_from(s,mid,mid+1))


    def get_palidrome_from(self,s,left,right):
        while left>=0 and right<len(s) and s[left]==s[right]:
            left-=1
            right+=1
        # 多走了一位
        return right-left-1,left+1
        # 返回值为两个数字，默认以tuple的形式存储

    # 双层循环法 O(n^3)
    # 以下是错误版本：双指针不能记录长度
    def longestPalindromeFace(self,s):
        if not s:
            return None
        
        for right_pointer in range(len(s)-1,-1,-1):
            for left_pointer in range(0,right_pointer):
                if self.is_palindrome(s,left_pointer,right_pointer):
                    return s[left_pointer:right_pointer+1]
                else:
                    continue
        return s[0]
    
    # 以下是正确版本：
    # 因为要找最长的，所以用长度递减，然后检测是否满足回文序列
    def PalindromeFace(self,s):
        if not s :
            return None
        
        for length in range(len(s),0,-1):
            for start in range(len(s)-length+1):
                if self.is_palindrome(s,start,start+length-1):
                    return s[start,start+length]
        return s[0]

    def is_palindrome(self,s, left,right):
        while left<right and s[left]==s[right]:
            left+=1
            right-=1
        return left>=right


my_solution=Solution()
print(my_solution.longestPalindromeFace('a'))
                    