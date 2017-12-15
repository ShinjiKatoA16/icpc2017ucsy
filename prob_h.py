#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
    2017 ICPC at UCSY
    Problem-H: Sum Square
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

    x = list(map(int,tc.infile.readline().split()))
    tc.dataset = x[0]
    tc.max_num = x[1]
    tc.base = x[2]
    tc.a0 = x[3]

    return


def ssd(b, n):
    val = 0
    while n > 0:
        val += (n % b) ** 2
        n //= b

    # print(b, n, val)
    return val

def prt_list(_list):
    while len(_list) >= 20:
        s = ' '.join(map(str,_list[:20]))
        print(s)
        _list = _list[20:]
    if len(_list):
        s = ' '.join(map(str, _list))
        print(s)
    return

def solve(tc):
    '''
        Input: Test Case
        Return: None
    '''

    parse_tc(tc)

    ak = tc.a0
    ssd_list = [ak]
    for i in range(tc.max_num):
        ssd_val = ssd(tc.base, ak)
        if ssd_val in ssd_list:
            index_k = ssd_list.index(ssd_val)
            print(tc.dataset, len(ssd_list)+1, len(ssd_list)-index_k)
            ssd_list.append(ssd_val)
            prt_list(ssd_list[index_k:])
            break
        ssd_list.append(ssd_val)
        ak = ssd_val
    else:
        print(tc.dataset, tc.max_num, 0)
        print(ak)


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
