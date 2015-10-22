__author__ = 'Amin'


# convert value provided as HH:MM to a number of minutes
def hours_and_minutes_to_minutes():
    d=input()
    print((int(d[0])*60+int(d[1])*6+int(d[3])*10+int(d[4])))


# check if provided number is lucky - sum of first three digits is equal to sum of next three digits
# eg.
# 111003 true
# 202121 true
def lucky_number():
    l=[int(i) for i in input()]
    if sum(l[0:3])==sum(l[3:6]):print "true"
    else:print "false"


# Two adventurers are going to duel, each of them has health points HP1 and HP2 and apply D1 and D2 damage at their opponents each round.
# Your program must output which adventurer win and how many round are needed to end the duel.
# There are no draw.
def duel():
    h1, d1 = [int(i) for i in input().split()]
    h2, d2 = [int(i) for i in input().split()]

    # TODO - this is bad! does not work for all possibilities
    if d2==0:
        d2=0.001
    # TODO - add extra check for d1!

    nm2=h1%d2
    n2 = h1//d2

    nm1=h2%d1
    n1=h2//d1

    if nm2!=0:
        n2+=1
    if nm1!=0:
        n1+=1

    if n1<n2:
        print("1 "+str(n1))
    else:
        print("2 "+str(n2))


# Your program must prepare a sentence for encryption and reshape it in a grid.
# You are given a sentence and a number of columns col.
# First, you need to remove all whitespaces.
# Then divide the processed text into parts of col characters each.
# The last part can contain less than col letters.
# Each part is placed on the new line.
# INPUT:
# Line 1: a text sentence.
# Line 2: an integer number col.
# OUTPUT:
# The text grid with col columns.
# CONSTRAINTS:
# 0 ? sentence length ? 100
# 0 < col ? 10
# A text contains at least one non-whitespace character.
# EXAMPLE:
# Input
# Hello Perfect World
# 5
# Output:
# Hello
# Perfe
# ctWor
# ld
def split_text_into_columns():
    s=input().replace(" ", "")
    c=int(input())
    r=s[0]
    for i in range(1,len(s)):
     if i%c==0:r+="\n"
     r+=s[i]
    print(r)


# Your program must perform a binary OR on two binary numbers given through the standard input and print the result to the standard output.
# OR Truth Table
# Input	Output
# A	B
# 0	0	0
# 0	1	1
# 1	0	1
# 1	1	1
# Warning, the number in output must have the same number of digits as the given numbers.
# INPUT:
# 2 binary numbers n1 and n2, separated by spaces.
# OUTPUT:
# The result of an OR between n1 and n2.
# CONSTRAINTS:
# n1 and n2 have the same number of digits.
# EXAMPLE:
# Input: 001 011
# Output: 011
def operation_or():
    n,m=input().split()
    r=""
    for k,l in zip(n,m):
     if k=="1" or l=="1":r+="1"
     else:r+="0"
    print(r)


# Your program must find the point that is exactly between two other points.
# You are given the coordinates (x, y) of two points which bind a line segment.
# The midpoint of this line segment is the target point.
# Be careful with float numbers and use . as a decimal mark.
def midpoint():
    x,y=[int(i)for i in input().split()]
    X,Y=[int(i)for i in input().split()]
    a=(x+X)/2
    b=(y+Y)/2
    if a-int(a)==0:a=int(a)
    if b-int(b)==0:b=int(b)
    print(str(a)+" "+str(b))


# How many times is the most common letter used in a given string?
# The string only contains lowercase letters and spaces.
def most_common_letter():
    w=input()
    l=[0]*40
    for c in w:
     if c!=" ":l[ord(c)-97]+=1
    print(max(l))

# list of values is given, sort them and print
def sort_values():
    n=int(raw_input())
    v=[]
    for i in range(n):
        v.append(int(raw_input()))
    v.sort()
    print(v)


if __name__ == "__main__":
    #split_text_into_columns()
    sort_values()