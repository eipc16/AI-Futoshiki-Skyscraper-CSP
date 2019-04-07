import numpy as np
from Models.Variables.FutoshikiVariable import FutoshikiVariable
from Models.Domains.Domain import Domain
from Models.Constraints.Constraints import LowerThan, GreaterThan, UniqueRow
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
                        variable = FutoshikiVariable(cell_value, i, j)
                        self.variables[i, j] = variable

                #Loading lt, gt constraints
                for i, row in enumerate(self.content[self.dims + 3:]):
                    if row == "\n":
                        break;

                    lower_value, higher_value = row.split(';')

                    lower_row_number, lower_cell_number = ord(lower_value[0]) - 65, int(lower_value[1]) - 1
                    lower_variable = self.variables[lower_row_number, lower_cell_number]

                    higher_row_number, higher_cell_number = ord(higher_value[0]) - 65, int(higher_value[1]) - 1
                    higher_variable = self.variables[higher_row_number, higher_cell_number]
                  
                    lower_constraint = LowerThan(lower_variable, higher_variable)
                    higher_constraint = GreaterThan(higher_variable, lower_variable)
                    
                    lower_variable.append_constraint(lower_constraint)
                    higher_variable.append_constraint(higher_constraint)

                #Setting unique variables
                for i in range(self.variables.shape[0]):
                    for j in range(self.variables.shape[1]):
                        variable = self.variables[i, j]
                        unique_constraint = UniqueRow(variable, self.variables[i][:].flatten())
                        unique_constraint_2 = UniqueRow(variable, self.variables[:][j].flatten())
                        variable.append_constraint(unique_constraint)
                        variable.append_constraint(unique_constraint_2)

        else:
            print("Incorrect file!")

    def get_var_constraint(self, var):
        result = ""
        for constraint in var.constraints:
            result = result + str(constraint) + "\n"
        return result

    def get_board(self, constraints=False):
        outstr = '------\nSize: %d\nDomain: %s\nState:\n%s\n' % (self.dims, self.domain, str(self.variables))
        if constraints == True:
            for var in self.variables.flatten():
                outstr = outstr + 'Variable: %s\n%s' % (var, self.get_var_constraint(var))

        return outstr + '------\n'

    def validate(self):
        for variable in self.variables.flatten():
            if variable.check() == False:
                return False
        return True

