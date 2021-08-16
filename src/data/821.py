import sys

sys.setrecursionlimit(100000)

N, Q = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(N - 1)]
CD = [list(map(int, input().split())) for _ in range(Q)]
G = [[] for _ in range(N)]
dp = [[0] * N for _ in range(2)]
visited = [0] * N


def dfs(x, c, a):
    for i in G[x]:
        if visited[i] == 0:
            visited[i] = 1
            dp[a][i] = c + 1
            dfs(i, c + 1, a)


for ab in AB:
    a, b = ab
    a -= 1
    b -= 1
    G[a].append(b)
    G[b].append(a)

for i in range(N):
    if len(G[i]) == 1:
        s = i
        break

visited = [0] * N
visited[s] = 1
dfs(s, 0, 0)
s = dp[0].index(max(dp[0]))
#print(s)
visited = [0] * N
visited[s] = 1
dfs(s, 0, 1)
#print(dp)
for cd in CD:
    c, d = cd
    c -= 1
    d -= 1
    if max(abs(dp[0][c] - dp[0][d]), abs(dp[1][c] - dp[1][d])) % 2 == 0:
        print("Town")
    else:
        print("Road")
