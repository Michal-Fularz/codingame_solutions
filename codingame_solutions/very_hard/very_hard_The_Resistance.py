__author__ = 'Amin'

# COMPLETED
# PYTHON 3.x

import sys
import math

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

        print("Error, next not found!", file=sys.stderr)
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
        # do not take into account the first element (root), that is equal to "x"
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
        s += str(self.level) + ": " + self.sign + ", "
        if self.flag_holds_words:
            s += ", ".join(self.words) + "\n"
        elif self.sign != "." and self.sign != "-":
            s += "\n"

        for element in self.next:
            s += element.get_as_string()

        return s

    def find_words(self, word_in_morse):
        current_element = self
        for sign in word_in_morse:
            if not current_element.contains(sign):
                return ""
            else:
                current_element = current_element.get_next(sign)

        return current_element.words

    def test_where_the_word_follows(self, word_in_morse):

        flag_end_of_tree = False

        current_element = self

        positions = []
        numbers_of_words = []

        for i, sign in enumerate(word_in_morse):

            if current_element.flag_holds_words:
                # there are some words here, remember this!
                positions.append(i)
                numbers_of_words.append(len(current_element.words))

            if not current_element.contains(sign):
                # this the end of tree, stop the loop
                flag_end_of_tree = True
                break
            else:
                current_element = current_element.get_next(sign)

        if not flag_end_of_tree:
            if current_element.flag_holds_words:
                # there are some words here, remember this!
                positions.append(len(word_in_morse))
                numbers_of_words.append(len(current_element.words))

        return positions, numbers_of_words


def print_morse_dict_info(morse_dictionary):
    print(morse_dictionary.get_as_string(), file=sys.stderr)
    print("morse_dictionary.count_words(): " + str(morse_dictionary.count_words()), file=sys.stderr)
    print("morse_dictionary.count_elements(): " + str(morse_dictionary.count_elements()), file=sys.stderr)


def generate_morse_dictionary(words, words_in_morse):
    morse_dictionary = MorseDictionaryElement(number=0)

    for word, word_in_morse in zip(words, words_in_morse):
        morse_dictionary.add(word_in_morse, word)

    return morse_dictionary


if __name__ == '__main__':
    #message, words, words_in_morse = load_from_prepared_data()
    message, words, words_in_morse = load_from_file("very_hard_The_Resistance_test_4.txt")

    morse_dictionary = generate_morse_dictionary(words, words_in_morse)
    print_morse_dict_info(morse_dictionary)

    solutions = [0] * (len(message)+1)
    solutions[0] = 1

    for i, sol in enumerate(solutions):

        if sol != 0:
            # check the part of message starting from index i where it gets you in the tree
            positions, numbers_of_words = morse_dictionary.test_where_the_word_follows(message[i:])

            for position, number in zip(positions, numbers_of_words):
                # if there is a need to find the word use the lines below:
                #word = morse_dictionary.find_words(message[i:(i+position)])
                #print(word, file=sys.stderr)
                solutions[i+position] += sol * number

    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr)

    print(solutions[-1])
