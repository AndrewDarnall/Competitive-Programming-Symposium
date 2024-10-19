import sys

if len(sys.argv) != 2:
    print("usage:\t{}\t<input-file.txt>".format(sys.argv[0]))
    sys.exit(-1)

fh = open(sys.argv[1])
of = open("output.txt", "+w")
for line in fh:
    lst = line.split()
    letter = lst[0]
    lst = lst[1:]
    pos = []
    for word in lst:
        i = 0
        for ltr in word:
            if letter == ltr:
                pos.append(str(i))
            i += 1
    if len(pos) == 0:
        of.write("none\n")
    else:
        result = " ".join(pos)
        result += "\n"
        of.write(result)

print("finished")

# Solution is 100% correct