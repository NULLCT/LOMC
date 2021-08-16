#import sys
#import numpy as np
import math
#from fractions import Fraction
import itertools
from collections import deque
from collections import Counter
import heapq
from fractions import gcd
#input=sys.stdin.readline
#import bisect

n, q = map(int, input().split())
v = tuple(
    tuple(map(lambda x: int(x) - 1,
              input().split())) for _ in range(n - 1))

node = [[] for _ in range(n)]

for pair in v:
    node[pair[0]].append(pair[1])
    node[pair[1]].append(pair[0])
d = deque()
check = [-1] * n
check[0] = 0
for i in node[0]:
    d.append(i)
    check[i] = 1

while True:
    if not d:
        break
    t = d.pop()
    dist = check[t]
    for i in node[t]:
        if check[i] != -1:
            continue
        d.append(i)
        check[i] = dist + 1
for i in range(q):
    c, d = map(int, input().split())
    c -= 1
    d -= 1
    if (check[c] + check[d]) % 2 == 0:
        print("Town")
    else:
        print("Road")
