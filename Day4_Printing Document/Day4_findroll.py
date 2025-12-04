'''
Docstring for Day4_findroll - https://adventofcode.com/2025/day/4

'''
def paper_rolls(content):
    # 1. Robust parsing: Filter out empty lines just in case
    grid = [line for line in content.strip().split('\n') if line]

    total_count = 0
    rows = len(grid)
    cols = len(grid[0])

    directions = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),           (0, 1),
        (1, -1),  (1, 0),  (1, 1)
    ]

    for r in range(rows):
        for c in range(cols):
            # Check if this cell is a roll
            if grid[r][c] != '@':
                continue
            
            # All this logic must be INSIDE the 'for c' loop
            neighbour = 0
            for dr, dc in directions:
                nr = r + dr
                nc = c + dc

                # Boundary Check
                if 0 <= nr < rows and 0 <= nc < cols:
                    if grid[nr][nc] == '@':
                        neighbour += 1

            if neighbour < 4:
                total_count += 1
            # --- END OF INDENTATION FIX ---
            
    return total_count

# --- RUNNER ---
# Make sure your filename matches exactly
with open('input(a).txt', 'r') as file:
    data = file.read()
    total = paper_rolls(data)
    print("Total:", total)





with open('input(a).txt', 'r') as file:
    data=file.read()
    total=paper_rolls(data)
    print("Total : ", total)