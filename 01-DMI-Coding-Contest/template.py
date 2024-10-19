import sys

if len(sys.argv) != 2:
    print("usage:\t{}\t<input-file.txt>".format(sys.argv[0]))
    sys.exit(-1)

with open(sys.argv[1]) as fh, open("output.txt", "+w") as of:
    for line in fh:
        print()

print("finished.")