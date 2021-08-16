from collections import deque

n, q = map(int, input().split())

m = n - 1

#隣接リストの初期化(1オリジンとするため0は使わない)
g = [[] for _ in range(n + 1)]
for _ in range(m):
    [a, b] = [int(x) for x in input().split()]
    g[a].append(b)
    g[b].append(a)
#print(g)

#深さを記録するリスト(1オリジンとするため0は使わない)
depth_vec = [-1 for _ in range(n + 1)]

# 1を根とする根付き木を作り、各頂点の深さを記録する
queue = deque()
queue.append((1, 0))  #1.伝播用確定
#print(queue)
while len(queue) > 0:
    (node, depth) = queue.pop()  #2.取り出し
    #print("node and depth is")
    #print(node,depth)
    depth_vec[node] = depth  #3.確定
    for child in g[node]:  #4.子ノードの一覧生成
        #print("child is")
        #print(child)
        #print("depth_vec[{}] is".format(child))
        #print(depth_vec[child])
        if depth_vec[child] >= 0:  #5.既に確定しているものは何もしない
            #print("continue")
            continue
        queue.append((child, depth + 1))  #6.子ノードの伝播用確定
        #print("queue is")
        #print(queue)

#print(g)
#print(depth_vec)

for i in range(q):
    [x, y] = [int(xx) for xx in input().split()]
    if (depth_vec[x] + depth_vec[y]) % 2 == 0:
        print("Town")
    else:
        print("Road")
