__author__ = 'Amin'

import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

N = int(raw_input())  # Number of elements which make up the association table.
Q = int(raw_input())  # Number Q of file names to be analyzed.

known_extensions = []
mime_types = []

for i in xrange(N):
     # EXT: file extension
     # MT: MIME type.
    EXT, MT = raw_input().split()
    known_extensions.append(EXT.lower())
    mime_types.append(MT)
for i in xrange(Q):
    FNAME = raw_input() # One file name per line.

    index_of_last_dot = FNAME.rfind(".")


    if index_of_last_dot != -1:
        # filename is not important
        extension = FNAME[index_of_last_dot+1:].lower()
    else:
        extension = ""

    print >> sys.stderr, "Extension: " + extension

    answer = "UNKNOWN"
    if extension != "":
        try:
            index = known_extensions.index(extension)
            #print >> sys.stderr, "Index: " + str(index)
            answer = mime_types[index]
        except ValueError:
            pass

    # Write an action using print
    # To debug: print >> sys.stderr, "Debug messages..."

    # For each of the Q filenames, display on a line the corresponding MIME type.
    # If there is no corresponding type, then display UNKNOWN.
    print answer
