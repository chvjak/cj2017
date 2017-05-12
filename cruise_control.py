#f = open("cc-small.in")
#f = open("cc-large.in")
f = open("cc1.in")


def input2():
       res = f.readline()
       return res


def get_max_speed():
    MAX_INT = 10 ** 20
    prev_v = MAX_INT
    prev_t = 0
    prev_s = D
    for s, v in horses:
        t = (D - s) / v
        if t < prev_t:
            delta_t = (prev_s - s) / (v - prev_v)       # time to randevous
            delta_s = D - (prev_s + prev_v * delta_t)   # the rest of the way

            t = delta_t + delta_s / prev_v              # new time to finish for Horse i
            v = (D - s) / t                             # new (VIRTUAL) speed

        prev_v = v
        prev_t = t
        prev_s = s

    return D / prev_t

T = int(input().strip())

for t in range(T):
    D, H = [int(x) for x in input().strip().split(' ')]

    horses = [None] * H # array of pairs (start pos, velocity)
    for h in range(H):
        horses[h] = [int(x) for x in input().strip().split(' ')]
    horses.sort(key = lambda x: x[0], reverse = True)

    res = get_max_speed()

    print("Case #{}: {}".format(t + 1, res))