class Variable:
    def __init__(self, value, predefined=False):
        self.value = value
        self._prev_value = value
        self.predefined = predefined
        self.constraints = []

    def update(self, value):
        if predefined != True:
            self._prev_value = self.value
            self.value = value
        else:
            print("You can't change this variable (%s)" % str(self))    

    def rollback(self):
        if predefined != True:
            self.value = self._prev_value
        else:
            print("You can't change this variable (%s)" % str(self))

    def append_constraint(self, constraint):
        self.constraints.append(constraint)

    def check(self):
        for constraint in self.constraints:
            if constraint.check() == False:
                print('Constraint %s - FAILED' % str(constraint))
                return False
            else:
                print('Constraint %s - SUCCEEDED' % str(constraint))
        return True

    def __repr__(self):
        return str(self.value)

    def __eq__(self, x):
        x = x.value if isinstance(x, Variable) else x
        return self.value == x

    def __ne__(self, x):
        x = x.value if isinstance(x, Variable) else x
        return self.value != x

    def __lt__(self, x):
        x = x.value if isinstance(x, Variable) else x
        return self.value < x

    def __le__(self, x):
        x = x.value if isinstance(x, Variable) else x
        return self.value <= x

    def __gt__(self, x):
        x = x.value if isinstance(x, Variable) else x
        return self.value > x

    def __ge__(self, x):
        x = x.value if isinstance(x, Variable) else x
        return self.value >= x