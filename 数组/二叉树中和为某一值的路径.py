# -*- coding: utf-8 -*-
"""
Created on Sat Jun 27 22:25:52 2020

@author: Administrator
"""


"""
题目描述：剑指 Offer 34. 二叉树中和为某一值的路径
输入一棵二叉树和一个整数，打印出二叉树中节点值的和为输入整数的所有路径。
从树的根节点开始往下一直到叶节点所经过的节点形成一条路径。

示例:
给定如下二叉树，以及目标和 sum = 22，

              5
             / \
            4   8
           /   / \
          11  13  4
         /  \    / \
        7    2  5   1
返回:

[
   [5,4,11,2],
   [5,8,4,5]
]

解题方法：

1.DFS + 回溯

#recursive dfs and backtrack
        self.res = []
        def dfs(node,stack,s):
            if not node: return 
            stack.append(node.val)
            if s == node.val and not node.left and not node.right:
                self.res.append(stack.copy())
            dfs(node.left, stack, s-node.val)
            dfs(node.right,stack, s-node.val)
            stack.pop()
        dfs(root,[], sum)
        return self.res
2. DFS 迭代

#itrative DFS
        if not root: return []
        stack = [(root, root.val, [root.val])]
        res = []
        while stack:
            node, val, temp = stack.pop()
            if val == sum and not node.left and not node.right: res.append(temp)
            if node.right:
                stack.append((node.right, val+node.right.val,temp + [node.right.val]))
            if node.left:
                stack.append((node.left, val+node.left.val, temp+[node.left.val]))
        return res
3. BFS 迭代

#itrative BFS
        if not root: return []
        queue = [(root, root.val, [root.val])]
        res = []
        while queue:
            node, val, temp = queue.pop(0)
            if val == sum and not node.left and not node.right: res.append(temp)
            if node.left:
                queue.append((node.left, val + node.left.val, temp+[node.left.val]))
            if node.right:
                queue.append((node.right, val + node.right.val , temp+[node.right.val]))
        return res
"""


# Definition for a binary tree node.

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def pathSum(self, root: TreeNode, sum: int):
        self.res = []
        def dfs(node,stack,s):
            if not node: return 
            stack.append(node.val)
            if s == node.val and not node.left and not node.right:
                self.res.append(stack.copy())
            dfs(node.left, stack, s-node.val)
            dfs(node.right,stack, s-node.val)
            stack.pop()
            
        dfs(root,[], sum)
        return self.res


    
test = TreeNode(5)
test.left = TreeNode(4)
test.left.left = TreeNode(11)
test.left.left.left = TreeNode(7)
test.left.left.right = TreeNode(2)

test.right = TreeNode(8)
test.right.left = TreeNode(13)
test.right.right = TreeNode(4)
test.right.right.left = TreeNode(5)
test.right.right.right = TreeNode(1)

target = 22

ss = Solution()
print('{}'.format(ss.pathSum(test, target))) 