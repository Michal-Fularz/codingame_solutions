__author__ = 'Amin'

# COMPLETED
# PYTHON 3.x

import sys
import math


def o_1(n: int):
    return 1


def o_log_n(n: int):
    return math.log2(n)


def o_n(n: int):
    return n


def o_n_log_n(n: int):
    return n * math.log2(n)


def o_n_2(n: int):
    return n * n


def o_n_2_log_n(n: int):
    return n * n * math.log2(n)


def o_n_3(n: int):
    return n * n * n


def o_2_n(n: int):
    return math.pow(2, n)

def normalize_difference(difference: float, n: int):
    normalized_difference = difference / n
    normalized_difference = abs(1 - normalized_difference)
    return normalized_difference


number_of_elements = int(input())

times = []
nums = []
for i in range(number_of_elements):
    num, t = [int(j) for j in input().split()]
    times.append(t)
    nums.append(num)

# calculate differences
differences = [0]*8
for t_previous, t, num_previous, num in zip(times[:-1], times[1:], nums[:-1], nums[1:]):

    t_quotient = t / t_previous
    t_quotient_o_1 = o_1(num) / o_1(num_previous)
    t_quotient_o_log_n = o_log_n(num) / o_log_n(num_previous)
    t_quotient_o_n = o_n(num) / o_n(num_previous)
    t_quotient_o_n_log_n = o_n_log_n(num) / o_n_log_n(num_previous)
    t_quotient_o_n_2 = o_n_2(num) / o_n_2(num_previous)
    t_quotient_o_n_2_log_n = o_n_2_log_n(num) / o_n_2_log_n(num_previous)
    t_quotient_o_n_3 = o_n_3(num) / o_n_3(num_previous)
    #t_quotient_o_2_n = o_2_n(num) / o_2_n(num_previous)

    differences[0] += t_quotient / t_quotient_o_1
    differences[1] += t_quotient / t_quotient_o_log_n
    differences[2] += t_quotient / t_quotient_o_n
    differences[3] += t_quotient / t_quotient_o_n_log_n
    differences[4] += t_quotient / t_quotient_o_n_2
    differences[5] += t_quotient / t_quotient_o_n_2_log_n
    differences[6] += t_quotient / t_quotient_o_n_3
    #differences[7] += t_quotient / t_quotient_o_2_n

# this can be somehow tricky (it was for me, when I was writing this)
# in short it changes each element of the list using the function provided
# it can be done without the function, it is used for readability
differences[:] = [normalize_difference(diff, number_of_elements-1) for diff in differences]

for diff in differences:
    print(str(diff), file=sys.stderr)

minimal_difference = min(differences)
index_of_minimal_difference = differences.index(minimal_difference)

print("Minimal difference: " + str(minimal_difference), file=sys.stderr)
print("Index: " + str(index_of_minimal_difference), file=sys.stderr)

# IMPORTANT: as calculating 2^n is impossible for most of the cases (overflow errors), we use a special trick
if minimal_difference > 0.1:
    index_of_minimal_difference = 7

# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)

r = ""
if index_of_minimal_difference == 0:
    r = "O(1)"
elif index_of_minimal_difference == 1:
    r = "O(log n)"
elif index_of_minimal_difference == 2:
    r = "O(n)"
elif index_of_minimal_difference == 3:
    r = "O(n log n)"
elif index_of_minimal_difference == 4:
    r = "O(n^2)"
elif index_of_minimal_difference == 5:
    r = "O(n^2 log n)"
elif index_of_minimal_difference == 6:
    r = "O(n^3)"
elif index_of_minimal_difference == 7:
    r = "O(2^n)"
else:
    print("Wrong index!", file=sys.stderr)

print(r)
