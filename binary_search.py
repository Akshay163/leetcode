# -*- coding: utf-8 -*-
"""
Created on Thu Feb 10 19:37:05 2022

@author: pandi
"""

def index_search(target, nums):
    first = 0
    index =  round(len(nums)/2)
    last = round(len(nums))-1
    while True:
        diff = last - first
        if nums[index] == target:
            value = index
            break
        elif nums[first] == target:
            value = first
            break
        elif nums[last] == target:
            value = last
            break
        elif target > nums[index] and max(nums) > target and diff > 1:
            first = index
            index = round((index + last)/2)
            print(index)
        elif target < nums[index] and min(nums) < target and diff > 1:
            last  = index
            index = round(index/2)
            print(index)
        else:
            value = -1
            break
    return(value)