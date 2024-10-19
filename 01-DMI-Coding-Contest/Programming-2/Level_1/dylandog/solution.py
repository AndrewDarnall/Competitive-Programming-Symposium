import sys

if len(sys.argv) != 2:
    print("usage:\t{}\t<input-file.txt>".format(sys.argv[0]))
    sys.exit(-1)

fh = open(sys.argv[1])
of = open("output.txt", "+w")
for line in fh:
    pos = 0
    lst = line.split()
    num = lst[1]
    lst = lst[2:]
    if num in lst:
        pos = lst.index(num) + 1
    of.write(str(pos) + "\n")

print("finished.")

# Solution 100% correct