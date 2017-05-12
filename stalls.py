# f = open("stals.txt")
#
# def input():
#       res = f.readline()
#       return res

import heapq
def pop_max_span(spans):
    ms = heapq.heappop(spans)
    return -ms

def pop_max_span0(spans):
    ms = max(spans)
    ix = spans.index(ms)
    spans.remove(ms)
    return ms

def push_span(spans, new_span):
    heapq.heappush(spans, -new_span)

def push_span0(spans, new_span):
    spans.append(new_span)



T = int(input().strip())
for t in range(T):
    N, K = [int(x) for x in input().strip().split(' ')]

    spans = [-N]
    for k in range(K):

        max_span = pop_max_span(spans)


        rs = max_span // 2
        if max_span % 2:
            ls = max_span // 2
        else:
            ls = max_span // 2 - 1

        push_span(spans, ls)
        push_span(spans, rs)

        res_max_span = max(ls, rs)
        res_min_span = min(ls, rs)




    print("Case #{}: {} {}".format(t + 1, res_max_span, res_min_span))





