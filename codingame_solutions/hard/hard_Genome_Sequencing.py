__author__ = 'Amin'

# COMPLETED
# PYTHON 3.x

import sys
import math
import itertools


def find_connections2(word1, word2):

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

    return len(longest_matched_part)

def find_connections(word1, word2):

    if word2 in word1:
        return len(word2)

    longest_matched_part = ""

    # calculate where to start based on the size of the words e.g.
    # AGATTA and TA we should start with index 4
    if len(word1) > len(word2):
        starting_index = len(word1) - len(word2)
    else:
        starting_index = 0

    # check form first letter of the word1 if it can be matched to the beginning of word 2
    for i in range(starting_index, len(word1)):
        w1_match_index = i
        w2_match_index = 0

        flag_matched = True
        while flag_matched and w1_match_index < len(word1): # and w2_match_index < len(word2):
            if word1[w1_match_index] != word2[w2_match_index]:
                flag_matched = False
            w1_match_index += 1
            w2_match_index += 1

        if flag_matched:
            matched_part = word1[i:]
        else:
            matched_part = ""

        if len(matched_part) > len(longest_matched_part):
            longest_matched_part = matched_part

    if len(longest_matched_part) > 0:
        print("Started from: " + str(i) + ", matched part: " + longest_matched_part, file=sys.stderr)
    else:
        print("No matches found", file=sys.stderr)

    return len(longest_matched_part)


sub_sequences = []

n = int(input())
for i in range(n):
    sub_sequences.append(input())

indexes = [i for i in range(0, len(sub_sequences))]
indexes_permutations = list(itertools.permutations(indexes, len(sub_sequences)))
print("Permutations: " + str(indexes_permutations), file=sys.stderr)

length_of_dna_sequence = 0
for sub_sequence in sub_sequences:
    length_of_dna_sequence += len(sub_sequence)

minimal_length_of_dna_sequence = length_of_dna_sequence
for indexes_permutation in indexes_permutations:
    current_length_of_dna_sequence = length_of_dna_sequence
    for index_1, index_2 in zip(indexes_permutation[:-1], indexes_permutation[1:]):
        word1 = sub_sequences[index_1]
        word2 = sub_sequences[index_2]
        print("Words: " + word1 + ", " + word2, file=sys.stderr)
        current_length_of_dna_sequence -= find_connections(word1, word2)

    if current_length_of_dna_sequence < minimal_length_of_dna_sequence:
        minimal_length_of_dna_sequence = current_length_of_dna_sequence

# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)

print(minimal_length_of_dna_sequence)

# AACCGG
# AACCTT
