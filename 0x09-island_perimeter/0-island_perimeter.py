#!/usr/bin/python3

"""Function to compute the perimeter of an island."""

def island_perimeter(grid):
    """
    Calculate the perimeter of the island based on the provided grid.

    Args:
        grid (List[List[int]]): A 2D list representing the grid.

    Returns:
        int: The perimeter of the island.
    """
    perimeter_count = 0
    num_rows = len(grid)
    num_cols = len(grid[0]) if num_rows else 0

    for i in range(num_rows):
        for j in range(len(grid[i])):

            neighbors = [(i - 1, j), (i, j - 1), (i, j + 1), (i + 1, j)]
            is_valid_neighbor = [1 if k[0] in range(num_rows) and k[1] in range(num_cols) else 0
                                 for k in neighbors]

            if grid[i][j]:
                perimeter_count += sum([1 if not is_water or not grid[k[0]][k[1]] else 0
                                        for is_water, k in zip(is_valid_neighbor, neighbors)])

    return perimeter_count
