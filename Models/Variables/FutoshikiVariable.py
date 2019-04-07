from Variable import Variable

class FutoshikiVariable(Variable):
    def __init__(self, value, row, col, predefined=False):
        super().__init__(value, predefined)
        self.row = row
        self.col = col

    def row_char(self):
        return chr(ord('A') + self.row)

    def column(self):
        return self.col + 1

    def name(self):
        return "%s%s" % (self.row_char(), self.column())

    def __str__(self):
        return "[%s x %s] Value = %d" % (self.row_char(), self.column(), self.value) 

    def __repr__(self):
        return str(self.value)

    def __eq__(self, x):
        return self.value == x.value