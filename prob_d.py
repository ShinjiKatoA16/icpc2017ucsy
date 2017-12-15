#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
    2017 ICPC at UCSY
    Problem-D: Primal Encryption 
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
    tc.array = list(map(int,tc.infile.readline().split()))

    return


def solve(tc, prime_list, non_prime_list):
    '''
        Input: Test Case
        Return: None
    '''

    # parse_tc(tc)
    str_in = tc.infile.readline().strip()

    index_p = 0
    index_n = 0
    outlist = list()

    for c in str_in:
        c2 = '00000000' + bin(ord(c))[2:]
        c2 = c2[len(c2)-8:]
        # print(c2)
        for bit in c2:
            if bit == '1':
                outlist.append(prime_list[index_p])
                index_p += 1
            elif bit == '0':
                outlist.append(non_prime_list[index_n])
                index_n += 1
            else:
                raise 'Logic Error'

    print(','.join(map(str,outlist)))

    return

def prep_prime_list():
    MAX_ITEM = 8*20  # 8bit 20 char
    SIEVE_SIZE = 2000

    # create List of Prime, Non prime using Eratosthenes's sieve
    primes = [True for i in range(SIEVE_SIZE)]
    primes[0] = False
    primes[1] = False
    chk_max = int(SIEVE_SIZE ** 0.5)

    for n in range(2, chk_max):
        if primes[n]:
            for index in range(n+n, SIEVE_SIZE, n):
                primes[index] = False

    # create prime_list, non_prime_list from SIEVE
    prime_list = list()
    non_prime_list = list()

    for i in range(2, SIEVE_SIZE):
        if len(prime_list) >= MAX_ITEM and len(non_prime_list) >= MAX_ITEM:
            break
        if primes[i]:
            if len(prime_list) < MAX_ITEM:
                prime_list.append(i)
        else:
            if len(non_prime_list) < MAX_ITEM:
                non_prime_list.append(i)

    # print('List size', len(prime_list), len(non_prime_list), prime_list[-1], non_prime_list[-1])

    return prime_list, non_prime_list


##
##  Main routine
##
if __name__ == '__main__':
    
    tc = TestCase()
    tc.infile = sys.stdin
    tc.t = int(tc.infile.readline())
    
    prime_list, non_prime_list = prep_prime_list()
    # print('Prime List', prime_list)
    # print('Non Prime List', non_prime_list)

    for i in range(tc.t):
        solve(tc, prime_list, non_prime_list)

    if tc.infile != sys.stdin:
        tc.infile.close()
