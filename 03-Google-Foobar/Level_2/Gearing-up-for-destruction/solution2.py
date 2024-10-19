# Example of a case 2 solution
def solution2(pegs):
    d = pegs[1] - pegs[0]
    for i in range(d):
        if ((i * 2) + i - d) == 0:
            print("Solution is\t{}".format(i))
            return (i, 1)

if __name__ == "__main__":
    print(solution2([4, 46]))

# The base case of 2 works just fine, what about its generalization?