#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 17 23:09:49 2022

@author: IsaacTang
"""
def countNegatives( grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        count = 0
        for i in range(m):

            if grid[i][0] < 0:
                count += n 
                continue

            l, r = 0, n-1

            while l<=r:
                
                mid = l+(r-l)//2

                if grid[i][mid] < 0 :
                    r = mid - 1
                else:
                    l = mid+1
            count += n-l 
            print(count)
        return count 
    
list2 = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
b = countNegatives(list2)
b
