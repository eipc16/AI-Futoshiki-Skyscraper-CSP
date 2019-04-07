class Variable:
    def __init__(self, value, domain, predefined=False):
        self.value = value
        self._prev_value = value
        self.predefined = predefined
        self.constraints = []
        self.domain = domain

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

    def check(self, debug=True):
        for constraint in self.constraints:
            if constraint.check() == False:
                if debug:
                    print('Constraint %s - FAILED' % str(constraint))
                return False
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