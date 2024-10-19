import sys

if len(sys.argv) != 2:
    print("usage:\t{}\t<input-file.txt>".format(sys.argv[1]))
    sys.exit(-1)

fh = open(sys.argv[1])
of = open("output.txt", "+w")
for line in fh:
    lst = line.split()
    lst = lst[1:]
    doppioni = 0
    lst.sort()
    trace = lst[0]
    lst = lst[1:]
    for item in lst:
        if trace == item:
            doppioni += 1
        trace = item
    of.write(str(doppioni) + "\n")

print("finished.")

# Solution is 100% correct