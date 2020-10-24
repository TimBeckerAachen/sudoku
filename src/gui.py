from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.popup import Popup

from src.sudoku_checker import SudokuChecker


class SudokuGrid(GridLayout):
    def __init__(self, unfinished_sudoku, **kwargs):
        super().__init__(**kwargs)
        self.sudoku_input = unfinished_sudoku
        self.rows = len(unfinished_sudoku)
        self.cols = self.rows
        self.sudoku_cells = []
        for row in self.sudoku_input:
            cols = []
            for col in range(self.rows):
                if row[col] != 0:
                    cell = SudokuCell(self.rows)
                    cell.text = str(row[col])
                else:
                    cell = InputCell(self.rows)
                self.add_widget(cell)
                cols.append(cell)
            self.sudoku_cells.append(cols)

    def get_current_state(self):
        current_sudoku = []
        for row in self.sudoku_cells:
            current_sudoku.append([cell.text if cell.text != '' else 0 for cell in row])
        return current_sudoku


class SudokuOperations(GridLayout):
    def __init__(self, sudokugrid, **kwargs):
        super().__init__(**kwargs)
        self.size_hint_y = 0.1
        self.rows = 1
        self.cols = 2
        self.sudokugrid = sudokugrid

        self.btn_check = Button(text="check", font_size=40)
        self.btn_check.bind(on_press=self.check_sudoku)
        self.add_widget(self.btn_check)

        self.btn_clear = Button(text="clear", font_size=40)
        self.btn_clear.bind(on_press=self.clear_sudoku)
        self.add_widget(self.btn_clear)

    def check_sudoku(self, instance):
        current_sudoku = [list(map(int, row)) for row in self.sudokugrid.get_current_state()]
        checker = SudokuChecker(current_sudoku)
        if checker.is_valid():
            self.result_popup('Congratulations! You solved the Sudoku.')
        else:
            self.result_popup('The answer is incorrect. Keep trying!')

    def clear_sudoku(self, instance):
        for row in self.sudokugrid.sudoku_cells:
            for cell in row:
                if not cell.readonly:
                    cell.text = ''

    @staticmethod
    def result_popup(text):
        content = FloatLayout()

        message = Label()
        message.text = text
        message.size_hint = 0.6, 0.2
        message.pos_hint = {"x": 0.2, "top": 0.9}
        content.add_widget(message)

        closeButton = Button()
        closeButton.text = 'close'
        closeButton.size_hint = 0.8, 0.2
        closeButton.pos_hint = {"x": 0.1, "y": 0.1}
        content.add_widget(closeButton)

        popupWindow = Popup(title="Result", content=content, size_hint=(.5, .5), pos_hint={'right': .75, 'top': 1})
        popupWindow.open()

        closeButton.bind(on_press=popupWindow.dismiss)


class SudokuGame(GridLayout):
    def __init__(self, unfinished_sudoku, **kwargs):
        super().__init__(**kwargs)
        self.cols = 1
        self.rows = 2

        sudokugrid = SudokuGrid(unfinished_sudoku)
        self.add_widget(sudokugrid)
        self.add_widget(SudokuOperations(sudokugrid))


class SudokuCell(TextInput):
    def __init__(self, dim, **kwargs):
        super().__init__(**kwargs)
        self.multiline = False
        self.on_text = self.foreground_color = (0, 0, 1, 1)

        self.readonly = True
        self.dim = dim


class InputCell(SudokuCell):
    def __init__(self, dim, **kwargs):
        super().__init__(dim, **kwargs)
        self.readonly = False
        self.on_text = self.foreground_color = (0, 0, 0, 1)

    def insert_text(self, substring, from_undo=False):
        text = substring if (substring.isdigit() and 0 < int(substring) <= self.dim) else ''
        return super(SudokuCell, self).insert_text(text, from_undo=from_undo)


class SudokuApp(App):
    def __init__(self, unfinished_sudoku, **kwargs):
        super().__init__(**kwargs)
        self.unfinished_sudoku = unfinished_sudoku

    def build(self):
        return SudokuGame(self.unfinished_sudoku)


