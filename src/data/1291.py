n, q = map(int, input().split())
root = [[] for i in range(n + 1)]
for i in range(n - 1):
    a, b = map(int, input().split())
    root[a].append(b)
    root[b].append(a)

d = [10**8] * (n + 1)
d[1] = 0

seen = [0] * (n + 1)
ind = [0] * (n + 1)


# record=[[] for i in range(n+1)] # 変数の情報記録
def tree_search(n, G, s, func1, func2, func3):
    #n...頂点の数
    #G...G[v]は頂点vから行ける頂点の配列
    #s...sが根
    #func1(now)...ある頂点に初めて訪れた時、その頂点のみでする処理。ない場合は0
    #func2(now,next)...nowからnextに移動する時に行う処理。ない場合は0
    #func3(now)...nowを去る時にする処理。なければ0

    search = [s]
    while search:
        now = search[-1]
        if seen[now] == 0 and func1 != 0: func1(now)
        seen[now] = 1
        if len(G[now]) > ind[now]:
            next = G[now][ind[now]]
            ind[now] += 1
            if seen[next] > 0: continue
            if func2 != 0: func2(now, next)
            search.append(next)
        else:
            if func3 != 0: func3(now)
            search.pop()


def f2(x, y):
    d[y] = d[x] + 1


tree_search(n, root, 1, 0, f2, 0)

for i in range(q):
    a, b = map(int, input().split())
    ans = d[a] - d[b]
    ans %= 2
    if ans == 0: print("Town")
    else: print("Road")
