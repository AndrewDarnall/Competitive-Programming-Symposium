# First attempt at generalization
def solution(pegs):
    global_distance = pegs[len(pegs) - 1] - pegs[0]
    mid_distances = []
    for k in range(1, len(pegs)):
        mid_distances.append(pegs[k] - pegs[k - 1])
    for j in range(1, global_distance):
        b = (j * 2)
        result = []
        result.append(j * 2)
        for i in range(len(mid_distances)):
            c = b - mid_distances[i]
            if (b + c) > mid_distances[i]:
                break
            b = c
            result.append(c)
        result.append(j)
    if (c + pegs[len(pegs) - 1] != mid_distances[len(mid_distances) - 1]):
        print("{} + {}".format(c,pegs[len(pegs) - 1]))
        return (result[0], 1)
    return (-1, -1)

if __name__ == "__main__":
    print("Solution:\t{}".format(solution([4, 30, 50])))
    print("Solution:\t{}".format(solution([4, 17, 50])))