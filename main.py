from src.sudoku_solver import SudokuSolver
from src.sudoku_checker import SudokuChecker
from src.gui import SudokuApp
# TODO: create a menu
# TODO: create unfinished sudoku
# TODO: timer
# TODO: solver option
# TODO: read sudoku from pic
# TODO: create boxes around squares
# TODO: add requirements and README

unfinished_sudoku_1 = [
    [5, 8, 6, 0, 3, 1, 0, 7, 0],
    [2, 0, 7, 8, 6, 0, 5, 1, 3],
    [0, 1, 0, 7, 0, 5, 2, 0, 6],
    [0, 2, 8, 0, 0, 4, 3, 6, 1],
    [6, 0, 4, 9, 1, 3, 7, 2, 0],
    [0, 3, 1, 6, 2, 0, 0, 9, 5],
    [4, 0, 5, 0, 8, 2, 0, 3, 7],
    [1, 7, 0, 4, 9, 6, 8, 0, 2],
    [0, 6, 2, 3, 5, 0, 1, 0, 9]
]

unfinished_sudoku_2 = [
    [7, 8, 0, 4, 0, 0, 1, 2, 0],
    [6, 0, 0, 0, 7, 5, 0, 0, 9],
    [0, 0, 0, 6, 0, 1, 0, 7, 8],
    [0, 0, 7, 0, 4, 0, 2, 6, 0],
    [0, 0, 1, 0, 5, 0, 9, 3, 0],
    [9, 0, 4, 0, 6, 0, 0, 0, 5],
    [0, 7, 0, 3, 0, 0, 0, 1, 2],
    [1, 2, 0, 0, 0, 7, 4, 0, 0],
    [0, 4, 9, 2, 0, 6, 0, 0, 7]
]


if __name__ == '__main__':
    SudokuApp(unfinished_sudoku_1).run()

    solver = SudokuSolver(unfinished_sudoku_2)
    solver.solve_sudoku()
    finished_sudoku = solver.data

    checker = SudokuChecker(finished_sudoku)
    if checker.is_valid():
        print('The Sudoku was solved correctly.')
    else:
        print('Something went wrong!')

