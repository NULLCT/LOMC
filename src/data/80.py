import collections

n, q = map(int, input().split())
tree = [[] for i in range(n)]
for i in range(n - 1):
    a, b = map(int, input().split())
    tree[a - 1].append(b - 1)
    tree[b - 1].append(a - 1)
colors = [0] * n
colors[0] = 1
stack = collections.deque([0])
while stack:
    tmp = stack.pop()
    tmp_color = colors[tmp]
    for i in tree[tmp]:
        if colors[i] == 0:
            colors[i] = tmp_color * -1
            stack.append(i)

for i in range(q):
    c, d = map(int, input().split())
    if colors[c - 1] == colors[d - 1]:
        print("Town")
    else:
        print("Road")
