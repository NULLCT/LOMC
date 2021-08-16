#解説を読んで挑戦
import queue

N, Q = map(int, input().split())
edge = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    edge[a].append(b)
    edge[b].append(a)

#頂点1からの距離の偶奇をBFSで求める

C = [0] * (N + 1)  # 頂点1からの距離の偶奇を求める
checked = [False] * (N + 1)

q = queue.Queue()
q.put(1)

while not (q.empty()):
    u = q.get()
    checked[u] = True
    for v in edge[u]:
        if checked[v] == False:
            C[v] = 1 - C[u] % 2
            q.put(v)

for _ in range(Q):
    c, d = map(int, input().split())
    if C[c] == C[d]:
        print("Town")
    else:
        print("Road")
