import sys

sys.setrecursionlimit(10**9)

N, Q = map(int, input().split())

G = [list() for i in range(N + 1)]
for i in range(N - 1):
    a, b = map(int, input().split())
    G[a].append(b)
    G[b].append(a)

query = []
for i in range(Q):
    c, d = map(int, input().split())
    query.append((c, d))

height = [-float('inf')] * (N + 1)
height[0] = -1


def dfs(pos, pre):
    height[pos] = height[pre] + 1
    for to in G[pos]:
        if height[to] != -float('inf'):
            continue
        dfs(to, pos)
    pass


dfs(1, 0)  # 1 の高さを０とするため、便宜上、hi\eight[0]= -1
# print(height)

for c, d in query:
    diff1 = height[c]
    diff2 = height[d]
    sum = diff1 + diff2
    if sum % 2 == 0:
        print("Town")
    else:
        print("Road")
