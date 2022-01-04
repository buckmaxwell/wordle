from random import choice

class Solver:
    def __init__(self):
        self.words = []
        with open("words.txt") as f:
            for line in f:
                self.words.append(line.strip())
        self.context = self.words.copy()
        self.guess = choice(self.words[:1000])

    def next_guess(self):
        return self.guess

    def get_next_guess(self, feedback):
        for i, letter in enumerate(self.guess):

            if feedback[i] == "-":
                # WRONG: Remove words with this letter
                self.context = [w for w in self.context if not letter in w]
            elif feedback[i] == "!":
                # RIGHT LETTER: Remove words with letter in this place
                self.context = [w for w in self.context if not w[i] == letter]
                # Remove words without this letter
                self.context = [w for w in self.context if letter in w]
            else:
                # CORRECT: Remove words that don't have this letter in this position
                self.context = [w for w in self.context if w[i] == letter]
        self.guess = self.context[0]

