__author__ = 'Amin'

import sys
import math

# COMPLETED
# PYTHON 3.x

n = int(input())
whole_file = ""
for i in range(n):
    cgxline = input()
    whole_file += cgxline

whole_file = whole_file.strip()

r = ""

flag_string = False
intend = 0
for c in whole_file:

    # register strings
    if c == "'" and not flag_string:
        flag_string = True
        r += c
    elif c == "'" and flag_string:
        flag_string = False
        r += c
    elif flag_string:
        r += c
    elif not flag_string:
        if c == " " or c == "\t":
            # ignore whitespace while not in string
            pass
        # special case of bracket after equal sign
        elif c == "(" and len(r) > 0 and r[-1] == "=":
            r += "\n"
            for i in range(intend):
                r += "    "
            r += c + "\n"
            intend += 1
            for i in range(intend):
                r += "    "
        elif c == "(":
            r += c + "\n"
            intend += 1
            for i in range(intend):
                r += "    "
        elif c == ")":
            # special case for empty parts of left bracket, right bracket
            last_bracket_index = str.rfind(r, "(")
            text_from_last_bracket = r[last_bracket_index:].strip(" ")
            if text_from_last_bracket == "(\n":
                r = r[:last_bracket_index+1]
            r += "\n"
            intend -= 1
            for i in range(intend):
                r += "    "
            r += c
        elif c == ";":
            r += c + "\n"
            for i in range(intend):
                r += "    "
        else:
            r += c

# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)

print(r)
