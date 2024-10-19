import sys

if len(sys.argv) != 2:
    print("usage:\t{}\t<input-file.txt>".format(sys.argv[0]))
    sys.exit(-1)

fh = open(sys.argv[1])
of = open("output.txt", "+w")
for line in fh:
    numbers = line.split()
    numbers = numbers[1:]
    int_nums = []
    for number in numbers:
        int_nums.append(int(number))
    of.write(str(max(int_nums)) + "\n")

print("finished")

# Excercise is 100% correct