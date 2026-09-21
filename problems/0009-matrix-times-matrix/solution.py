import numpy as np

def matrixmul(a:list[list[int|float]],
              b:list[list[int|float]])-> list[list[int|float]]:


    col = len(a[0])
    row = len(b)

    c = -1

    if col == row:   
        c = np.matmul(a, b)
        
    return c