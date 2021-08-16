from collections import deque
from collections import defaultdict as ddict


def main():
    N, Q = map(int, input().split())

    way = ddict(list)
    for _ in range(N - 1):
        a, b = map(int, input().split())
        way[a].append(b)
        way[b].append(a)

# print(way)
    ansdic = {1: 0}
    mita = {1: 1}

    que = deque([1])
    fukasa = 0

    while que:
        #print(que, fukasa)
        q = que.popleft()
        fukasa += 1
        if q in ansdic:
            fukasa = ansdic[q] + 1
        tmp = deque([])
        for town in way[q]:
            if town in mita:
                continue
            mita[town] = 1
            que.append(town)
            ansdic[town] = fukasa

        #   print(ansdic)

    inlis = []
    for _ in range(Q):
        c, d = map(int, input().split())
        inlis.append([c, d])

    for i in range(Q):
        c, d = inlis[i]
        cpo = ansdic[c]
        dpo = ansdic[d]
        #print(c,d,cpo,dpo)
        if abs(dpo - cpo) % 2 == 1:
            print('Road')
        else:
            print('Town')

if __name__ == "__main__":
    main()
