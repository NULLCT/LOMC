n, q = map(int, input().split())
connected = {i: [] for i in range(n)}

for _ in range(n - 1):
    a, b = map(int, input().split())
    a, b = a - 1, b - 1
    connected[a].append(b)
    connected[b].append(a)

que = [(-1, 0, [0, 0])]  # previous, now, rank
ranks = [[] for _ in range(n)]

while len(que) >= 1:
    previous, now, rank = que.pop()
    ranks[now] = rank
    next_town = [t for t in connected[now] if t != previous]
    if len(next_town) == 1:
        next_t = next_town[0]
        rank_n = rank.copy()
        rank_n[-1] += 1
        que.append((now, next_t, rank_n))
    elif len(next_town) >= 2:
        for i, next_t in enumerate(next_town):
            rank_i = rank.copy()
            rank_i += [i, 1]
            que.append((now, next_t, rank_i))


def calc_distance(rank1, rank2):
    # rank1 <= rank2 にする
    if len(rank1) > len(rank2):
        rank1, rank2 = rank2, rank1

    dist = -1
    while dist < 0:
        if rank1[:2] == rank2[:2]:
            if len(rank1) == 2:
                rank1 = [0, 0]
            else:
                rank1 = rank1[2:]
            rank2 = rank2[2:]
        elif rank1[0] != rank2[0]:
            dist = sum(rank1[1::2]) + sum(rank2[1::2])
        elif rank1[0] == rank2[0]:
            dist = abs(sum(rank1[1::2]) - sum(rank2[1::2]))
    return (dist)


for _ in range(q):
    c, d = map(int, input().split())
    c, d = c - 1, d - 1
    dist = calc_distance(ranks[c], ranks[d])
    if dist % 2 == 0:
        print('Town')
    else:
        print('Road')
