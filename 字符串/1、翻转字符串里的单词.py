# -*- coding: utf-8 -*-
"""
Created on Sun Jun 14 12:15:59 2020

@author: Administrator
"""

"""
leetcode 151.翻转字符串里的单词 
给定一个字符串，逐个翻转字符串中的每个单词。

示例 1：

输入: "the sky is blue"
输出: "blue is sky the"

"""

class Solution:
    def reverseWord(self, s: str) -> str:
        return s[::-1]
    def reverseWords(self, s: str) -> str:
        res = ""
        for word in s.split(" "):
            if word == "":
                continue
            print(word)
            if res != "":
                res += " "
            res += self.reverseWord(word)
        print(res)
        return self.reverseWord(res)


test = " I am a student. "
ss = Solution()
print('{} to {}'.format(test , ss.reverseWords(test))) 