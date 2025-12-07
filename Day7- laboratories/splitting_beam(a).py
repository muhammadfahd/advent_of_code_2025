'''
Day 7 - Laboratories
https://adventofcode.com/2025/day/7

Beam Simulation Solution (FINAL SAFE VERSION)
'''

def read_grid(input_text):
    return [list(line) for line in input_text.splitlines()]


def find_start(grid):
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == 'S':
                return r, c


def simulate_beams(grid):
    rows = len(grid)
    cols = len(grid[0])

    start_r, start_c = find_start(grid)

    # Beam starts moving downward from S
    beams = [(start_r + 1, start_c)]
    split_count = 0

    visited = set()   
    while beams:
        new_beams = []

        for r, c in beams:

            # Stop if beam leaves grid
            if r < 0 or r >= rows or c < 0 or c >= cols:
                continue

            #  If we've already visited this cell, stop this beam
            if (r, c) in visited:
                continue

            visited.add((r, c))  # Mark visited

            cell = grid[r][c]

            #  Empty → continue straight down
            if cell == '.':
                new_beams.append((r + 1, c))

            # Splitter → split and go down
            elif cell == '^':
                split_count += 1
                new_beams.append((r + 1, c - 1))  # left-down
                new_beams.append((r + 1, c + 1))  # right-down

            # Any other symbol → treat as empty
            else:
                new_beams.append((r + 1, c))

        beams = new_beams

    return split_count


with open("input(a).txt", "r") as file:
    data = file.read()

grid = read_grid(data)
answer = simulate_beams(grid)

print("Total Beam Splits:", answer)
