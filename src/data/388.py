n, q = map(int, input().split())
town = [[] for _ in range(n)]
for _ in range(n - 1):
    a, b = map(int, input().split())
    town[a - 1].append(b)
    town[b - 1].append(a)

deep, data = [-1] * n, [[1, 0]]
cnt = 0

while len(data) > 0:
    temp, depth = data.pop(0)
    if deep[temp - 1] >= 0:
        continue
    deep[temp - 1] = depth
    depth += 1
    for i in town[temp - 1]:
        if deep[i - 1] >= 0:
            continue
        data.append([i, depth])

for _ in range(q):
    c, d = map(int, input().split())
    ans = abs(deep[c - 1] - deep[d - 1])
    if ans % 2 == 0:
        print("Town")
    else:
        print("Road")
