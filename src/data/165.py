import collections
from collections import defaultdict
import math
from math import gcd
from collections import Counter

for _ in range(1):
    #for t in range(int(input())):

    #n = int(input())
    n, q1 = [int(x) for x in input().split()]
    #x1,x2,y1,y2,z1,z2=[int(c) for c in input().split()]
    #c=[int(x) for x in input().split()]
    adj = defaultdict(lambda: [])
    for i in range(n - 1):
        z = [int(x) for x in input().split()]
        adj[z[0] - 1].append(z[1] - 1)
        adj[z[1] - 1].append(z[0] - 1)

    c = [-1] * n
    c[0] = 0
    level = 0
    visited = defaultdict(lambda: False)
    #we know the graph is bipartile
    q = [0]
    visited[0] = True
    while len(q) > 0:
        z = []
        level = 1 - level
        for x in q:
            for y in adj[x]:
                if not visited[y]:
                    z.append(y)
                    visited[y] = True
                    c[y] = level

        q = z

    for i in range(q1):
        a, b = [int(x) for x in input().split()]
        a -= 1
        b -= 1
        if c[a] - c[b] % 2 == 0:
            print('Town')
        else:
            print("Road")

    #length of shortest path is : even -> Town
    #                         odd  -> Road
