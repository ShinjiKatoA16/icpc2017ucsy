#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
    2017 ICPC at UCSY
    Problem-F: Optimization
'''
import sys


class TestCase():
    pass


def parse_tc(tc):
    '''
        Input: Test Case
        Update: 
        Return: None
    '''

    tc.l, tc.s = map(int,tc.infile.readline().split())

    return


def solve(tc):
    '''
        Input: Test Case
        Return: None
    '''

    parse_tc(tc)

    # At first allocate all resource to chair
    num_chair = min(tc.l, tc.s // 2)
    num_table = 0
    lrg_remain = tc.l - num_chair
    sml_remain = tc.s - (num_chair * 2)

    # if Large and Small block remains, allocate them to table
    if lrg_remain and sml_remain:
        num_table += min(lrg_remain, sml_remain)
        lrg_remain -= num_table
        sml_remain -= num_table

    # then if Large block remains, convert 1 chair to 2 table
    if lrg_remain:
        num_table += min(lrg_remain, num_chair) * 2
        num_chair -= min(lrg_remain, num_chair)

    print(num_table, num_chair)
    return


##
##  Main routine
##
if __name__ == '__main__':
    
    tc = TestCase()
    tc.infile = sys.stdin
    tc.t = int(tc.infile.readline())
    
    for i in range(tc.t):
        solve(tc)

    if tc.infile != sys.stdin:
        tc.infile.close()
