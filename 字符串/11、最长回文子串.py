# -*- coding: utf-8 -*-
"""
Created on Sun Jun 14 14:39:36 2020

@author: Administrator
"""

"""
题目描述：最长回文子串 leetcode 5
给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。

示例 1：

输入: "babad"
输出: "bab"
注意: "aba" 也是一个有效答案。
示例 2：

输入: "cbbd"
输出: "bb"

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-palindromic-substring
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

"""


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
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        
        if len(s) <= 0:
            return ""

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
                start = i-j+1
                end = i+j
            #偶数
            j = 0
            while i-j>=0 and i+j+1<n:
                if s[i-j] != s[i+j+1]:
                    break
                c = j*2+2
                j+=1
            if c > max:
                max = c
                start = i-j+1
                end = i+j+1
        
        
        return s[start:end]
        
test = "abba"
ss = Solution()
print('{} to {}'.format(test , ss.longestPalindrome(test)))      
