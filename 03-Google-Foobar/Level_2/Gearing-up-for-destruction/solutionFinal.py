# Final solution attempt
""" The given solution is correct in theory but might not work for certain edge cases """
def solution(pegs):
    mid = []
    global_d = pegs[len(pegs) - 1] - pegs[0]
    for j in range(1, len(pegs)):
        mid.append(pegs[j] - pegs[j - 1])
    output = [-1, -1]
    i = 1
    while (i * 2) < mid[0]:
        # print("Iter = {}".format(i))
        b = (i * 2)
        result = []
        k = 1
        c = mid[k - 1] - b
        # print("c = {}".format(c))
        while (k < len(mid)) and (c < mid[k]):
            result.append(c)
            b = c
            k = k + 1
            c = mid[k - 1] - c
        # print("result:\t{}".format(result))
        prod = 0
        for l in range(len(result)):
            prod += result[l]
        # print("prod:\t{}".format(prod))
        # print("{} + ({} * 2) + ({} * 2) = {}".format(i,i,prod,(i * (i * 2) + (prod * 2))))
        if (i + (i * 2) + (prod*2)) == global_d:
            # print("{} + ({} * 2) + ({} * 2) = {}".format(i,i,prod,(i * (i * 2) + (prod * 2))))
            output = [(i * 2), 1]
        i = i + 1
    return output

# Dumbass mistakes are my achille's heal!

if __name__ == "__main__":
    print("Solution:\t{}".format(solution([4, 30, 50])))
    print("Solution:\t{}".format(solution([4, 17, 50])))
    print("Solution:\t{}".format(solution([2, 12, 20, 50])))
    print("Solution:\t{}".format(solution([4, 18, 28, 34, 40])))
    print("Solution:\t{}".format(solution([4, 20])))
    print("Solution:\t{}".format(solution([4, 16])))