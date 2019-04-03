class Variable:
    def __init__(self, value):
        self.value = value
        self._prev_value = value

    def update(self, value):
        self._prev_value = self.value
        self.value = value

    def rollback(self):
        self.value = self._prev_value

class Model:
    def __init__(self, default_value=0):
        self.default_value = default_value
        self.variables = []
        self.domain = []
        self.constrains = {}

    def validate(self, variable):
        for constraint in self.constrains.get(variable, []):
            if not constraint():
                return False
        return True

    def append_constraint(self, variable, constraint):
        if not self.constraints.get(variable):
            self.constraints[variable] = []

        self.constraints[variable].append(constraint)
