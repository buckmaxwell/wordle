from solver import Solver

puzzle = Solver()

for _ in range(6):
    print(f"I will guess '{puzzle.next_guess()}'")
    # '----- -- all wrong
    # 'xxxxx' -- all right
    # '!!!!!' -- right letter wrong place
    feedback = input("How did I do?: ")
    puzzle.get_next_guess(feedback)
