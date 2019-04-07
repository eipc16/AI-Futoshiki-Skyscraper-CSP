class Model:
    def __init__(self, default_value=0):
        self.default_value = default_value
        self.variables = []
        self.domain = None
        self.constraints = dict()

    def validate(self, variable):
        for constraint in self.constrains.get(variable, []):
            if not constraint():
                return False
        return True

    def append_constraint(self, variable, constraint):
        self.constraints.update({variable: constraint})
