#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May  3 23:24:12 2024

@author: akshay
"""

import string

'''
This is the case when we are allowed to use additional Data Structures (Like Hash tables: dict in python)
'''

def is_unique(strs):
    
    letters = list(string.printable)
    
    let_dict = {a:0 for a in letters}
    
    for a in strs:
        if a in let_dict.keys():
            let_dict[a] += 1
            if let_dict[a] > 1:
                return False
    return True

'''
This is the case when we are NOT allowed to use additional Data Structures (Like Hash tables: dict in python)
'''

def is_unique_noht(strs):
    sort_strs = sorted(strs)
    for i in range(1, len(sort_strs)):
        if sort_strs[i - 1] == sort_strs[i]:
            return False
    return True
