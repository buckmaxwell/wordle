from solver import Solver

puzzle = Solver()

for _ in range(6):
    print(f"I will guess '{puzzle.guess}'")
    # '----- -- all wrong
    # 'xxxxx' -- all right
    # '!!!!!' -- right letter wrong place
    feedback = input("How did I do?: ")
    puzzle.set_next_guess(feedback)
