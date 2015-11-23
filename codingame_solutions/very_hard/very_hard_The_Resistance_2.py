__author__ = 'Amin'

import sys
import math
from collections import deque
import copy
# TODO: ordered dict require manual sorting after all the items were inserted
# TODO: I am not sure if this will speed the is in part
from collections import OrderedDict

import cProfile


class Morse:
    def __init__(self):
        self.morse_alphabet = []

        self.morse_alphabet.append((".", "E"))

        self.morse_alphabet.append(("..", "I"))
        self.morse_alphabet.append((".-", "A"))

        self.morse_alphabet.append(("...", "S"))
        self.morse_alphabet.append(("..-", "U"))
        self.morse_alphabet.append((".-.", "R"))
        self.morse_alphabet.append((".--", "W"))

        self.morse_alphabet.append(("....", "H"))
        self.morse_alphabet.append(("...-", "V"))
        self.morse_alphabet.append(("..-.", "F"))
        self.morse_alphabet.append((".-..", "L"))
        self.morse_alphabet.append((".--.", "P"))
        self.morse_alphabet.append((".---", "J"))

        self.morse_alphabet.append(("-", "T"))

        self.morse_alphabet.append(("-.", "N"))
        self.morse_alphabet.append(("--", "M"))

        self.morse_alphabet.append(("-..", "D"))
        self.morse_alphabet.append(("-.-", "K"))
        self.morse_alphabet.append(("--.", "G"))
        self.morse_alphabet.append(("---", "O"))

        self.morse_alphabet.append(("-...", "B"))
        self.morse_alphabet.append(("-..-", "X"))
        self.morse_alphabet.append(("-.-.", "C"))
        self.morse_alphabet.append(("-.--", "Y"))
        self.morse_alphabet.append(("--..", "Z"))
        self.morse_alphabet.append(("--.-", "Q"))

    def convert_word_to_morse(self, word):
        word_in_morse = ""
        for letter in word:
            sign_representation_of_letter = [x[0] for x in self.morse_alphabet if x[1] == letter]
            word_in_morse += "".join(sign_representation_of_letter)

        return word_in_morse


class Solution:
    def __init__(self, number_of_words=0, words_thus_far=[], part_to_use_start_index=0, part_in_use_end_index=1):
        self.number_of_words = number_of_words
        self.words_thus_far = words_thus_far
        self.part_to_use_start_index = part_to_use_start_index
        self.part_in_use_end_index = part_in_use_end_index


class very_hard_The_Resistance_2:

    def __init__(self):
        self.morse = Morse()
        self.words = []
        self.keys = set()#[]
        for i in range(0, 50):
            self.words.append(OrderedDict())
            #self.keys.append(set())
        self.l = ""


        print([len(x) for x in self.words], file=sys.stderr)

    def load_from_file(self):
        f = open("very_hard_The_Resistance_test_4.txt")
        self.l = f.readline()
        n = int(f.readline())

        keys_length = []

        for i in range(n):
            w = f.readline()
            key = self.morse.convert_word_to_morse(w)
            keys_length.append(len(key))
            self.words[len(key)][key] = w
            self.keys.add(key)

        #keys_length.sort()
        #print(keys_length, file=sys.stderr)
        #print(max(keys_length), file=sys.stderr)

    def use_prepared_set(self):
        self.l = "......-...-..---.-----.-..-..-.."
        word = "HELL"
        word_in_morse = self.morse.convert_word_to_morse(word)
        self.words[len(word_in_morse)][word_in_morse] = word
        word = "HELLO"
        word_in_morse = self.morse.convert_word_to_morse(word)
        self.words[len(word_in_morse)][word_in_morse] = word
        word = "LL"
        word_in_morse = self.morse.convert_word_to_morse(word)
        self.words[len(word_in_morse)][word_in_morse] = word
        word = "LLO"
        word_in_morse = self.morse.convert_word_to_morse(word)
        self.words[len(word_in_morse)][word_in_morse] = word
        word = "OWORLD"
        word_in_morse = self.morse.convert_word_to_morse(word)
        self.words[len(word_in_morse)][word_in_morse] = word
        word = "WORLD"
        word_in_morse = self.morse.convert_word_to_morse(word)
        self.words[len(word_in_morse)][word_in_morse] = word
        word = "TEST"
        word_in_morse = self.morse.convert_word_to_morse(word)
        self.words[len(word_in_morse)][word_in_morse] = word

    def spawn_new_solution(self, solutions, part_to_use_start_index, part_in_use_end_index):
        solutions.append(Solution(
            #copy.deepcopy(current_solution.words_thus_far),
            part_to_use_start_index=copy.deepcopy(part_to_use_start_index),
            part_in_use_end_index=copy.deepcopy(part_in_use_end_index)
        ))

    def get_dict_key(self, current_solution):
        return self.l[current_solution.part_to_use_start_index:current_solution.part_in_use_end_index]

    def is_currently_anaylzed_part_in_dictionary1(self, current_dict_key):

        if len(self.words[len(current_dict_key)]) > 0:
            if self.words[len(current_dict_key)].get(current_dict_key, "") != "":
                return True
            else:
                return False
        else:
            return False

    def is_currently_anaylzed_part_in_dictionary(self, current_dict_key):

        #if len(self.words[len(current_dict_key)]) > 0:
            #if current_dict_key in self.words[len(current_dict_key)]:
            if current_dict_key in self.keys:
                return True
            else:
                return False
        #else:
            #return False

    def is_currently_anaylzed_part_in_dictionary3(self, current_dict_key):

        if len(self.words[len(current_dict_key)]) > 0:
            try:
                self.words[len(current_dict_key)][current_dict_key]
                return True
            except KeyError:
                return False
        else:
            return False



    def check_one_solution(self, current_solution, solutions):

        current_dict_key = ""
        current_dict_key_len = 0
        l_len = len(self.l)

        # if solution still has signs to process
        # TODO - add min value
        # TODO - this does not work as it should - current_dict_len is not passed to new solutions
        # TODO - same goes with current_dict_key
        # TODO - change string as key to values - it should be faster
        # TODO - http://code.activestate.com/recipes/198157-improve-dictionary-lookup-performance/
        while current_solution.part_in_use_end_index < l_len and current_dict_key_len < 48:
            # get new sign to process
            # add it to the collections holding currently processed set of signs
            # TODO - check how fast this part is - maybe join is faster?
            current_dict_key += self.l[current_solution.part_in_use_end_index-1]
            current_solution.part_in_use_end_index += 1
            current_dict_key_len += 1

            #print("current_solution.part_in_use: " + "".join(current_solution.part_in_use), file=sys.stderr)
            # if current analysed set of signs is a word in dictionary
            if self.is_currently_anaylzed_part_in_dictionary(current_dict_key):
                # spawn new solution that continue looking for longer words
                self.spawn_new_solution(solutions, current_solution.part_to_use_start_index, current_solution.part_in_use_end_index)

                # get all available words
                #words_found = self.words[len(current_dict_key)][current_dict_key]

                #print("words_found: " + str(words_found), file=sys.stderr)

                # clear currently processed set of signs
                current_solution.part_to_use_start_index = current_solution.part_in_use_end_index
                current_dict_key_len = 0

                # for all words except last spawn new solutions
                # for word in words_found[:-1]:
                #     new_words_thus_far = copy.deepcopy(current_solution.words_thus_far)
                #     new_words_thus_far.append(word)
                #     solutions.append(Solution(
                #         current_solution.position_in_dictionary,
                #         new_words_thus_far,
                #         copy.deepcopy(current_solution.part_to_use),
                #         copy.deepcopy(current_solution.part_in_use)
                #     ))
                #
                # current_solution.words_thus_far.append(words_found[-1])
                #current_solution.words_thus_far.append(words_found)
                current_solution.number_of_words += 1

    def find_results(self, solutions):
        results = []

        # keep solutions on stack, and do one after another
        while len(solutions) > 0:

            # get one solution
            current_solution = solutions.popleft()

            self.check_one_solution(current_solution, solutions)

            # print("current_solution.part_in_use: " + str(current_solution.part_in_use), file=sys.stderr)
            #print("current_solution.words_thus_far: " + str(current_solution.words_thus_far), file=sys.stderr)
            # TODO - use with new = solution without lists
            #if len(current_solution.part_in_use) == 0:
                #results.append(current_solution.words_thus_far)

        return results

    def run(self):

        # l = input()
        #
        # n = int(input())
        # for i in range(n):
        #     w = input()
        #     words[morse.convert_word_to_morse(w)] = w

        solutions = deque()

        solutions.append(Solution(
            part_to_use_start_index=0,
            part_in_use_end_index=1
        ))

        results = self.find_results(solutions)

        r = ""
        for result in results:
            r += str(result) + "\n"

        print("result: " + r, file=sys.stderr)

        # Write an action using print
        # To debug: print("Debug messages...", file=sys.stderr)

        print(len(results))


def foo():
    app = very_hard_The_Resistance_2()
    app.load_from_file()
    #app.use_prepared_set()
    #print(app.words, file=sys.stderr)
    app.run()

if __name__ == "__main__":
    cProfile.run('foo()')
    #foo()
