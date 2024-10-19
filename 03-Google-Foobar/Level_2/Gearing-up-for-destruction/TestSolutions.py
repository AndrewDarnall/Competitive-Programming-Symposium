import solution3

def test1(pegs):
    if solution3.solution4(pegs) == (12,1):
        print("TEST 1 - PASSED")
    else:
        print("TEST 1 - FAILED")

def test2(pegs):
    if solution3.solution4(pegs) == (-1,-1):
        print("TEST 2 - PASSED")
    else:
        print("TEST 2 - FAILED")

# This code snippet makes sure that the code is only activated within this source file
if __name__ == "__main__":
    test1([4, 30, 50])
    test2([4, 17, 50])