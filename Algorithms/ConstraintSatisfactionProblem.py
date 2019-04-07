import numpy as np

class ConstraintSatisfactionProblem:
    def __init__(self, model, defvalue=0):
        self.model = model
        self.defvalue = defvalue
        self.active_variables = np.extract(model.variables == defvalue, model.variables)
        self.domain = model.domain

        self.timer = 0.0
        self.iterations = 0

    def print_active(self):
        for var in self.active_variables:
            print(var.name())
