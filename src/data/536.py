import queue
############################
n, q = map(int, input().split())
#無向グラフ。隣接リストを使用
graph = [[] for i in range(n)]
for i in range(n - 1):
    a, b = map(int, input().split())
    graph[a - 1].append(b - 1)
    graph[b - 1].append(a - 1)
##########################
que = queue.Queue()
#街へは確実に移動できるので、街1からのコストをカウントする
color = [-1] * n
#偶奇がわかればよいので、コストが偶数なら０，奇数なら1とする
#１→１は移動ゼロなので、偶数
color[0] = 0
#キューに0を入れる
que.put(0)
#キューが空になるまで実施
while not que.empty():
    #ターゲットを取り出す
    t = que.get()
    #街tからいける場所を確認していく
    for i in graph[t]:
        #未確認の場合
        if color[i] == -1:
            #深く潜るので、起点と偶奇が変わる
            color[i] = 1 - color[t]
            #潜った先をキューに追加
            que.put(i)
###########
#アウトプット
for i in range(q):
    c, d = map(int, input().split())
    #cとdの偶奇が同じなら、どこかの街で合流
    if color[c - 1] == color[d - 1]:
        print("Town")
    else:
        print("Road")
