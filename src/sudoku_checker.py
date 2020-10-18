import numpy as np


class SudokuChecker(object):
    def __init__(self, data):
        self.N = len(data)
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
        root_N = int(np.sqrt(self.N))
        valid_squares = []
        for n1 in range(0, self.N, root_N):
            for n2 in range(0, self.N, root_N):
                valid_squares.append(sum([self.data[y][x] for x in range(n1 + 0, n1 + root_N) for y in
                                          range(n2 + 0, n2 + root_N)]) == sum(range(self.N + 1)))
        return all(valid_squares)




