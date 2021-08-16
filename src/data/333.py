import sys

INF = float('inf')
#10**20,2**63,float('inf')
MOD = 10**9 + 7
MOD2 = 998244353


#from collections import defaultdict
def II():
    return int(sys.stdin.readline())


def LI():
    return list(map(int, sys.stdin.readline().split()))


def LC():
    return list(input())


def IC():
    return [int(c) for c in input()]


def MI():
    return map(int, sys.stdin.readline().split())


N, Q = MI()
Graph = [[] for _ in range(N)]
for _ in range(N - 1):
    A, B = MI()
    A -= 1
    B -= 1
    Graph[A].append(B)
    Graph[B].append(A)
Color = [0] * N  # 頂点iの色(1 or -1)


# 頂点を1と-1で塗っていく
def dfs(s, c):
    Color[s] = c  # 頂点vをcで塗る
    for t in Graph[s]:
        # 隣接している頂点が同じ色ならFalse
        if Color[t] == c:
            return False
        # 隣接している頂点がまだ塗られていないなら-cで塗る
        if Color[t] == 0 and not dfs(t, -c):
            return False
    # すべての頂点を塗れたらTrue
    return True


sys.setrecursionlimit(10**6)  #再帰関数ではコメントにしないこと！！
dfs(0, 1)
for _ in range(Q):
    C, D = MI()
    C -= 1
    D -= 1
    if (Color[C] == Color[D]):
        print("Town")
    else:
        print("Road")
