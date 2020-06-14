# -*- coding: utf-8 -*-
"""
Created on Sun Jun 14 14:06:10 2020

@author: Administrator
"""

"""
题目描述：链表回文 leetcode 234

[https://leetcode-cn.com/problems/palindrome-linked-list/](https://leetcode-cn.com/problems/palindrome-linked-list/)

请判断一个链表是否为回文链表。
**示例 1:**

```
输入: 1->2
输出: false
```

**示例 2:**

```
输入: 1->2->2->1
输出: true
```

"""

# Definition for singly-linked list.
class ListNode:
     def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:        
        fast = head
        slow = head
        prev = None
        flag = True
        
        while (fast and fast.next):
            fast = fast.next.next
            slow.next = prev
            prev = slow
            slow = slow.next
            
        if fast:
            node1 = fast
            node2 = slow.next
        else:
            node1 = fast
            node2 = slow
            
        while(node1 and node2):
            if node1.val != node2.val:
                flag = False
            node1, node2 = node1.next, node2.next
            
        back = slow
        while(prev):
            temp = prev.next
            prev.next = back
            back = prev
            prev = temp
        return flag
  