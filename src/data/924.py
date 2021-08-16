from collections import deque

n, q = map(int, input().split())

pic = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    x, y = map(int, input().split())
    pic[x].append(y)
    pic[y].append(x)


def BFS(x):

    visited = [None] * (n + 1)  #注_'None'を演算に使用するとエラーが返る
    visited[x] = 0  #頂点'x'から頂点'x'までの距離は'0'なので問題なし

    queue = deque([])  #探索候補の器、初期化
    queue.append(x)  #スタート位置('X')のみ追加しとく

    while queue:
        tmp = queue.popleft()  #探索候補を'popleft'
        for i in pic[tmp]:  #探索候補の隣接頂点を探索
            if visited[i] != None:  #訪問済の場合
                continue  #何もしない
            else:  #未訪問('None')の場合
                #visited[i]に'x'からの距離を一つ手前(visited[tmp])'+1'として記録
                visited[i] = visited[tmp] + 1
                queue.append(i)  #現在地を探索候補に'append'
    return visited  # visited[0]はダミーなので[1]以降をリストで出力


MAP = BFS(1)
for i in range(q):
    c, d = map(int, input().split())
    tmp = MAP[c] + MAP[d]
    if tmp % 2 == 0:
        print('Town')
    else:
        print('Road')
