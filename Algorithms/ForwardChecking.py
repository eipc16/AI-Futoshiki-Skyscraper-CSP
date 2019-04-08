from Algorithms.ConstraintSatisfactionProblem import ConstraintSatisfactionProblem
import random as r

class ForwardChecking(ConstraintSatisfactionProblem):
    def __init__(self, model, defvalue=0):
        super().__init__(model, defvalue)

    def has_valid_value(self, variable):
        for value in self.domain:
            variable.update(value)
            
            if variable.check():
                variable.update(0)
                return True

        variable.update(0)
        return False  

    def valid_variable(self, var):
        if var == 0 and not self.has_valid_value(var):
            return False

        return True

    def validate(self, var):
        super().validate(var)
        if not var.check():
            return False

        for variable in var.constrained_variables:
            if variable == 0 and not self.has_valid_value(variable):
                return False

        return True




