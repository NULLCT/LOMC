import sys

input = sys.stdin.readline
N, Q = map(int, input().split())
AB = [tuple(map(int, input().split())) for i in range(N - 1)]
CD = [tuple(map(int, input().split())) for i in range(Q)]

es = [[] for _ in range(N)]
for a, b in AB:
    a, b = a - 1, b - 1
    es[a].append(b)
    es[b].append(a)

MK = len(bin(N)) - 1
dp = [[-1] * N for _ in range(MK)]
depth = [0] * N
visited = [0] * N
visited[0] = 1
stack = [0]
while stack:
    v = stack.pop()
    for to in es[v]:
        if visited[to]: continue
        visited[to] = 1
        dp[0][to] = v
        depth[to] = depth[v] + 1
        stack.append(to)

for k in range(MK - 1):
    for i in range(N):
        if dp[k][i] < 0: continue
        dp[k + 1][i] = dp[k][dp[k][i]]


def lca(s, t):
    if depth[s] < depth[t]: s, t = t, s
    for k in range(MK):
        if ((depth[s] - depth[t]) >> k) & 1:
            s = dp[k][s]
    if s == t: return s
    for k in range(MK - 1, -1, -1):
        if dp[k][s] != dp[k][t]:
            s = dp[k][s]
            t = dp[k][t]
    return dp[0][s]


ans = []
for c, d in CD:
    c, d = c - 1, d - 1
    a = lca(c, d)
    dist = depth[c] + depth[d] - depth[a] * 2
    ans.append('Road' if dist % 2 else 'Town')
print(*ans, sep='\n')
