import sys

if len(sys.argv) != 2:
    print("usage:\t{}\t<input-file.txt>".format(sys.argv[0]))
    sys.exit(-1)

fh = open(sys.argv[1])
of = open("output.txt", "+w")
for line in fh:
    print()

print("finished.")