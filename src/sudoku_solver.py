import numpy as np


class SudokuSolver(object):
    def __init__(self, data):
        self.N = len(data)
        self.data = data
        self.actions = []

    def get_all_empty_pos(self):
        empty_pos = []
        for row in range(self.N):
            for col in range(self.N):
                if self.is_empty_pos(row, col):
                    empty_pos.append((row, col))
        return empty_pos

    def get_count_related_empty_pos(self, row, col):
        return len(set(self.get_empty_pos_row(row) + self.get_empty_pos_col(col) +
                       self.get_empty_pos_square(row, col)))

    def get_empty_pos_row(self, row):
        return [(row, idx) for idx, entry in enumerate(self.data[row]) if entry == 0]

    def get_empty_pos_col(self, col):
        return [(idx, col) for idx, row in enumerate(self.data) if row[col] == 0]

    def get_empty_pos_square(self, row, col):
        root_N = int(np.sqrt(self.N))
        square_row_idx, square_col_idx = self.get_square_index(row, col)
        return [(x, y) for x in range(square_row_idx, square_row_idx + root_N) for y in
                range(square_col_idx, square_col_idx + root_N) if self.data[x][y] == 0]

    def get_empty_pos(self, ordered=True):
        if ordered:
            empty_pos = self.get_all_empty_pos()
            min_related_empty = self.N * self.N
            min_empty_pos = None
            for x, y in empty_pos:
                num_empty_pos = self.get_count_related_empty_pos(x, y)
                if min_related_empty > num_empty_pos:
                    min_related_empty = num_empty_pos
                    min_empty_pos = (x, y)
            return min_empty_pos
        else:
            for row in range(self.N):
                for col in range(self.N):
                    if self.is_empty_pos(row, col):
                        return row, col

    def is_empty_pos(self, row, col):
        return self.data[row][col] == 0

    def get_square_index(self, row, col):
        root_N = int(np.sqrt(self.N))
        return (row // root_N) * root_N, (col // root_N) * root_N

    def is_not_in_row(self, num, row):
        return all(entry != num for entry in self.data[row])

    def is_not_in_col(self, num, col):
        return all(row[col] != num for row in self.data)

    def is_not_in_square(self, num, row, col):
        root_N = int(np.sqrt(self.N))
        square_row_idx, square_col_idx = self.get_square_index(row, col)
        return all(self.data[x][y] != num for x in range(square_row_idx, square_row_idx + root_N) for y in
                   range(square_col_idx, square_col_idx + root_N))

    def is_valid_num(self, num, row, col):
        return all([self.is_not_in_row(num, row), self.is_not_in_col(num, col), self.is_not_in_square(num, row, col)])

    def solve_sudoku(self):
        pos = self.get_empty_pos()

        if pos is None:
            return True

        row, col = pos
        for num in range(1, self.N+1):
            if self.is_valid_num(num, row, col):
                self.data[row][col] = num

                if self.solve_sudoku():
                    return True

                self.data[row][col] = 0

        return False



