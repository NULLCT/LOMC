from collections import Counter, defaultdict
import sys
import bisect
# sys.setrecursionlimit(10 ** 5 + 10)
# input = sys.stdin.readline
from math import factorial
import heapq, bisect
import math
import itertools
from copy import deepcopy
import queue
from collections import deque
import copy

import heapq


def main():
    node_num, q_num = map(int, input().split())
    data = [list(map(int, input().split())) for i in range(node_num - 1)]
    query = [list(map(int, input().split())) for i in range(q_num)]

    node_data = defaultdict(set)

    for i in range(node_num - 1):
        a, b = data[i]
        node_data[a].add(b)
        node_data[b].add(a)

    flg = [-1 for i in range(node_num + 1)]
    now_set = set()
    now_set.add(1)
    next_set = set()
    # potiton = [set(), set()]
    # potiton[0].add(1)
    flg[1] = 0
    while now_set:
        for node_ele in now_set:
            for next_ele in node_data[node_ele]:
                if flg[next_ele] != -1:
                    continue
                next_set.add(next_ele)
                flg[next_ele] = flg[node_ele] ^ 1
        now_set = next_set
        next_set = set()

    # print(flg)

    for i in range(q_num):
        c, d = query[i]
        if flg[c] == flg[d]:
            print("Town")
        else:
            print("Road")


if __name__ == '__main__':
    main()
