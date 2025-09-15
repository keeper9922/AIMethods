import itertools
import math
square = [1, 2, 3,
          4, 5, 6,
          7, 8, 9]
def result(sqr: list) -> bool | tuple[bool, list, ...]:
    n = len(sqr)
    jump = int(math.sqrt(n))

    magical_constant = (jump * (jump*jump + 1)) / 2 # эвристика
    row_sum = []
    column_sum = []
    diagonal_sum = []
    # линии
    for i in range(jump):
        s = 0
        for j in range(jump):
            s += sqr[j+jump*i]
        row_sum.append(s)
    # колонки
    for i in range(jump):
        s = 0
        for j in range(jump):
            s += sqr[i+jump*j]
        column_sum.append(s)
    # диагонали
    s1, s2 = 0, 0
    for i in range(jump):
        s1 += sqr[i+i*jump]
        s2 += sqr[(jump-1)*(i+1)]
    diagonal_sum.append(s1)
    diagonal_sum.append(s2)
    # print(magical_constant)
    # print(row_sum)
    # print(column_sum)
    # print(diagonal_sum)
    for i in range(jump):
        if row_sum[i] != magical_constant:
            return False
        if column_sum[i] != magical_constant:
            return False
    if diagonal_sum[0] != magical_constant or diagonal_sum[1] != magical_constant:
        return False
    return True, row_sum, column_sum, diagonal_sum


def check(numbers: list):
    squares = itertools.permutations(numbers)
    for i in squares:
        r = result(i)
        if r:
            print(i, "\n", r[1], r[2], r[3])
            jump = int(math.sqrt(len(i)))
            for j in range(jump):
                print(i[0+j*jump], i[1+j*jump], i[2+j*jump])
            return

check(square)
