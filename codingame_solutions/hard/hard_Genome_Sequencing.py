__author__ = 'Amin'

import sys
import math
import itertools


class Match:
    def __init__(self):
        self.word1 = ""
        self.word2 = ""
        self.matched_part = ""


def find_connections(word1, word2):

    longest_matched_part = ""

    # check form first letter of word1 if it can be matched to beginning of word 2
    for i in range(len(word1)):
        matched_part = ""
        w1_match_index = i
        w2_match_index = 0
        # ATTENTION: it is important which of the condition is checked first!
        # word1[w1_match_index] == word2[w2_match_index] requires indexes to be within appropriate ranges
        while w1_match_index < len(word1) and w2_match_index < len(word2) and word1[w1_match_index] == word2[w2_match_index]:
            w1_match_index += 1
            w2_match_index += 1
            matched_part += word1[i]

        if len(matched_part) > len(longest_matched_part):
            longest_matched_part = matched_part

    if len(longest_matched_part) > 0:
        print("Started from: " + str(i) + ", matched part: " + longest_matched_part, file=sys.stderr)
    else:
        print("No matches found", file=sys.stderr)


sub_sequences = []

n = int(input())
for i in range(n):
    sub_sequences.append(input())

# for i in range(len(sub_sequences)):
#     word1 = sub_sequences[i]
#     for j in range(i+1, len(sub_sequences)):
#         word2 = sub_sequences[j]
#         print("Words: " + word1 + ", " + word2, file=sys.stderr)
#         find_connections(word1, word2)
#         print("Words: " + word2 + ", " + word1, file=sys.stderr)
#         find_connections(word2, word1)

indexes = [i for i in range(0, len(sub_sequences))]
permutations = list(itertools.permutations(indexes, len(sub_sequences)))
print(permutations)

for indexes in permutations:
    word1 = sub_sequences[indexes[0]]
    word2 = sub_sequences[indexes[1]]
    print("Words: " + word1 + ", " + word2, file=sys.stderr)
    find_connections(word1, word2)


# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)

print("answer")

