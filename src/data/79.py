from collections import deque

N, QQ = map(int, input().split())

graph = []
for i in range(N + 1):
    graph.append([])

for i in range(N - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

cd = []
for i in range(QQ):
    c, d = map(int, input().split())
    cd.append([c, d])

Q = deque()
Q.append(1)
memo = [-1] * (N + 1)
TF = [False] * (N + 1)
TF[0] = True
memo[1] = 0
TF[1] = True

while len(Q) > 0:
    tmp = Q.popleft()
    for z in graph[tmp]:
        if not TF[z]:
            TF[z] = True
            memo[z] = memo[tmp] + 1
            Q.append(z)

for x, y in cd:
    if abs(memo[y] - memo[x]) % 2 == 0:
        print("Town")
    else:
        print("Road")
