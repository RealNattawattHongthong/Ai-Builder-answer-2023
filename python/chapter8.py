import numpy as np
from collections import Counter
import pandas as pd

def SudokuQuadrantChecker(strArr):
    # convert strArr to fucking 2D numpy array
    arr = np.array([list(eval(x)) for x in strArr])
    
    # check if any fucking row or column has duplicate values
    for i in range(9):
        if len(set(arr[i,:])) != 9 or len(set(arr[:,i])) != 9:
            return "illegal"
    
    # check each fucking quadrant for duplicate values
    quad_errors = []
    for i in range(3):
        for j in range(3):
            quad = arr[3*i:3*i+3, 3*j:3*j+3].flatten()
            counts = Counter(quad)
            for num, count in counts.items():
                if num != 'x' and count > 1:
                    quad_errors.append((i*3+j+1, num))
    
    # format fucking errors as a fucking string of quadrant numbers
    if quad_errors:
        df = pd.DataFrame(quad_errors, columns=['quadrant', 'number'])
        quadrants_with_errors = ', '.join([str(x) for x in sorted(df.quadrant.unique())])
        return quadrants_with_errors
    else:
        return "legal"
# legal damn thing    
input1 = ['[5, 3, 2, 6, 7, 8, 1, 4, 9]', '[6, 4, 7, 1, 9, 5, 3, 2, 8]', '[9, 1, 8, 2, 4, 3, 5, 6, 7]', '[8, 2, 5, 9, 6, 1, 4, 7, 3]', '[4, 9, 6, 8, 5, 3, 7, 1, 2]', '[7, 1, 3, 5, 2, 4, 9, 8, 6]', '[1, 6, 9, 7, 3, 4, 2, 8, 5]', '[2, 8, 1, 4, x, 7, 6, 9, 5]', '[3, 5, 4, 2, 8, 6, 1, 7, 9]']
output1 = SudokuQuadrantChecker(input1)
print(output1)

# illegal damn thing    
input2 = ['[5, 3, x, x, 7, x, x, x, x]', '[6, x, x, 1, 9, 5, x, x, x]', '[x, 9, 8, x, x, x, x, 6, x]', '[8, x, x, x, 6, x, x, x, 3]', '[4, x, x, 8, x, 3, x, x, 1]', '[7, x, x, x, 2, x, x, x, 6]', '[x, 6, x, x, x, x, 2, 8, x]', '[x, x, x, 4, 1, x, x, x, 5]', '[x, x, x, x, 8, x, x, 7, 9]']
output2 = SudokuQuadrantChecker(input2)
print(output2)