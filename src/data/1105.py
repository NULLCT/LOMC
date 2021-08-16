# -*- coding: utf-8 -*-
import sys
import queue

sys.setrecursionlimit(10000000)
input = sys.stdin.readline

from collections import defaultdict

N, Q = list(map(int, input().split()))
edges = defaultdict(list)
for _ in range(N - 1):
    a, b = list(map(lambda x: int(x) - 1, input().split()))
    edges[a].append(b)
    edges[b].append(a)

queries = [None] * Q
for i in range(Q):
    a, b = list(map(lambda x: int(x) - 1, input().split()))
    queries[i] = [a, b]

is_even = [False] * N
is_even[0] = True
visited = [False] * N
que = queue.Queue()
que.put((0, 0))  # index, distance
visited[0] = True
while not que.empty():
    index, distance = que.get()
    for to in edges[index]:
        if visited[to]:
            continue
        visited[to] = True
        is_even[to] = ((distance + 1) % 2 == 0)
        que.put((to, distance + 1))

for query in queries:
    a, b = query
    if is_even[a] == is_even[b]:
        print('Town')
    else:
        print('Road')
