import os, sys, time, collections, math, pprint, itertools as it, operator as op, bisect as bs, functools as fn

maxx, localsys, mod = 1 << 60, 0, int(1e9 + 7)
nCr = lambda n, r: reduce(mul, range(n - r + 1, n + 1), 1) // factorial(r)
ceil = lambda n, x: (n + x - 1) // x
osi, oso = '/home/priyanshu/Documents/cp/input.txt', '/home/priyanshu/Documents/cp/output.txt'
if os.path.exists(osi):
    sys.stdin = open(osi, 'r')
    sys.stdout = open(oso, 'w')

input = sys.stdin.readline


def maps():
    return map(int, input().split())


from queue import Queue


#THINK ABOUT THE EDGE CASES ..........
def BFS(s, d, n):
    q, c = [s], 0
    color = {}
    color[s] = 0
    while q:
        s = q.pop(0)
        for v in d[s]:
            if v not in color:
                q.append(v)
                color[v] = color[s] ^ 1
    return color


n, queries = maps()
graph = [[] for _ in range(n)]
for _ in range(n - 1):
    a, b = maps()
    graph[a - 1].append(b - 1)
    graph[b - 1].append(a - 1)
color = BFS(0, graph, n)
for _ in range(queries):
    a, b = maps()
    if color[a - 1] != color[b - 1]:
        print('Road')
    else:
        print('Town')
