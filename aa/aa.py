import numpy as np
from collections import Counter
import pandas as pd

def SudokuQuadrantChecker(strArr):
    # convert strArr to 2D numpy array
    arr = np.array([eval(x.replace('x', 'None')) for x in strArr])
    
    # check if any row or column has duplicate values
    for i in range(9):
        if len(set(arr[i,:])) != 9 or len(set(arr[:,i])) != 9:
            return "illegal"
    
    # check each quadrant for duplicate values
    quad_errors = []
    for i in range(3):
        for j in range(3):
            quad = arr[3*i:3*i+3, 3*j:3*j+3].flatten()
            counts = Counter(quad)
            for num, count in counts.items():
                if num is not None and count > 1:
                    quad_errors.append((i*3+j+1, num))
    
    # format errors as a string of quadrant numbers
    if quad_errors:
        df = pd.DataFrame(quad_errors, columns=['quadrant', 'number'])
        quadrants_with_errors = ', '.join([str(x) for x in sorted(df.quadrant.unique())])
        return quadrants_with_errors
    else:
        return "legal"

# legal input
input1 = input2 = ['[5, 3, None, None, 7, None, None, None, None]', '[6, None, None, 1, 9, 5, None, None, None]', '[None, 9, 8, None, None, None, None, 6, None]', '[8, None, None, None, 6, None, None, None, 3]', '[4, None, None, 8, None, 3, None, None, 1]', '[7, None, None, None, 2, None, None, None, 6]', '[None, 6, None, None, None, None, 2, 8, None]', '[None, None, None, 4, 1, None, None, None, 5]', '[None, None, None, None, 8, None, None, 7, 9]']
output1 = SudokuQuadrantChecker(input1)
print(output1)

# illegal input
input2 = ['[5, 3, None, None, 7, None, None, None, None]', '[6, None, None, 1, 9, 5, None, None, None]', '[None, 9, 8, None, None, None, None, 6, None]', '[8, None, None, None, 6, None, None, None, 3]', '[4, None, None, 8, None, 3, None, None, 1]', '[7, None, None, None, 2, None, None, None, 6]', '[None, 6, None, None, None, None, 2, 8, None]', '[None, None, None, 4, 1, None, None, None, 5]', '[None, None, None, None, 8, None, None, 7, 9]']
output2 = SudokuQuadrantChecker(input2)
print(output2)