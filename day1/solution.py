# https://adventofcode.com/2015/day/1

import time

if __name__ == "__main__":
    begin = time.perf_counter()
    f = open('input.txt')
    lines = f.readlines()
    
    floor = 0
    for char in lines[0]:
        if char == '(':
            floor += 1
        elif char == ')':
            floor -= 1
    
    print(f"Floor: {floor}") # Floor: 232
    print(f"Finished in: {time.perf_counter() - begin:.6f}s") # Finished in: 0.000663s