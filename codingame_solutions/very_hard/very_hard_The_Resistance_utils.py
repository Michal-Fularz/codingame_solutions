__author__ = 'Amin'


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


def load_from_file(filename):
    morse = Morse()
    words_in_morse = {}

    f = open(filename)
    l = f.readline()
    n = int(f.readline())
    #keys_length = []
    for i in range(n):
        w = f.readline()
        words_in_morse[morse.convert_word_to_morse(w)] = w
        #key = self.morse.convert_word_to_morse(w)
        #keys_length.append(len(key))
        #self.words[len(key)][key] = w
        #self.keys.add(key)

    #keys_length.sort()
    #print(keys_length, file=sys.stderr)
    #print(max(keys_length), file=sys.stderr)

    return l, words_in_morse


def load_from_input():
    morse = Morse()
    words_in_morse = {}
    l = input()

    n = int(input())
    for i in range(n):
        w = input()
        words_in_morse[morse.convert_word_to_morse(w)] = w

    return l, words_in_morse


def load_from_prepared_data():
    morse = Morse()
    words_in_morse = {}
    l = "......-...-..---.-----.-..-..-.."

    w = "HE"
    words_in_morse[morse.convert_word_to_morse(w)] = w
    w = "HELL"
    #word_in_morse = self.morse.convert_word_to_morse(word)
    #self.words[len(word_in_morse)][word_in_morse] = word
    words_in_morse[morse.convert_word_to_morse(w)] = w
    w = "HELLO"
    words_in_morse[morse.convert_word_to_morse(w)] = w
    w = "LL"
    words_in_morse[morse.convert_word_to_morse(w)] = w
    w = "LLO"
    words_in_morse[morse.convert_word_to_morse(w)] = w
    w = "OWORLD"
    words_in_morse[morse.convert_word_to_morse(w)] = w
    w = "WORLD"
    words_in_morse[morse.convert_word_to_morse(w)] = w
    w = "TEST"
    words_in_morse[morse.convert_word_to_morse(w)] = w

    return l, words_in_morse
