# Triplet-based solution
def solution3(xs):
    d = xs[len(xs) - 1] - xs[0]
    for i in range(1,d+1):
        print("({} * {}) + {} - {} = {}".format(i,2,i,d,((i * 2) + i - d)))
        if ((i * 2) + i - d) == 0:
            print("Solution:\t{}".format(i*2))
            return (i, i * 2, (i + (i * 2) - d))
        
# This solution works in the case of 3 elements in the array, but I need to generalize it to n elements
def solution4(xs):
    global_dist = xs[len(xs) - 1] - xs[0]
    mid_distances = []
    for j in range(1,len(xs)):
        mid_distances.append(xs[j] - xs[j - 1])
    for i in range(1, global_dist):
        res = (global_dist - (i + (i * 2))) / 2
        # print("res = {}".format(res))
        if res % 1 == 0:
            if (res + i) <= mid_distances[len(mid_distances) - 1] and (res + (i * 2)) <= mid_distances[0]:
                print("result:\t{}".format(i * 2))
                return (i * 2,1)
    print("Result:\t{}".format(-1))
    return(-1,-1)

        
if __name__ == "__main__":
    # print(solution3([4, 30, 50]))
    print(solution4([4, 30, 50]))
    print(solution4([4, 17, 50]))