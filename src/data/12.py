import sys


#input()
def I():
    return sys.stdin.readline().rstrip()


#list(input())
def SI():
    return list(sys.stdin.readline().rstrip())


#int(input())
def II():
    return int(sys.stdin.readline().rstrip())


#map(int,input().split())
def MI():
    return map(int, sys.stdin.readline().rstrip().split())


#map(str, input().split())
def MS():
    return map(str, sys.stdin.readline().rstrip().split())


#list(map(int,input().split()))
def LI():
    return list(map(int, sys.stdin.readline().rstrip().split()))


#行列
def LLI(rows_number):
    return [LI() for _ in range(rows_number)]


from heapq import heappop, heappush

n, Q = MI()
graph = [[] for _ in range(n)]
oe = [0] * n

for i in range(n - 1):
    a, b = MI()
    graph[a - 1].append(b - 1)
    graph[b - 1].append(a - 1)


def dijkstra(s, g):  # 始点・隣接グラフ
    INF = 10**18
    check = [False] * n
    dist = [INF] * n
    dist[s] = 0
    q = [(0, s)]  # 距離・ノード
    while q:
        node = heappop(q)[1]  # 今いる所までの距離・そのノード
        if check[node]: continue
        check[node] = True
        for i in g[node]:  # これから行く所までの距離・そのノード
            if check[i]: continue
            if dist[i] <= dist[node] + 1: continue
            dist[i] = dist[node] + 1
            heappush(q, [dist[i], i])
    return dist


d = dijkstra(0, graph)
for i in range(n):
    if d[i] % 2 == 1:
        oe[i] = 1

for i in range(Q):
    c, d = MI()
    if oe[c - 1] == oe[d - 1]:
        print("Town")
    else:
        print("Road")
