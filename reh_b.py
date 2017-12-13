#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
    2017 ICPC at UCSY
    Rehearsal-B: 
'''
import sys


class TestCase():
    pass


class Conic():
    def __init__(self):
        self.x2_coef = 0
        self.xy_coef = 0
        self.y2_coef = 0
        self.x_coef = 0
        self.y_coef = 0
        self.const = 0
        self.type = None

def fomula2tokens(fomula):

    tokens = list()
    token = ''

    for c in fomula:
        if c in '+-=':
            if token != '':
                tokens.append(token)
                token = ''
        token += c

    # print(tokens)
    return tokens

def coef(token):
    sign = 1   # positive
    digit = ''

    for c in token:
        if c == '-':
            sign = -1
        elif c in 'xy=':
            break
        else:
            digit += c

    if digit == '':
        return sign * 1
    elif digit == '+':
        return 1
    else:
        return sign * int(digit)

def analyze_token(tokens):
    conic = Conic()

    # print('Tokens: ', tokens)
    for token in tokens:
        if 'x^2' in token:
            conic.x2_coef = coef(token)
        elif 'xy' in token:
            conic.xy_coef = coef(token)
        elif 'y^2' in token:
            conic.y2_coef = coef(token)
        elif 'x' in token:
            conic.x_coef = coef(token)
        elif 'y' in token:
            conic.y_coef = coef(token)
        else:
            conic.const = coef(token)

    # print(conic.x2_coef, conic.xy_coef, conic.y2_coef, conic.x_coef, conic.y_coef, conic.const)
    return conic

def parse_tc(tc):
    '''
        Input: Test Case
        Update: 
        Return: None
    '''

    tc.formula = tc.infile.readline().strip()
    tokens = fomula2tokens(tc.formula)
    tc.conic = analyze_token(tokens)

    return


def center(conic):
    x = -conic.x_coef / (conic.x2_coef * 2)
    y = -conic.y_coef / (conic.y2_coef * 2)
    return x, y

def solve(tc):
    '''
        Input: Test Case
        Return: None
    '''

    parse_tc(tc)

    if tc.conic.xy_coef != 0:
        print ('Others')
        return

    if tc.conic.x2_coef == 0 and tc.conic.y2_coef == 0:
        print ('Others')
        return

    shape = tc.conic.x2_coef * tc.conic.y2_coef

    if tc.conic.x2_coef == tc.conic.y2_coef: # Circle
        if tc.conic.x2_coef == 0:
            print('Others')
            return

        x, y = center(tc.conic)
        print('Circle,(', x, ',', y, ')', sep='')

    elif shape > 0: # Ellipse
        x, y = center(tc.conic)
        print('Ellipse,(', x, ',', y, '),', sep='', end='')
        if abs(tc.conic.x2_coef) < abs(tc.conic.y2_coef):
            print('x=', x, sep='')
        else:
            print('y=', y, sep='')

    elif shape < 0: # Hyperbola
        x, y = center(tc.conic)
        const = x*x*tc.conic.x2_coef + y*y*tc.conic.y2_coef + tc.conic.const
        # print(x, y, const)
        print('Hyperbola,(', x, ',', y, '),', sep='', end='')
        if tc.conic.x2_coef * const > 0:
            print('x=', x, sep='')
        else:
            print('y=', y, sep='')

    elif shape == 0: # parabola
        if tc.conic.x2_coef:
            x = -tc.conic.x_coef / (tc.conic.x2_coef * 2)
            const = tc.conic.const - x*x
            y = -const / tc.conic.y_coef
            print('Parabola,(', x, ',', y, '),x=', x, sep='')
        else:
            y = -tc.conic.y_coef / (tc.conic.y2_coef * 2)
            const = tc.conic.const - y*y
            x = -const / tc.conic.x_coef
            print('Parabola,(', x, ',', y, '),y=', y, sep='')

    

    return


##
##  Main routine
##
if __name__ == '__main__':
    
    tc = TestCase()
    tc.infile = sys.stdin
    tc.t = int(tc.infile.readline())
    
    for i in range(tc.t):
        print('Case ', i+1, ':', sep='', end='')
        solve(tc)

    if tc.infile != sys.stdin:
        tc.infile.close()
