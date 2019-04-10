from Algorithms.ConstraintSatisfactionProblem import ConstraintSatisfactionProblem


class BackTracking(ConstraintSatisfactionProblem):
    def __init__(self, model):
        super().__init__(model)

    def validate(self, var):
        super().validate(var)
        return var.check()
