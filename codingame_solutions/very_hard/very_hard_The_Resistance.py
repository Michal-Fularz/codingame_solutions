__author__ = 'Amin'

import sys
import math
from collections import deque
import copy

class MorseDictionaryElement:
    def __init__(self, sign="x", flag_holds_word=False, word="", number=0):
        self.sign = sign
        self.number = number
        self.next = []
        self.flag_holds_word = flag_holds_word
        self.word = word
        
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

    def contains(self, sign):
        for element in self.next:
            if element.sign == sign:
                return True
        return False

    def __convert_word_to_morse(self, word):
        word_in_morse = ""
        for letter in word:
            sign_representation_of_letter = [x[0] for x in self.morse_alphabet if x[1] == letter]
            word_in_morse += "".join(sign_representation_of_letter)

        return word_in_morse

    # this is the similar to
    # next(x for x in self.next if x.sign == sign)
    def get_next(self, sign):
        for element in self.next:
            if element.sign == sign:
                return element
        #print("Error, next not found!", file=sys.stderr)
        return None

    def __add_sign(self, sign, flag_holds_word=False, word=""):
        if not self.contains(sign):
            new_element = MorseDictionaryElement(sign, flag_holds_word, word, self.number+1)
            self.next.append(new_element)
            return new_element
        else:
            return next(x for x in self.next if x.sign == sign)

    def __add(self, word_in_morse: list, word: str):
        current_element = self

        #print("word: " + str(word) + " in morse: " + str(word_in_morse), file=sys.stderr)

        for sign in word_in_morse[:-1]:
            current_element = current_element.__add_sign(sign)

        current_element = current_element.__add_sign(word_in_morse[-1], True, word)

        # check if the new element was created and holds the word
        if current_element.word == word and current_element.flag_holds_word:
            pass
        else:
            current_element.word = word
            current_element.flag_holds_word = True

    def add(self, word):
        word_in_morse = self.__convert_word_to_morse(word)
        self.__add(word_in_morse, word)

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
        # do not take into account first element (root)
        if self.flag_holds_word:
            count = 1
        else:
            count = 0

        for element in self.next:
            count += element.count_words()

        return count

    def get_as_string(self, s=""):
        #s = ""
        s += str(self.number) + ": " + self.sign + ", "
        s_until_now = s
        if self.flag_holds_word:
            s += self.word + "\n"
        #elif self.sign == "x":
        elif self.sign != "." and self.sign != "-":
            s += "\n"

        for element in self.next:
            s += element.get_as_string(copy.deepcopy(s_until_now))

        return s

    def find_word(self, signs):
        current_element = self
        for sign in signs:
            #print("current_element.sign: " + str(current_element.sign), file=sys.stderr)
            #print("current_element.word: " + str(current_element.word), file=sys.stderr)
            #print("sign: " + str(sign), file=sys.stderr)

            if not current_element.contains(sign):
                return ""
            else:
                current_element = current_element.get_next(sign)

        return current_element.word


class Solution:
    def __init__(self, words_thus_far, position_in_dictionary, part_to_use, part_in_use=[]):
        self.words_thus_far = words_thus_far
        self.part_in_use = part_in_use
        self.position_in_dictionary = position_in_dictionary
        self.part_to_use = part_to_use


morse_dictionary = MorseDictionaryElement(number=0)

# morse_dictionary.add("HELLO")
# morse_dictionary.add("PROBLEM?")
# morse_dictionary.add("WORLD")
#
# print(morse_dictionary.get_as_string(), file=sys.stderr)
#
# print("Word found: " + morse_dictionary.find_word(list("......-...-..---")), file=sys.stderr)
# print("Word found: " + morse_dictionary.find_word(list(".-----.-..-..-..")), file=sys.stderr)
# print("Word found: " + morse_dictionary.find_word(list("--")), file=sys.stderr)
#
# l = "......-...-..---.-----.-..-..-...--..-.----....-...--"

# morse_dictionary.add("H")
# morse_dictionary.add("HE")
# morse_dictionary.add("HELL")
# morse_dictionary.add("HELLO")
# morse_dictionary.add("LL")
# morse_dictionary.add("LLO")
# morse_dictionary.add("OWORLD")
# morse_dictionary.add("WORLD")
# morse_dictionary.add("TEST")
#
# print("Word found: " + morse_dictionary.find_word(list("......-...-..")), file=sys.stderr)
# print("Word found: " + morse_dictionary.find_word(list("......-...-..---")), file=sys.stderr)
# print("Word found: " + morse_dictionary.find_word(list(".-----.-..-..-..")), file=sys.stderr)
# print("Word found: " + morse_dictionary.find_word(list("---.-----.-..-..-..")), file=sys.stderr)
# print("Word found: " + morse_dictionary.find_word(list("-....-")), file=sys.stderr)
#
# l = "......-...-..---.-----.-..-..-.."

f = open("very_hard_The_Resistance_test_4.txt")
l = f.readline()
n = int(f.readline())
for i in range(n):
    w = f.readline()
    morse_dictionary.add(w)

# l = input()
#
# n = int(input())
# for i in range(n):
#     w = input()
#     morse_dictionary.add(w)

print("morse_dictionary.count_words(): " + str(morse_dictionary.count_words()), file=sys.stderr)
print("morse_dictionary.count_elements(): " + str(morse_dictionary.count_elements()), file=sys.stderr)
#print(morse_dictionary.get_as_string(), file=sys.stderr)

solutions = deque()
position_in_dictionary = morse_dictionary
part_to_use = deque(iterable=list(l))
words_thus_far = []
solutions.append(Solution(words_thus_far, position_in_dictionary, part_to_use, []))

results = []

while len(solutions) > 0:

    current_solution = solutions.popleft()

    while len(current_solution.part_to_use) > 0 and current_solution.position_in_dictionary is not None:
        current_sign = current_solution.part_to_use.popleft()
        current_solution.part_in_use.append(current_sign)
        current_solution.position_in_dictionary = current_solution.position_in_dictionary.get_next(current_sign)

        if current_solution.position_in_dictionary is not None:
            if current_solution.position_in_dictionary.flag_holds_word:
                word_found = current_solution.position_in_dictionary.word
                #print("word_found: " + str(word_found), file=sys.stderr)
                solutions.append(Solution(
                    copy.deepcopy(current_solution.words_thus_far),
                    copy.deepcopy(current_solution.position_in_dictionary),
                    copy.deepcopy(current_solution.part_to_use),
                    copy.deepcopy(current_solution.part_in_use)
                ))
                current_solution.words_thus_far.append(word_found)
                current_solution.part_in_use.clear()
                current_solution.position_in_dictionary = morse_dictionary

    # print("current_solution.part_in_use: " + str(current_solution.part_in_use), file=sys.stderr)
    # print("current_solution.words_thus_far: " + str(current_solution.words_thus_far), file=sys.stderr)
    if current_solution is not None and len(current_solution.part_in_use) == 0:
        results.append(current_solution.words_thus_far)

r = ""
for result in results:
    r += str(result) + "\n"

print("result: " + r, file=sys.stderr)

# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)

#print(max([len(words) for words in result]))
print(len(results))
