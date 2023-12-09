# https://adventofcode.com/2015/day/1

import time

if __name__ == "__main__":
    begin = time.perf_counter()
    f = open('input.txt')
    lines = f.readlines()

    floor = 0
    basement_index = 0
    for i, char in enumerate(lines[0]):
        if floor == -1:
            basement_index = i
            break
        if char == '(':
            floor += 1
        elif char == ')':
            floor -= 1
    
    print(f"Basement index: {basement_index}") # Basement index: 1783
    print(f"Finished in: {time.perf_counter() - begin:.6f}s") # Finished in: 0.000289s