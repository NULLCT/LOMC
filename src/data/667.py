from collections import deque


def bfs(v):
    ## キューを作成
    que = deque()
    ## 深さ記録用のリストを作成
    depth_log = [None for _ in range(N + 1)]
    ## 初期値として、1つ目のノードの接続先ノードをQueに入れる
    current_depth = 0
    depth_log[0] = 0  # 使用しない0番目の値も0にしておく
    depth_log[v] = 0
    for node in graph[v]:
        depth_log[node] = current_depth + 1
        que.append(node)

    # que がなくなるまで以下を繰り返し
    while que:
        node = que.popleft()
        for _ in graph[node]:
            current_depth = depth_log[node] + 1
            if depth_log[_] == None:
                depth_log[_] = current_depth
                que.append(_)
    return depth_log


## 入力
N, Q = [int(i) for i in input().split()]

graph = [[] for _ in range(N + 1)]

graph[0].append(0)

for _ in range(N - 1):
    a, b = [int(i) for i in input().split()]
    graph[a].append(b)
    graph[b].append(a)

bfs_graph = bfs(1)

for q in range(Q):
    c, d = [int(i) for i in input().split()]
    if (bfs_graph[c] - bfs_graph[d]) % 2 == 1:
        print('Road')
    else:
        print('Town')
