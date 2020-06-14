# -*- coding: utf-8 -*-
"""
Created on Sun Jun 14 13:43:53 2020

@author: Administrator
"""

"""
题目描述：字符串全排列
输入一个字符串，打印出该字符串的所有排列，例如输入“abc”，则输出由字符“a”，“b”，“c”能排列
的所有字符串“abc”，“acb”，“bca”，“bac”，“cab”，“cba”

解法1：递归


解法2：字典序排列
算法起点：字典序最小的排列1-n；如“12345”
算法终点：字段序最大的排列n-1；如"54321"

- a、找到排列中最后一个升序的首位位置i, x=ai
- b、找到排列中第i位右边最后一个比ai大的位置j，y=aj
- c、交换x和y
- d、把第i+1位和最后的部分翻转，

例如：

21543举例，过程为：

- x=1
- y=3
- 1和3交换，得到23541
- 翻转541，得到23145

23145即为21543的下一个排列

"""

class Solution:
    # 解法1
    def permute1(self, s: str) -> str:
        return self.return_permute1(s, 0)
    def return_permute1(self, s: str, index: int) -> str:    
        # end condition
        if index >= len(s):
            return [""]
        
        s_output = self.return_permute1(s, index+1)
        current = s[index]
        output = list()
        for per_output in s_output:
            for i in range(len(per_output)+1):
                output.append(per_output[0:i] + current + per_output[i:])

        return output

    def permute2(self, s: str, i: int) -> str:
        # end condition
        if len(s) == i:
            print(s)
        for j in range(i,len(s)):
            s[j],s[i] = s[i],s[j]
            self.permute2(s, i+1)
            s[j],s[i] = s[i],s[j]

    # 解法2
    def permute3(self, s: str) -> str:
        print(s)
        while(self.return_permute(s)):
            print(s)
            continue
    
    def return_permute(self, s: str):
        #步骤1 找到排列中最后一个升序的首位位置i
        for i in range(len(s)-1,-1,-1):
            if i < 1:
                return False
            
            if ord(s[i]) > ord(s[i-1]):
                i-=1
                #print(i)
                break
        
        #步骤2 找到排列中第i位右边最后一个比ai大的位置j
        for j in range(len(s)-1,-1,-1):
            if ord(s[j]) > ord(s[i]):
                #print(j)
                break
            
        #步骤3 交换x和y
        s[i], s[j] = s[j], s[i]
               
        #步骤4 把第i+1位到最后的部分翻转
        s[i+1:] = s[:i:-1]
 
        return True

test = "abc"
test1 = list(test)
ss = Solution()
re = ss.permute1(test1) 
ss.permute2(test1, 0)
ss.permute3(test1) 