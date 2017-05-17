import Network
import random
import msvcrt
import pickle


class Main(object):
    def __init__(self):
        self.letters = {"a": [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        "b": [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        "c": [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        "d": [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        "e": [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        "f": [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        "g": [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        "h": [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        "i": [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        "j": [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        "k": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        "l": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        "m": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        "n": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        "o": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        "p": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        "q": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        "r": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                        "s": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
                        "t": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
                        "u": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                        "v": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
                        "w": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
                        "x": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                        "y": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
                        "z": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]}
        self.run()

    @staticmethod
    def read_text_file(path):
        with open(path, "r") as file:
            return [list(line.strip().lower()) for line in file]

    def convert_letters(self, data):
        for outer_index, word in enumerate(data):
            for inner_index, letter in enumerate(word):
                for key, value in self.letters.items():
                    if letter == key:
                        word[inner_index] = value
            data[outer_index] = word

        return data

    @staticmethod
    def set_language(data, language):
        return [language] * len(data)

    def run(self):
        # define training set
        english = self.convert_letters(self.read_text_file("english.txt"))
        german = self.convert_letters(self.read_text_file("german.txt"))

        language_set = english + german

        # English = [1, 0] German = [0, 1]
        language_teach = [self.set_language(english, [1, 0]) + self.set_language(german, [0, 1])]

        xor_set = [[0, 0], [0, 1], [1, 0], [1, 1]]
        xor_teach = [[0], [1], [1], [0]]

        try:
            with open("ffn", "rb") as file:
                ffn = pickle.loads(file.read())
            print("Loaded network data from file")
        except IOError:
            ffn = Network.FeedForwardNetwork(15, 15, 2)
            print("Failed to load network data, most likely does not exist")

        print("Valid input options:\n",
              "train: randomly feed training data to network, esc to stop training\n",
              "input: directly input pattern to network\n",
              "quit: save training data, end the program\n")
        while True:
            mode = input("Enter mode: ").lower()

            if mode == "train":
                count = 0
                while True:
                    rnd = random.randint(0, len(language_set))

                    ffn.forward(language_set[rnd])
                    ffn.backwards(language_teach[rnd])

                    if msvcrt.kbhit():
                        if msvcrt.getch() == b'\x1b':
                            break

                    if (ffn.get_output()[0][0] * 100) > ((1 - ffn.get_output()[0][0]) * 100):
                        print("Iteration:", count, "True, accuracy (percent):", round((ffn.get_output()[0][0] * 100), 2))
                    else:
                        print("Iteration:", count, "False, accuracy (percent):", round(((1 - ffn.get_output()[0][0]) * 100), 2))

                    count += 1
            elif mode == "input":
                raw = list(input("Enter pattern: "))
                ffn.forward(raw)
                if (ffn.get_output()[0][0] * 100) > ((1 - ffn.get_output()[0][0]) * 100):
                    print("True, accuracy (percent):", round((ffn.get_output()[0][0] * 100), 2))
                else:
                    print("False, accuracy (percent):", round(((1 - ffn.get_output()[0][0]) * 100), 2))

            elif mode == "quit":
                break

            else:
                print("Invalid input")

        with open("ffn", "wb") as file:
            file.write(pickle.dumps(ffn))

if __name__ == '__main__':
    main_executor = Main()
    main_executor.run()
