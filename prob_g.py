#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
    2017 ICPC at UCSY
    Problem-G: Stone
'''
import sys
#from heapq import heappush, heapify


class TestCase():
    pass


class Node():
    def __init__(self, stones, cost):
        self.stones = stones[:]
        self.cost = cost

    def append_stone(self, stone):
        self.stones.append(stone)

    def dup_node(self):
        new_nd = Node(self.stones, self.cost)
        return new_nd

    def __str__(self):
        return '<cost:{} stones:{}'.format(self.cost, self.stones)

    def __lt__(self, other):
        if self.cost == other.cost:
            return self.stones[-1] < other.stones[-1]
        else:
            return self.cost < other.cost

def parse_tc(tc):
    '''
        Input: Test Case
        Update: 
        Return: None
    '''

    tc.n = int(tc.infile.readline())
    tc.stone = list(map(int,tc.infile.readline().split()))

    return

def clean_up(nodes):
    '''
        Input: List of Node class object
        Return: List of Node class object
    '''

    node_s = [(n.stones[-1], n.cost, nodes.index(n)) for n in nodes]
    node_s.sort()  # sort by Last stone value+Cost
    #print('Nodes sorted status', node_s)

    remove_list = list()
    prev_ls = None   # Last stone(stones[-1]) of previous node
    for ns in node_s:
        node_x = nodes[ns[2]]
        if ns[0] == prev_ls:
            #print('Index', ns[2], node_x.stones, node_x.cost, 'will be removed')
            remove_list.append(node_x)
        prev_ls = ns[0]
        
    for nx in remove_list:
        nodes.remove(nx)

    return nodes


def update_nodes(nodes, st):
    '''
        Input: Node class object
               Integer
        Return: Node class object
    '''
    new_list = []
    stone_added = list()

    for nd in nodes:
        if st == nd.stones[-1]:
            nd.append_stone(st)
            #heappush(new_list, nd)
            new_list.append(nd)
            if st not in stone_added:
                stone_added.append(st)
        elif st < nd.stones[-1]:
            nd.cost += st
            new_list.append(nd)
        else:  # st > nd.stone[-1]
            if st not in stone_added:
                #print('New node created', st, nd.stones[-1])
                new_nd = nd.dup_node()
                new_nd.append_stone(st)
                stone_added.append(st)
                new_list.append(new_nd)

            nd.cost += st
            new_list.append(nd)


    new_list.sort()
    #print('Node is updated with', st)
    #for nd in new_list:
    #    print(nd)
    return new_list
    #return new_list


def lowest_cost(nodes):
    l_cost = nodes[0].cost
    for n in nodes:
        if n.cost < l_cost:
            l_cost = n.cost
    return l_cost


def solve(tc):
    '''
        Input: Test Case
        Return: None
    '''

    parse_tc(tc)
    nodes = [Node([0], 0)]

    for st in tc.stone:
        nodes = update_nodes(nodes, st)
        
    removed_weight = lowest_cost(nodes)
    print(removed_weight)
    return


##
##  Main routine
##
if __name__ == '__main__':
    
    tc = TestCase()
    tc.infile = sys.stdin
    tc.t = int(tc.infile.readline())
    
    for i in range(tc.t):
        print('Case ', i+1, ': ', sep='', end='')
        solve(tc)

    if tc.infile != sys.stdin:
        tc.infile.close()
