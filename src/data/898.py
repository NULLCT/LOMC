# AtCoder Beginner Contest 209
# D - Collision

N, Q = map(int, input().split())
G = [[] for i in range(N)]

for i in range(N - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    G[a].append(b)
    G[b].append(a)

white = set()
black = set()

todo = []
todo.append(1)
white.add(1)

col = 0  #0:white 1:black

while len(todo) > 0:
    v = todo.pop()
    if v in white:
        col = 0
    else:
        col = 1

    for i in range(len(G[v])):
        nxt = G[v][i]
        if nxt in white or nxt in black:
            continue
        if col == 0:
            black.add(nxt)
        else:
            white.add(nxt)
        todo.append(nxt)

# print(white)
# print(black)

for i in range(Q):
    c, d = map(int, input().split())
    c -= 1
    d -= 1
    if c in white and d in white:
        print("Town")
    if c in black and d in black:
        print("Town")
    if c in white and d in black:
        print("Road")
    if c in black and d in white:
        print("Road")
