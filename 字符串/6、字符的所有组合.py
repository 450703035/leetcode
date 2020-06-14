# -*- coding: utf-8 -*-
"""
Created on Sun Jun 14 13:55:23 2020

@author: Administrator
"""


"""
题目描述：如果输入"abc"，它的组合有"a"，"b"，"c"，"ab"，"ac"，"bc"，"abc"

解法：
在递去过程中解决问题
function recursion(大规模){
    if (end_condition){      // 剩余最后一个字符
        end;   // 简单情景
    }else{            // 在将问题转换为子问题的每一步，解决该步中剩余部分的问题
        solve;                // 递去
				
        recursion(小规模);     // 递到最深处后，不断地归来
    }
}

"""


class Solution:
    def subset(self, s: str) -> str:
        if len(s) < 1:
            return [[]]
        
        output = list()
        output.append(s)
    
        for i in range(len(s)):
            temp_s = s.copy()
            temp_s.pop(i)
            output.extend(self.subset(temp_s))
        
        results_mod = []

        for i, item in enumerate(output):
            if i == output.index(item):
                results_mod.append(item)
        
        return results_mod
    

test = "abc"
test_c = list(test)
ss = Solution()
print('{} to {}'.format(test_c , ss.subset(test_c)))  