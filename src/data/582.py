N, Q = map(int, input().split())
path = [[] * N for i in range(N)]
for i in range(N - 1):
    a, b = map(int, input().split())
    path[a - 1].append(b - 1)
    path[b - 1].append(a - 1)
par = [True] * N
stack = [0]
checked = [False] * N
while len(stack) > 0:
    node = stack.pop(-1)
    if checked[node]:
        continue
    checked[node] = True
    for i in path[node]:
        if checked[i]:
            continue
        par[i] = not par[node]
        stack.append(i)

inp = []
for _ in range(Q):
    c, d = map(int, input().split())
    cf = par[c - 1]
    df = par[d - 1]
    if cf == df:
        print("Town")
    else:
        print("Road")
