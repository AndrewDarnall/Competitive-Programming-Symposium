def compute_leaps(line_1, line_2):
    possible_leaps = 0
    original_entropy = 1 * abs(line_2[line_1[1]] - line_2[line_1[2]])
    N = line_1[0]
    for i in range(N):
        for j in range(N):
            if i != j:
                new_entropy = 1 * abs(line_2[i] - line_2[j])
                if new_entropy >= original_entropy:
                    print("Possible State:\t{}".format((i,j)))
                    possible_leaps += 1
    return possible_leaps



input_data_1 = input("Enter N x y: ")
input_data_2 = input("Enter energey levels: ")

# Split the input string into a list of numbers
line_1 = list(map(int, input_data_1.split()))
line_2 = list(map(int, input_data_2.split()))

print("Possible Leaps From the Frog Particle:\t{}".format(compute_leaps(line_1, line_2)))