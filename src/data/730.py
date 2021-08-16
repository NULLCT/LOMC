def get_pass(road, start, end):
    count = 0
    now = [start]
    passed = {start: 0}
    while (1):
        count += 1
        next_now = []
        for i in now:
            next_towns = road[i]
            for next_town in next_towns:
                if next_town in passed:
                    pass
                if (next_town == end):
                    return (count)
                else:
                    passed[next_town] = 0
                    next_now.append(next_town)
        now = next_now


def get_all_pass(road, n):
    count = 0
    start = 1
    now = [start]
    road_count = [0] * (n + 1)
    passed = {start: 0}
    while (len(passed) < n):
        count += 1
        next_now = []
        for i in now:
            next_towns = road[i]
            for next_town in next_towns:
                if next_town in passed:
                    pass
                else:
                    passed[next_town] = 0
                    next_now.append(next_town)
                    road_count[next_town] = count
        now = next_now
    return (road_count)


n, q = map(int, input().split())
road = {}

for i in range(n - 1):
    a, b = map(int, input().split())
    if (not a in road):
        road[a] = [b]
    else:
        road[a].append(b)
    if (not b in road):
        road[b] = [a]
    else:
        road[b].append(a)

road_count = get_all_pass(road, n)
#print(get_all_pass(road, n))
for i in range(q):
    c, d = map(int, input().split())
    #if(get_pass(road, c, d) % 2 == 0):
    if ((road_count[c] - road_count[d]) % 2 == 0):
        print("Town")
    else:
        print("Road")
