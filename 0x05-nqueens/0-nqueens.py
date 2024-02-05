#!/usr/bin/python3
""" N Queens Algorithm with Backtracking (Recursion Inside Loop) """
import sys


class NQueensSolver:
    """ Class for solving N Queens Problem """

    def __init__(self, board_size):
        """ Initialize the NQueensSolver object """
        self.n = board_size
        self.column_positions = [0 for _ in range(self.n + 1)]
        self.solutions = []

    def can_place_queen(self, current_row, current_column):
        """ Checks if a queen can be placed in the current column of the current row """
        for previous_row in range(1, current_row):
            if (
                self.column_positions[previous_row] == current_column
                or abs(self.column_positions[previous_row] - current_column) == abs(
                    previous_row - current_row
                )
            ):
                return False
        return True

    def solve_n_queens(self, current_row):
        """ Recursively tries to place queens on the chessboard """
        for current_column in range(1, self.n + 1):
            if self.can_place_queen(current_row, current_column):
                self.column_positions[current_row] = current_column
                if current_row == self.n:
                    solution = []
                    for i in range(1, self.n + 1):
                        solution.append([i - 1, self.column_positions[i] - 1])
                    self.solutions.append(solution)
                else:
                    self.solve_n_queens(current_row + 1)

    def get_solutions(self):
        """ Returns the list of solutions """
        return self.solutions


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    n_value = sys.argv[1]

    try:
        board_size = int(n_value)
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if board_size < 4:
        print("N must be at least 4")
        sys.exit(1)

    n_queens_solver = NQueensSolver(board_size)
    n_queens_solver.solve_n_queens(1)
    solutions = n_queens_solver.get_solutions()

    for solution in solutions:
        print(solution)
