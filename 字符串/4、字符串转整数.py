# -*- coding: utf-8 -*-
"""
Created on Sun Jun 14 13:58:57 2020

@author: Administrator
"""

"""
题目描述：
请你来实现一个 atoi 函数，使其能将字符串转换成整数。

首先，该函数会根据需要丢弃无用的开头空格字符，直到寻找到第一个非空格的字符为止。接下来的转化规则如下：

如果第一个非空字符为正或者负号时，则将该符号与之后面尽可能多的连续数字字符组合起来，形成一个有符号整数。
假如第一个非空字符是数字，则直接将其与之后连续的数字字符组合起来，形成一个整数。
该字符串在有效的整数部分之后也可能会存在多余的字符，那么这些字符可以被忽略，它们对函数不应该造成影响。
注意：假如该字符串中的第一个非空格字符不是一个有效整数字符、字符串为空或字符串仅包含空白字符时，则你的函数不需要进行转换，即无法进行有效转换。

在任何情况下，若函数不能进行有效的转换时，请返回 0 。

提示：

本题中的空白字符只包括空格字符 ' ' 。
假设我们的环境只能存储 32 位大小的有符号整数，那么其数值范围为 [−231, 231 − 1]。如果数值超过这个范围，请返回 INT_MAX (231 − 1) 或 INT_MIN (−231) 。

示例 1:

输入: "42"
输出: 42
示例 2:

输入: " -42"
输出: -42
解释: 第一个非空白字符为 '-', 它是一个负号。 我们尽可能将负号与后面所有连续出现的数字组合起来，最后得到 -42 。

来源：力扣（LeetCode）8题
链接：[https://leetcode-cn.com/problems/string-to-integer-atoi](https://leetcode-cn.com/problems/string-to-integer-atoi)


解法：

"""


class Solution:
    def myAtoi(self, str: str) -> int:
        numdic = {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}
        length = len(str)
        i = 0
        
        #字符为空
        if length <= 0:
            return 0
        
        #去掉空格
        while (str[i] == " "):
            i+=1
            if i>=length:
                return 0
        
        #pdb.set_trace()
        #判断正负
        sign = 1
        if str[i] == '-':
            sign = -1
            i+=1
        elif str[i] == '+':
            sign = 1
            i+=1
        
        # 边界
        boundry = (1<<31)-1 if sign > 0 else 1<<31
        num = 0
    
        #解析
        while (i < length and str[i] in numdic):
            num = num *10 + numdic[str[i]]
            if num > boundry:
                return sign*boundry
            
            i+=1
        return sign*num

test = " -42"        
ss = Solution()
print('{} to {}'.format(test , ss.myAtoi(test)))  