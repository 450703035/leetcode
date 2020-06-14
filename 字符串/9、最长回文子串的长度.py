# -*- coding: utf-8 -*-
"""
Created on Sun Jun 14 11:10:01 2020

@author: Administrator
"""

"""
题目描述： 给定一个字符串，求它的最长回文子串的的长度

解法1：longestPalindrome1
中心扩展法：我们枚举中心位置，然后在该位置上向两边扩展，记录并更新得到的最长回文串的长度

解法2：longestPalindrome2
Manacher算法：上面的算法需要考虑奇数和偶数的情况，是否有一种不需要考虑奇数和偶数的算法。
例如，我们能否把所有情况都转换为奇数的情况，这就是Manacher算法。
Manacher算法首先在每个字符的两边插入一个特殊的符号，例如"abba"两边插入#号就变成"#a#b#b#a"，
"aba"两边插入#号就变成"#a#b#a"。  

"""

class Solution:
    def longestPalindrome1(self, s: str) -> str:
        n = len(s)
        
        if len(s) <= 1:
            return 0

        max = 0
        
        # 1、枚举中心位置
        for i in range(len(s)):
            j = 0
            # 2、向两边扩展
            #奇数
            while i-j>=0 and i+j<n:
                if s[i-j] != s[i+j]:
                    break
                c = j*2+1
                j+=1
            
            # 3、记录并更新得到的最长回文串的长度
            if c > max:
                max = c
            #偶数
            j = 0
            while i-j>=0 and i+j+1<n:
                if s[i-j] != s[i+j+1]:
                    break
                c = j*2+2
                j+=1
            if c > max:
                max = c
        
        return max
    
    def longestPalindrome2(self, s: str) -> str:
        pass
        
        
test = "abba"
ss = Solution()
print('{} to {}'.format(test , ss.longestPalindrome1(test)))      