import sys
import Levenshtein

if len(sys.argv) != 2:
    print("usage:\t{}\t<input-file.txt>".format(sys.argv[0]))
    sys.exit(-1)

def ispalindrome(word):
    count = 0
    palindrome = False
    for i in range(0, len(word)):
        if word[i] == word[len(word) - 1 - i]:
            count += 1
    if count >= len(word) - 2:
        palindrome = True
    return palindrome

fh = open(sys.argv[1])
of = open("output.txt", "+w")
for line in fh:
    ln = line.split()
    ln = ln[1:]
    result = []
    for word in ln:
        accum = ""
        for letter in word[::-1]:
            accum += letter
        if ispalindrome(word):
            result.append(word)
    output = str(len(result)) + " "
    output += " ".join(result)
    output += "\n"
    of.write(output)

print("finished.")

# Solution 100% correct