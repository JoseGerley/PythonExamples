

import math
import os
import random
import re
import sys

first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

m = int(first_multiple_input[1])

matrix = []

for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)

matrix_transpose = [[matrix[j][i] for j in range(n)] for i in range(m)]
matrix_transpose = [y for x in matrix_transpose for y in x]
msj_initial = "".join(matrix_transpose)
msj_initial  = re.sub(r'(?<=[a-zA-Z0-9])[^a-zA-Z0-9]+(?=[a-zA-Z0-9])', ' ', msj_initial)
print(msj_initial)
    