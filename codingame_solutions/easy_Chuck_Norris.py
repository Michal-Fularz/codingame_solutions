__author__ = 'Amin'

import sys
import math


def prepare_answer(bit_type, count, flag_without_trailing_space=False):
    answer = ""
    if bit_type == 1:
        answer += "0"
    else:
        answer += "00"
    answer += " "
    for i in xrange(0, count):
        answer += "0"
    if not flag_without_trailing_space:
        answer += " "
    return answer

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

MESSAGE = raw_input()

characters = list(MESSAGE)
bits = []
for char in characters:
    # iterate over each bit
    for i in reversed(xrange(0, 7)):
        bit = (ord(char) >> i) & 0x01
        bits.append(bit)

answer = ""

bit_type = 0
count = 0

for bit in bits:
    if count == 0:
        if bit == 1:
            bit_type = 1
        else:
            bit_type = 0
        count += 1
    else:
        if bit != bit_type:
            # the sign has changed
            answer += prepare_answer(bit_type, count)
            bit_type = bit
            count = 1
        else:
            count += 1

# add the last part (accumulated but not added to answer)
answer += prepare_answer(bit_type, count, True)
# instead of using flag in function it is possible to just remove last character
# (space) like this
#answer = answer[:-1]

# Write an action using print
# To debug: print >> sys.stderr, "Debug messages..."
print answer
