__author__ = 'Amin'

import sys
import math

from collections import deque
import copy

from codingame_solutions.very_hard.very_hard_The_Resistance_utils import load_from_file, load_from_input, load_from_prepared_data
from codingame_solutions.very_hard.very_hard_The_Resistance import generate_morse_dictionary, print_morse_dict_info

import cProfile


class Solution:
    def __init__(self, position_in_dictionary, words_thus_far=[], number_of_words_thus_far=0, part_to_use_start_index=0, part_in_use_end_index=1):
        self.position_in_dictionary = position_in_dictionary
        self.words_thus_far = words_thus_far
        self.number_of_words_thus_far = number_of_words_thus_far
        self.part_to_use_start_index = part_to_use_start_index
        self.part_in_use_end_index = part_in_use_end_index


def process_solutions(solutions, message, morse_dictionary):
    results = []

    # keep solutions on stack, and do one after another
    while len(solutions) > 0:

        # get one solution
        current_solution = solutions.popleft()

        flag_no_more_elements = False
        # if solution still has signs to process and its pointer to dictionary is valid
        while current_solution.part_in_use_end_index < len(message) and not flag_no_more_elements:
            # get new sign to process
            current_sign = message[current_solution.part_in_use_end_index]
            # add it to the collections holding currently processed set of signs
            current_solution.part_in_use_end_index += 1
            # get next element from dictionary based on current sign
            current_solution.position_in_dictionary = current_solution.position_in_dictionary.get_next(current_sign)

            # if new position is valid
            if current_solution.position_in_dictionary is not None:
                # if there are some words for this position
                if current_solution.position_in_dictionary.flag_holds_words:
                    # spawn new solution that continue looking for longer words
                    solutions.append(Solution(
                        current_solution.position_in_dictionary,
                        copy.deepcopy(current_solution.words_thus_far),
                        current_solution.number_of_words_thus_far,
                        current_solution.part_to_use_start_index,
                        current_solution.part_in_use_end_index
                    ))

                    # get all available words
                    words_found = current_solution.position_in_dictionary.words

                    # clear currently processed set of signs
                    current_solution.part_to_use_start_index = current_solution.part_in_use_end_index - 1
                    # and set dictionary pointer to first element
                    current_solution.position_in_dictionary = morse_dictionary
                    current_solution.number_of_words_thus_far += 1

                    # for all words except last spawn new solutions
                    for word in words_found[:-1]:
                        new_words_thus_far = copy.deepcopy(current_solution.words_thus_far)
                        new_words_thus_far.append(word)
                        solutions.append(Solution(
                            current_solution.position_in_dictionary,
                            new_words_thus_far,
                            current_solution.number_of_words_thus_far,
                            current_solution.part_to_use_start_index,
                            current_solution.part_in_use_end_index
                        ))

                    current_solution.words_thus_far.append(words_found[-1])
            else:
                flag_no_more_elements = True

        if current_solution is not None and current_solution.part_in_use_end_index - current_solution.part_to_use_start_index == 1:
            results.append(current_solution.words_thus_far)

    return results


def process_and_print_results(results):
    r = ""
    for result in results:
        r += str(result) + "\n"

    print("result: " + r, file=sys.stderr)

    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr)

    print(len(results))


def main():
    #message, words, words_in_morse = load_from_prepared_data()
    message, words, words_in_morse = load_from_file("very_hard_The_Resistance_test_4.txt")

    morse_dictionary = generate_morse_dictionary(words, words_in_morse)
    print_morse_dict_info(morse_dictionary)

    solutions = deque()

    solutions.append(Solution(
        position_in_dictionary=morse_dictionary,
        words_thus_far=[],
        part_to_use_start_index=0,
        part_in_use_end_index=0
    ))

    results = process_solutions(solutions, message, morse_dictionary)

    process_and_print_results(results)

if __name__ == '__main__':
    cProfile.run('main()')
