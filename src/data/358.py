import queue
# tree の depthで算出する方法を試す
# Query は複数飛んでくるので cache しないと間に合わない

N, Q = map(int, input().split())

# Edge は N-1 しかない
abn = [tuple(map(int, input().split())) for _ in range(N - 1)]
cdq = [tuple(map(int, input().split())) for _ in range(Q)]


def show2d(a2d):
    print("===show2d===")
    for i, a1d in enumerate(a2d):
        print(i + 1, a1d)


# It can Not be comlete.-> -root is always lesser than any leaves.-
# ex.) 1-3-2
tree = [set() for _ in range(N)]

for a, b in abn:

    a -= 1
    b -= 1

    # registor parent v
    tree[b].add(a)
    tree[a].add(b)

#if len(  list(filter(lambda a:a==-1,tree))  ) > 0:
#  print(abn)
#  show2d(tree)
#  raise ValueError()

#show2d(tree)
depth = [-1] * N
depth[0] = 0

Q = queue.Queue()
Q.put(0)

while not Q.empty():

    p = Q.get()

    for v in filter(lambda a: depth[a] == -1, tree[p]):
        depth[v] = depth[p] + 1
        Q.put(v)
        #print("d:",depth)

#print(depth)
for c, d in cdq:
    c -= 1
    d -= 1
    t = depth[c] + depth[d]

    print("Road" if t % 2 == 1 else "Town")
