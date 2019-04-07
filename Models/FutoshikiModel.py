import numpy as np

class FutoshikiModel(Model):
    def __init__(self, path):
        super().__init__()
        self._load_data(path)

    def _load_data(self, path):
        print('Futo: %s' % path)
        if "futo" in path:
            with open(path) as file:
                self.content = file.readlines()
                self.dims = int(self.content[0])
                self.domain = list(range(1, self.dims + 1))
                self.variables = np.empty((self.dims, self.dims), dtype=FutoshikiVariable)

                #Loading variables
                for i, row in enumerate(self.content[2: self.dims + 2]):
                    for j, cell in enumerate(str(row).split(';')):
                        cell_value = int(cell)
                        variable = FutoshikiVariable(cell_value, i, j)
                        self.variables[i, j] = variable

                #Loading constraints
                for i, row in enumerate(self.content[self.dims + 3:]):
                    if row == "\n":
                        break;

                    lower_value, higher_value = row.split(';')

                    lower_row_number, lower_cell_number = ord(lower_value[0]) - 65, int(lower_value[1]) - 1
                    lower_variable = self.variables[lower_row_number, lower_cell_number]

                    higher_row_number, higher_cell_number = ord(higher_value[0]) - 65, int(higher_value[1]) - 1
                    higher_variable = self.variables[higher_row_number, higher_cell_number]
                    
                    _is_lower = self.is_lower(lower_variable, higher_variable)

                    self.append_constraint(lower_variable.name(), {"var": higher_variable.name(), "value": _is_lower})
                    self.append_constraint(higher_variable.name(), {"var": lower_variable.name(), "value": not _is_lower})
        else:
            print("Incorrect file!")
        
    def is_lower(self, x, y):
        return y.value == self.default_value or x.value > y.value

    def is_unique(self, x, array):
        return np.count_nonzero(array == x) == 1

    def print_info(self):
        print('-----')
        print('Size: %d' % self.dims)
        print('Variables: ')
        print(self.variables)
        print('Constraints: ')
        print(self.constraints)
        print('-----')

    def check_unique(self):
        for row in self.variables:
            print(row)
            for val in row:
                print("%s%s" % (val, self.is_unique(val, row)))

        for col in self.variables.T:
            print(col)
            for val in col:
                print("%s%s" % (val, self.is_unique(val, col)))