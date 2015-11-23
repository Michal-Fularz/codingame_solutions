__author__ = 'Amin'

import sys
import math
from collections import deque
import copy

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
    def __init__(self, words_thus_far=[], part_to_use=deque(), part_in_use=deque()):
        self.words_thus_far = words_thus_far
        self.part_to_use = part_to_use
        self.part_in_use = part_in_use


class very_hard_The_Resistance_2:

    def __init__(self):
        pass

    def run(self):
        morse = Morse()
        words = {}

        # l = input()
        #
        # n = int(input())
        # for i in range(n):
        #     w = input()
        #     words[morse.convert_word_to_morse(w)] = w

        f = open("very_hard_The_Resistance_test_4.txt")
        l = f.readline()
        n = int(f.readline())
        for i in range(n):
            w = f.readline()
            words[morse.convert_word_to_morse(w)] = w

        # l = "......-...-..---.-----.-..-..-.."
        # words[morse.convert_word_to_morse("HELL")] = "HELL"
        # words[morse.convert_word_to_morse("HELLO")] = "HELLO"
        # words[morse.convert_word_to_morse("LL")] = "LL"
        # words[morse.convert_word_to_morse("LLO")] = "LLO"
        # words[morse.convert_word_to_morse("OWORLD")] = "OWORLD"
        # words[morse.convert_word_to_morse("WORLD")] = "WORLD"
        # words[morse.convert_word_to_morse("TEST")] = "TEST"
        #
        # print(words, file=sys.stderr)

        solutions = deque()

        solutions.append(Solution(
            part_to_use=deque(iterable=list(l))
        ))

        results = []

        # keep solutions on stack, and do one after another
        while len(solutions) > 0:

            # get one solution
            current_solution = solutions.popleft()

            # if solution still has signs to process
            while len(current_solution.part_to_use) > 0:
                # get new sign to process
                current_sign = current_solution.part_to_use.popleft()
                # add it to the collections holding currently processed set of signs
                current_solution.part_in_use.append(current_sign)

                #print("current_solution.part_in_use: " + "".join(current_solution.part_in_use), file=sys.stderr)
                # if current analysed set of signs is a word in dictionary
                if "".join(current_solution.part_in_use) in words:
                    # spawn new solution that continue looking for longer words
                    solutions.append(Solution(
                        copy.deepcopy(current_solution.words_thus_far),
                        copy.deepcopy(current_solution.part_to_use),
                        copy.deepcopy(current_solution.part_in_use)
                    ))

                    # get all available words
                    words_found = words["".join(current_solution.part_in_use)]

                    print("words_found: " + str(words_found), file=sys.stderr)

                    # clear currently processed set of signs
                    current_solution.part_in_use.clear()

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
                    current_solution.words_thus_far.append(words_found)


            # print("current_solution.part_in_use: " + str(current_solution.part_in_use), file=sys.stderr)
            # print("current_solution.words_thus_far: " + str(current_solution.words_thus_far), file=sys.stderr)
            if len(current_solution.part_in_use) == 0:
                results.append(current_solution.words_thus_far)

        r = ""
        for result in results:
            r += str(result) + "\n"

        print("result: " + r, file=sys.stderr)

        # Write an action using print
        # To debug: print("Debug messages...", file=sys.stderr)

        print(len(results))


if __name__ == "__main__":
    app = very_hard_The_Resistance_2()
    cProfile.run('app.run()')

