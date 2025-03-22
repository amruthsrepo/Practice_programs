def apply_gravity(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    
    # Step 1: Find all the 'F' cells in the matrix and collect them as part of the figure
    figure_positions = []
    for r in range(rows):
        for c in range(cols):
            if matrix[r][c] == 'F':
                figure_positions.append((r, c))
    
    # Step 2: Find the lowest possible position the figure can fall without hitting an obstacle
    max_fall = rows
    for r, c in figure_positions:
        fall_distance = 0
        for nr in range(r + 1, rows):
            if matrix[nr][c] in ('#', 'F'):  # Can't fall past an obstacle or another 'F'
                break
            fall_distance += 1
        max_fall = min(max_fall, fall_distance)
    
    # Step 3: Clear the current figure from the matrix
    for r, c in figure_positions:
        matrix[r][c] = '-'
    
    # Step 4: Move the figure to the lowest valid position
    for r, c in figure_positions:
        matrix[r + max_fall][c] = 'F'
    
    return matrix






matrix = [
    ['-', '-', '-', '-', '-'],
    ['-', 'F', 'F', '-', '-'],
    ['-', 'F', '-', '-', '-'],
    ['-', '-', '-', '-', '-'],
    ['-', '-', '-', '-', '-']
]

result = apply_gravity(matrix)
for row in result:
    print(''.join(row))

matrix = [
    ['F','F','F'],
['-','F','-'],
['-','F','F'],
['F','F','-'],
['-','-','-'],
['-','-','-']
]

print('Next\n\n\n')
result = apply_gravity(matrix)
for row in result:
    print(''.join(row))



print('Next\n\n\n')
matrix = [
    ['F','F','F'],
    ['-','F','-'],
    ['#','F','-'],
    ['F','F','-'],
    ['-','-','-'],
    ['-','-','#'],
    ['-','-','-']
]

print('Next')
result = apply_gravity(matrix)
for row in result:
    print(''.join(row))



