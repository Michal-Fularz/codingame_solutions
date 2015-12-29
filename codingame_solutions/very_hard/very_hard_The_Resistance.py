__author__ = 'Amin'

import sys
import math
from collections import deque
import copy

import cProfile

from codingame_solutions.very_hard.very_hard_The_Resistance_utils import Morse
from codingame_solutions.very_hard.very_hard_The_Resistance_utils import load_from_file, load_from_input, load_from_prepared_data


class MorseDictionaryElement:
    def __init__(self, sign="x", flag_holds_words=False, number=0):
        self.sign = sign
        self.level = number
        self.next = []
        self.flag_holds_words = flag_holds_words
        self.words = []

    def contains(self, sign):
        for element in self.next:
            if element.sign == sign:
                return True
        return False

    # this is the similar to
    # next(x for x in self.next if x.sign == sign)
    def get_next(self, sign):
        for element in self.next:
            if element.sign == sign:
                return element
        #print("Error, next not found!", file=sys.stderr)
        return None

    def __add_sign(self, sign):
        if not self.contains(sign):
            new_element = MorseDictionaryElement(sign, number=self.level+1)
            self.next.append(new_element)
            return new_element
        else:
            return self.get_next(sign)

    def __fill_with_word(self, word):
        self.flag_holds_words = True
        self.words.append(word)

    def add(self, word_in_morse, word):
        current_element = self

        for sign in word_in_morse:
            current_element = current_element.__add_sign(sign)

        current_element.__fill_with_word(word)

    def count_elements(self):
        # do not take into account first element (root)
        #if self.sign == "x":
        if self.sign != "." and self.sign != "-":
            count = 0
        else:
            count = 1

        for element in self.next:
            count += element.count_elements()

        return count

    def count_words(self):
        if self.flag_holds_words:
            count = len(self.words)
        else:
            count = 0

        for element in self.next:
            count += element.count_words()

        return count

    def get_as_string(self, s=""):
        #s = ""
        s += str(self.level) + ": " + self.sign + ", "
        #s_until_now = s
        if self.flag_holds_words:
            s += ", ".join(self.words) + "\n"
        #elif self.sign == "x":
        elif self.sign != "." and self.sign != "-":
            s += "\n"

        for element in self.next:
            #s += element.get_as_string(copy.deepcopy(s_until_now))
            s += element.get_as_string()

        return s

    def find_words(self, word_in_morse):
        current_element = self
        for sign in word_in_morse:
            #print("current_element.sign: " + str(current_element.sign), file=sys.stderr)
            #print("current_element.words: " + str(current_element.words), file=sys.stderr)
            #print("sign: " + str(sign), file=sys.stderr)

            if not current_element.contains(sign):
                return ""
            else:
                current_element = current_element.get_next(sign)

        return current_element.words

    def test_where_the_word_follows(self, word_in_morse):

        flag_end_of_tree = False

        current_element = self

        position = []
        number_of_words = []

        for i, sign in enumerate(word_in_morse):

            if current_element.flag_holds_words:
                # there are some words here, remember this!
                position.append(i)
                number_of_words.append(len(current_element.words))

            if not current_element.contains(sign):
                # this the end of tree, stop the loop
                flag_end_of_tree = True
                break
            else:
                current_element = current_element.get_next(sign)

        if not flag_end_of_tree:
            if current_element.flag_holds_words:
                # there are some words here, remember this!
                position.append(len(word_in_morse))
                number_of_words.append(len(current_element.words))


        return position, number_of_words




class Message:
    def __init__(self, value):
        self.value = value


class Solution:
    def __init__(self, position_in_dictionary, words_thus_far=[], number_of_words_thus_far=0, part_to_use_start_index=0, part_in_use_end_index=1):
        self.position_in_dictionary = position_in_dictionary
        self.words_thus_far = words_thus_far
        self.number_of_words_thus_far = number_of_words_thus_far
        self.part_to_use_start_index = part_to_use_start_index
        self.part_in_use_end_index = part_in_use_end_index


def is_position_in_dictionary_not_none(position):
    if position is not None:
        return True
    else:
        return False


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
            #if current_solution.position_in_dictionary is not None:
            if is_position_in_dictionary_not_none(current_solution.position_in_dictionary):
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

                    #print("words_found: " + str(words_found), file=sys.stderr)

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


def print_morse_dict_info(morse_dictionary):
    print(morse_dictionary.get_as_string(), file=sys.stderr)
    print("morse_dictionary.count_words(): " + str(morse_dictionary.count_words()), file=sys.stderr)
    print("morse_dictionary.count_elements(): " + str(morse_dictionary.count_elements()), file=sys.stderr)


def generate_morse_dictionary(words, words_in_morse):
    morse_dictionary = MorseDictionaryElement(number=0)

    for word, word_in_morse in zip(words, words_in_morse):
        morse_dictionary.add(word_in_morse, word)

    return morse_dictionary


def main():
    #message, words, words_in_morse = load_from_prepared_data()
    message, words, words_in_morse = load_from_file("very_hard_The_Resistance_test_4.txt")

    morse_dictionary = generate_morse_dictionary(words, words_in_morse)

    print_morse_dict_info(morse_dictionary)

    # print("Words found: " + "".join(morse_dictionary.find_words(list("......-...-.."))), file=sys.stderr)
    # print("Words found: " + "".join(morse_dictionary.find_words(list("......-...-..---"))), file=sys.stderr)
    # print("Words found: " + "".join(morse_dictionary.find_words(list(".-----.-..-..-.."))), file=sys.stderr)
    # print("Words found: " + "".join(morse_dictionary.find_words(list("---.-----.-..-..-.."))), file=sys.stderr)
    # print("Words found: " + "".join(morse_dictionary.find_words(list("-....-"))), file=sys.stderr)

    solutions = [0] * (len(message)+1)
    solutions[0] = 1

    for i, sol in enumerate(solutions):

        #print(i, file=sys.stderr)
        #print(solutions, file=sys.stderr)

        if sol != 0:
            # check the part of message starting from index i where it gets you
            #print(message[i:], file=sys.stderr)
            positions, numbers_of_words = morse_dictionary.test_where_the_word_follows(message[i:])
            #print(positions, file=sys.stderr)
            #print(numbers_of_words, file=sys.stderr)

            #print("Words:", file=sys.stderr)
            for position, number in zip(positions, numbers_of_words):
                word = morse_dictionary.find_words(message[i:(i+position)])
                #print(word, file=sys.stderr)
                solutions[i+position] += sol * number

    print(solutions[-1])

    # old part

    # solutions = deque()
    #
    # solutions.append(Solution(
    #     position_in_dictionary=morse_dictionary,
    #     words_thus_far=[],
    #     part_to_use_start_index=0,
    #     part_in_use_end_index=0
    # ))
    #
    # results = process_solutions(solutions, message, morse_dictionary)
    #
    # process_and_print_results(results)


if __name__ == '__main__':
    #cProfile.run('main()')
    main()
