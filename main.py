import random
import time


class bracket:

    def __init__(self, length):
        self.length = length
        self.entries = []

    def enter(self, name):
        self.entries.append(name)

    def draw(self):
        return random.choice(self.entries)


class timed_raffle:

    def __init__(self, brackets=None):
        self.brackets = {}

        if brackets is None:
            self.construct_empty()
        else:
            for weight, length in brackets:
                self.brackets[weight] = bracket(length)

    def construct_empty(self):
        while True:
            cmd = input('\nEnter "new" to create a new bracket, or "done" to begin the raffle: ')
            if cmd == "new":
                try:
                    w = int(input("How many entries should participants in this bracket be granted? >>> "))
                    l = int(input("For how many seconds should this bracket be available? >>> "))
                except:
                    print("Please enter positive integer.")
                    continue
                self.brackets[w] = bracket(l)
            elif cmd == "done":
                if self.brackets == {}:
                    print("Please create at least one bracket.")
                else:
                    break

    def run(self, exit_command: str = "draw"):
        self.start = time.time()
        while True:
            name = input('\nPlease enter your name: ')

            if name == exit_command:
                return

            if self.enter(name):
                print("You have been entered successfully.")
            else:
                print("Something is wrong, please try again.")

    def enter(self, name):
        entry_time = time.time() - self.start
        bToAppend = None
        for weight in self.brackets:
            if self.brackets[weight].length > entry_time:
                bToAppend = self.brackets[weight]
                break

        if bToAppend is None:
            return False

        bToAppend.entries.append(name)
        return True

    def draw(self):
        pool = []

        for weight in self.brackets:

            b = self.brackets[weight]

            for entry in b.entries:
                for i in range(int(weight)):
                    pool.append(entry)

        return random.choice(pool)

if __name__ == '__main__':

    raffle = timed_raffle()

    raffle.run()

    print(raffle.draw())