import numpy as np
from Models.Variables.SkyscraperVariable import SkyscraperVariable
from Models.Domains.Domain import Domain
from Models.Constraints.Constraints import SkyscraperRule, Unique
from Models.ConstraintSatisfactionProblemModel import Model


class SkyscraperModel(Model):
    def __init__(self, path):
        super().__init__()

        self.top, self.bottom, self.right, self.left = None, None, None, None

        self.skyscraper_constraints = []

        self._load_data(path)

    def _load_data(self, path):
        print('Skyscraper: %s' % path)
        if "sky" in path:
            with open(path) as file:
                self.content = file.readlines()
                self.dims = int(self.content[0])
                self.domain = Domain(list(range(1, self.dims + 1)))
                self.variables = np.empty((self.dims, self.dims), dtype=SkyscraperVariable)

                for i in range(1, 5):
                    row = self.content[i].split(';')
                    label = row[0]
                    values = np.array([int(v) for v in row[1:]])

                    if label == "G":
                        self.top = np.array(values)
                    elif label == "D":
                        self.bottom = np.array(values)
                    elif label == "L":
                        self.left = np.array(values)
                    elif label == "P":
                        self.right = np.array(values)
                    else:
                        print('Error')
                        return

                for i in range(self.dims):
                    for j in range(self.dims):
                        variable = SkyscraperVariable(0, i, j, Domain(list(range(1, self.dims + 1))), predefined=False)
                        self.variables[i, j] = variable

                # Setting unique variables
                for i in range(self.variables.shape[0]):
                    for j in range(self.variables.shape[1]):
                        variable = self.variables[i, j]
                        cons_row = self.variables[i, :]
                        col_row = self.variables[:, j]
                        row = np.concatenate([cons_row, col_row])

                        unique_constraint = Unique(variable, cons_row)
                        unique_constraint_2 = Unique(variable, col_row)

                        variable.append_constraint(unique_constraint)
                        variable.append_constraint(unique_constraint_2)
                        variable.append_constrained_variable(row)

                for i in range(self.variables.shape[0]):
                    row = self.variables[i, :]
                    skyscraper_constraint = SkyscraperRule(row, self.left[i], self.right[i], orientation="h")
                    self.model_constraints.append(skyscraper_constraint)

                    col = self.variables[:, i]
                    skyscraper_constraint = SkyscraperRule(col, self.top[i], self.bottom[i], orientation="v")
                    self.model_constraints.append(skyscraper_constraint)


        else:
            print("Incorrect file!")

    def validate(self):
        var_validate = np.prod([x.check() for x in self.variables.ravel()])
        model_validate = np.prod([c.check() for c in self.model_constraints])
        return var_validate and model_validate

    def validate_non_zero(self):
        return self.validate() and np.count_nonzero(self.variables.flatten() == 0) == 0

    def get_board(self):
        outstr = '------\nDomain: %s\nState:' % self.domain
        top_str = '\t' + '\t'.join(['[%s]' % str(x) for x in self.top])
        bottm_str = '\t' + '\t'.join(['[%s]' % str(x) for x in self.bottom])
        middle = ''

        for i in range(self.variables.shape[0]):
            middle += '[%d]\t' % self.left[i]
            for j in range(self.variables.shape[1]):
                middle += ' %d \t' % self.variables[i, j].value

            middle += '[%d]\n' % self.right[i]

        return '%s\n%s\n%s%s\n' % (outstr, top_str, middle, bottm_str)
