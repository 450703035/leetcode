# -*- coding: utf-8 -*-
"""
Created on Mon Jun 15 20:36:12 2020

@author: Administrator
"""

"""
题目描述：有n个整数，请找出其中最小的k个数，要求时间复杂度尽可能低

解法1：全部排序
快速排序的算法复杂度是O(nlog(n))，输出前k个数的复杂度是O(k)，所以整体的时间复杂度是
O(nlogn)+O(k)=O(nlogn)

解法2：部分排序
题目只要求最小的k个数有序，因此我们只需要对部分元素进行排序。
时间复杂度是O(nk)

解法3：堆
和解法2类似

解法4：线性选择算法
1、选取数组中的一个元素作为主元privot，然后将数组分为Sa和Sb，像快速排序那样。
2、如果k = privot_index，则找到，直接返回
3、否则，就在Sb中，

"""

class Solution:
    # 快速排序
    def sort_a_little_bit(self, itmes, begin_index, end_index):
        left_index = begin_index
        pivot_index  = end_index
        pivot_value = itmes[pivot_index]

        while (pivot_index != left_index):
            item = itmes[left_index]

            if item <= pivot_value:
                left_index += 1
                continue

            itmes[left_index] = itmes[pivot_index - 1]
            itmes[pivot_index - 1] = pivot_value
            itmes[pivot_index] = item
            pivot_index -= 1

        return pivot_index

    def sort_all(self, items, begin_index, end_index):
        if end_index <= begin_index:
            return

        pivot_index = self.sort_a_little_bit(items, begin_index, end_index)
        self.sort_all(items, begin_index, pivot_index - 1)
        self.sort_all(items, pivot_index + 1, end_index)

    def quicksort(self, items):
        self.sort_all(items, 0, len(items) - 1)
    
    
    def getLeastNumbers1(self, arr: list, k: int) -> list:
        self.quicksort(arr)
        return arr[:k]
        
    def getLeastNumbers2(self, arr: list, k: int) -> list:
        for iteration in range(k):
            min = iteration
            for index in range(iteration+1 ,len(arr)):
                if arr[min] > arr[index]:
                    min = index
            
            temp = arr[min]
            arr[min] = arr[iteration]
            arr[iteration] = temp
        
        return arr[:k]
    
    def getLeastNumbers4(self, arr: list, k: int) -> list:
        if k <= 0:
            return []
        if k >= len(arr):
            self.sort_all(arr, 0, k-1)
            return arr
            
        index = self.sort_a_little_bit(arr, 0, len(arr)-1)
        
        while(1):
            #print(arr)
            if index == k-1:
                self.sort_all(arr, 0, k)
                return arr[:k]
            elif index > k-1:
                index = self.sort_a_little_bit(arr, 0, index-1)
            elif index < k-1:
                index = self.sort_a_little_bit(arr, index+1, k)
            
        
test = [0,1,2,3,4,0,3,3,8,1,4,6,2,8,8,15,10,0,9,9,1,2,17,8,17,25,18,18,16,13,18,29,2,3,32,2,26,23,18,8,34,8,11,36,36,39,46,30,21,25,21,14,41,10,31,55,45,16,33,47,4,52,59,60,1,43,42,10,12,56,12,27,22,52,38,12,41,42,71,5,42,76,8,3,31,65,11,29,28,68,33,50,73,87,22,68,31,1,38,89]
#test = [0,0,2,3,2,1,1,2,0,4]  
#test = [0,1,0,3,2,7,0,2,1,0,8,5,2]
ss = Solution()
re = ss.getLeastNumbers4(test, 60)