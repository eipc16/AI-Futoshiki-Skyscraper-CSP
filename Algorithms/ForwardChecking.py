from Algorithms.ConstraintSatisfactionProblem import ConstraintSatisfactionProblem


class ForwardChecking(ConstraintSatisfactionProblem):
    def __init__(self, model):
        super().__init__(model)

    def has_valid_value(self, variable):
        for value in variable.domain:
            variable.update(value)
            
            if variable.check():
                variable.update(0)
                return True

        variable.update(0)
        return False

    def validate(self, var):
        super().validate(var)

        if not var.check():
            return False

        for variable in var.constrained_variables:
            #variable.domain.remove(var.value)
            if variable == 0 and not self.has_valid_value(variable):
                #variable.domain.append(var.value)
                return False

        return True




