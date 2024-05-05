#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May  3 23:24:12 2024

@author: akshay
"""

import string

letters = list(string.printable)


def track_str(strs):
    let_dict = {a: 0 for a in letters}
    for a in strs:
        if a in let_dict.keys():
            let_dict[a] += 1
    return let_dict

def permute_str(str1, str2):
    str1_dict = track_str(str1)
    str2_dict = track_str(str2)

    str1_list = list(str1_dict.values())
    str2_list = list(str2_dict.values())
    
    if str1_list == str2_list:
        return True
    
    return False