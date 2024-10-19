from utils import create_matrix, get_matrix_list

import sys
import numpy as np

if len(sys.argv) != 2:
    print("usage:\t{}\t<input-file.txt>".format(sys.argv[0]))
    sys.exit(-1)

with open(sys.argv[1]) as fh, open("output.txt", "+w") as of:
    for line in fh:
        split_line = line.strip().split(" ")
        inputs = [int(element) for element in split_line]
        n = inputs[0]
        m = inputs[1]
        p = inputs[2]
        mat_1 = create_matrix(inputs[3 : 3 + (n*m)], n, m)
        mat_2 = create_matrix(inputs[3 + (n*m) : ], m, p)
        mat_3 = np.dot(mat_1, mat_2)
        res_list = get_matrix_list(mat_3)
        of.writelines(f"{number} " for number in res_list)
        of.write(f"\n")

print("finished.")