__author__ = 'Amin'

import sys


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


def find_longest_word(words):
    longest_word_length = max([len(word) for word in words])

    print("Longest word consist of: " + str(longest_word_length) + " signs", file=sys.stderr)


def load_from_file(filename):
    morse = Morse()
    words = []
    words_in_morse = []

    f = open(filename)
    l = f.readline().replace("\n", "")
    n = int(f.readline())
    for i in range(n):
        w = f.readline().replace("\n", "")
        words.append(w)
        words_in_morse.append(morse.convert_word_to_morse(w))

    find_longest_word(words_in_morse)

    return l, words, words_in_morse


def load_from_input():
    morse = Morse()
    words = []
    words_in_morse = []
    l = input()

    n = int(input())
    for i in range(n):
        w = input()
        words.append(w)
        words_in_morse.append(morse.convert_word_to_morse(w))

    find_longest_word(words_in_morse)

    return l, words, words_in_morse


def load_from_prepared_data():
    morse = Morse()
    words = []
    words_in_morse = []
    l = "......-...-..---.-----.-..-..-.."

    w = "EEEEE"
    words.append(w)
    words_in_morse.append(morse.convert_word_to_morse(w))
    w = "HE"
    words.append(w)
    words_in_morse.append(morse.convert_word_to_morse(w))
    w = "HELL"
    words.append(w)
    words_in_morse.append(morse.convert_word_to_morse(w))
    w = "HELLO"
    words.append(w)
    words_in_morse.append(morse.convert_word_to_morse(w))
    w = "LL"
    words.append(w)
    words_in_morse.append(morse.convert_word_to_morse(w))
    w = "LLO"
    words.append(w)
    words_in_morse.append(morse.convert_word_to_morse(w))
    w = "OWORLD"
    words.append(w)
    words_in_morse.append(morse.convert_word_to_morse(w))
    w = "WORLD"
    words.append(w)
    words_in_morse.append(morse.convert_word_to_morse(w))
    w = "TEST"
    words.append(w)
    words_in_morse.append(morse.convert_word_to_morse(w))

    find_longest_word(words_in_morse)

    return l, words, words_in_morse
