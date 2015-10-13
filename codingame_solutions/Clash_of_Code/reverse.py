__author__ = 'Amin'


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


NWD:
import sys
import math

def nwd( m, n ):
    while True: # petla, czyli "wroc do kroku", tylko ze oznaczone u celu, a nie na poczatku skoku. W pythonie nie ma goto (prawie...;))
        r = m % n # przypisanie reszty
        if not r: # jesli r rowne 0 to
            return n # zwroc n
        m, n = n, r # w przeciwnym przypadku przypisz co trzeba i powtorz

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

a, b = [int(i) for i in input().split()]

m= nwd(a, b)

print(str(a-b), file=sys.stderr)
print(str(a+b), file=sys.stderr)
print(str(a*b), file=sys.stderr)
print(str(m), file=sys.stderr)

# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)

print(m)



import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n, r = [int(i) for i in input().split()]

# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)

l = []
for i in range(n):
    l.append(pow(r, i))

p = ""
for k in l:
    p += str(k) + " "
print(p[:-1])
#print("N numbers...")



if __name__ == "__main__":
