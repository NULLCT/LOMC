from collections import deque

N, Q = map(int, input().split())
tree = [[] for _ in range(N + 1)]
for i in range(N - 1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)
cd = []
for j in range(Q):
    c, d = map(int, input().split())
    cd.append([c, d])
que = deque()
bi = [False] * (N + 1)
que.append(1)
while que:
    cp = que.popleft()
    for k in tree[cp]:
        if bi[k] == False:
            bi[k] = not bi[cp]
            que.append(k)
for c, d in cd:
    print('Town' if bi[c] == bi[d] else 'Road')
