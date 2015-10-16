__author__ = 'Amin'


def dna(s):
    nuclobases = ["A", "T", "C", "G"]
    nuclobases_complementary = ["T", "A", "G", "C"]

    r = ""
    for c in s:
        if c in nuclobases:
            index = nuclobases.index(c)
            r += nuclobases_complementary[index]

    return r


def dna_if(s):
    r = ""
    for c in s:
        if c == "A":
            r += "T"
        elif c == "T":
            r += "A"
        elif c == "C":
            r += "G"
        elif c == "G":
            r += "C"
        else:
            r += c

    return r


def l33t(s):
    normal_speach = "EeAaOo"
    l33t_speach = "334400a"

    for ns, ls in zip(normal_speach, l33t_speach):
        s = s.replace(ns, ls)

    return s


def count_letters(s):
    count = 0
    for c in s:
        if c.lower() or c.upper():
            count += 1

    return count


def sum_of_letters_values(s):
    sum_of_letters = 0
    for c in s:
        sum_of_letters += ord(c)

    return sum_of_letters


def sort_tuples():
    n = int(input())

    elements = []
    for i in range(n):
        item, distance = input().split()
        distance = float(distance)
        elements.append((item, distance))

    elements_sorted = sorted(elements, key=lambda tup: tup[1])
    r = ""
    for x, y in reversed(s):
        r += x + " "

    print(r[:-1])


# you are provided with a and b coefficients and then for each calc you have to calculate y=a*x+b
# and print each y in separate line
def linear_function():
    a, b = [int(i) for i in input().split()]
    n = int(input())

    for i in range(n):
        x = int(input())
        y = a * x + b
        print(y)


if __name__ == "__main__":
    linear_function()
    s = raw_input()
    print dna(s)
    print dna_if(s)
    print l33t(s)
    print count_letters(s)