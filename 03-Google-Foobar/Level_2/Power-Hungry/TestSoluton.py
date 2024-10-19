import finalSolution

def test1(input):
    if finalSolution.solution(input) == "8":
        print("TEST 1 - PASSED")
    else:
        print("TEST 1 - FAILED")

def test2(input):
    if finalSolution.solution(input) == "60":
        print("TEST 2 - PASSED")
    else:
        print("TEST 2 - FAILED")

test1([2, 0, 2, 2, 0])
test2([-2, -3, 4, -5])