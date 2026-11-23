import numpy as np

def matrix_transpose(A: list) -> np.ndarray:
    """
    Returns the transposed matrix as a NumPy array.
    """
    # Write code here
    row = len(A)
    col = len(A[0])
    result = np.array([[0 for _ in range(row)]  for _ in range(col)])
    for r  in range(row):
        for c in range(col):
            result[c][r] = A[r][c]
    return  result
    pass
