"""
Write a function that will solve a 9x9 Sudoku puzzle. The function will take one argument consisting of the 2D puzzle array, with the value 0 representing an unknown square.

The Sudokus tested against your function will be "easy" (i.e. determinable; there will be no need to assume and test possibilities on unknowns) and can be solved with a brute-force approach.
"""

import time
import unittest
from typing import List


def sudoku(puzzle):
    solver = SudokuSolver()
    return solver(Sudoku(puzzle)).grid


class Sudoku:
    """
    Sudoku base class
    9x9 grid, x: horizontal row, y: vertical col
    """

    def __init__(self, grid: List[List[int]]):
        self.grid = grid

    def get_horizontal(self, x: int) -> List[int]:
        """Returns the digits of the horizontal x-th row"""
        return self.grid[x]

    def get_vertical(self, y: int) -> List[int]:
        """Returns the digits of the vertical y-th column"""
        return [row[y] for row in self.grid]

    def get_square(self, x: int, y: int) -> List[int]:
        """Returns the digits of the 3x3 square at the x, y coordinates"""
        square_row = x // 3 * 3
        square_col = y // 3 * 3
        return [
            digit for col in self.grid[square_row:square_row + 3]
            for digit in col[square_col:square_col + 3]
        ]

    def get_all(self, x: int, y: int) -> List[int]:
        """Returns the digits of the row, col and square"""
        return self.get_horizontal(x) + self.get_vertical(y) + self.get_square(x, y)

    def display(self):
        for row in self.grid:
            print(row)


class SudokuSolver:

    def __call__(self, sudoku: Sudoku, verbose: bool = False):
        self.solved_sudoku = sudoku

        if verbose:
            self._init_with_verbose()
        else:
            self._init()

        return self.solved_sudoku

    def _init_with_verbose(self):
        print("Solving the sudoku...")
        time_start = time.time()
        if not self.solve():
            raise Exception("Error while solving the sudoku")
        time_end = time.time()
        print(
            f"Sudoku solved in {round((time_end - time_start) * 1000)}ms!")

    def _init(self):
        if not self.solve():
            raise Exception("Error while solving the sudoku")

    def find_empty(self):
        """
        Find the first empty cell in the sudoku, an empty cell contains a 0 digit.
        If no empty cell found, returns None.
        """
        for x in range(9):
            for y in range(9):
                if not self.solved_sudoku.grid[x][y]:
                    return x, y
        return None

    def solve(self):
        cell = self.find_empty()
        if not cell:
            return self.solved_sudoku

        x, y = cell
        presents = set(self.solved_sudoku.get_all(x, y))
        for possibility in set(range(10)) - presents:
            self.solved_sudoku.grid[x][y] = possibility

            if self.solve():
                return self.solved_sudoku

            self.solved_sudoku.grid[x][y] = 0

        return False


class SudokuTest(unittest.TestCase):
    def basic_tests(self):
        puzzle = [
            [5, 3, 0, 0, 7, 0, 0, 0, 0],
            [6, 0, 0, 1, 9, 5, 0, 0, 0],
            [0, 9, 8, 0, 0, 0, 0, 6, 0],
            [8, 0, 0, 0, 6, 0, 0, 0, 3],
            [4, 0, 0, 8, 0, 3, 0, 0, 1],
            [7, 0, 0, 0, 2, 0, 0, 0, 6],
            [0, 6, 0, 0, 0, 0, 2, 8, 0],
            [0, 0, 0, 4, 1, 9, 0, 0, 5],
            [0, 0, 0, 0, 8, 0, 0, 7, 9]
        ]

        solution = [
            [5, 3, 4, 6, 7, 8, 9, 1, 2],
            [6, 7, 2, 1, 9, 5, 3, 4, 8],
            [1, 9, 8, 3, 4, 2, 5, 6, 7],
            [8, 5, 9, 7, 6, 1, 4, 2, 3],
            [4, 2, 6, 8, 5, 3, 7, 9, 1],
            [7, 1, 3, 9, 2, 4, 8, 5, 6],
            [9, 6, 1, 5, 3, 7, 2, 8, 4],
            [2, 8, 7, 4, 1, 9, 6, 3, 5],
            [3, 4, 5, 2, 8, 6, 1, 7, 9]
        ]

        solver = SudokuSolver()
        solved = solver(Sudoku(puzzle))

        self.assertEqual(solved.grid, solution,
                         "Incorrect solution for the following puzzle: " + str(puzzle))


def main():
    test = SudokuTest()
    test.basic_tests()


if __name__ == '__main__':
    main()
