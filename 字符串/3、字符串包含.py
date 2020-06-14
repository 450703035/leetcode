# -*- coding: utf-8 -*-
"""
Created on Sun Jun 14 12:18:20 2020

@author: Administrator
"""

## 字符串包含

"""
题目描述：给定一个长字符串a和一个短字符串b，如何快速的判断处字符串b中的所有字符是否都在a中？
例如字符串a是“ABCD”,字符串b是“BAD”，则返回True；如果a是“ABCD”，b是“BCE”则返回False

解法1：蛮力轮询
最简单的思路是轮询字符串b中的每一字符，逐个与字符串a中的每个字符进行比较。看看是否在a中。

解法2:
先将两个字符串排序，然后再轮询。

解法3：素数相乘
a、按照从小到大的顺序，用26个素数分别代替长字符串a中所有的字目
b、遍历长字符串a，求得a中得所有字母对应得素数的乘积
c、遍历短字符串b，判断上一步得到的乘机能否被b中的字母对应的素数整除

解法4：位运算
可以用位运算为长字符串a计算出一个签名，再遍历字符串b在a中查找

"""



class Solution:
    # 解法1
    def stringContain1(self, s1: str, s2: str):
        for c in s2:
            if c not in s1:
                return False
            
        return True

    # 解法2
    def stringContain2(self, s1: str, s2: str):
        # sort s1 s2
        s1="".join((lambda x:(x.sort(),x)[1])(list(s1)))
        s2="".join((lambda x:(x.sort(),x)[1])(list(s2)))
        
        j = 0
        for i, c in enumerate(s2):
            while(j < len(a) and s1[j] < s2[i]):
                j+=1
            if (j>=len(s1) or s1[j] > s2[i]):
                return False
        return True

    # 解法3
    def stringContain3(self, s1: str, s2: str):
        p = [2,3,5, 7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,101]
        
        f = 1
        for c in s1:
            x = p[ord(c) - 65]
            if f%x:
                f *= x
                
        for c in s2:
            x = p[ord(c) - 65]
            if f%x:
                return False
        return True
    
    # 解法4
    def stringContain4(self, s1: str, s2: str):
        hash = 0
        for c in s1:
            hash |= 1 << (ord(c) - 65)
        
        for c in s2:
            if (hash & (1 << (ord(c) - 65)) == 0):
                return False
        
        return True
    
a = "AVBC"
b = "VCD"
ss = Solution()
print('{} {} to {}'.format(a, b, ss.stringContain1(a, b)))
print('{} {} to {}'.format(a, b, ss.stringContain2(a, b))) 
print('{} {} to {}'.format(a, b, ss.stringContain3(a, b))) 
print('{} {} to {}'.format(a, b, ss.stringContain4(a, b))) 