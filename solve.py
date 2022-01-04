from solver import Solver

puzzle = Solver()

for _ in range(6):
    print("I will guess", puzzle.next_guess())
    # '----- -- all wrong
    # 'xxxxx' -- all right
    # '!!!!!' -- right letter wrong place
    info = input("How did I do?: ")
    puzzle.get_next_guess(info)
