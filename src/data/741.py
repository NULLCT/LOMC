from collections import deque
#入力が1-indxなのでリスト番号も1-indに
#1-indなのでfor文の範囲も変わってることに注意

n, q = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for i in range(1, n):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

dist = [-1] * (n + 1)
dist[1] = 0
dist[0] = 0
#-1が未訪問

d = deque()
d.append(1)  #頂点1を訪問

while d:
    #print(d)
    v = d.popleft()  #要素の左端を削除して取得
    for i in graph[v]:
        if dist[i] != -1:  #訪問済みであれば
            continue
        dist[i] = dist[v] + 1  #未訪問ならdistを計算 今いる場所の隣なので+1
        d.append(i)  #今回新しく見つけた頂点を追加
    #print(d)

#for i in range(1,n+1):
#    print(i,dist[i])

for i in range(q):
    c, d = map(int, input().split())
    judge = dist[d] + dist[c]
    #print(dist[c],dist[d])
    #本来の距離ではない
    #絶対的な距離はLCAを考慮する必要あり

    if judge % 2 == 0:
        print('Town')
    else:
        print('Road')
