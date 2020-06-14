# -*- coding: utf-8 -*-
"""
Created on Sun Jun 14 12:10:06 2020

@author: Administrator
"""

"""
面试题58 - II. 左旋转字符串
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/zuo-xuan-zhuan-zi-fu-chuan-lcof
"""

"""
题目描述：字符串的左旋转操作是把字符串前面的若干个字符转移到字符串的尾部。请定义一个函数
实现字符串左旋转操作的功能。比如，输入字符串"abcdefg"和数字2，该函数将返回左旋转两位得
到的结果"cdefgab"。

解法1：蛮力移位
可能首先想到的方法就是将需要移动的字符一个一个的移动到字符串的尾部。

解法2：反转
我们再想一想有没有简单一点的方法。是不是可以把需要移动的字符和不需要移动的字符分开处理。
例如：字符串“abcdef“需要"abc"移动到字符串的尾部，即移动后为"defabc"。
第一步：先将字符串分为”abc“和”def“两部分。
第二步：将两个字符串反转即为"cba"和"fed"，然后合并为"cbafed"
第三步：将合并后的字符串整个反转即得到"defabc"
"""


class Solution:
    # 解法1
    def reverseLeftWords1(self, s: str, n: int) -> str:
        if n == 0:
            print(s)
            return s
        n -=1
        a = self.reverseLeftWords1(s[1:]+s[0], n)
        return a
    
    # 解法2
    def reserveString(self, s: str) -> str:
        return s[::-1]

    def reverseLeftWords2(self, s: str, n: int) -> str:
        a = self.reserveString(s[:n])
        b = self.reserveString(s[n:])
        s = self.reserveString(a+b)
        return s
        

test = "fabcd"
ss = Solution()
print('{} to {}'.format(test , ss.reverseLeftWords1(test, 3))) 
print('{} to {}'.format(test , ss.reverseLeftWords2(test, 3))) 


