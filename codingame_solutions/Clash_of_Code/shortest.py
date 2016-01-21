__author__ = 'Amin'

import sys
import math

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
 if sum(l[0:3])==sum(l[3:6]):print("true")
 else:print("false")


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
 l=[0]*40
 for c in input():
  if c!=" ":l[ord(c)-97]+=1
 print(max(l))

# list of values is given, sort them and print
def sort_values():
 v=[]
 for i in range(int(input())):
  v.append(int(input()))
 v.sort()
 print(v)

# TODO:
# The Hofstadter Conway sequence is defined like so:
# a(1) = 1.
# a(2) = 1.
# a(n) = a(a(n - 1)) + a(n - a(n - 1)), for n > 2.
# Your program must ouput the first N terms of this sequence.

def a(n):
 if n<3:
     return 1
 else:
  return a(a(n-1)+a(n-a(n-1)))
 # try converting to this:
 #return(a(a(n-1)+a(n-a(n-1))),1)[n<3]

# C version from Kuba:
# N,i;
# int a(int b){return b<3?1:(a(a(b-1))+a(b-a(b-1)));};
# int main()
# {
# scanf("%d",&N);
# for(i=1;i<N;i++)
# printf("%d ",a(i));
# printf("%d\n"",a(N));
# }


# Given a certain number of blocks N, your program must return the height of the tallest possible 2D pyramid that can be created, followed by the number of unused blocks remaining.
# For example, a pyramid of height 3 contains 6 blocks: 3 for the first level, 2 for the second level and 1 for the last level.
# INPUT:
# Line 1: An integer N, the number of blocks to be used for the pyramid.
# OUTPUT:
# Line 1: Two integers H and R, where H is the greatest possible pyramid height, and R is the remaining unused blocks.
# CONSTRAINTS:
# 0 ? N < 50000
# EXAMPLE:
# Input
# 10
# Output
# 4 0

# general version
#     n=int(input())
#     flag_continue = True
#     h=0
#     r=n
#     while flag_continue:
#         print("h: " + str(h), file=sys.stderr)
#         print("r: " + str(r), file=sys.stderr)
#         if r>=(h+1):
#             h+=1
#             r-=h
#         else:
#             flag_continue = False
#     print(str(h) + " " + str(r))

def tallest_pyramid():
 f,h=1,0
 r=int(input())
 while f:
  if r>=h+1:h+=1;r-=h
  else:f=0
 print(str(h)+" "+str(r))


# The program:
# Your given a scrambled sentence. You must output an unscrambled version of the same sentence using these rules:
# - First, print one in every two characters.
# - Then print every other character starting from the end, going backwards. Make sure you handle strings of both even and odd lengths.
def scrambled():
 s=input();print(s[0::2]+s[1::2][::-1])


if __name__ == "__main__":

    hours_and_minutes_to_minutes()

    lucky_number()

    duel()

    split_text_into_columns()

    operation_or()

    midpoint()

    most_common_letter()

    sort_values()

    # Hofstadter Conway done but without reading values etc

    tallest_pyramid()

    scrambled()
