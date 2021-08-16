from collections import deque

N, QE = map(int, input().split())

#頂点iからつながる辺のリストGの定義
G = []
for _ in range(N):
    G.append([])

for i in range(N - 1):
    ai, bi = map(int, input().split())
    #indexを０始まりに直す
    ai -= 1
    bi -= 1
    G[ai].append(bi)
    G[bi].append(ai)

color = []

for _ in range(N):
    color.append(-1)

color[0] = 0
Q = deque()
Q.append(0)

ans = []

while len(Q) > 0:

    i = Q.popleft()

    for j in G[i]:
        if color[j] == -1:
            color[j] = 1 - color[i]
            Q.append(j)

for i in range(QE):
    ci, di = map(int, input().split())
    ci -= 1
    di -= 1
    if color[ci] == color[di]:
        ans.append("Town")
    else:
        ans.append("Road")

for i in ans:
    print(i)
