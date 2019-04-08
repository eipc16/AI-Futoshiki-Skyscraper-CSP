class Variable:
    def __init__(self, value, domain, predefined=False):
        self.value = value
        self._prev_value = value
        self.predefined = predefined
        self.constraints = []
        self.constrained_variables = set()
        self.domain = domain

    def update(self, value):
        if self.predefined != True:
            self._prev_value = self.value
            self.value = value
        else:
            print("You can't change this variable (%s)" % str(self))    

    def rollback(self):
        if self.predefined != True:
            self.value = self._prev_value
        else:
            print("You can't change this variable (%s)" % str(self))

    def append_constraint(self, constraint):
        self.constraints.append(constraint)

    def append_constrained_variable(self, variable):
        if isinstance(variable, Variable):
            self.constrained_variables.add(variable)
        else:
            self.constrained_variables.update(variable)

    def check(self, debug=False):
        for constraint in self.constraints:
            if not constraint.check():
                if debug:
                    print('Constraint %s - FAILED' % str(constraint))
                return False
        return True

    def check_count(self):
        failed = 0
        for constraint in self.constraints:
            if consraint.check() == False:
                failed += 1
        return failed

    def constrained_variables(self):
        constrained_vars = set()
        for constraint in self.constraints:
            constrained = constraint.get_constrained()

            if(isinstance(constrained, Variable)):
                constrained_vars.add(constrained)
            else:
                constrained_vars.update(constrained)

            #constrained_vars.update(constraint.get_constrained())
        return constrained_vars

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

    def __hash__(self):
        return hash(self.value)