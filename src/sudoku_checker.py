import numpy as np


class SudokuChecker(object):
    def __init__(self, data):
        self.N = len(data)
        self.root_N = int(np.sqrt(self.N))
        self.data = data

    def is_valid(self):
        for test in [self.has_valid_types, self.has_valid_dim, self.has_valid_rows, self.has_valid_cols,
                     self.has_valid_squares]:
            if not test():
                print(f'test {test.__name__} failed')
                return False
        return True

    def has_valid_types(self):
        return all(type(x) == int for row in self.data for x in row)

    def has_valid_dim(self):
        return set([len(row) for row in self.data]) == {self.N}

    def has_valid_rows(self):
        return all(sum(row) == sum(range(self.N+1)) for row in self.data)

    def has_valid_cols(self):
        return all(sum([row[col] for row in self.data]) == sum(range(self.N + 1)) for col in range(self.N))

    def has_valid_squares(self):
        valid_squares = []
        for square_row_idx in range(0, self.N, self.root_N):
            for square_col_idx in range(0, self.N, self.root_N):
                valid_squares.append(self.is_valid_square(square_row_idx, square_col_idx))
        return all(valid_squares)

    def is_valid_square(self, square_row_idx, square_col_idx):
        return sum([self.data[x][y] for x in range(square_row_idx, square_row_idx + self.root_N) for y in
                    range(square_col_idx, square_col_idx + self.root_N)]) == sum(range(self.N + 1))




