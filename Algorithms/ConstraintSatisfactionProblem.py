import numpy as np
import time

class ConstraintSatisfactionProblem:
    def __init__(self, model):
        self.model = model
        self.variables = model.variables
        # self.active_variables = self.variables.ravel()
        self.active_variables = np.extract(model.variables == 0, self.variables)
        self.domain = model.domain

        print([x.name() for x in self.active_variables])

        self.timer = 0.0
        self.iterations = 0

        self.solutions = -1

    def validate(self, var):
        ''' for implementation in child classes '''
        pass

    def solve(self, index):
        self.iterations += 1
        
        if index == len(self.active_variables):
            return True

        if self.iterations % 100000 == 0:
            print('Yay i\'m on %d iterations' % self.iterations)

        var = self.active_variables[index]

        for value in var.domain:
            var.update(value)

            if self.validate(var) and self.solve(index + 1):
                if index + 1 == len(self.active_variables) and self.model.validate():
                    print('Found solution')
                    self.solutions += 1
                    print(self.get_info())
                    print(self.model.get_board())
                    var.update(0)
                    return True
                elif index + 1 == len(self.active_variables):
                    var.update(0)
                    return False

        var.update(0)

        return False

    def run(self):
        self.timer = time.time()
        self.solutions = 0
        self.model.get_board()
        self.solve(0)

    def get_info(self):
        return "Elapsed time: %5.2f | Iterations: %5d | Solutions: %5d" % (time.time() - self.timer, self.iterations, self.solutions)

    @staticmethod
    def get_var_constraint(self, var):
        result = ""
        for constraint in var.constraints:
            result = result + str(constraint) + "\n"
        return result

    @staticmethod
    def print_active(self):
        print('not predefined vars')
        for var in self.active_variables:
            print(var.name())
        print('end not predefined vars')
