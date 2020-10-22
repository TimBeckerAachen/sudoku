from src.sudoku_solver import SudokuSolver

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

finished_sudoku_1 = [
    [5, 8, 6, 2, 3, 1, 9, 7, 4],
    [2, 4, 7, 8, 6, 9, 5, 1, 3],
    [3, 1, 9, 7, 4, 5, 2, 8, 6],
    [9, 2, 8, 5, 7, 4, 3, 6, 1],
    [6, 5, 4, 9, 1, 3, 7, 2, 8],
    [7, 3, 1, 6, 2, 8, 4, 9, 5],
    [4, 9, 5, 1, 8, 2, 6, 3, 7],
    [1, 7, 3, 4, 9, 6, 8, 5, 2],
    [8, 6, 2, 3, 5, 7, 1, 4, 9]
]


def test_find_empty_pos():
    solver = SudokuSolver(unfinished_sudoku_1)

    assert (0, 3) == solver.get_empty_pos(ordered=False)

    assert (4, 8) == solver.get_empty_pos(ordered=True)


def test_get_square_index():
    solver = SudokuSolver(unfinished_sudoku_1)

    assert (0, 0) == solver.get_square_index(0, 0)
    assert (2, 2) == solver.get_square_index(8, 8)
    assert (0, 2) == solver.get_square_index(0, 8)
    assert (1, 1) == solver.get_square_index(4, 5)


def test_is_not_in_row():
    solver = SudokuSolver(unfinished_sudoku_1)

    assert solver.is_not_in_row(9, 0)
    assert not solver.is_not_in_row(1, 2)
    assert solver.is_not_in_row(3, 2)


def test_not_in_col():
    solver = SudokuSolver(unfinished_sudoku_1)

    assert not solver.is_not_in_col(4, 0)
    assert solver.is_not_in_col(4, 8)


def test_not_in_square():
    solver = SudokuSolver(unfinished_sudoku_1)

    assert solver.is_not_in_square(3, 1, 1)
    assert solver.is_not_in_square(4, 6, 6)
    assert not solver.is_not_in_square(1, 6, 6)
    assert solver.is_not_in_square(5, 3, 3)


def test_is_valid_num():
    solver = SudokuSolver(unfinished_sudoku_1)

    assert solver.is_valid_num(2, 0, 3)


def test_solve_sudoku():
    solver = SudokuSolver(unfinished_sudoku_1)

    solver.solve_sudoku()

    assert solver.data == finished_sudoku_1


def test_get_all_empty_pos():
    solver = SudokuSolver(unfinished_sudoku_1)

    assert len(solver.get_all_empty_pos()) == 25


def test_get_empty_pos_row():
    solver = SudokuSolver(unfinished_sudoku_1)

    assert solver.get_empty_pos_row(0) == [(0, 3), (0, 6), (0, 8)]
    assert solver.get_empty_pos_row(1) == [(1, 1), (1, 5)]


def test_get_count_empty_pos_col():
    solver = SudokuSolver(unfinished_sudoku_1)

    assert solver.get_empty_pos_col(0) == [(2, 0), (3, 0), (5, 0), (8, 0)]
    assert solver.get_empty_pos_col(1) == [(1, 1), (4, 1), (6, 1)]


def test_get_count_empty_pos_square():
    solver = SudokuSolver(unfinished_sudoku_1)

    assert solver.get_empty_pos_square(0, 0) == [(1, 1), (2, 0), (2, 2)]
    assert solver.get_empty_pos_square(3, 6) == [(4, 8), (5, 6)]


def test_get_count_related_empty_pos():
    solver = SudokuSolver(unfinished_sudoku_1)

    assert solver.get_count_related_empty_pos(0, 0) == 9
    assert solver.get_count_related_empty_pos(3, 6) == 7

