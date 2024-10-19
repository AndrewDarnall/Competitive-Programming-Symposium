import sys

if len(sys.argv) != 2:
    print("usage:\t{}\t<input-file.txt>".format(sys.argv[0]))
    sys.exit(-1)

vowels = ['a', 'e', 'i', 'o', 'u']

fh = open(sys.argv[1])
of = open("output.txt", "+w")
for line in fh:
    words = line.split()
    words = words[1:]
    result = []
    for word in words:
        w_list = list(word)
        for i in range(5):
            while vowels[i] in w_list:
                w_list.remove(vowels[i])
        mid = "".join(w_list)
        result.append(mid)
    output = " ".join(result) + "\n"
    of.write(output)

print("finished")

# Solution 100% complete