#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
    2017 ICPC at UCSY
    Problem-C: Pixel Virus 
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

    tc.xmax, tc.ymax,tc.s = map(int,tc.infile.readline().split())
    tc.x, tc.y = map(int,tc.infile.readline().split())

    return


class Pixel():
    def __init__(self, number, x, y):
        self.number = number
        self.x = x
        self.y = y
        self.neighbor = [None, None, None, None]
        self.status = False  # Not affected to virus

def solve(tc):
    '''
        Input: Test Case
        Return: None
    '''

    parse_tc(tc)

    pixel_xy = list()

    number = tc.s   # Starting number
    for x in range(tc.xmax+1):
        list_y = list()
        for y in range(tc.ymax+1):
            list_y.append(Pixel(number, x, y))
            number += 1
        pixel_xy.append(list_y)

    for x in range(tc.xmax+1):
        for y in range(tc.ymax+1):
            pixel = pixel_xy[x][y]
            if x > 0:
                pixel.neighbor[0] = pixel_xy[x-1][y]
            if y > 0:
                pixel.neighbor[1] = pixel_xy[x][y-1]
            if y < tc.ymax:
                pixel.neighbor[2] = pixel_xy[x][y+1]
            if x < tc.xmax:
                pixel.neighbor[3] = pixel_xy[x+1][y]
                
    pixel_xy[tc.x][tc.y].status = True  # 1st virus affected Pixel
    virus_list = [pixel_xy[tc.x][tc.y]]
    print(pixel_xy[tc.x][tc.y].number)

    while virus_list:  # while active pixel exists
        new_pixel = list()
        rm_pixel = list()
        for pixel in virus_list:
            for i in range(4):
                if pixel.neighbor[i] and not pixel.neighbor[i].status:
                    #print(pixel.neighbor[i].number, 'is affected')
                    pixel.neighbor[i].status = True
                    new_pixel.append(pixel.neighbor[i])
                    break
            else:
                rm_pixel.append(pixel)
                #print(pixel.number, 'is inactive')

        for pixel in rm_pixel:
            virus_list.remove(pixel)
        
        if new_pixel:
            new_number = list()
            for pixel in new_pixel:
                virus_list.append(pixel)
                new_number.append(pixel.number)

            new_number.sort()
            print(' '.join(map(str,new_number)))

    return


##
##  Main routine
##
if __name__ == '__main__':
    
    tc = TestCase()
    tc.infile = sys.stdin
    tc.t = int(tc.infile.readline())
    
    for i in range(tc.t):
        print('Case ', i+1, ':', sep='')
        solve(tc)

    if tc.infile != sys.stdin:
        tc.infile.close()
