import numpy as np
from Models.Variables.FutoshikiVariable import FutoshikiVariable
from Models.Domains.Domain import Domain
from Models.Constraints.Constraints import LowerThan, GreaterThan, Unique
from Models.ConstraintSatisfactionProblemModel import Model

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
                self.domain = Domain(list(range(1, self.dims + 1)))
                self.variables = np.empty((self.dims, self.dims), dtype=FutoshikiVariable)
                #Loading variables
                for i, row in enumerate(self.content[2: self.dims + 2]):
                    for j, cell in enumerate(str(row).split(';')):
                        cell_value = int(cell)
                        predefined = True
                        domain = []
                        
                        if(cell_value == 0):
                            predefined = False
                            domain = self.domain.copy()

                        variable = FutoshikiVariable(cell_value, i, j, Domain(list(range(1, self.dims + 1))), predefined=predefined)
                        self.variables[i, j] = variable

                #Loading lt, gt constraints
                for i, row in enumerate(self.content[self.dims + 3:]):
                    if row == "\n":
                        break

                    lower_value, higher_value = row.split(';')

                    lower_row_number, lower_cell_number = ord(lower_value[0]) - 65, int(lower_value[1]) - 1
                    lower_variable = self.variables[lower_row_number, lower_cell_number]

                    higher_row_number, higher_cell_number = ord(higher_value[0]) - 65, int(higher_value[1]) - 1
                    higher_variable = self.variables[higher_row_number, higher_cell_number]

                    lower_constraint = LowerThan(lower_variable, higher_variable)
                    higher_constraint = GreaterThan(higher_variable, lower_variable)

                    lower_variable.append_constraint(lower_constraint)
                    lower_variable.append_constrained_variable(higher_variable)
                    higher_variable.append_constraint(higher_constraint)
                    higher_variable.append_constrained_variable(lower_variable)

                #Setting unique variables
                for i in range(self.variables.shape[0]):
                    for j in range(self.variables.shape[1]):
                        variable = self.variables[i, j]
                        cons_row = self.variables[i,:]
                        col_row = self.variables[:,j]
                        row = np.concatenate([cons_row, col_row])

                        unique_constraint = Unique(variable, cons_row)
                        unique_constraint_2 = Unique(variable, col_row)

                        variable.append_constraint(unique_constraint)
                        variable.append_constraint(unique_constraint_2)
                        variable.append_constrained_variable(row)

        else:
            print("Incorrect file!")

    def validate(self):
        return np.prod([x.check() for x in self.variables.ravel()])
    
    def validate_non_zero(self):
        return self.validate() and np.count_nonzero(self.variables.flatten() == 0) == 0

    def get_board(self):
        outstr = '------\nDomain: %s\nState:' % self.domain
        middle = ''

        for i in range(self.variables.shape[0]):
            for j in range(self.variables.shape[1]):
                middle += '%d\t' % self.variables[i, j].value
            middle += '\n'
        return '%s\n%s' % (outstr, middle)
