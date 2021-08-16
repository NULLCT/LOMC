N, Q = map(int, input().split())

Graph = [[] for _ in range(N + 1)]

sumc = 0

for i in range(N - 1):
    a, b = map(int, input().split())
    Graph[a].append(b)
    Graph[b].append(a)
# print(Graph)

from collections import deque


def dfs(Graph, N, s, t):
    todo_stack = deque()
    done_list = [0] * N
    todo_stack.append(s)
    dist = [0] * N  # sからの距離

    while todo_stack:
        # スタックからチェック対象を取り出す
        now = todo_stack.pop()
        # 接続ノードごとに未確認の場合、距離を計算、確認済、todoに追加
        for node in Graph[now]:
            if done_list[node] == 0:
                dist[node] = dist[now] + 1
                done_list[node] = 1
                todo_stack.append(node)
    # return(dist[t])

    # 1からの距離で偶数ノードと奇数ノードを分ける。
    node_gk = [0] * N
    for i in range(N):
        node_gk[i] = dist[i] % 2

    return (node_gk)


node_gk = dfs(Graph, N + 1, 1, N)
# print(node_gk)

for i in range(Q):
    c, d = map(int, input().split())
    if node_gk[c] == node_gk[d]:
        print("Town")
    else:
        print("Road")
