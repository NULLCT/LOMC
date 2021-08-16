import queue

N, Q = map(int, input().split())
G = [[] for _ in range(N)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    G[a - 1].append(b - 1)
    G[b - 1].append(a - 1)

# 初期ノードからの距離
vec = [-1] * N
vec[0] = 0

# キューの作成
q = queue.Queue()
q.put(0)

while not q.empty():
    v = q.get()
    for g in G[v]:
        if vec[g] == -1:
            vec[g] = vec[v] + 1
            q.put(g)

for _ in range(Q):
    c, d = map(int, input().split())
    if (vec[c - 1] + vec[d - 1]) % 2 == 0:
        print("Town")
    else:
        print("Road")
