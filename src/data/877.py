from collections import deque, Counter
from collections import defaultdict as dfd
from bisect import bisect, bisect_left
from math import sqrt, gcd, ceil, factorial
from heapq import heapify, heappush, heappop

MOD = 10**9 + 7
inf = float("inf")
ans_ = []


def nin():
    return int(input())


def ninf():
    return int(file.readline())


def st():
    return (input().strip())


def stf():
    return (file.readline().strip())


def read():
    return list(map(int, input().strip().split()))


def readf():
    return list(map(int, file.readline().strip().split()))


def readfl():
    return list(map(float, input().strip().split()))


def readffl():
    return list(map(float, file.readline().strip().split()))


# file = open("input.txt", "r")
def solve():
    #     for _ in range(nin()):
    n, q = read()
    adj = [[] for i in range(n + 1)]
    for i in range(n - 1):
        u, v = read()
        adj[u].append(v)
        adj[v].append(u)

    stk = [[1, 1]]
    vis = [-1] * (n + 1)
    vis[1] = 1
    while stk:
        curr, par = stk.pop()
        for i in adj[curr]:
            if vis[i] == -1:
                stk.append([i, 1 ^ par])
                vis[i] = 1 ^ par

    for i in range(q):
        c, d = read()
        if vis[c] == vis[d]:
            ans_.append("Town")
        else:
            ans_.append("Road")


solve()

for i in ans_:
    print(i)
