import sys  #PyPy3
import queue  #PyPy3

input = sys.stdin.readline
import copy  #PyPy3
from itertools import product  #PyPy3
from itertools import accumulate  #PyPy3
# for i in list(product([0,1], repeat=n)):
import math  #PyPy3
import collections  #PyPy3
import statistics as st  #PyPy3

#li = sorted(li, reverse=True, key=lambda x: x[1])  #[1]に注目してソート

sys.setrecursionlimit(2 * 10**6)  #再帰の上限をUP

n, q = map(int, input().split())
li = [[] for _ in range(n)]

for i in range(n - 1):
    a, b = map(int, input().split())
    li[a - 1].append(b - 1)
    li[b - 1].append(a - 1)

INF = 100100100100
d = [INF] * n


def bfs():
    que = queue.Queue()
    que.put(0)
    d[0] = 0

    while not que.empty():
        u = que.get()
        for i in li[u]:
            if d[i] != INF:
                continue
            else:
                d[i] = d[u] + 1
                que.put(i)


bfs()

for i in range(q):
    s, g = map(int, input().split())
    if (d[s - 1] + d[g - 1]) % 2 == 0:
        print("Town")
    else:
        print("Road")
