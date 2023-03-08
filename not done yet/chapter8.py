import numpy as np
from collections import Counter
import pandas as pd

def check_sudoku(board):
    # Check fucking rows
    for row in board:
        if set(row) != set(range(1, 10)):
            return False
    
    # Check fucking columns
    for col in board.T:
        if set(col) != set(range(1, 10)):
            return False
    
    # Check fucking sub-grids
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            subgrid = board[i:i+3, j:j+3].flatten()
            if set(subgrid) != set(range(1, 10)):
                return False
    
    return True

# Example fucking Sudoku board
board = np.array([
    [5, 3, 4, 6, 7, 8, 9, 1, 2],
    [6, 7, 2, 1, 9, 5, 3, 4, 8],
    [1, 9, 8, 3, 4, 2, 5, 6, 7],
    [8, 5, 9, 7, 6, 1, 4, 2, 3],
    [4, 2, 6, 8, 5, 3, 7, 9, 1],
    [7, 1, 3, 9, 2, 4, 8, 5, 6],
    [9, 6, 1, 5, 3, 7, 2, 8, 4],
    [2, 8, 7, 4, 1, 9, 6, 3, 5],
    [3, 4, 5, 2, 8, 6, 1, 7, 9]
])

# Check the fucking Sudoku board
if check_sudoku(board):
    print("Valid Sudoku board")
else:
    print("Invalid Sudoku board")

# Convert board to fucking pandas DataFrame
df = pd.DataFrame(board)

# Aggregate value counts in fucking rows, columns, and sub-grids
value_counts = pd.concat([
    df.apply(Counter, axis=1),
    df.apply(Counter, axis=0),
    pd.DataFrame({
        "subgrid": [
            Counter(df.iloc[i:i+3, j:j+3].values.flatten())
            for i in range(0, 9, 3) for j in range(0, 9, 3)
        ]
    })
], axis=1)
# Convert the Counter object to a DataFrame
value_counts = pd.DataFrame.from_dict(value_counts, orient='index').reset_index()

# Rename the columns
value_counts.columns = ['value', 'count']

# Count the number of times each value appears
value_counts['count'] = value_counts.apply(lambda x: x['count'].get(x['value'], 0), axis=1)

# Print the value counts
print(value_counts)