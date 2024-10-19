# Test solution to check the ammount of test cases
def solution(xs):
    global_dist = xs[len(xs) - 1] - xs[0]
    mid_distances = []
    for j in range(1,len(xs)):
        mid_distances.append(xs[j] - xs[j - 1])
    for i in range(1, global_dist):
        res = (global_dist - (i + (i * 2))) / 2
        # print("res = {}".format(res))
        if res % 1 == 0:
            if (res + i) <= mid_distances[len(mid_distances) - 1] and (res + (i * 2)) <= mid_distances[0]:
                return (i * 2,1)
    return(-1,-1)