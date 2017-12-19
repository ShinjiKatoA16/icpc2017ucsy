#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
    2017 ICPC at UCSY
    Problem-A: Proper Binary Tree
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

    tc.n = int(tc.infile.readline())

    return

cmap = dict()
cmap[0] = ['o--|__', 'o--|']


MAX_T = 13
def create_cmap():
    for i in range(1, MAX_T):
        cmap[i] = cmap[i-1][:] + cmap[i-1][:]
        y_pos = 2**(i-1)
        x_pos = 6 + 3*(i-1)

        num_row = len(cmap[i])
        for row in range(num_row):
            if row >= y_pos and row < len(cmap[i]) - y_pos:
                cmap[i][row] += (' '*(x_pos - len(cmap[i][row])))
                cmap[i][row] += '|'
        cmap[i][num_row // 2 - 1] += '__'

        '''
        for row in range(num_row):
            print(cmap[i][row])
        print()
        '''


def solve(tc):
    '''
        Input: Test Case
        Return: None
    '''

    parse_tc(tc)

    for line in cmap[tc.n-1]:
        print(line)

    return


##
##  Main routine
##
if __name__ == '__main__':
    
    tc = TestCase()
    tc.infile = sys.stdin
    tc.t = int(tc.infile.readline())
    create_cmap()
    
    for i in range(tc.t):
        print('Case ', i+1, ':', sep='')
        solve(tc)

    if tc.infile != sys.stdin:
        tc.infile.close()
