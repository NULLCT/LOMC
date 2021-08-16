from collections import deque

N, Q = list(map(int, input().strip().split()))
tree = [[] for _ in range(N)]
for _ in range(N - 1):
    a, b = list(map(int, input().strip().split()))
    a -= 1
    b -= 1
    tree[a] += [b]
    tree[b] += [a]

level = [-1] * N
root = 0
que = deque([root])
level[root] = 0
while que:
    node = que.popleft()
    for neighbor in tree[node]:
        if level[neighbor] == -1:
            que += [neighbor]
            level[neighbor] = level[node] + 1

Ans = ""
for _ in range(Q):
    c, d = list(map(int, input().strip().split()))
    c -= 1
    d -= 1
    if (level[c] - level[d]) % 2 == 0:
        Ans += "Town\n"
    else:
        Ans += "Road\n"
print(Ans)
