import Network
import random
import msvcrt


class Main(object):
    def __init__(self):
        self.run()

    @staticmethod
    def run():
        # define training set
        xor_set = [[0, 0], [0, 1], [1, 0], [1, 1]]
        xor_teach = [[0], [1], [1], [0]]

        ffn = Network.FeedForwardNetwork(2, 2, 1)

        try:
            ffn.startup()
            print("Loaded network data from ffn.txt")
        except IOError:
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
                    rnd = random.randint(0, 3)

                    ffn.forward(xor_set[rnd])
                    ffn.backwards(xor_teach[rnd])

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

        ffn.shutdown()

if __name__ == '__main__':
    Main.run()
