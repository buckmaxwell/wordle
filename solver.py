from random import choice


class Solver:
    def __init__(self):
        self.words = []
        with open("words.txt") as f:
            for line in f:
                self.words.append(line.strip())
        self.context = self.words.copy()
        self.guess = choice(self.words[:1000])

    def set_next_guess(self, feedback):
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


if __name__ == "__main__":
    # Test performance

    def get_feedback(answer, guess):
        result = len(answer) * ["-"]
        for i, letter in enumerate(guess):
            if letter in answer:
                result[i] = "!"
            if letter == answer[i]:
                result[i] = "x"
        return "".join(result)

    numbers_of_tries = []
    solver = Solver()
    for answer in solver.words[:500] + solver.words[len(solver.words) - 500 :]:
        puzzle = Solver()
        for number_of_tries in range(1, 8):
            if number_of_tries > 7:
                raise Exception("Did not get word")
            if puzzle.guess == answer:
                numbers_of_tries.append(number_of_tries)
                break
            feedback = get_feedback(answer, puzzle.guess)
            puzzle.set_next_guess(feedback)

    print(
        f"Guessed 1000 words correctly in {sum(numbers_of_tries)}, {sum(numbers_of_tries) / 1000} tries on average"
    )
