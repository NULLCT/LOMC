from heapq import heappush, heappop, heapify

import sys

sys.setrecursionlimit(2147483647)
INF = float('inf')


def LI():
    return list(map(int, sys.stdin.readline().split()))


def LLI():
    return list(map(lambda x: int(x) - 1, sys.stdin.readline().split()))


def I():
    return int(sys.stdin.readline())


def LS():
    return sys.stdin.readline().rstrip().split()


def S():
    return sys.stdin.readline().rstrip()


def IR(n):
    return [I() for i in range(n)]


def LIR(n):
    return [LI() for i in range(n)]


def SR(n):
    return [S() for i in range(n)]


def LSR(n):
    return [LS() for i in range(n)]


def SRL(n):
    return [list(S()) for i in range(n)]


def MSRL(n):
    return [[int(j) for j in list(S())] for i in range(n)]


mod = 1000000007


def main():
    N, Q = LI()
    g = [[] for _ in range(N)]
    for _ in range(N - 1):
        a, b = LLI()
        g[a].append((1, b))
        g[b].append((1, a))
    cost, _ = dijkstra(0, g)
    for _ in range(Q):
        c, d = LLI()
        v = abs(cost[c] - cost[d])
        if v % 2 == 0:
            print('Town')
        else:
            print('Road')


def dijkstra(s, g):
    # g：グラフ
    #   i番目の要素：ノードiに接続されたノードのリスト（各ノードをタプル(iとjの間のコストc, ノードj)で表現）
    hq = [(0, s)]
    heapify(hq)  # リストを優先度付きキューに変換
    cost = [INF] * len(g)  # 行ったことのないところはinf
    cost[s] = 0  # 開始地点は0
    prev = [-1] * len(g)
    while hq:
        c, v = heappop(hq)
        if c > cost[v]:  # コストが現在のコストよりも高ければスルー
            continue
        for d, u in g[v]:
            tmp = d + cost[v]
            if tmp < cost[u]:
                cost[u] = tmp
                heappush(hq, (tmp, u))
                prev[u] = v
    return cost, prev


if __name__ == '__main__':
    main()
