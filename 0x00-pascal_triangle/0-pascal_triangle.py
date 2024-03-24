#!/usr/bin/python3
'''
    Pascal's Triangle.
'''

def pascal_triangle(n):
    '''
    Generates Pascal's Triangle up to the nth row.

    Args:
        n (int): Number of rows in the Pascal's Triangle.

    Returns:
        list of lists: Pascal's Triangle represented as a list of lists.
    '''
    # Handle edge cases
    if n <= 0:
        return []
    if n == 1:
        return [[1]]
    if n == 2:
        return [[1], [1, 1]]

    # Initialize Pascal's Triangle with the first two rows
    triangle = [[1], [1, 1]]

    # Generate subsequent rows
    for i in range(2, n):
        row = [1]  # Each row starts with 1
        for j in range(1, i):
            # Calculate values for the current row based on the previous row
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
        row.append(1)  # Each row ends with 1
        triangle.append(row)

    return triangle
