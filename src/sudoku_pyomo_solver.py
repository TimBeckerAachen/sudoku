import pyomo.environ as pyo
import numpy as np

from pyomo.opt import SolverFactory


# TODO: smarter obj fct? yes!
# TODO: how to see if there are several solutions?
#  https://github.com/Pyomo/pyomo/blob/master/examples/doc/pyomobook/attic/scripts/sudoku/sudoku.py integer cut
# TODO: no strings?
# TODO: clean Sets -> rename col, row, ...
# TODO: fix instead of constrain
# TODO: results might not be exactly 1


class SudokuPyomo:
    def __init__(self, input_sudoku):
        self.sudoku = input_sudoku
        assert set([len(input_sudoku)]) == set([len(row) for row in input_sudoku]), \
            'dimension of sudoku are not supported'
        self.N = len(self.sudoku)
        self.rootN = int(np.sqrt(self.N))
        self.m = pyo.ConcreteModel()

    def construct_pyomo_model(self):
        self.m.numbers = pyo.Set(initialize=[str(i+1) for i in range(self.N)])
        self.m.sudoku = pyo.Var(self.m.numbers, self.m.numbers, self.m.numbers, domain=pyo.Boolean)
        self._set_constraints()

    def solve_pyomo_model(self):
        def obj_rule(m):
            return sum(m.sudoku[row, col, num] for row in self.m.numbers for col in self.m.numbers
                       for num in self.m.numbers)

        self.m.value = pyo.Objective(rule=obj_rule, sense=pyo.maximize)
        optimizer = SolverFactory('glpk')
        results = optimizer.solve(self.m)
        self.m.solutions.load_from(results)

    def print_pyomo_model(self):
        print(self.m.pprint())

    def _set_constraints(self):
        self._set_constraints_known_numbers()
        self._set_constraints_unique_num()
        self._set_constraints_rows()
        self._set_constraints_cols()
        self._set_constraints_squares()

    def _set_constraints_known_numbers(self):
        def known_number(model, row, col, num):
            if self.sudoku[int(row)-1][int(col)-1] == int(num):
                return model.sudoku[row, col, num] == 1
            else:
                return pyo.Constraint.Skip
        self.m.known_number = pyo.Constraint(self.m.numbers, self.m.numbers, self.m.numbers, rule=known_number)

    def _set_constraints_unique_num(self):
        def valid_num(model, row, col):
            return sum([model.sudoku[row, col, num] for num in model.numbers]) == 1
        self.m.unique_num = pyo.Constraint(self.m.numbers, self.m.numbers, rule=valid_num)

    def _set_constraints_rows(self):
        def valid_row(model, row, num):
            return sum([model.sudoku[row, col, num] for col in model.numbers]) == 1
        self.m.row = pyo.Constraint(self.m.numbers, self.m.numbers, rule=valid_row)

    def _set_constraints_cols(self):
        def valid_col(model, col, num):
            return sum([model.sudoku[row, col, num] for row in model.numbers]) == 1
        self.m.col = pyo.Constraint(self.m.numbers, self.m.numbers, rule=valid_col)

    def _set_constraints_squares(self):
        def valid_square(model, square, num):
            row_idx = (int(square)-1) % self.rootN
            col_idx = (int(square)-1) // self.rootN
            return sum([model.sudoku[str(row+1), str(col+1), num] for row in range(row_idx*self.rootN,
                                                                                   (row_idx+1)*self.rootN)
                        for col in range(col_idx*self.rootN, (col_idx+1)*self.rootN)]) == 1
        self.m.square = pyo.Constraint(self.m.numbers, self.m.numbers, rule=valid_square)

    def get_solved_sudoku(self):
        result = getattr(self.m, 'sudoku').get_values()
        sudoku = self._get_empty_sudoku()
        for entry in result.keys():
            if result[entry] == 1:
                sudoku[int(entry[0]) - 1][int(entry[1]) - 1] = int(entry[2])
        return sudoku

    def _get_empty_sudoku(self):
        return [[0 for _ in range(self.N)] for _ in range(self.N)]


if __name__ == '__main__':
    sudoku_2 = [
        [0, 4, 2, 3],
        [3, 2, 4, 1],

        [4, 1, 3, 2],
        [2, 3, 1, 4]
    ]

    solver = SudokuPyomo(sudoku_2)
    solver.construct_pyomo_model()
    solver.solve_pyomo_model()
    print(solver.get_solved_sudoku())



