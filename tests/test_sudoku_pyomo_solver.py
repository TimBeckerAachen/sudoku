from src.sudoku_pyomo_solver import SudokuPyomo


sudoku_2 = [
    [0, 4, 2, 3],
    [3, 2, 4, 1],

    [4, 1, 3, 2],
    [2, 3, 1, 4]
]

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

finished_sudoku_2 = [
    [7, 8, 5, 4, 3, 9, 1, 2, 6],
    [6, 1, 2, 8, 7, 5, 3, 4, 9],
    [4, 9, 3, 6, 2, 1, 5, 7, 8],
    [8, 5, 7, 9, 4, 3, 2, 6, 1],
    [2, 6, 1, 7, 5, 8, 9, 3, 4],
    [9, 3, 4, 1, 6, 2, 7, 8, 5],
    [5, 7, 8, 3, 9, 4, 6, 1, 2],
    [1, 2, 6, 5, 8, 7, 4, 9, 3],
    [3, 4, 9, 2, 1, 6, 8, 5, 7]
]



def test_get_empty_sudoku():
    empty_sudoku = [[0, 0, 0, 0],
                    [0, 0, 0, 0],
                    [0, 0, 0, 0],
                    [0, 0, 0, 0]]
    solver = SudokuPyomo(sudoku_2)
    assert empty_sudoku == solver._get_empty_sudoku()


def test_get_solved_sudoku():
    sudoku = [[1, 0, 0, 0],
              [0, 0, 0, 4],
              [0, 0, 0, 0],
              [0, 0, 0, 0]]
    solver = SudokuPyomo(sudoku_2)
    solver.m.sudoku = DummyResult
    assert solver.get_solved_sudoku() == sudoku


class DummyResult:
    @staticmethod
    def get_values():
        return {('1', '1', '1'): 1.0, ('1', '1', '2'): 0.0, ('1', '1', '3'): 0.0, ('1', '1', '4'): 0.0,
                ('2', '4', '4'): 1.0}


def test_solve_pyomo_model():
    solver = SudokuPyomo(unfinished_sudoku_1)
    solver.construct_pyomo_model()
    solver.solve_pyomo_model()
    assert solver.get_solved_sudoku() == finished_sudoku_1

    solver = SudokuPyomo(unfinished_sudoku_2)
    solver.construct_pyomo_model()
    solver.solve_pyomo_model()
    assert solver.get_solved_sudoku() == finished_sudoku_2







