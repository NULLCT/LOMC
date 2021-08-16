import heapq, math
from collections import defaultdict, deque
from os import getcwd
#from functools import cmp_to_key

import sys, os.path

sys.setrecursionlimit(10000000)

if (os.path.exists('C:/Users/Dhanush/Desktop/cp/input.txt')):
    sys.stdout = open('C:/Users/Dhanush/Desktop/cp/output.txt', 'w')
    sys.stdin = open('C:/Users/Dhanush/Desktop/cp/input.txt', 'r')

input = sys.stdin.readline


def dfs(cur, col):
    colour[cur] = col
    visit[cur] = 1
    for next in d[cur]:
        if (visit[next] == 0):
            dfs(next, 1 - col)


n, q = map(int, input().split())
d = defaultdict(list)
for i in range(n - 1):
    a, b = map(int, input().split())
    d[a].append(b)
    d[b].append(a)
visit = [0 for _ in range(n + 1)]
colour = [-1 for _ in range(n + 1)]
dfs(1, 0)
for i in range(q):
    a, b = map(int, input().split())
    if (colour[a] == colour[b]):
        print('Town')
    else:
        print('Road')
