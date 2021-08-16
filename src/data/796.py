N, Q = map(int, input().split())
AB = [[int(item) for item in input().split()] for _ in range(N - 1)]
# print(AB)
AB.sort(key=lambda x: (x[0], x[1]))
Next_Dict = {n: [] for n in range(1, N + 1)}
for ab in AB:
    Next_Dict[ab[0]].append(ab[1])
    Next_Dict[ab[1]].append(ab[0])

# print(Next_Dict)
min_list = [N for _ in range(N + 1)]
min_list[1] = 0

import queue

q = queue.Queue()

q.put(1)

tuuka = [False for _ in range(0, N + 1)]
while not q.empty():
    item = q.get()
    if tuuka[item]:
        continue
    tuuka[item] = True
    # print("item", item)
    d = min_list[item]
    # print("d", d)
    for next in Next_Dict[item]:
        q.put(next)
        min_list[next] = min(d + 1, min_list[next])
    # print("min_list", min_list)

# print(min_list)

CD = [[int(item) for item in input().split()] for _ in range(Q)]

for cd in CD:
    c, d = cd
    print('Town' if (min_list[c] + min_list[d]) % 2 == 0 else 'Road')
