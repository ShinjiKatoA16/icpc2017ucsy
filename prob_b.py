#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
    2017 ICPC at UCSY
    Problem-B: Enemy of Enemy
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

    tc.n, tc.m  = map(int,tc.infile.readline().split())
    tc.friend_pair = list()
    tc.enemy_pair = list()
    tc.query = list()

    for i in range(tc.n):
        tc.friend_pair.append(tc.infile.readline().split())

    for i in range(tc.m):
        tc.enemy_pair.append(tc.infile.readline().split())

    while True:
        pair = tc.infile.readline().split()
        if pair == ['*', '*']: break
        tc.query.append(pair)

    return


class Member():
    def __init__(self, name):
        self.name = name
        self.friend_list = [self]
        self.enemy_list = list()
        self.friend_names = list()
        self.enemy_names = list()
    
    def add_friend(self, friend):
        if friend not in self.friend_list:
            self.friend_list.append(friend)
    
    def add_enemy(self, enemy):
        if enemy not in self.enemy_list:
            self.enemy_list.append(enemy)

    def extend_known(self):
        list_size = len(self.friend_list) + len(self.enemy_list)
        for friend in self.friend_list:
            friend.append_friend_list(self.friend_list)
            friend.append_enemy_list(self.enemy_list)

        for enemy in self.enemy_list:
            enemy.append_friend_list(self.enemy_list)
            enemy.append_enemy_list(self.friend_list)

        if list_size != len(self.friend_list) + len(self.enemy_list):
            return True   # List is updated
        else:
            return False  # List is not updated

    def append_friend_list(self, _list):
        for friend in self.friend_list:
            if friend not in _list:
                _list.append(friend)

    def append_enemy_list(self, _list):
        for enemy in self.enemy_list:
            if enemy not in _list:
                _list.append(enemy)


def extend_db(names):
    
    while True:
        db_updated = False
        for member_name in names:
            if names[member_name].extend_known():
                db_updated = True
        if not db_updated:
            break


def create_db(tc):
    names = dict()
    for x in tc.friend_pair:
        p1, p2 = x
        if p1 not in names:
            names[p1] = Member(p1)

        if p2 not in names:
            names[p2] = Member(p2)

        names[p1].add_friend(names[p2])
        names[p2].add_friend(names[p1])

    for x in tc.enemy_pair:
        p1, p2 = x
        if p1 not in names:
            names[p1] = Member(p1)

        if p2 not in names:
            names[p2] = Member(p2)

        names[p1].add_enemy(names[p2])
        names[p2].add_enemy(names[p1])

    extend_db(names)

    # Create Friene/Enemy Name List
    for member_name in names:
        member = names[member_name]
        for p in member.friend_list:
            member.friend_names.append(p.name)
        for p in member.enemy_list:
            member.enemy_names.append(p.name)

    '''
    for member in names:
        print(names[member].name, end = ':')
        for p in names[member].friend_list:
            print(p.name, end = ' ')
        print(':', end = ' ')
        for p in names[member].enemy_list:
            print(p.name, end = ' ')
        print()
    '''

    return names

def solve(tc):
    '''
        Input: Test Case
        Return: None
    '''

    parse_tc(tc)
    names = create_db(tc)

    for query in tc.query:
        p1, p2 = query
        if p1 == p2:
            print('SAME_PERSON')
        elif p1 not in names:
            print('IMPOSSIBLE_TO_TELL')
        elif p2 in names[p1].friend_names:
            print('FRIENDS')
        elif p2 in names[p1].enemy_names:
            print('ENEMIES')
        else:
            print(p1, p2, names[p1].friend_names, names[p1].enemy_names)

    print()

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
