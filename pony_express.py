f = open("C-large-practice.in")
#f = open("pony_express_small.txt")

# IDEA: do full traversal of the tree, in each node try both keep and change the horse, also use cache

def input():
       res = f.readline()
       return res

def FW():
    for k in range(1, N + 1):
        for i in range(1, N + 1):
            for j in range(1, N + 1):
                if min_dist[i][k] + min_dist[k][j] < min_dist[i][j]:
                    min_dist[i][j] = min_dist[i][k] + min_dist[k][j]
                    min_path[i][j] = min_path[i][k]


def get_next_city(city_from, target_city):

    city_to = min_path[city_from][target_city]
    distance = G[city_from - 1][city_to - 1]

    return city_to, distance


def get_min_time(city, target_city, horse):
    if (city, target_city, horse) in cache:
        return cache[(city, target_city, horse)]

    if city == target_city:
        return 0
    else:
        res = MAX_INT
        for next_city, next_city_dist in G1[city]:
            if next_city in discovered:
                continue
            else:
                discovered.add(next_city)

                endurance, speed = horses[city - 1]
                if endurance >= next_city_dist:
                    change_res = next_city_dist / speed + get_min_time(next_city, target_city, (endurance - next_city_dist, speed))
                else:
                    change_res = MAX_INT

                endurance, speed = horse
                if endurance >= next_city_dist:
                    not_change_res = next_city_dist / speed + get_min_time(next_city, target_city, (endurance - next_city_dist, speed))
                else:
                    not_change_res = MAX_INT

                res = min(res, change_res, not_change_res)

                discovered.remove(next_city)

        cache[(city, target_city, horse)] = res
        return res


def get_min_time0(city, target_city, horse):
    if (city, target_city, horse) in cache:
        return cache[(city, target_city, horse)]

    if city == target_city:
        return 0
    else:

        next_city, next_city_dist = get_next_city(city, target_city)

        endurance, speed = horses[city - 1]
        if endurance >= next_city_dist:
            change_res = next_city_dist / speed + get_min_time(next_city, target_city, (endurance - next_city_dist, speed))
        else:
            change_res = MAX_INT

        endurance, speed = horse
        if endurance >= next_city_dist:
            not_change_res = next_city_dist / speed + get_min_time(next_city, target_city, (endurance - next_city_dist, speed))
        else:
            not_change_res = MAX_INT

        res = min(change_res, not_change_res)
        cache[(city, target_city, horse)] = res
        return res

MAX_INT = 10 ** 20
T = int(input().strip())

for t in range(T):

    N, Q = [int(x) for x in input().strip().split(' ')]

    horses = [None] * N                 # array of pairs (endurance, velocity)
    for h in range(N):
        horses[h] = tuple(int(x) for x in input().strip().split(' '))

    # read G
    G = [None] * N   # incidency matrix
    G1 = [None] * (N + 1)  # connected verteces list

    # CONSIDER keeping adjacency matrix if for FW it's better
    for i in range(N):
        roads = [int(x) for x in input().strip().split(' ')]
        G[i] = roads
        if G1[i + 1] is None:
            G1[i + 1] = []

        for ix, w in enumerate(roads):
            if w != -1:
                G1[i + 1].append((ix + 1, w))

    # do FW
    min_dist = [None] * (N + 1)
    min_path = [None] * (N + 1)
    for i in range(N + 1):
        min_dist[i] = [MAX_INT] * (N + 1)
        min_path[i] = [None] * (N + 1)

    for i in range(N):
        for j in range(N):
            if G[i][j] != -1:
                min_dist[i + 1][j + 1] = G[i][j]
                min_path[i + 1][j + 1] = j + 1

    #FW()

    # read Qs
    res = []
    for q in range(Q):
        city_from, city_to = [int(x) for x in input().strip().split(' ')]

        # or instead of FW do dijkstra here

        cache = {}
        discovered = set([city_from])
        if t == 68:
            print(horses)
            print(G1)
            continue
        res.append(str(get_min_time(city_from, city_to, horses[0])))

    # CONSIDER single res!
    print("Case #{}: {}".format(t + 1, ' '.join(res)))