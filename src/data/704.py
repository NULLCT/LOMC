n, q = map(int, input().split())

edges = [[] for _ in range(n)]
for _ in range(n - 1):
    a, b = map(int, input().split())
    edges[a - 1].append(b - 1)
    edges[b - 1].append(a - 1)

# DFS
root = 0
heights = [-1] * n
heights[root] = 0
todo = [root]
while todo:
    a = todo.pop()
    for b in edges[a]:
        if heights[b] == -1:
            heights[b] = heights[a] + 1
            todo.append(b)

ans = ['Town'] * q
for i in range(q):
    c, d = map(int, input().split())
    if heights[c - 1] + heights[d - 1] & 1:
        ans[i] = 'Road'
print(*ans, sep='\n')
