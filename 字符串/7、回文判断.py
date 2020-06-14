# -*- coding: utf-8 -*-
"""
Created on Sun Jun 14 14:01:28 2020

@author: Administrator
"""

"""
题目描述：判断一个字符串是否回文字符串？
给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。
说明：本题中，我们将空字符串定义为有效的回文串。

示例 1:
输入: "A man, a plan, a canal: Panama"
输出: true

来源：力扣（LeetCode）125
链接：[https://leetcode-cn.com/problems/valid-palindrome](https://leetcode-cn.com/problems/valid-palindrome)


解法1：双指针

解法2：从中间往两边扫

"""

class Solution:
    def not_alpha_digit(self, c):
        return not 'A' <= c <= 'Z' and not 'a' <= c <= 'z' and not '0' <= c <= '9'

    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s)-1
        
        if len(s) <= 1:
            return True
        
        while left < right:
            if self.not_alpha_digit(s[left]):
                left+=1
            elif self.not_alpha_digit(s[right]):
                right-=1
            elif s[left].lower() != s[right].lower():
                return False
            else:
                left+=1
                right-=1

        return True

test = "aba"
ss = Solution()
print('{} to {}'.format(test , ss.isPalindrome(test)))  