import sys
from collections import defaultdict, deque
from itertools import permutations, combinations
from math import factorial, ceil, floor
from decimal import Decimal


def i_input():
    return int(input())


def map_str():
    return input().split()


def map_int():
    return map(int, input().split())


def lmap_int():
    return list(map(int, input().split()))


def lmap_str():
    return list(map(input().split()))

# mod = 10**9 + 7


# g: 二次元配列(あるノードがどのノードと隣接しているかを示す)
# q: キュー
def bfs(g, q, dist):
    while q:
        # キューの先頭が現在地
        current = q.popleft()
        # 隣接する各ノードについて
        for node in g[current]:
            if dist[node] != 0: continue
            dist[node] = dist[current] + 1
            q.append(node)
    return dist


def main():
    sys.setrecursionlimit(3 * 10**5)
    n, r = map_int()
    g = [[] for _ in range(n)]
    for _ in range(n - 1):
        a, b = map_int()
        g[a - 1].append(b - 1)
        g[b - 1].append(a - 1)
    q = deque([0])
    dist = [0] * n
    dist[0] = 1
    dist = bfs(g, q, dist)

    for _ in range(r):
        c, d = map_int()
        if dist[c - 1] == dist[d - 1]:
            if c - 1 in g[d - 1]:
                print("Road")
                continue
        if (dist[c - 1] - dist[d - 1]) % 2 == 0:
            print("Town")
        else:
            print("Road")


if __name__ == '__main__':
    main()
