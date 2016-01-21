__author__ = 'Amin'

import sys
import math


# Test 1 -
# Provided Input: Abcde fghij klmno pqrs tuv wxyz
# Expected Output: true
# Test 2 -
# Provided Input: this sentence does not have what it should
# Expected Output: false
# Test 3 -
# Provided Input: Portez ce vieux whisky au juge blond qui fume
# Expected Output: true
# Test 4 -
# Provided Input: abcde ghijklmnopqrstuvwxyz
# Expected Output: false
# Test 5 -
# Provided Input: abcde fghij klmno pqrs tuv wxyy
# Expected Output: false
def upper_letter():
    s = input()

    flag_upper = False
    for c in s:
        if c.isupper():
            flag_upper = True

    if flag_upper:
        print("true")
    else:
        print("false")


# Test 1 -
# Provided Input: 169 104
# Expected Output: 13
# Test 2 -
# Provided Input: 100 250
# Expected Output: 50
# Test 3 -
# Provided Input: 1 1
# Expected Output: 1
# Test 4 -
# Provided Input: 1000000 5
# Expected Output: 5
# Test 5 -
# Provided Input: 104711 104717
# Expected Output: 1
# Test 6 -
# Provided Input: 98304 65536
# Expected Output: 32768
def _gcd(m, n):
    while True:  # petla, czyli "wroc do kroku", tylko ze oznaczone u celu, a nie na poczatku skoku. W pythonie nie ma goto (prawie...;))
        r = m % n  # przypisanie reszty
        if not r:  # jesli r rowne 0 to
            return n  # zwroc n
        m, n = n, r  # w przeciwnym przypadku przypisz co trzeba i powtorz


def greatest_common_divisor():
    a, b = [int(i) for i in input().split()]

    m = _gcd(a, b)

    print(m)


# Test 1 -
# Provided Input: 5 2
# Expected Output: 1 2 4 8 16
def print_powers():
    n, r = [int(i) for i in input().split()]

    l = []
    for i in range(n):
        l.append(pow(r, i))

    p = ""
    for k in l:
        p += str(k) + " "
    print(p[:-1])


# convert int values to 0-1 representation
def _convert_to_bin_string(x):
    l = []
    flag_c = True
    v = x
    while flag_c:
        if v > 1:
            if v % 2 == 1:
                l.append(1)
            else:
                l.append(0)
            v = v // 2
        else:
            if v == 1:
                l.append(1)
            else:
                l.append(0)
            flag_c = False

    r = ""
    for i in reversed(l):
        r += str(i)
    return r


def print_as_binary():
    n = int(input())

    for i in range(n):
        x = int(input())
        # three different ways
        #print(_convert_to_bin_string(x))
        #print(bin(x)[2:])
        print("{0:b}".format(x))


def _convert_to_int(c):
    if c == "F":
        return 15
    elif c == "E":
        return 14
    elif c == "D":
        return 13
    elif c == "C":
        return 12
    elif c == "B":
        return 11
    elif c == "A":
        return 10
    else:
        return int(c)


# you are provided with a number in hexadecimal format and should convert it to decimal value
def hex_string_to_int_value():
    number = input()

    print("number: " + str(number), file=sys.stderr)

    r=0
    for i, c in enumerate(reversed(number)):
        v = _convert_to_int(c)
        r += 16**i * v

    print(r)


if __name__ == "__main__":

    upper_letter()

    greatest_common_divisor()

    print_powers()

    print_as_binary()

    hex_string_to_int_value()

