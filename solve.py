from random import choice

words = []
with open("words.txt") as f:
    for line in f:
        words.append(line.strip())


def get_next_guess(guess, info, context):
    for i, letter in enumerate(guess):

        if info[i] == "-":
            # WRONG: Remove words with this letter
            context = [w for w in context if not letter in w]
        elif info[i] == "!":
            # RIGHT LETTER: Remove words with letter in this place
            context = [w for w in context if not w[i] == letter]
            # Remove words without this letter
            context = [w for w in context if letter in w]
        else:
            # CORRECT: Remove words that don't have this letter in this position
            context = [w for w in context if w[i] == letter]
    return context[0], context


# 6 Tries

context = words.copy()
guess = choice(words[:1000])
for _ in range(0, 5):
    print("I will guess", guess)
    # '----- -- all wrong
    # 'xxxxx' -- all right
    # '!!!!!' -- right letter wrong place
    info = input("How did I do?: ")
    guess, context = get_next_guess(guess, info, context)
