from src.sudoku_checker import SudokuChecker
# TODO: define test sudokus at the beginning
# TODO: more test sudokus


def test_has_valid_types():
    invalid_sudoku_1 = [[True]]
    checker = SudokuChecker(invalid_sudoku_1)
    assert not checker.has_valid_types()

    valid_sudoku_2 = [
        [1, 4, 2, 3],
        [3, 2, 4, 1],

        [4, 1, 3, 2],
        [2, 3, 1, 4]
    ]
    checker = SudokuChecker(valid_sudoku_2)
    assert checker.has_valid_types()


def test_has_valid_dim():
    valid_sudoku_1 = [
        [1, 4, 2, 3],
        [3, 2, 4, 1],

        [4, 1, 3, 2],
        [2, 3, 1, 4]
    ]
    checker = SudokuChecker(valid_sudoku_1)
    assert checker.has_valid_dim()

    invalid_sudoku_2 = [
        [1, 4, 2, 3],
        [3, 2, 4, 1],

        [4, 1, 3, 2],
        [2, 3, 1]
    ]
    checker = SudokuChecker(invalid_sudoku_2)
    assert not checker.has_valid_dim()


def test_has_valid_rows():
    valid_sudoku_1 = [
        [1, 4, 2, 3],
        [3, 2, 4, 1],

        [4, 1, 3, 2],
        [2, 3, 1, 4]
    ]
    checker = SudokuChecker(valid_sudoku_1)
    assert checker.has_valid_rows()

    invalid_sudoku_2 = [
        [1, 4, 3, 3],
        [3, 2, 4, 1],

        [4, 1, 3, 2],
        [2, 3, 1, 4]
    ]
    checker = SudokuChecker(invalid_sudoku_2)
    assert not checker.has_valid_rows()


def test_has_valid_cols():
    valid_sudoku_1 = [
        [1, 4, 2, 3],
        [3, 2, 4, 1],

        [4, 1, 3, 2],
        [2, 3, 1, 4]
    ]
    checker = SudokuChecker(valid_sudoku_1)
    assert checker.has_valid_cols()

    invalid_sudoku_2 = [
        [1, 4, 3, 3],
        [3, 2, 4, 1],

        [4, 1, 3, 2],
        [2, 3, 1, 4]
    ]
    checker = SudokuChecker(invalid_sudoku_2)
    assert not checker.has_valid_cols()


def test_has_valid_squares():
    valid_sudoku_1 = [
        [1, 4, 2, 3],
        [3, 2, 4, 1],

        [4, 1, 3, 2],
        [2, 3, 1, 4]
    ]
    checker = SudokuChecker(valid_sudoku_1)
    assert checker.has_valid_squares()

    invalid_sudoku_2 = [
        [1, 4, 3, 3],
        [3, 2, 4, 1],

        [4, 1, 3, 2],
        [2, 3, 1, 4]
    ]
    checker = SudokuChecker(invalid_sudoku_2)
    assert not checker.has_valid_squares()


def test_is_valid():
    valid_sudoku_1 = [
        [1, 4, 2, 3],
        [3, 2, 4, 1],

        [4, 1, 3, 2],
        [2, 3, 1, 4]
    ]
    checker = SudokuChecker(valid_sudoku_1)
    assert checker.is_valid()

    invalid_sudoku_2 = [
        [1, 4, 3, 3],
        [3, 2, 4, 1],

        [4, 1, 3, 2],
        [2, 3, 1, 4]
    ]
    checker = SudokuChecker(invalid_sudoku_2)
    assert not checker.is_valid()
