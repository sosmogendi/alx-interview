#!/usr/bin/python3
"""
Rotate a 2D matrix by 90 degrees clockwise.
"""

def rotate_2d_matrix(matrix):
    """
    Rotates a 2D matrix 90 degrees clockwise in place.

    Args:
        matrix (list of list of ints): The 2D matrix to be rotated.
    """
    n = len(matrix)
    
    # Step 1: Transpose the matrix (swap rows with columns)
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    
    # Step 2: Reverse each row
    for i in range(n):
        matrix[i].reverse()
