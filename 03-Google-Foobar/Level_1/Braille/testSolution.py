import solution

def test1(input):
    if solution.solution(input) == "000001011110110010100010000000111110101001010100100100101000000000110000111010101010010111101110000000110100101010101101000000010110101001101100111100011100000000101010111001100010111010000000011110110010100010000000111000100000101011101111000000100110101010110110":
        print("TEST 1 - PASSED")
    else:
        print("TEST 1 - FAILED")

def test2(input):
    if solution.solution(input) == "100100101010100110100010":
        print("TEST 2 - PASSED")
    else:
        print("TEST 2 - FAILED")

def test3(input):
    if solution.solution(input) == "000001110000111010100000010100111000111000100010":
        print("TEST 3 - PASSED")
    else:
        print("TEST 3 - FAILED")

test1("The quick brown fox jumps over the lazy dog")
test2("code")
test3("Braille")