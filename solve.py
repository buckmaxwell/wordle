from solver import Solver

puzzle = Solver()

# 6 Tries
for _ in range(0, 5):
    print("I will guess", puzzle.next_guess())
    # '----- -- all wrong
    # 'xxxxx' -- all right
    # '!!!!!' -- right letter wrong place
    info = input("How did I do?: ")
    puzzle.get_next_guess(info)
