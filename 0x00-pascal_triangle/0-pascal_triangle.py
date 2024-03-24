def pascal_triangle(n):
    """
    Generate Pascal's Triangle up to the nth row.

    Args:
        n (int): Number of rows in the Pascal's Triangle.

    Returns:
        list of lists: Pascal's Triangle represented as a list of lists.

    """
    if n <= 0:
        return []

    triangle = []

    for i in range(n):
        row = [None] * (i + 1)
        row[0] = 1
        row[-1] = 1

        for j in range(1, len(row) - 1):
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]

        triangle.append(row)

    return triangle
