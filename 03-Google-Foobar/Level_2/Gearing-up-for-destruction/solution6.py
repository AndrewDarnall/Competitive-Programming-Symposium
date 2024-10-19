def solution(pegs):
    global_d = pegs[len(pegs) - 1] - pegs[0]
    mid = []

    # Populate mid list
    for i in range(1, len(pegs)):
        mid.append(pegs[i] - pegs[i - 1])

    j = 1

    while ((j * 2) < mid[0]):
        b = j * 2
        result = [b]

        for k in range(1, len(mid)):
            c = mid[k - 1] - b

            if (c + b) > mid[k]:
                break  # This break only exits the inner for loop

            result.append(c)
            b = c

        if (c + j) != mid[len(mid) - 1]:
            return (result[0], 1)

        j = j + 1
        print("{} < {}".format((j * 2),mid[0]))

    return (-1, -1)

if __name__ == "__main__":
    print("Solution:\t{}".format(solution([4, 30, 50])))
    print("solution:\t{}".format(solution([4, 17, 50])))
