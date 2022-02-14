# -*- coding: utf-8 -*-
"""
Created on Sat Feb 12 01:18:49 2022

@author: pandi
"""

import math
class Solution:
    def firstBadVersion(self, n: int) -> int:
        last = n
        first = 1
        diff = last - first
        if first == last:
            return(last)
        elif isBadVersion(last) and not isBadVersion(last-1):
            return(last)
        elif isBadVersion(last) and isBadVersion(last-1) and diff == 1:
            return(last-1)
        else:
            while True:
                diff = last - first
                if isBadVersion(first):
                    last = first
                    break
                elif isBadVersion(last) and not isBadVersion(last-1):
                    first = last
                    break
                elif isBadVersion(last) and isBadVersion(last-1) and diff == 1:
                    last = last - 1
                    break
                if  not isBadVersion(first) and diff == 2:
                    break
                elif isBadVersion(math.ceil((last + first)/2)) and diff != 2:
                    last = math.ceil((last + first)/2)
                else:
                    first = math.ceil((last + first)/2)
            return(math.ceil((last + first)/2))