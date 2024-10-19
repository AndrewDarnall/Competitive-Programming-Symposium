from fractions import Fraction  

def solution(pegs):

    if (len(pegs) % 2) == 0:
        even = True
    else:
        even = False

    if even:
        sum = pegs[len(pegs) - 1] - pegs[0]
    else:
        sum = pegs[len(pegs) - 1] + pegs[0]

    if (len(pegs) > 2):
        for index in range(1, len(pegs) - 1):
            sum += 2 * (-1)**(index+1) * pegs[index]

    FirstGearRadius = Fraction(2 * (float(sum)/3 if even else sum)).limit_denominator()

    if FirstGearRadius < 2:
        return [-1,-1]

    currentRadius = FirstGearRadius
    for index in range(0, arrLength-2):
        CenterDistance = pegs[index+1] - pegs[index]
        NextRadius = CenterDistance - currentRadius
        if (currentRadius < 1 or NextRadius < 1):
            return [-1,-1]
        else:
            currentRadius = NextRadius

    return [FirstGearRadius.numerator, FirstGearRadius.denominator]

if __name__ == "__main__":
    print("Solution:\t{}".format(solution([4, 30, 50])))
    print("Solution:\t{}".format(solution([4, 17, 50])))