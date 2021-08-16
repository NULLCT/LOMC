import sys

sys.setrecursionlimit(1000000)
n, q = map(int, input().split())
graph = [set([]) for _ in range(n)]
for _ in range(n - 1):
    a, b = map(int, input().split())
    graph[a - 1].add(b - 1)
    graph[b - 1].add(a - 1)


def dfs(i):
    if temp[i]:
        return
    temp[i] = True
    if i in odd:
        for j in graph[i]:
            even.add(j)
            dfs(j)
    else:
        for j in graph[i]:
            odd.add(j)
            dfs(j)


temp = [False] * n
odd = set([])
even = set([])
odd.add(0)
dfs(0)
ans = []
for i in range(q):
    c, d = map(int, input().split())
    if (c - 1 in odd and d - 1 in odd) or (c - 1 in even and d - 1 in even):
        ans.append("Town")
    else:
        ans.append("Road")
for i in ans:
    print(i)
