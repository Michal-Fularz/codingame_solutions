__author__ = 'Amin'

# COMPLETED
# PYTHON 3.x

import sys
import math


class Word:
    def __init__(self, text: str):
        self.__number_of_letters = ord("z") - ord("a") + 1
        # self.__alphabet_1_point = ["e", "a", "i", "o", "n", "r", "t", "l", "s", "u"]
        # self.__alphabet_2_point = ["d", "g"]
        # self.__alphabet_3_point = ["b", "c", "m", "p"]
        # self.__alphabet_4_point = ["f", "h", "v", "w", "y"]
        # self.__alphabet_5_point = ["k"]
        # self.__alphabet_8_point = ["j", "x"]
        # self.__alphabet_10_point = ["q", "z"]

        # self.alphabets = [
        #     (self.__alphabet_1_point, 1),
        #     (self.__alphabet_2_point, 2),
        #     (self.__alphabet_3_point, 3),
        #     (self.__alphabet_4_point, 4),
        #     (self.__alphabet_5_point, 5),
        #     (self.__alphabet_8_point, 8),
        #     (self.__alphabet_10_point, 10),
        # ]

        self.letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
        self.values  = [ 1,   3 ,  3,   2,   1,   4,   2,   4,   1,   8,   5,   1,   3,   1,   1,   3,   10,  1,   1,   1,   1,   4,   4,   8,   4,   10]

        self.alphabet = [0] * self.__number_of_letters
        self.original = text

        for letter in text:
            index = self.get_letter_index(letter)
            self.alphabet[index] += 1

    def get_letter_index(self, letter):
        return ord(letter) - ord("a")

    def compare(self, w):
        score = 0
        for letter_count_1, letter_count_2, value in zip(self.alphabet, w.alphabet, self.values):
            occurences_in_both_words = 0
            if letter_count_1 < letter_count_2:
                occurences_in_both_words = letter_count_1
            else:
                occurences_in_both_words = letter_count_2

            score += occurences_in_both_words * value

        if not self.__check_if_subset(w):
            score = 0

        return score

    def __check_if_subset(self, w):
        flag_subset = True
        for letter_count_1, letter_count_2 in zip(self.alphabet, w.alphabet):
            if letter_count_1 < letter_count_2:
                flag_subset = False

        return flag_subset

# w1 = Word("arwtsre")
# w2 = Word("arrest")
# w3 = Word("waster")
#
# print(w1.compare(w2))
# print(w1.compare(w3))

dictionary = []

n = int(input())
for i in range(n):
    w = input()
    if len(w) <= 7:
        dictionary.append(Word(w))
letters = input()
my_word = Word(letters)

best_score = 0
best_word = ""
for word in dictionary:
    score = my_word.compare(word)
    if score > best_score:
        best_score = score
        best_word = word

# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)

print(best_word.original)
