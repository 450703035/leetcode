# -*- coding: utf-8 -*-
"""
Created on Sun Jun 14 14:35:55 2020

@author: Administrator
"""

"""
题目描述：回文子串 leetcode 647
给定一个字符串，你的任务是计算这个字符串中有多少个回文子串。

具有不同开始位置或结束位置的子串，即使是由相同的字符组成，也会被计为是不同的子串。

示例 1:

输入: "abc"
输出: 3
解释: 三个回文子串: "a", "b", "c".
示例 2:

输入: "aaa"
输出: 6
说明: 6个回文子串: "a", "a", "a", "aa", "aa", "aaa".
"""

class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        cnt = 0
        
        if len(s) < 1:
            return 0

        for i in range(len(s)):
            print(i)
            j = 0
            #奇数
            while i-j>=0 and i+j<n:
                if s[i-j] != s[i+j]:
                    break
                cnt+=1
                j+=1
 
            #偶数
            j = 0
            while i-j>=0 and i+j+1<n:
                if s[i-j] != s[i+j+1]:
                    break
                j+=1
                cnt+=1

        return cnt
    
    
test = "abba"
ss = Solution()
print('{} to {}'.format(test , ss.countSubstrings(test)))   