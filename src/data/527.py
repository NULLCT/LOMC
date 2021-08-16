n, q = map(int, input().split())
e = [list() for _ in range(n)]
for _ in range(n - 1):
    a, b = map(lambda x: int(x) - 1, input().split())
    e[a].append(b)
    e[b].append(a)
depth = [0] * n

stack = [(0, -1, 0)]


def dfs(crt, par, d):
    depth[crt] = d
    for nxt in e[crt]:
        if nxt != par:
            stack.append((nxt, crt, d + 1))


while stack:
    dfs(*stack.pop())
for _ in range(q):
    c, d = map(lambda x: int(x) - 1, input().split())
    if (depth[c] + depth[d]) % 2 == 0:
        print('Town')
    else:
        print('Road')
