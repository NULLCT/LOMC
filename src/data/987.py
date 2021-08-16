import sys

sys.setrecursionlimit(10**5)
n, q = map(int, input().split())
graph = [[] for i in range(n)]

#木であることに注意
for i in range(n - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    graph[a].append(b)
    graph[b].append(a)

depth = [-1 for i in range(n)]
visited = [False for i in range(n)]
visited[0] = True

#0からの深さをdepth配列に記録。０番目の要素をhukasa0で記録
depth[0] = 0


def dfs(i):
    a = graph[i]
    for j in a:
        #print(j)
        if not (visited[j]):
            depth[j] = depth[i] + 1
            visited[j] = True
            dfs(j)
        else:
            continue


dfs(0)
for i in range(q):
    c, d = map(int, input().split())
    c -= 1
    d -= 1

    if abs(depth[c] - depth[d]) % 2 == 0:
        print("Town")
    else:
        print("Road")
